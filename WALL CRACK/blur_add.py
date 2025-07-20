import cv2
import os

def add_blur(img):
    return cv2.GaussianBlur(img, (9, 9), 0)

input_dir = "WALL CRACK/blur_ds/trainA/Positive"
output_dir = "WALL CRACK/blur_ds/trainB"

os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(input_dir):
    img_path = os.path.join(input_dir, file)
    img = cv2.imread(img_path)
    if img is not None:
        blur_img = add_blur(img)
        cv2.imwrite(os.path.join(output_dir, file), blur_img)
