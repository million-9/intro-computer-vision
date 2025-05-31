import numpy as np

def computeBilinerWeights(q):

    ## - Compute bilinear weights for point q
    ## - Entry 0 weight for pixel (x, y)
    ## - Entry 1 weight for pixel (x + 1, y)
    ## - Entry 2 weight for pixel (x, y + 1)
    ## - Entry 3 weight for pixel (x + 1, y + 1)

    x, y = q
    x0 = int(np.floor(x))
    y0 = int(np.floor(y))
    a = x - x0
    b = y - y0

    weights = [
        (1 - a) * (1 - b),  # top-left (x, y)
        a * (1 - b),        # top-right (x+1, y)
        (1 - a) * b,        # bottom-left (x, y+1)
        a * b               # bottom-right (x+1, y+1)
    ]
    return weights


def computeGaussianWeights(winsize, sigma):

    ## - Fill matrix with gaussian weights
    ## - Note, the center is ((winSize.width - 1) / 2, (winSize.height - 1) / 2)

    w, h = winsize
    cx = (w - 1) / 2.0
    cy = (h - 1) / 2.0

    weights = np.zeros((h, w), dtype=np.float64)
    for y in range(h):
        for x in range(w):
            x_hat = (cx - x) / w
            y_hat = (cy - y) / h
            weights[y, x] = np.exp(-(x_hat**2 + y_hat**2) / (2 * sigma**2))
    return weights

def invertMatrix2x2(A):

    ## - Compute the inverse of the 2 x 2 Matrix A

    a, b = A[0, 0], A[0, 1]
    c, d = A[1, 0], A[1, 1]
    det = a * d - b * c

    if abs(det) < 1e-10:
        return np.zeros_like(A)  # Singular matrix

    invA = (1.0 / det) * np.array([[d, -b],
                                   [-c, a]])
    return invA

