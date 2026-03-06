import os
import re

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
cafe_path = os.path.join(base_dir, "cafe.html")

with open(cafe_path, "r", encoding="utf-8") as f:
    cafe = f.read()

# Replace the arbitrary scale class with an inline style
old_img = '<img src="assets/gobelet_4oz.png" alt="Gobelet 4oz avec dimensions" class="w-full h-full object-contain p-0 scale-[1.35] origin-center">'
new_img = '<img src="assets/gobelet_4oz.png" alt="Gobelet 4oz avec dimensions" class="w-full h-full object-contain p-0 origin-center" style="transform: scale(1.6);">'

if old_img in cafe:
    cafe = cafe.replace(old_img, new_img)
    with open(cafe_path, "w", encoding="utf-8") as f:
        f.write(cafe)
    print("✅ cafe.html: Replaced tailwind class with inline style scale(1.6)")
else:
    # try regex just in case
    pattern = re.compile(
        r'(<img src="assets/gobelet_4oz\.png" alt="Gobelet 4oz avec dimensions"[^>]*?)(?:scale-\[1.35\]|scale-125|scale-150)([^>]*?>)'
    )
    if pattern.search(cafe):
        cafe = pattern.sub(r'\1\2', cafe)
        # inject style attribute
        cafe = cafe.replace('class="w-full h-full object-contain p-0  origin-center">', 'class="w-full h-full object-contain p-0 origin-center" style="transform: scale(1.6);">')
        with open(cafe_path, "w", encoding="utf-8") as f:
            f.write(cafe)
        print("✅ cafe.html: Updated 4oz image to inline style via regex.")
    else:
        print("⚠️ 4oz image tag not found.")
