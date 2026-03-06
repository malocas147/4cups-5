import os
import re

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
cafe_path = os.path.join(base_dir, "cafe.html")

with open(cafe_path, "r", encoding="utf-8") as f:
    cafe = f.read()

# Current tag has scale-125
# <img src="assets/gobelet_4oz.png" alt="Gobelet 4oz avec dimensions" class="w-full h-full object-contain p-0 scale-125 origin-center">
old_img = '<img src="assets/gobelet_4oz.png" alt="Gobelet 4oz avec dimensions" class="w-full h-full object-contain p-0 scale-125 origin-center">'

# Increased to scale-150. If there are clipping issues, we might need overflow-visible on detailed-image, 
# but detailed-image has a fixed height usually. Let's start by trying scale-150.
new_img = '<img src="assets/gobelet_4oz.png" alt="Gobelet 4oz avec dimensions" class="w-full h-full object-contain p-0 scale-[1.35] origin-center">'

if old_img in cafe:
    cafe = cafe.replace(old_img, new_img)
    with open(cafe_path, "w", encoding="utf-8") as f:
        f.write(cafe)
    print("✅ cafe.html: Zoomed in on the 4oz image further (scale-135).")
else:
    # Try a regex just in case it was modified differently
    pattern = re.compile(
        r'(<img src="assets/gobelet_4oz\.png" alt="Gobelet 4oz avec dimensions" class="[^"]*?)scale-125([^"]*?">)'
    )
    if pattern.search(cafe):
        cafe = pattern.sub(r'\1scale-[1.35]\2', cafe)
        with open(cafe_path, "w", encoding="utf-8") as f:
            f.write(cafe)
        print("✅ cafe.html: Zoomed in on the 4oz image further using regex.")
    else:
        print("⚠️ 4oz image tag not found. Check if it's already updated.")
