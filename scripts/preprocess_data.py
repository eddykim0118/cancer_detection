import os
from PIL import Image
from sklearn.model_selection import train_test_split
import shutil

def preprocess_images(input_dir, output_dir, img_size=(128, 128)):
    """
    Resize images and organize them into train/test splits.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Iterate through class folders (e.g., "no" and "yes")
    for label in ["no", "yes"]:
        input_folder = os.path.join(input_dir, label)
        output_folder = os.path.join(output_dir, label)
        os.makedirs(output_folder, exist_ok=True)

        for img_name in os.listdir(input_folder):
            img_path = os.path.join(input_folder, img_name)
            try:
                img = Image.open(img_path)
                img = img.resize(img_size)
                img.save(os.path.join(output_folder, img_name))
            except Exception as e:
                print(f"Error processing image {img_name}: {e}")

    print(f"Preprocessed images saved to {output_dir}")

if __name__ == "__main__":
    input_dir = "./data/raw/brain_tumor_dataset"
    output_dir = "./data/processed/brain_tumor_dataset"
    preprocess_images(input_dir, output_dir)
