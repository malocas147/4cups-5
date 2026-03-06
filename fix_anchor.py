import os

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
idx_path = os.path.join(base_dir, "index.html")

with open(idx_path, "r", encoding="utf-8") as f:
    idx = f.read()

# The link "Découvrir nos produits" points to "#apropos"
# BUT we want it to point to the "Nos Services" / Sectors grid.
# The Sectors section currently starts with:
#         <!-- Sectors -->
#         <section class="py-20 md:py-28 bg-background">

# Let's add an ID "gammes" to that section:
idx = idx.replace('<section class="py-20 md:py-28 bg-background">', '<section id="gammes" class="py-20 md:py-28 bg-background" style="scroll-margin-top: 100px;">', 1)

# Now update the link href
idx = idx.replace('<a href="#apropos"\n                            class="inline-flex items-center justify-center px-8 py-3.5 rounded-full bg-primary', '<a href="#gammes"\n                            class="inline-flex items-center justify-center px-8 py-3.5 rounded-full bg-primary')

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(idx)

print("✅ index.html: Anchor link fixed to point to #gammes with scroll-margin-top")
