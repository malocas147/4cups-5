import os
import re

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# I will find all divs containing partner-11.png and remove them.
# The div looks like:
#                     <div
#                         class="flex-shrink-0 w-48 h-24 bg-background border border-border rounded-xl shadow-sm flex items-center justify-center p-4">
#                         <img src="assets/partner-11.png" alt="Logo Wok 4you"
#                             class="max-w-full max-h-full object-contain transition-all duration-300">
#                     </div>

pattern = re.compile(r'\s*<div[^>]*>\s*<img src="assets/partner-11\.png"[^>]*>\s*</div>')
html = pattern.sub('', html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Nuked partner-11 (the bad Nori logo) from the carousel HTML.")
