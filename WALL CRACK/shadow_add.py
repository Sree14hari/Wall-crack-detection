import cv2
import numpy as np
import os

def add_shadow(img):
    h, w = img.shape[:2]
    top_x, bot_x = np.random.randint(0, w), np.random.randint(0, w)
    mask = np.zeros_like(img)
    polygon = np.array([[[top_x, 0], [bot_x, h], [bot_x+100, h], [top_x+100, 0]]])
    cv2.fillPoly(mask, polygon, (50, 50, 50))  # Dark area
    shadowed = cv2.addWeighted(img, 1.0, mask, 0.5, 0)
    return shadowed

input_dir = "WALL CRACK/shadow_ds/trainA/Positive"
output_dir = "WALL CRACK/shadow_ds/trainB"
os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(input_dir):
    img_path = os.path.join(input_dir, file)
    img = cv2.imread(img_path)
    if img is not None:
        shadow_img = add_shadow(img)
        cv2.imwrite(os.path.join(output_dir, file), shadow_img)
