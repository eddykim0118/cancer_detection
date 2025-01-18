import os
import kagglehub as kh

def download_dataset(dataset_name, output_dir):
    """
    Download the dataset from Kaggle and save it to the specified output directory.
    Skips downloading if the directory already exists.
    """
    # Check if data already exists
    if os.path.exists(output_dir):
        print(f"Dataset already exists at {output_dir}. Skipping download.")
        return output_dir

    # Download dataset if not already present
    print(f"Downloading dataset {dataset_name}...")
    path = kh.dataset_download(dataset_name)
    print(f"Dataset downloaded to: {path}")

    # Move dataset to the desired directory
    os.makedirs(output_dir, exist_ok=True)
    if os.path.isdir(path):
        os.rename(path, output_dir)
    print(f"Dataset organized at: {output_dir}")
    return output_dir

if __name__ == "__main__":
    # Dataset and output path configuration
    dataset_name = "navoneel/brain-mri-images-for-brain-tumor-detection"
    output_dir = "./data/raw/brain_tumor_dataset"
    
    # Download and organize dataset
    dataset_path = download_dataset(dataset_name, output_dir)
    print(f"Dataset is ready at: {dataset_path}")
