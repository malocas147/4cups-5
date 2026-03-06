import os

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# The current class string on the logos
old_class = 'class="max-w-full max-h-full object-contain grayscale opacity-60 hover:grayscale-0 hover:opacity-100 transition-all duration-300"'

# The new class string (removing the grayscale and opacity filters, keeping the rest)
new_class = 'class="max-w-full max-h-full object-contain transition-all duration-300"'

if old_class in html:
    html = html.replace(old_class, new_class)
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("✅ index.html: Removed grayscale filters from partner logos.")
else:
    print("⚠️ Could not find exact class string in index.html")
