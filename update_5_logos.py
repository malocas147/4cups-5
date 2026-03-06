import os
import shutil
import re

downloads_dir = r"C:\Users\Laptop\Downloads"
base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
assets_dir = os.path.join(base_dir, "assets")

# Mapping downloads to target assets
# 4: La Grillardière
# 5: Nouri
# 8: Al Itkane
# 10: Adoro Cafe
# 11: Wok 4you
files_to_copy = {
    "Gemini_Generated_Image_g4yblog4yblog4yb.png": "partner-4.png",
    "Gemini_Generated_Image_qt1koyqt1koyqt1k.png": "partner-5.png",
    "ALITKANE.webp": "partner-8.webp",
    "Gemini_Generated_Image_c3zz7qc3zz7qc3zz.png": "partner-10.png",
    "logo-white.be222262894cc65b4f6d.png": "partner-11.png"
}

index_path = os.path.join(base_dir, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

for src_name, target_name in files_to_copy.items():
    src_path = os.path.join(downloads_dir, src_name)
    target_path = os.path.join(assets_dir, target_name)
    
    if os.path.exists(src_path):
        shutil.copy2(src_path, target_path)
        print(f"✅ Copied {src_name} to {target_name}")
        
        # Determine the base ID (e.g., partner-4) to update HTML regardless of previous extension
        base_id = target_name.split('.')[0] # e.g., partner-4
        new_ext = target_name.split('.')[1] # e.g., webp or png
        
        # Regex to update either .png, .jpg, .svg, etc. to the new extension
        pattern = rf'src="assets/{base_id}\.[a-z]+"'
        replacement = rf'src="assets/{base_id}.{new_ext}"'
        html = re.sub(pattern, replacement, html)
    else:
        print(f"⚠️ Source not found: {src_path}")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ index.html updated with newly assigned specific partner logos.")
