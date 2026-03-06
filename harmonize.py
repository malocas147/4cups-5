import os
import re

html_files = ["cafe.html", "restaurants.html", "fast-food.html", "glaciers.html"]
base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"

head_insert = """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            important: '#tailwind-contact',
            corePlugins: { preflight: false },
            darkMode: ["class"],
            theme: {
                container: { center: true, padding: "2rem", screens: { "2xl": "1400px" } },
                extend: {
                    fontFamily: {
                        heading: ['Playfair Display', 'serif'],
                        body: ['DM Sans', 'sans-serif'],
                    },
                    colors: {
                        border: "hsl(35 20% 88%)",
                        input: "hsl(35 20% 88%)",
                        ring: "hsl(145 35% 32%)",
                        background: "hsl(40 33% 97%)",
                        foreground: "hsl(30 10% 15%)",
                        primary: { DEFAULT: "hsl(145 35% 32%)", foreground: "hsl(40 33% 97%)" },
                        secondary: { DEFAULT: "hsl(30 30% 88%)", foreground: "hsl(30 10% 15%)" },
                        muted: { DEFAULT: "hsl(35 20% 92%)", foreground: "hsl(30 8% 50%)" },
                        accent: { DEFAULT: "hsl(28 60% 58%)", foreground: "hsl(40 33% 97%)" },
                        card: { DEFAULT: "hsl(40 25% 95%)", foreground: "hsl(30 10% 15%)" },
                    },
                    borderRadius: { lg: "0.75rem", md: "calc(0.75rem - 2px)", sm: "calc(0.75rem - 4px)" }
                }
            }
        }
    </script>
    <script src="https://unpkg.com/lucide@latest"></script>
</head>"""

# Load the section string from index.html
with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    idx_content = f.read()
    
# Extract contact and footer from index
contact_match = re.search(r'(<!-- Contact Section -->\s*<section id="contact".*?)<script>', idx_content, re.DOTALL)
if not contact_match:
    raise Exception("Could not find contact section in index.html")

new_contact_footer = contact_match.group(1).replace("</main>", "")

new_body_end = f"""<!-- Contact Section -->
    <div id="tailwind-contact">
        {new_contact_footer.strip()}
    </div>
    
    <script src="script.js"></script>
    <script>
        // Initialize Lucide icons
        if(typeof lucide !== 'undefined') {{
            lucide.createIcons();
        }}
    </script>
</body>
</html>
"""

for fname in html_files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace </head> with head_insert
    if "<script src=\"https://cdn.tailwindcss.com\"></script>" not in content:
        content = content.replace("</head>", head_insert)
    
    # Replace from <!-- Contact Section --> to the end of the file
    content = re.sub(r'<!-- Contact Section -->.*', new_body_end, content, flags=re.DOTALL)
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Done!")
