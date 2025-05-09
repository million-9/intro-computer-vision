import cv2

def scale_down(images):
    """
    Scales down a list of images by a factor of 0.5 in both dimensions.

    Parameters:
    - images (list of ndarray): List of OpenCV image arrays.

    Returns:
    - List of scaled-down images.
    """
    scaled_images = []
    for img in images:
        height, width = img.shape[:2]
        scaled = cv2.resize(img, (width // 2, height // 2), interpolation=cv2.INTER_AREA)
        scaled_images.append(scaled)
    return scaled_images
