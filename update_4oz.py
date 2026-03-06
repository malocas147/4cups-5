import os
import re

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
cafe_path = os.path.join(base_dir, "cafe.html")

with open(cafe_path, "r", encoding="utf-8") as f:
    cafe = f.read()

# We need to replace the image src ONLY for the 4oz cup block.
# The block starts with <!-- Gobelet 4 oz --> or something similar, up to <h3>Gobelet 4 oz</h3>.

# Using a regex to find the Gobelet 4 oz block and replace the img inside it.
pattern = re.compile(
    r'(<div class="detailed-card fade-in-up".*?)'
    r'(<img src="assets/gobelet_blanc\.png" alt="Gobelet en carton blanc empilé" class="w-full h-full object-contain p-4">)'
    r'(.*?<h3>Gobelet 4 oz</h3>)',
    re.DOTALL
)

new_img = '<img src="assets/gobelet_4oz.png" alt="Gobelet 4oz avec dimensions" class="w-full h-full object-contain p-4">'

cafe_new = pattern.sub(r'\1' + new_img + r'\3', cafe)

with open(cafe_path, "w", encoding="utf-8") as f:
    f.write(cafe_new)

print("✅ cafe.html: Updated 4oz gobelet image")
