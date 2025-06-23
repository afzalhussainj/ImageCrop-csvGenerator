from PIL import Image
import os

# === Configuration ===
input_folder = "watches"        # folder with original images
output_folder = "watches_cropped"      # folder to save cropped images
overwrite = False              # Set to True to overwrite originals

# === Make output folder if needed ===
if not overwrite and not os.path.exists(output_folder):
    os.makedirs(output_folder)

# === Crop function ===
def crop_to_square(image):
    width, height = image.size
    min_dim = min(width, height)
    left = (width - min_dim) // 2
    top = (height - min_dim) // 2
    right = left + min_dim
    bottom = top + min_dim
    return image.crop((left, top, right, bottom))

# === Process all images ===
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        input_path = os.path.join(input_folder, filename)
        with Image.open(input_path) as img:
            cropped_img = crop_to_square(img)
            save_path = input_path if overwrite else os.path.join(output_folder, filename)
            cropped_img.save(save_path)
            print(f"Cropped and saved: {save_path}")

print("✅ Done cropping all images!")
 