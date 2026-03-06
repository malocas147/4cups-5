import os

html_files = ["cafe.html", "restaurants.html", "fast-food.html", "glaciers.html"]
base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"

# Revert index.html back to semi-transparent
idx_path = os.path.join(base_dir, "index.html")
with open(idx_path, "r", encoding="utf-8") as f:
    idx = f.read()

idx = idx.replace(
    'class="fixed top-0 left-0 right-0 z-50 bg-background backdrop-blur-md border-b border-border"',
    'class="fixed top-0 left-0 right-0 z-50 bg-background/80 backdrop-blur-md border-b border-border"'
)

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(idx)

# Update category pages to use semi-transparent warm cream matching index.html
for fname in html_files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = content.replace(
        "background: hsl(40, 33%, 97%) !important;",
        "background: hsla(40, 33%, 97%, 0.8) !important;"
    )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Done - reverted to semi-transparent navbar on all pages!")
