import cv2
import numpy as np

def separate_channels(images):
    """
    Separates a list of BGR images into their blue, green, and red channel images.

    Parameters:
    - images (list of ndarray): List of BGR images.

    Returns:
    - List of lists: Each sublist contains 3 images [blue_img, green_img, red_img] for one input.
    """
    separated = []

    for image in images:
        zeros = np.zeros_like(image)

        blue_img = zeros.copy()
        green_img = zeros.copy()
        red_img = zeros.copy()

        blue_img[:, :, 0] = image[:, :, 0]
        green_img[:, :, 1] = image[:, :, 1]
        red_img[:, :, 2] = image[:, :, 2]

        separated.append([blue_img, green_img, red_img])

    return separated
