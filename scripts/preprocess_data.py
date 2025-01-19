# import warnings
import numpy as np
import matplotlib.pyplot as plt
import os
import math
from PIL import Image
from sklearn.model_selection import train_test_split
import shutil
import glob

# warnings.filterwarnings("ignore")
ROOT_DIR = "data/raw/brain_tumor_dataset"
number_of_images = {}

# Loop through each directory (yes/no)
for dir_name in os.listdir(ROOT_DIR):
    dir_path = os.path.join(ROOT_DIR, dir_name)
    # Only process if it's a directory
    if os.path.isdir(dir_path):
        number_of_images[dir_name] = len(os.listdir(dir_path))

print("Number of images in each class:")
for class_name, count in number_of_images.items():
    print(f"{class_name}: {count} images")

# Get only the binary classes (yes/no) by explicitly filtering
types = [d for d in os.listdir(ROOT_DIR) if d in ['yes', 'no']]
print("\nClasses in the dataset:", types)

'''
we will split the datat such that:
* 70% for Train Data
* 15% for Validation
* 15% for Testing
'''

# Create a training folder
def dataFolder(path, split):
    if not os.path.exists("./{path}"):
        os.mkdir("./{path}")

        for dir in os.listdir(ROOT_DIR):
            os.makedirs(f"./{path}/{dir}")
            image_list = os.listdir(os.path.join(ROOT_DIR, dir))

            if len(image_list) < math.floor(0.7*number_of_images[dir] - 2):
                raise ValueError(f"Insufficient images in {dir} class")
            
            for img in np.random.choice(a = os.listdir(os.path.join(ROOT_DIR, dir)), 
                                        size = (math.floor(split*number_of_images[dir]) - 2),
                                        replace = False):
                
                O = os.path.join(ROOT_DIR, dir, img)
                D = os.path.join("./{path}", dir)
                shutil.copy(O, D)
                os.remove(O)

    else:
        print(f"{path} folder already exists. Skipping...")

def ratio(train_ratio, validation_ratio, test_ratio):
    dataFolder("train", train_ratio)
    dataFolder("validation", validation_ratio)
    dataFolder("test", test_ratio)
    
