import os

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"

# ============================================================
# 1. Update text in index.html FAQ
# ============================================================
idx_path = os.path.join(base_dir, "index.html")
with open(idx_path, "r", encoding="utf-8") as f:
    idx = f.read()

# Change "15 à 20 jours" -> "7 à 10 jours"
idx = idx.replace("15 à 20 jours", "7 à 10 jours")

# Change "carton" -> "papier alimentaire" in the FAQ
faq_start = idx.find('id="faq"')
if faq_start != -1:
    faq_end = idx.find('id="contact"', faq_start)
    if faq_end == -1: faq_end = len(idx)
    
    faq_section = idx[faq_start:faq_end]
    faq_section_updated = faq_section.replace("carton", "papier alimentaire")
    
    idx = idx[:faq_start] + faq_section_updated + idx[faq_end:]
    print("✅ index.html: FAQ updated text")
else:
    print("⚠️ FAQ section not found in index.html")

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(idx)

# ============================================================
# 2. Reorder sections in cafe.html
# ============================================================
cafe_path = os.path.join(base_dir, "cafe.html")
with open(cafe_path, "r", encoding="utf-8") as f:
    cafe = f.read()

# We want to swap "Tableau Comparatif" and "Section Couvercles"
table_start_marker = "    <!-- Tableau Comparatif -->"
couvercles_start_marker = "    <!-- Section Couvercles -->"
contact_start_marker = "    <!-- Contact Section -->"

table_idx = cafe.find(table_start_marker)
couvercles_idx = cafe.find(couvercles_start_marker)
# Find the exact end of couvercles (which is right before contact)
contact_idx = cafe.find(contact_start_marker, couvercles_idx)

if table_idx != -1 and couvercles_idx != -1 and contact_idx != -1:
    # First part: before table
    part1_before_table = cafe[:table_idx]
    
    # Table section
    table_section = cafe[table_idx:couvercles_idx]
    
    # Couvercles section
    # Note: there is probably a closing tag for the main container or section that might belong
    # We just swap the exact blocks as delimited by comments
    
    # Wait, the Table section sits outside the "products" section?
    # Actually, Table is in <section class="container" style="padding-top: 4rem; padding-bottom: 4rem;">
    # Couvercles is in <section class="products overflow-hidden" style="padding-top: 0;">
    # Contact is next. This implies they are siblings at the body level.
    
    # Just do a string swap
    couvercles_section = cafe[couvercles_idx:contact_idx]
    
    # Build new structure: Part1 + Couvercles + Table + Contact...
    cafe_new = part1_before_table + couvercles_section + table_section + cafe[contact_idx:]
    
    with open(cafe_path, "w", encoding="utf-8") as f:
        f.write(cafe_new)
    print("✅ cafe.html: Reordered Couvercles before Tableau Comparatif")
else:
    print(f"⚠️ Missing section markers in cafe.html: T={table_idx}, C={couvercles_idx}, C2={contact_idx}")

