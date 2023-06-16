import os
from PIL import Image
import numpy as np

# Create the "output" subfolder if it doesn't exist
output_folder = "output"
if not os.path.exists(output_folder):
    print("Creating output folder...")
    os.makedirs(output_folder)

# Get a list of all .png files in the current directory
png_files = [file for file in os.listdir('.') if file.endswith('.png')]

# Process each .png file
for png_file in png_files:
    # Open the image using PIL
    image = Image.open(png_file)

    # Extract the color channels as numpy arrays
    red_channel, green_channel, blue_channel, _ = image.split()

    # Convert the color channels to float32 arrays for calculations
    red_channel = np.array(red_channel, dtype=np.float32) / 255.0
    green_channel = np.array(green_channel, dtype=np.float32) / 255.0

    # Calculate the blue channel using the formula: blue_channel = sqrt(1 - (red_channel^2 + green_channel^2))
    blue_channel = np.sqrt(1 - np.clip((red_channel ** 2 + green_channel ** 2), 0.0, 1.0))

    # Convert the color channels back to uint8
    red_channel = np.array(red_channel * 255.0, dtype=np.uint8)
    green_channel = np.array(green_channel * 255.0, dtype=np.uint8)
    blue_channel = np.array(blue_channel * 255.0, dtype=np.uint8)

    # Merge the color channels back together and save the image
    new_image = Image.merge('RGB', (Image.fromarray(red_channel), Image.fromarray(green_channel), Image.fromarray(blue_channel)))
    new_image.save(os.path.join(output_folder, png_file))

print("All images processed.")
