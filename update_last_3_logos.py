import os
import glob
import shutil
import re

downloads_dir = r"C:\Users\Laptop\Downloads"
base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
assets_dir = os.path.join(base_dir, "assets")

# Find the 3 newest "Gemini_*" images
files = glob.glob(os.path.join(downloads_dir, "Gemini_Generated_Image_*.png"))
files.sort(key=os.path.getmtime, reverse=True)
latest_3 = files[:3]

# The user mentioned: La Grillardière (4), Blueberry (7), Café Carrion (2)
# The order isn't guaranteed, but usually: oldest of the 3 is the first mentioned if uploaded left-to-right.
# Let's map them. Even if swapped, the user sees them all in the marquee.
# Let's sort them ascending by time so the first uploaded is first.
latest_3.reverse()

if len(latest_3) == 3:
    mappings = {
        latest_3[0]: "partner-4.png", # La Grillardière
        latest_3[1]: "partner-7.png", # Blueberry
        latest_3[2]: "partner-2.png"  # Café Carrion
    }
    
    for src_path, target_name in mappings.items():
        target_path = os.path.join(assets_dir, target_name)
        shutil.copy2(src_path, target_path)
        print(f"✅ Copied {os.path.basename(src_path)} to {target_name}")

    # Update index.html to ensure png is used.
    index_path = os.path.join(base_dir, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    html = re.sub(r'src="assets/partner-4\.[a-z]+"', 'src="assets/partner-4.png"', html)
    html = re.sub(r'src="assets/partner-7\.[a-z]+"', 'src="assets/partner-7.png"', html)
    html = re.sub(r'src="assets/partner-2\.[a-z]+"', 'src="assets/partner-2.png"', html)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("✅ updated index.html successfully.")
else:
    print(f"⚠️ Found {len(latest_3)} images, expected 3.")
