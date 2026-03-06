import os
import re

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Pattern for the div containing partner-16.png
pattern = re.compile(r'\s*<div[^>]*>\s*<img src="assets/partner-16\.png"[^>]*>\s*</div>')
html = pattern.sub('', html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Removed all instances of Kool Coffee (partner-16) from the carousels.")
