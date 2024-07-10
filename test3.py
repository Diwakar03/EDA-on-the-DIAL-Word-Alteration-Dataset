import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate the ratio of red, green, and blue pixels in an image
def calculate_ratios(img):
    b, g, r = cv2.split(img)
    total_pixels = img.shape[0] * img.shape[1]
    red_ratio = np.sum(r) / total_pixels
    green_ratio = np.sum(g) / total_pixels
    blue_ratio = np.sum(b) / total_pixels
    return red_ratio, green_ratio, blue_ratio

# Path to the folder containing images
input_folder = 'C:\\Users\\diwak\\Downloads\\Black INK Orig\\Original'

# Initialize lists to store data
red_ratios = []
green_ratios = []
blue_ratios = []

# Sort images in the folder
image_paths = sorted([os.path.join(input_folder, image) for image in os.listdir(input_folder) if image.endswith('.tif')])

# Loop through images in batches of 18
for i in range(0, len(image_paths), 18):
    batch_red_ratios = []
    batch_green_ratios = []
    batch_blue_ratios = []

    # Iterate through images in the batch
    for j in range(i, min(i + 18, len(image_paths))):
        img = cv2.imread(image_paths[j])
        red_ratio, green_ratio, blue_ratio = calculate_ratios(img)
        batch_red_ratios.append(red_ratio)
        batch_green_ratios.append(green_ratio)
        batch_blue_ratios.append(blue_ratio)

    # Append mean ratios for the batch to the main lists
    red_ratios.append(batch_red_ratios)
    green_ratios.append(batch_green_ratios)
    blue_ratios.append(batch_blue_ratios)

# Create DataFrames for each color
red_df = pd.DataFrame(red_ratios, columns=[f'Red_{i+1}' for i in range(18)])
green_df = pd.DataFrame(green_ratios, columns=[f'Green_{i+1}' for i in range(18)])
blue_df = pd.DataFrame(blue_ratios, columns=[f'Blue_{i+1}' for i in range(18)])

# Plot boxplots for each color
plt.figure(figsize=(12, 8))
red_df.boxplot()
plt.title('Red Color Ratios for Each Batch')
plt.xlabel('Batch')
plt.ylabel('Ratio')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))
green_df.boxplot()
plt.title('Green Color Ratios for Each Batch')
plt.xlabel('Batch')
plt.ylabel('Ratio')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))
blue_df.boxplot()
plt.title('Blue Color Ratios for Each Batch')
plt.xlabel('Batch')
plt.ylabel('Ratio')
plt.tight_layout()
plt.show()
