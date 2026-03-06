import os
import re

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"

# We need to find the logo container in the new tailwind navbar
# For example, in index.html (and other pages):
# <div class="flex items-center gap-2">
#     <a href="index.html" class="flex items-center gap-2">
#         <div class="w-10 h-10 rounded-xl bg-primary flex items-center justify-center">
#             <span class="text-primary-foreground font-heading font-bold text-xl">4C</span>
#         </div>
#         <span class="font-heading font-bold text-2xl text-foreground tracking-tight">4CUPS</span>
#     </a>
# </div>

# We will replace that entire <a> inner content with an <img> tag pointing to our new logo.png
# Let's target the exact structure that is common across all files

files_to_update = ["index.html", "cafe.html", "restaurants.html", "fast-food.html", "glaciers.html"]

logo_html = """        <a href="index.html" class="flex items-center gap-2">
            <img src="assets/logo.png" alt="4CUPS Logo" class="h-12 w-auto object-contain">
        </a>"""

# The regex should capture from `<a href="index.html" class="flex items-center gap-2">`
# to `</a>` right before `<!-- Desktop Menu -->` or the `<ul>` tag. Let's make a precise regex.

old_logo_pattern = re.compile(
    r'<a href="index\.html" class="flex items-center gap-2">\s*'
    r'<div class="w-10 h-10 rounded-xl bg-primary flex items-center justify-center">\s*'
    r'<span class="text-primary-foreground font-heading font-bold text-xl">4C</span>\s*'
    r'</div>\s*'
    r'<span class="font-heading font-bold text-2xl text-foreground tracking-tight">4CUPS</span>\s*'
    r'</a>',
    re.DOTALL
)

for file_name in files_to_update:
    path = os.path.join(base_dir, file_name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Check if the pattern exists
        if old_logo_pattern.search(content):
            new_content = old_logo_pattern.sub(logo_html, content)
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"✅ {file_name}: logo updated")
        else:
            print(f"⚠️ {file_name}: old logo pattern not found")

