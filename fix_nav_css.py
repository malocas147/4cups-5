import os

html_files = ["cafe.html", "restaurants.html", "fast-food.html", "glaciers.html"]
base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"

# CSS overrides to neutralize styles.css conflicts within the tailwind navbar
override_css = """
    <style>
        /* Override styles.css conflicts for the Tailwind navbar */
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
        }
        .tailwind-scope nav .container {
            max-width: 1400px !important;
            margin: 0 auto !important;
            padding: 0 2rem !important;
            display: flex !important;
            align-items: center !important;
            justify-content: space-between !important;
            height: 5rem !important;
        }
        .tailwind-scope nav a {
            text-decoration: none !important;
            position: static !important;
            padding: 0 !important;
        }
        .tailwind-scope nav a::after {
            display: none !important;
            content: none !important;
        }
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
        .tailwind-scope nav ul li::marker {
            display: none !important;
            content: none !important;
        }
        /* Logo style override - match index.html exactly */
        .tailwind-scope nav a[href="index.html"]:first-child {
            font-family: 'Playfair Display', serif !important;
            font-size: 1.875rem !important;
            font-weight: 700 !important;
            color: hsl(145, 35%, 32%) !important;
            letter-spacing: -0.025em !important;
        }
        /* Nav link styles */
        .tailwind-scope nav ul li a {
            font-family: 'DM Sans', sans-serif !important;
            font-size: 0.875rem !important;
            font-weight: 500 !important;
            color: hsl(30, 8%, 50%) !important;
            transition: color 0.15s ease !important;
        }
        .tailwind-scope nav ul li a:hover {
            color: hsl(145, 35%, 32%) !important;
        }
        .tailwind-scope nav ul li a.nav-active {
            color: hsl(145, 35%, 32%) !important;
        }
        /* CTA button */
        .tailwind-scope nav ul li a[href="#contact"].cta-btn {
            display: inline-flex !important;
            align-items: center !important;
            padding: 0.625rem 1.25rem !important;
            border-radius: 9999px !important;
            background-color: hsl(145, 35%, 32%) !important;
            color: hsl(40, 33%, 97%) !important;
            font-size: 0.875rem !important;
            font-weight: 600 !important;
        }
        .tailwind-scope nav ul li a[href="#contact"].cta-btn:hover {
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
        .tailwind-scope #tailwind-mobile-menu {
            background: hsl(40, 33%, 97%) !important;
            border-bottom: 1px solid hsl(35, 20%, 88%) !important;
        }
        .tailwind-scope #tailwind-mobile-menu ul {
            flex-direction: column !important;
        }
        .tailwind-scope #tailwind-mobile-menu ul li a {
            font-size: 1rem !important;
            color: hsl(30, 10%, 15%) !important;
        }
        .tailwind-scope #tailwind-mobile-menu ul li a:hover {
            color: hsl(145, 35%, 32%) !important;
        }

        /* Also fix the contact/footer section */
        .tailwind-scope section,
        .tailwind-scope footer {
            padding: inherit !important;
        }

        /* Ensure body padding-top for fixed nav */
        body {
            padding-top: 5rem !important;
        }
    </style>
"""

for fname in html_files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove any previous override block if present
    if "/* Override styles.css conflicts for the Tailwind navbar */" in content:
        import re
        content = re.sub(r'\s*<style>\s*/\* Override styles\.css conflicts.*?</style>', '', content, flags=re.DOTALL)
    
    # Also add cta-btn and nav-active classes to the right elements
    # CTA button: the last <a href="#contact"> that says "Demander un devis"
    content = content.replace(
        'class="inline-flex items-center px-5 py-2.5 rounded-full bg-primary text-primary-foreground text-sm font-semibold hover:opacity-90 transition-opacity"',
        'class="inline-flex items-center px-5 py-2.5 rounded-full bg-primary text-primary-foreground text-sm font-semibold hover:opacity-90 transition-opacity cta-btn"'
    )
    
    # Remove double cta-btn if script ran twice
    content = content.replace('cta-btn cta-btn', 'cta-btn')

    # Insert override CSS right before </head>
    content = content.replace('</head>', override_css + '\n</head>')

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Done adding CSS overrides!")
