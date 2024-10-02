import os
import cv2
import numpy as np

# Define the list of valid RGB values
valid_rgb_values = [
    [0.0, 0.0, 0.0],
    [128.0, 0.0, 0.0],
    [0.0, 128.0, 128.0],
    [128.0, 0.0, 128.0],
    [128.0, 128.0, 0.0],
    [0.0, 128.0, 0.0],
    [0.0, 0.0, 128.0],
]


# Function to process PNG files in a directory
def process_png_files(directory):
    # Iterate through PNG files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            # Read the PNG file
            print(filename)
            image = cv2.imread(os.path.join(directory, filename))

            # Iterate through each pixel in the image
            for y in range(image.shape[0]):
                for x in range(image.shape[1]):
                    # Check if the pixel's color is not in the list of valid RGB values
                    pixel_color = image[y, x].tolist()
                    if pixel_color not in valid_rgb_values:
                        # Set the pixel's color to black
                        image[y, x] = [0, 0, 0]

            # Save the modified image
            cv2.imwrite(os.path.join(directory, f"processed_{filename}"), image)


# Example usage: Process PNG files in the current directory
process_png_files(".")
