import os
import shutil

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
downloads_dir = r"C:\Users\Laptop\Downloads"
assets_dir = os.path.join(base_dir, "assets")

# Copy the 3 files
files_to_copy = {
    "oliveri.svg": "partner-1.svg",
    "picks.jpg": "partner-3.jpg",
    "gelato lab.jpg": "partner-9.jpg"
}

for src_name, target_name in files_to_copy.items():
    src_path = os.path.join(downloads_dir, src_name)
    target_path = os.path.join(assets_dir, target_name)
    
    # Simple logic to find the file even if there are slight spelling differences
    # but based on earlier `ls`, they are named exactly this.
    if os.path.exists(src_path):
        shutil.copy2(src_path, target_path)
        print(f"✅ Copied {src_name} to {target_name}")
    else:
        print(f"⚠️ Source not found: {src_path}")

# Update index.html
index_path = os.path.join(base_dir, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace('src="assets/partner-1.png"', 'src="assets/partner-1.svg"')
html = html.replace('src="assets/partner-3.png"', 'src="assets/partner-3.jpg"')
html = html.replace('src="assets/partner-9.png"', 'src="assets/partner-9.jpg"')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ index.html updated to reference proper file extensions for Oliveri, Picks, and Gelato Lab.")
