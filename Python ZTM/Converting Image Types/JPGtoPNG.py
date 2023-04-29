import sys
import os
from PIL import Image

# input folder and output folder
image_folder = sys.argv[1]
converted_folder = sys.argv[2]

# if converted folder doesn't exist, make one
if not os.path.exists(converted_folder):
    os.makedirs(converted_folder)

# loop through files in desired folder
for filename in os.listdir(image_folder):
    image = Image.open(f"{filename}")  # open file

    # split the file into its name and type (grab the name)
    clean_name = os.path.splitext(filename)[0]
    image.save(f'{converted_folder}{clean_name}.jpg',
               "jpg")  # save images i new folder
