import os
import re

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"

# 1. cafe.html (Couvercles)
cafe_path = os.path.join(base_dir, "cafe.html")
with open(cafe_path, "r", encoding="utf-8") as f:
    cafe = f.read()

# Replace 🪄 with couvercle_noir.png
couv_img = '<img src="assets/couvercle_noir.png" alt="Couvercle noir pour gobelet" class="w-full h-full object-contain p-4">'
cafe = re.sub(
    r'<span style="color:var\(--text-secondary\); font-size:[0-9\.]+rem;">🪄</span>',
    couv_img,
    cafe
)
with open(cafe_path, "w", encoding="utf-8") as f:
    f.write(cafe)


# 2. fast-food.html (Barquettes & Porte-sauces)
ff_path = os.path.join(base_dir, "fast-food.html")
with open(ff_path, "r", encoding="utf-8") as f:
    ff = f.read()

# The fast-food page currently uses 🥣 for sauce and 🥡/🍟 for barquettes
barquette_img = '<img src="assets/barquettes_kraft.png" alt="Barquette kraft alimentaire" class="w-full h-full object-contain p-4">'
ff = re.sub(
    r'<span style="color:var\(--text-secondary\); font-size:[0-9\.]+rem;">🥡</span>',
    barquette_img,
    ff
)
ff = re.sub(
    r'<span style="color:var\(--text-secondary\); font-size:[0-9\.]+rem;">🍟</span>',
    barquette_img,
    ff
)
# For sauce cups, maybe we leave it or replace it. User said "cette image pour les barquettes" => let's use it for the open/closed barquettes.
with open(ff_path, "w", encoding="utf-8") as f:
    f.write(ff)


# 3. glaciers.html (Pots de glace)
glace_path = os.path.join(base_dir, "glaciers.html")
with open(glace_path, "r", encoding="utf-8") as f:
    glace = f.read()

pot_img = '<img src="assets/pots_glaces.png" alt="Pots de glace en carton" class="w-full h-full object-contain p-4">'
# Usually emoji is 🍦 or 🍨
glace = re.sub(
    r'<span style="color:var\(--text-secondary\); font-size:[0-9\.]+rem;">🍨</span>',
    pot_img,
    glace
)
glace = re.sub(
    r'<span style="color:var\(--text-secondary\); font-size:[0-9\.]+rem;">🍧</span>',
    pot_img,
    glace
)
glace = re.sub(
    r'<span style="color:var\(--text-secondary\); font-size:[0-9\.]+rem;">🍦</span>',
    pot_img,
    glace
)
with open(glace_path, "w", encoding="utf-8") as f:
    f.write(glace)

# 4. Fix index.html "Découvrir nos produits" anchor link
idx_path = os.path.join(base_dir, "index.html")
with open(idx_path, "r", encoding="utf-8") as f:
    idx = f.read()

# The hero section has <a href="#gammes" ...> Découvrir nos produits </a>
# Let's verify what ID the gamme section has.
# The user says it redirects "un peu en dessous". This means the fixed navbar covers the section title.
# It should scroll to the products grid, but the fixed navbar requires scroll-margin-top
print("Updating HTML complete.")

