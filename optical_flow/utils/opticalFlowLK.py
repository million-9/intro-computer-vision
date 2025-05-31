import numpy as np
import cv2

from optical_flow.utils import computeGaussianWeights, computeBilinerWeights, invertMatrix2x2


class OpticalFlowLK:

    def __init__(self, winsize, epsilon, iterations):
        self.winsize = winsize
        self.epsilon = epsilon
        self.iterations = iterations

    def compute(self, prevImg, nextImg, prevPts):

        assert prevImg.size != 0 and nextImg.size != 0, "check prevImg and nextImg"
        assert prevImg.shape[0] == nextImg.shape[0], "size mismatch, rows."
        assert prevImg.shape[1] == nextImg.shape[1], "size mismatch, cols."

        N = prevPts.shape[0]
        status = np.ones(N, dtype=int)
        nextPts = np.copy(prevPts)

        prevDerivx = []
        prevDerivy = []

        ##
        ## Compute the spacial derivatives of prev using the Scharr function
        ## - Make sure to use the normalized Scharr filter!!
        prevDerivx = cv2.Scharr(prevImg, cv2.CV_64F, 1, 0) / 32.0
        prevDerivy = cv2.Scharr(prevImg, cv2.CV_64F, 0, 1) / 32.0

        halfWin = np.array([(self.winsize[0] - 1) * 0.5, (self.winsize[1] - 1) * 0.5])
        weights = computeGaussianWeights(self.winsize, 0.3)

        for ptidx in range(N):
            u0 = prevPts[ptidx].copy()
            u0 -= halfWin

            u = u0.copy()
            iu0 = [int(np.floor(u0[0])), int(np.floor(u0[1]))]

            if iu0[0] < 0 or \
               iu0[0] + self.winsize[0] >= prevImg.shape[1] - 1 or \
               iu0[1] < 0 or \
               iu0[1] + self.winsize[1] >= prevImg.shape[0] - 1:
                status[ptidx] = 0
                continue

            bw = computeBilinerWeights(u0)

            bprev = np.zeros((self.winsize[0] * self.winsize[1], 1))
            A = np.zeros((self.winsize[0] * self.winsize[1], 2))
            AtWA = np.zeros((2, 2))
            invAtWA = np.zeros((2, 2))

            for y in range(self.winsize[1]):
                for x in range(self.winsize[0]):
                    gx = int(iu0[0] + x)
                    gy = int(iu0[1] + y)


                    ## Compute the following parts of step 2.
                    ##   bprev      Size: (w*h) x 1 Matrix
                    ##   A          Size: (w*h) x 2 Matrix
                    ##   AtWA       Size:     2 x 2 Matrix
                    ## Use the bilinear weights bw!
                    ## W is stored in 'weights', but not as a diagonal matrix!!!
                    index = y * self.winsize[0] + x  # flattened index in the window

                    # Gradient values at (gx, gy)
                    Ix = prevDerivx[gy, gx]
                    Iy = prevDerivy[gy, gx]

                    # Intensity at (gx, gy)
                    I = prevImg[gy, gx]

                    # Weight at this (x, y) location
                    w = weights[y, x]

                    # Fill bprev
                    bprev[index, 0] = w * I

                    # Fill A matrix with gradients
                    A[index, 0] = w * Ix
                    A[index, 1] = w * Iy

                    # Accumulate AtWA
                    AtWA[0, 0] += w * Ix * Ix
                    AtWA[0, 1] += w * Ix * Iy
                    AtWA[1, 0] += w * Iy * Ix
                    AtWA[1, 1] += w * Iy * Iy


            ## Compute invAtWA
            ## Use the function invertMatrix2x2

            invAtWA = invertMatrix2x2(AtWA)

            u = u0

            ## Iterative solver
            for j in range(self.iterations):
                iu = [int(np.floor(u[0])), int(np.floor(u[1]))]

                if iu[0] < 0 or iu[0] + self.winsize[0] >= prevImg.shape[1] - 1 \
                        or iu[1] < 0 or iu[1] + self.winsize[1] >= prevImg.shape[0] - 1:
                    status[ptidx] = 0
                    break

                bw = computeBilinerWeights(u)  # used if needed for subpixel sampling
                bnext = np.zeros((self.winsize[0] * self.winsize[1], 1))
                AtWbnbp = np.zeros((2, 1))  # 2x1 vector

                for y in range(self.winsize[1]):
                    for x in range(self.winsize[0]):
                        gx = iu[0] + x
                        gy = iu[1] + y
                        index = y * self.winsize[0] + x

                        px = u[0] + x
                        py = u[1] + y
                        x0 = int(np.floor(px))
                        y0 = int(np.floor(py))

                        if x0 < 0 or x0 + 1 >= nextImg.shape[1] or y0 < 0 or y0 + 1 >= nextImg.shape[0]:
                            continue

                        bw = computeBilinerWeights((px, py))

                        Iq = (
                                bw[0] * nextImg[y0, x0] +
                                bw[1] * nextImg[y0, x0 + 1] +
                                bw[2] * nextImg[y0 + 1, x0] +
                                bw[3] * nextImg[y0 + 1, x0 + 1]
                        )

                        w = weights[y, x]
                        bnext[index, 0] = w * Iq
                        diff = bnext[index, 0] - bprev[index, 0]

                        AtWbnbp[0] += A[index, 0] * diff
                        AtWbnbp[1] += A[index, 1] * diff

                AtWA = np.matmul(A.transpose(), A)

                # Solve for deltaU
                deltaU = -np.linalg.inv(AtWA) @ AtWbnbp
                u = u + deltaU.flatten()

                # Early termination condition
                if np.sum(deltaU ** 2) < self.epsilon:
                    break

            nextPts[ptidx] = u + halfWin

        return nextPts, status
