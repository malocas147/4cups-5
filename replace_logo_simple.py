import os

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
files_to_update = ["index.html", "cafe.html", "restaurants.html", "fast-food.html", "glaciers.html"]

old_logo_html = '<a href="index.html" class="font-heading text-2xl md:text-3xl font-bold text-primary tracking-tight">\n                4 cups\n            </a>'
old_logo_html_alt = '<a href="index.html" class="font-heading text-2xl md:text-3xl font-bold text-primary tracking-tight">\r\n                4 cups\r\n            </a>'

new_logo_html = '<a href="index.html" class="flex items-center" style="height: 100%;">\n                <img src="assets/logo.png" alt="4CUPS Logo" style="height: 3rem; width: auto; object-fit: contain;">\n            </a>'

for file_name in files_to_update:
    path = os.path.join(base_dir, file_name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace either newline flavor
        if old_logo_html in content:
            new_content = content.replace(old_logo_html, new_logo_html)
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"✅ {file_name}: logo replaced")
        elif old_logo_html_alt in content:
            new_content = content.replace(old_logo_html_alt, new_logo_html)
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"✅ {file_name}: logo replaced (CRLF)")
        else:
            print(f"⚠️ {file_name}: pattern not found")
