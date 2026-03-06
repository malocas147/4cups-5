import os

html_files = ["cafe.html", "restaurants.html", "fast-food.html", "glaciers.html"]
base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"

for fname in html_files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Override the body background to match index.html's warm cream
    # Also override --bg-color CSS variable so all elements using it get the warm cream
    old = "/* Body padding for fixed nav */\n        body {"
    new = """/* Body background to match index.html warm cream */
        :root {
            --bg-color: #f7f3ed !important; /* hsl(40, 33%, 97%) converted */
        }
        body {
            background-color: #f7f3ed !important;
        }

        /* Body padding for fixed nav */
        body {"""
    content = content.replace(old, new)
    
    # Also try the other format
    old2 = "/* Ensure body padding-top for fixed nav */\n        body {"
    new2 = """/* Body background to match index.html warm cream */
        :root {
            --bg-color: #f7f3ed !important;
        }
        body {
            background-color: #f7f3ed !important;
        }

        /* Ensure body padding-top for fixed nav */
        body {"""
    content = content.replace(old2, new2)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Done - body background now matches index.html warm cream!")
