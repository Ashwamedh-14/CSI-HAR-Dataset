import os
import shutil
from sklearn.model_selection import train_test_split

dataset_dir = 'CSI-HAR-Dataset'
categories = ['bend', 'fall', 'lie down', 'run', 'sitdown', 'standup', 'walk']

train_dir = os.path.join(dataset_dir, 'Train')
test_dir = os.path.join(dataset_dir, 'Test')
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

for category in categories:
    category_dir = os.path.join(dataset_dir, category)
    files = os.listdir(category_dir)
    train_files, test_files = train_test_split(files, test_size=0.2, random_state=42)
    
    # Create category directories in train and test folders
    os.makedirs(os.path.join(train_dir, category), exist_ok=True)
    os.makedirs(os.path.join(test_dir, category), exist_ok=True)
    
    # Move files to train and test directories
    for file in train_files:
        shutil.move(os.path.join(category_dir, file), os.path.join(train_dir, category, file))
    for file in test_files:
        shutil.move(os.path.join(category_dir, file), os.path.join(test_dir, category, file))
