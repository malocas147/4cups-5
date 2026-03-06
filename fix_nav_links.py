import os
import re

html_files = ["cafe.html", "restaurants.html", "fast-food.html", "glaciers.html"]
base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"

# More aggressive CSS overrides - force ALL nav links to use DM Sans at 0.875rem
additional_css = """
        /* Force all nav links to consistent styling */
        .tailwind-scope nav ul li a,
        .tailwind-scope nav ul a,
        .tailwind-scope nav li a,
        .tailwind-scope nav a:not(:first-child) {
            font-family: 'DM Sans', sans-serif !important;
            font-size: 0.875rem !important;
            font-weight: 500 !important;
            line-height: 1.5 !important;
            letter-spacing: normal !important;
            color: hsl(30, 8%, 50%) !important;
            margin-bottom: 0 !important;
        }
        .tailwind-scope nav ul li a:hover,
        .tailwind-scope nav a:not(:first-child):hover {
            color: hsl(145, 35%, 32%) !important;
        }
        /* Override CTA btn specifically */
        .tailwind-scope nav a.cta-btn,
        .tailwind-scope nav ul li a.cta-btn {
            color: hsl(40, 33%, 97%) !important;
            font-weight: 600 !important;
            padding: 0.625rem 1.25rem !important;
            background-color: hsl(145, 35%, 32%) !important;
            border-radius: 9999px !important;
            display: inline-flex !important;
            align-items: center !important;
        }
        .tailwind-scope nav a.cta-btn:hover,
        .tailwind-scope nav ul li a.cta-btn:hover {
            color: hsl(40, 33%, 97%) !important;
            opacity: 0.9 !important;
        }
        /* Make sure headings inside nav don't inherit old styles */
        .tailwind-scope nav * {
            margin-bottom: 0 !important;
        }
"""

for fname in html_files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Insert before the closing </style> that has our overrides
    # Find the override style block and append to it
    content = content.replace(
        "/* Ensure body padding-top for fixed nav */",
        additional_css + "\n        /* Ensure body padding-top for fixed nav */"
    )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Done adding additional nav link overrides!")
