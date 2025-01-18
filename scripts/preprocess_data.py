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
