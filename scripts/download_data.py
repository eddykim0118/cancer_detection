import kagglehub as kh

path = kh.dataset_download("navoneel/brain-mri-images-for-brain-tumor-detection")

output_file = "BrainTumorData.zip"

print("Path to dataset files:", path)