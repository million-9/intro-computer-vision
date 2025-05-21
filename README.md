📷 Introduction to Computer Vision

Welcome to the Introduction to Computer Vision repository! This collection comprises exercises and implementations from the Computer Vision course at Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU). The assignments are designed to provide hands-on experience with fundamental computer vision techniques using Python and OpenCV.

🗂️ Introduction

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

🗂️ Vectorization

📷 Box Filter Implementation

Implements a manual box filter (mean filter) operation using nested loops in Python and NumPy. This task is part of the vectorization exercise aimed at understanding the performance and correctness differences between loop-based and vectorized approaches. A grayscale image is fetched from an online source and processed using a sliding window method to compute the local mean.

🧪 Implemented Functions

1. `box_filter_loop(img, box_width, box_height)`
   Applies a box filter using nested loops. For each pixel, the function computes the average of surrounding pixel values defined by the kernel size.

2. Overflow Handling
   Pixel values are stored as `uint8`, which can cause overflow during summation. To prevent this, each pixel is explicitly cast to `int` before addition:

   ```python
   local_sum += int(img[filter_y, filter_x])
   ```

   Alternatively, the input image is converted to a larger data type at the start:

   ```python
   img = img.astype(np.int32)
   ```

3. `show(img)`
   Displays grayscale or color images using `matplotlib`. Supports concatenation of image lists for side-by-side visualization.
