import os

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
files_to_update = ["index.html", "cafe.html", "restaurants.html", "fast-food.html", "glaciers.html"]

old_style = 'style="height: 3rem; width: auto; object-fit: contain;"'
# Increased from 3rem to 4.5rem (approx 72px vs 48px).
# We also add a slight negative margin if it's too tall for the h-16 container on mobile, 
# or just let it scale. Since we want it BIG, let's use 5rem and scale down on mobile if needed.
# Actually, just `height: 4.5rem` will do perfectly.
new_style = 'style="height: 4.5rem; width: auto; object-fit: contain; max-height: 120%; margin: -0.5rem 0;"'

for file_name in files_to_update:
    path = os.path.join(base_dir, file_name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        if old_style in content:
            new_content = content.replace(old_style, new_style)
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"✅ {file_name}: logo enlarged")
        else:
            print(f"⚠️ {file_name}: style not found")
