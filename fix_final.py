import os
import re

html_files = ["cafe.html", "restaurants.html", "fast-food.html", "glaciers.html"]
base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"

for fname in html_files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove all previous override style blocks
    content = re.sub(r'\s*<style>\s*/\* Override styles\.css conflicts.*?</style>', '', content, flags=re.DOTALL)
    
    # Remove old duplicate tailwind/lucide insertions if any
    # (cleanup from prior scripts)
    
    # Build fresh, comprehensive override CSS
    fresh_css = """
    <style>
        /* === NAVBAR OVERRIDES - Force match with index.html === */
        
        /* Nav container */
        .tailwind-scope,
        .tailwind-scope nav,
        .tailwind-scope nav *,
        .tailwind-scope nav a,
        .tailwind-scope nav ul,
        .tailwind-scope nav ul li,
        .tailwind-scope nav ul li a,
        .tailwind-scope nav button,
        .tailwind-scope nav div {
            box-sizing: border-box !important;
        }

        .tailwind-scope nav {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            right: 0 !important;
            z-index: 50 !important;
            background: hsla(40, 33%, 97%, 0.8) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            border-bottom: 1px solid hsl(35, 20%, 88%) !important;
            padding: 0 !important;
            box-shadow: none !important;
            margin: 0 !important;
        }
        
        .tailwind-scope nav > div {
            max-width: 1400px !important;
            margin: 0 auto !important;
            padding: 0 2rem !important;
            display: flex !important;
            align-items: center !important;
            justify-content: space-between !important;
            height: 5rem !important;
        }

        /* Logo */
        .tailwind-scope nav > div > a:first-child {
            font-family: 'Playfair Display', serif !important;
            font-size: 1.875rem !important;
            font-weight: 700 !important;
            color: hsl(145, 35%, 32%) !important;
            letter-spacing: -0.025em !important;
            text-decoration: none !important;
            line-height: 1.2 !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        /* Remove ALL underlines and pseudo-elements from nav links */
        .tailwind-scope nav a::before,
        .tailwind-scope nav a::after {
            display: none !important;
            content: none !important;
        }

        /* All navigation links */
        .tailwind-scope nav ul {
            list-style: none !important;
            margin: 0 !important;
            padding: 0 !important;
            display: flex !important;
            align-items: center !important;
            gap: 2rem !important;
        }

        .tailwind-scope nav ul li {
            list-style: none !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        .tailwind-scope nav ul li::before,
        .tailwind-scope nav ul li::after,
        .tailwind-scope nav ul li::marker {
            display: none !important;
            content: none !important;
        }

        /* ALL links inside nav ul must use DM Sans at 14px */
        .tailwind-scope nav ul li a {
            font-family: 'DM Sans', sans-serif !important;
            font-size: 0.875rem !important;
            font-weight: 500 !important;
            color: hsl(30, 8%, 50%) !important;
            text-decoration: none !important;
            line-height: 1.5 !important;
            letter-spacing: normal !important;
            margin: 0 !important;
            padding: 0 !important;
            position: static !important;
            display: inline !important;
        }

        .tailwind-scope nav ul li a:hover {
            color: hsl(145, 35%, 32%) !important;
        }

        /* CTA button - "Demander un devis" */
        .tailwind-scope nav ul li a.cta-btn {
            display: inline-flex !important;
            align-items: center !important;
            padding: 0.625rem 1.25rem !important;
            border-radius: 9999px !important;
            background-color: hsl(145, 35%, 32%) !important;
            color: hsl(40, 33%, 97%) !important;
            font-size: 0.875rem !important;
            font-weight: 600 !important;
            font-family: 'DM Sans', sans-serif !important;
        }

        .tailwind-scope nav ul li a.cta-btn:hover {
            opacity: 0.9 !important;
            color: hsl(40, 33%, 97%) !important;
        }

        /* Mobile button */
        .tailwind-scope nav button {
            background: none !important;
            border: none !important;
            padding: 0 !important;
            cursor: pointer !important;
            color: hsl(30, 10%, 15%) !important;
        }

        /* Mobile menu panel */
        .tailwind-scope nav > div:last-of-type ul {
            flex-direction: column !important;
        }
        
        /* Body padding for fixed nav */
        body {
            padding-top: 5rem !important;
        }

        /* === FOOTER & CONTACT OVERRIDES === */
        .tailwind-scope section {
            padding-top: 6rem !important;
            padding-bottom: 8rem !important;
        }
        .tailwind-scope footer {
            padding-top: 3rem !important;
            padding-bottom: 3rem !important;
        }
    </style>
"""
    
    # Insert right before </head>
    content = content.replace('</head>', fresh_css + '\n</head>')
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Done with fresh CSS overrides!")
