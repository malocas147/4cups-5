import os
import re

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
cafe_path = os.path.join(base_dir, "cafe.html")

with open(cafe_path, "r", encoding="utf-8") as f:
    html = f.read()

# Current states based on previous code
# 4oz: style="transform: scale(1.6);"
# 6oz: style="transform: scale(0.85);"
# 8oz: style="transform: scale(1.15);"
# 12oz: style="transform: scale(1.35);"

# Let's recalibrate:
# 4oz is tightly cropped, so scale down
# 6oz, 8oz, 12oz have wide whitespace, so scale up progressively.
# All should stick to the bottom so they look aligned on a table.

replacements = [
    (r'<img src="assets/gobelet_4oz\.png"([^>]+)style="transform: scale\(1\.6\);"',
     r'<img src="assets/gobelet_4oz.png"\1style="transform: scale(0.8); transform-origin: bottom;"'),
     
    (r'<img src="assets/gobelet_6oz\.png"([^>]+)style="transform: scale\(0\.85\);"',
     r'<img src="assets/gobelet_6oz.png"\1style="transform: scale(1.1);"'),
     
    (r'<img src="assets/gobelet_8oz\.png"([^>]+)style="transform: scale\(1\.15\);"',
     r'<img src="assets/gobelet_8oz.png"\1style="transform: scale(1.25);"'),
     
    (r'<img src="assets/gobelet_12oz\.png"([^>]+)style="transform: scale\(1\.35\);"',
     r'<img src="assets/gobelet_12oz.png"\1style="transform: scale(1.4);"'),
]

for pattern, repl in replacements:
    html = re.sub(pattern, repl, html)

# Fix the origin-center on the 4oz to origin-bottom
html = html.replace('origin-center', 'origin-bottom')

with open(cafe_path, "w", encoding="utf-8") as f:
    f.write(html)
    
print("✅ cafe.html cup zoom ratios adjusted.")
