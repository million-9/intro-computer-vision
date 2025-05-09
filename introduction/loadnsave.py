import cv2
import os


def show_images(images, window_names=None):
    """
    Displays each image in a separate OpenCV window.

    Parameters:
    - images (list of ndarray): List of OpenCV image arrays.
    - window_names (list of str): Optional list of window titles. Defaults to Image0, Image1, ...
    """
    if window_names is None:
        window_names = [f"Image{i}" for i in range(len(images))]

    for img, name in zip(images, window_names):
        cv2.imshow(name, img)

    # Wait for a key press indefinitely
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()


def save_images(images, filenames, folder='resources'):
    """
    Saves images to the specified folder with the given filenames.

    Parameters:
    - images (list of ndarray): List of OpenCV image arrays.
    - filenames (list of str): List of filenames to save each image as.
    - folder (str): Folder to save images in.
    """
    os.makedirs(folder, exist_ok=True)

    for img, fname in zip(images, filenames):
        path = os.path.join(folder, fname)
        success = cv2.imwrite(path, img)
        if not success:
            print(f"Failed to save image: {path}")
        else:
            print(f"Saved image: {path}")
