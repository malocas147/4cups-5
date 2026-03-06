import os
import re

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Remove the entire div or img tag for Nouri logo.
# The HTML looks like:
# <img src="assets/partner-5-v2.png" alt="Logo Nouri" class="max-w-full max-h-full object-contain transition-all duration-300">
# The image might be inside a list item or a container. Wait, looking at grep, it's just an <img> tag. Let's see if we can find its <div> container or just delete the <img> tag. If it's just an <img> tag, we can remove it.

# Let's see the context of the img tag first to be safe, but a regex can remove the <img> tag.
pattern = re.compile(r'\s*<img[^>]*src="assets/partner-5-v2\.png"[^>]*>')
html = pattern.sub('', html)

# Also check for partner-5.png just in case
pattern2 = re.compile(r'\s*<img[^>]*src="assets/partner-5\.png"[^>]*>')
html = pattern2.sub('', html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)
    
print("Removed Nori logo from index.html")
