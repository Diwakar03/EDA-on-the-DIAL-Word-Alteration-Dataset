import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate the ratio of red, green, and blue pixels in an image
def calculate_ratios(image_path):
    img = cv2.imread(image_path)
    b, g, r = cv2.split(img)
    total_pixels = img.shape[0] * img.shape[1]
    red_ratio = np.sum(r) / total_pixels
    green_ratio = np.sum(g) / total_pixels
    blue_ratio = np.sum(b) / total_pixels
    return red_ratio, green_ratio, blue_ratio

# Path to the folder containing images
input_folder = 'C:\\Users\\diwak\\Downloads\\Black INK Orig\\Original'

# Initialize lists to store data
pen_names = []
red_ratios = []
green_ratios = []
blue_ratios = []

# Iterate through each pen image
for pen_image in os.listdir(input_folder):
    if pen_image.endswith('.tif'):
        pen_name = os.path.splitext(pen_image)[0]
        pen_names.append(pen_name)

        red_ratio, green_ratio, blue_ratio = calculate_ratios(os.path.join(input_folder, pen_image))
        red_ratios.append(red_ratio)
        green_ratios.append(green_ratio)
        blue_ratios.append(blue_ratio)

# Create a DataFrame to store the data
data = {
    'Pen': pen_names,
    'Red Ratio': red_ratios,
    'Green Ratio': green_ratios,
    'Blue Ratio': blue_ratios
}
df = pd.DataFrame(data)

# Group data by Pen and calculate summary statistics
grouped_data = df.groupby('Pen').agg({'Red Ratio': 'mean', 'Green Ratio': 'mean', 'Blue Ratio': 'mean'})

# Plot boxplots with larger figure size
plt.figure(figsize=(12, 8))  # Adjust width and height as needed
grouped_data.boxplot(rot=45)
plt.title('Average Color Ratios for Each Pen')
plt.xlabel('Color')
plt.ylabel('Average Ratio')
plt.tight_layout()
plt.show()
