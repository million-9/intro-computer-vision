📷 Introduction to Computer Vision


Welcome to the Introduction to Computer Vision repository! This collection comprises exercises and implementations from the Computer Vision course at Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU). The assignments are designed to provide hands-on experience with fundamental computer vision techniques using Python and OpenCV.

🗂️ Repository Structure

introduction/main/: Contains the main scripts for loading, displaying, saving, and processing images.

introduction/resources/: Includes sample images used for testing and demonstration purposes.

🧪 Implemented Functions

1. Image Loading and Display
show_images(images, window_names=None):
Displays a list of images in separate OpenCV windows. The program waits until a key is pressed before closing all windows.

2. Save_images(images, filenames, folder='resources'):
Saves a list of images to the specified folder with the given filenames.

3. Image Resizing
scale_down(images):
Resizes each image in the provided list by a factor of 0.5 in both width and height using OpenCV's resize function.

4. Color Channel Separation
separate_channels(images):
Separates each image into its Blue, Green, and Red channels. Returns a list where each element is a list of three images corresponding to the individual color channels.

🛠️ Getting Started
Prerequisites
Ensure you have Python 3.x installed. Install the required packages

📁 Sample Images
The resources folder contains sample images used to test and demonstrate the implemented functions. You can replace these with your own images as needed.
