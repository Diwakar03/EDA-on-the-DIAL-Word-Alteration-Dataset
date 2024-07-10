import os
import cv2
import numpy as np

# Function to split an image into its RGB channels and calculate mean
def split_and_save(image_path, output_folder):
    # Read the image
    img = cv2.imread(image_path)

    # Split the image into RGB channels
    b, g, r = cv2.split(img)

    # Calculate mean of each channel
    mean_b = np.mean(b)
    mean_g = np.mean(g)
    mean_r = np.mean(r)

    # Save mean values to text file
    with open(os.path.join(output_folder, 'mean_values.txt'), 'a') as f:
        f.write(f'{image_path}, Mean B: {mean_b}, Mean G: {mean_g}, Mean R: {mean_r}\n')

    # Save each channel as a separate image
    cv2.imwrite(os.path.join(output_folder, f'red_{os.path.basename(image_path)}'), r)
    cv2.imwrite(os.path.join(output_folder, f'green_{os.path.basename(image_path)}'), g)
    cv2.imwrite(os.path.join(output_folder, f'blue_{os.path.basename(image_path)}'), b)

# Path to the folder containing pen images
input_folder = 'C:\\Users\\diwak\\Downloads\\Black INK Orig\\Original'

# Path to the folder where output will be saved
output_folder = 'C:\\Users\\diwak\\Downloads\\Black INK Orig\\newimg'
# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate through each image in the input folder
for pen_image in os.listdir(input_folder):
    if pen_image.endswith('.tif'):
        pen_image_path = os.path.join(input_folder, pen_image)
        split_and_save(pen_image_path, output_folder)
