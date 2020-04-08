import sys
import os
from PIL import Image

# grabs the first and 2nd arg
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)

# check if new exists, else create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]  # splits file name and type into tuple
    img.save(f'{output_folder}{clean_name}.png', 'png')  # adds png file name on each file and saves as png

