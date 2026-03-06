import os
import re

ALL_FILES = ["index.html", "cafe.html", "restaurants.html", "fast-food.html", "glaciers.html"]
base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"

for fname in ALL_FILES:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # === 1. Change "Nom complet" to "Nom" ===
    content = content.replace('placeholder="Nom complet"', 'placeholder="Nom"')

    # === 2. Remove the "Sujet" input and its wrapper ===
    # The Sujet input is inside a grid div with the phone input
    # We need to remove just the Sujet input, keep the phone input
    # Remove the entire <input> for Sujet (multiline)
    content = re.sub(
        r'\s*<input type="text" placeholder="Sujet"[^/]*/>\s*',
        '\n',
        content
    )

    # === 3. Fix body background color on category pages ===
    if fname != "index.html":
        # Check if background override already exists
        if "background-color: #f7f3ed" not in content:
            # Find the style block with our overrides and add background rule
            content = content.replace(
                "body {\r\n            padding-top: 5rem !important;\r\n        }",
                "body {\r\n            padding-top: 5rem !important;\r\n            background-color: #f7f3ed !important;\r\n        }"
            )
            # Also try unix line endings just in case
            content = content.replace(
                "body {\n            padding-top: 5rem !important;\n        }",
                "body {\n            padding-top: 5rem !important;\n            background-color: #f7f3ed !important;\n        }"
            )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Done! Contact form updated + body background fixed.")
