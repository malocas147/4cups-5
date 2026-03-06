import os

# 1. First move the generated image
media_path = r"C:\Users\Laptop\.gemini\antigravity\brain\cb36bf15-5e39-4f5f-bcd3-73268ecf66ea\gobelet_simple_1772664705292.png"
asset_path = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website\assets\gobelet_simple.png"
os.system(f'copy "{media_path}" "{asset_path}"')

# 2. Update cafe.html
base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
cafe_path = os.path.join(base_dir, "cafe.html")

with open(cafe_path, "r", encoding="utf-8") as f:
    cafe = f.read()

# Replace the stack image with the single cup, and apply growing scales
# 6 oz -> scale(1.1)
# 8 oz -> scale(1.25)
# 12 oz -> scale(1.4)

import re

# We need to target each gobelet specifically to apply different scales.
# Target 6 oz:
cafe = re.sub(
    r'(<!-- Gobelet 6 oz -->.*?<div class="detailed-image">\s*)<img.*?>',
    r'\1<img src="assets/gobelet_simple.png" alt="Gobelet 6 oz blanc" class="w-full h-full object-contain p-0 origin-bottom" style="transform: scale(1.0);">',
    cafe,
    flags=re.DOTALL
)

# Target 8 oz:
cafe = re.sub(
    r'(<!-- Gobelet 8 oz -->.*?<div class="detailed-image">\s*)<img.*?>',
    r'\1<img src="assets/gobelet_simple.png" alt="Gobelet 8 oz blanc" class="w-full h-full object-contain p-0 origin-bottom" style="transform: scale(1.15);">',
    cafe,
    flags=re.DOTALL
)

# Target 12 oz:
cafe = re.sub(
    r'(<!-- Gobelet 12 oz -->.*?<div class="detailed-image">\s*)<img.*?>',
    r'\1<img src="assets/gobelet_simple.png" alt="Gobelet 12 oz blanc" class="w-full h-full object-contain p-0 origin-bottom" style="transform: scale(1.35);">',
    cafe,
    flags=re.DOTALL
)


with open(cafe_path, "w", encoding="utf-8") as f:
    f.write(cafe)

print("✅ cafe.html: Updated 6oz, 8oz, 12oz images with progressive scaling.")
