import os

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
cafe_path = os.path.join(base_dir, "cafe.html")

with open(cafe_path, "r", encoding="utf-8") as f:
    cafe = f.read()

old_img = '<img src="assets/gobelet_4oz.png" alt="Gobelet 4oz avec dimensions" class="w-full h-full object-contain p-4">'
# Removed p-4 (padding reduces size), added scale-125 (zoom by 25%) and origin-center just in case.
new_img = '<img src="assets/gobelet_4oz.png" alt="Gobelet 4oz avec dimensions" class="w-full h-full object-contain p-0 scale-125 origin-center">'

if old_img in cafe:
    cafe = cafe.replace(old_img, new_img)
    with open(cafe_path, "w", encoding="utf-8") as f:
        f.write(cafe)
    print("✅ cafe.html: Zoomed in on the 4oz image.")
else:
    print("⚠️ 4oz image tag not found. Checking if p-4 was already modified.")
