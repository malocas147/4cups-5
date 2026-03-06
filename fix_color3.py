import os

html_files = ["cafe.html", "restaurants.html", "fast-food.html", "glaciers.html"]
base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"

# On index.html the nav is semi-transparent cream over a cream body = visually solid cream.
# On category pages the body is blue-white (#f8fafc), so semi-transparent cream looks different.
# Fix: make category navbars fully opaque with the exact cream color from the homepage.

for fname in html_files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = content.replace(
        "background: hsla(40, 33%, 97%, 0.8) !important;",
        "background: hsl(40, 33%, 97%) !important;"
    )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Done - category navbars now solid cream matching homepage visual!")
