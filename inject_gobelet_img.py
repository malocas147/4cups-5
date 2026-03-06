import os

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
cafe_path = os.path.join(base_dir, "cafe.html")

with open(cafe_path, "r", encoding="utf-8") as f:
    cafe = f.read()

# Replace the emoji placeholders with the image for gobelets
# The current placeholder looks like:
# <span style="color:var(--text-secondary); font-size:4rem;">☕</span>
# <span style="color:var(--text-secondary); font-size:4.5rem;">☕</span>
# <span style="color:var(--text-secondary); font-size:5rem;">☕</span>
# <span style="color:var(--text-secondary); font-size:6rem;">🥤</span>

import re

# We will replace these specific spans within the gobelet detailed-image block
# Only replace emojis corresponding to the gobelets (☕, 🥤) and not others
image_html = '<img src="assets/gobelet_blanc.png" alt="Gobelet en carton blanc empilé" class="w-full h-full object-contain p-4">'

cafe = re.sub(
    r'<span style="color:var\(--text-secondary\); font-size:[0-9\.]+rem;">☕</span>',
    image_html,
    cafe
)

cafe = re.sub(
    r'<span style="color:var\(--text-secondary\); font-size:[0-9\.]+rem;">🥤</span>',
    image_html,
    cafe
)

with open(cafe_path, "w", encoding="utf-8") as f:
    f.write(cafe)

print("✅ cafe.html: Gobelet placeholders replaced by image")
