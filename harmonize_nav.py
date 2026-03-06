import os
import re

html_files = ["cafe.html", "restaurants.html", "fast-food.html", "glaciers.html"]
base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"

with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    idx_content = f.read()

# Extract Navbar
nav_match = re.search(r'(<!-- Navbar -->\s*<nav.*?</nav>)', idx_content, re.DOTALL)
new_nav = nav_match.group(1)

# Extract Scripts
script_match = re.search(r'(<script>\s*// Initialize Lucide icons.*?</script>)', idx_content, re.DOTALL)
new_scripts = script_match.group(1)

for fname in html_files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Change config
    if "important: '#tailwind-contact'" in content:
        content = content.replace("important: '#tailwind-contact'", "important: '.tailwind-scope'")
    
    if 'id="tailwind-contact"' in content:
        content = content.replace('id="tailwind-contact"', 'class="tailwind-scope"')

    # Active state highlighting logic (optional but good)
    file_nav = new_nav
    file_nav = file_nav.replace(f'href="{fname}"\n                        class="font-body text-sm font-medium text-muted-foreground hover:text-primary transition-colors"',
                                f'href="{fname}"\n                        class="font-body text-sm font-medium text-primary hover:text-primary transition-colors"')
    
    file_nav = file_nav.replace(f'href="{fname}"\n                        class="font-body text-base text-foreground hover:text-primary transition-colors"',
                                f'href="{fname}"\n                        class="font-body text-base text-primary hover:text-primary transition-colors"')

    # Replace old nav
    # The old nav looks like: <!-- Navigation -->\n<nav ...> ... </nav>
    content = re.sub(r'<!-- Navigation -->.*?<\/nav>', f'<!-- Navigation -->\n    <div class="tailwind-scope">\n{file_nav}\n    </div>', content, flags=re.DOTALL)

    # Replace old inline scripts block with the one from index.html
    # In category pages, the old inline script starts with <script>\n        // Initialize Lucide icons
    content = re.sub(r'<script>\s*// Initialize Lucide icons.*?<\/script>', new_scripts, content, flags=re.DOTALL)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Done NAVBAR harmonization!")
