import os
import re

html_files = ["cafe.html", "restaurants.html", "fast-food.html", "glaciers.html"]
base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"

for fname in html_files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Add rule to force-hide the mobile menu by default
    mobile_hide_css = """
        /* Force hide mobile menu by default */
        .tailwind-scope #tailwind-mobile-menu {
            display: none !important;
        }
        .tailwind-scope #tailwind-mobile-menu.show {
            display: block !important;
        }
        /* Hide mobile button on desktop */
        .tailwind-scope nav button#tailwind-mobile-btn {
            display: none !important;
        }
        @media (max-width: 768px) {
            .tailwind-scope nav button#tailwind-mobile-btn {
                display: block !important;
            }
            .tailwind-scope nav ul.hidden {
                display: none !important;
            }
        }
"""
    
    # Insert before the body padding-top rule
    content = content.replace(
        "/* Body padding for fixed nav */",
        mobile_hide_css + "\n        /* Body padding for fixed nav */"
    )
    # Also fix for the version that has "Ensure body padding-top"
    content = content.replace(
        "/* Ensure body padding-top for fixed nav */",
        mobile_hide_css + "\n        /* Ensure body padding-top for fixed nav */"
    )

    # Fix the mobile menu toggle to use 'show' class instead of removing 'hidden'
    old_toggle = '''mobileMenu.classList.remove("hidden");'''
    new_toggle = '''mobileMenu.classList.add("show");'''
    content = content.replace(old_toggle, new_toggle)
    
    old_toggle2 = '''mobileMenu.classList.add("hidden");'''
    new_toggle2 = '''mobileMenu.classList.remove("show");'''
    content = content.replace(old_toggle2, new_toggle2)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Done hiding mobile menu!")
