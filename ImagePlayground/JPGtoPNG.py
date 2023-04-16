#JPGtoPNG converter
#Terminal: python JPGtoPNG.py Pictures/ Output/

import sys
import os
from PIL import Image

#grabs arguments from command linee
image_folder = sys.argv[1] #Pictures/

output_folder = sys.argv[2] #Output/

#check if Output/ exist, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
#loop through Pictures, convert to png
for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{filename}")
    clean_name = os.path.splitext(filename)[0]
    img.save(f"{output_folder} {clean_name}.png", "PNG")
    print("Image saved")
#save them to a new folder