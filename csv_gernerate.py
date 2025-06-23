import os
import csv

# === Configuration ===
image_folder = "watches_cropped"  # Folder containing your images
output_csv = "watches_cropped_urls.csv"
shopify_url_template = "https://cdn.shopify.com/s/files/1/0699/9185/8339/files/{}"

# === Gather image URLs ===
image_data = []
for filename in os.listdir(image_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        safe_filename = filename.replace(" ", "_")
        full_url = shopify_url_template.format(safe_filename)
        image_data.append([filename, full_url])

# === Write to CSV ===
with open(output_csv, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Image Name", "Shopify URL"])  # header
    writer.writerows(image_data)

print(f"✅ CSV created: {output_csv}")
