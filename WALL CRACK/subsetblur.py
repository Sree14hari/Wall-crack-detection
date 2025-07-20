import os
import shutil

# Your original dataset paths
original_trainA = 'WALL CRACK/shadow_ds/trainA'
original_trainB = 'WALL CRACK/shadow_ds/trainB'

# New lightweight dataset for training
mini_dataset_root = '.WALL CRACK/MiniBlur'
mini_trainA = os.path.join(mini_dataset_root, 'trainA')
mini_trainB = os.path.join(mini_dataset_root, 'trainB')

# Create directories
os.makedirs(mini_trainA, exist_ok=True)
os.makedirs(mini_trainB, exist_ok=True)

# Copy first 500 images
for i, fname in enumerate(sorted(os.listdir(original_trainA))):
    if i >= 500:
        break
    shutil.copy(os.path.join(original_trainA, fname), mini_trainA)

for i, fname in enumerate(sorted(os.listdir(original_trainB))):
    if i >= 500:
        break
    shutil.copy(os.path.join(original_trainB, fname), mini_trainB)

print("✅ Copied first 500 images to blur2clear/trainA and trainB.")
