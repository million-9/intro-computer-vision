from loadnsave import *
from resize import *
from colorchan import *
if __name__ == "__main__":

    #load and Save
    img1 = cv2.imread("resources/img.png")
    images = [img1]
    filenames = ["img1.jpg"]

    show_images(images)
    save_images(images, filenames)

    #scale
    scaled_images = scale_down(images)
    show_images(scaled_images, ["Scaled1"])

    #channel seperation
    channel_scaled_images = separate_channels(scaled_images)
    all_channels_sflat = [img for triplet in channel_scaled_images for img in triplet]
    names = ["Img1 - Blue", "Img1 - Green", "Img1 - Red"]
    show_images(all_channels_sflat, names)
