import os
import re

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"

# --- 1. GLACIERS ---
glaciers_path = os.path.join(base_dir, "glaciers.html")
with open(glaciers_path, "r", encoding="utf-8") as f:
    html = f.read()

# Remove 'Bacs Isothermes Famille' block
bac_pattern = re.compile(r'<!-- Bacs Isothermes -->.*?</div>\s*</div>\s*</div>', re.DOTALL)
html = bac_pattern.sub('', html)

# New Glaciers Products
new_glaciers = """
                <!-- Pot 4 Boules -->
                <div class="detailed-card fade-in-up" style="transition-delay: 0.2s;">
                    <div class="detailed-image">
                        <span style="color:var(--text-secondary); font-size:4rem;">🍦</span>
                    </div>
                    <div class="detailed-info">
                        <h3>Pot à Glace Kraft/Blanc</h3>
                        <div class="capacity-subtitle">Pour 4 Boules (500 ml)</div>
                        <table class="spec-table">
                            <tr><td>Capacité:</td><td>16 oz</td></tr>
                            <tr><td>Matériau:</td><td>Carton glacé résistant au froid</td></tr>
                            <tr><td>Options:</td><td>Couvercle en dôme disponible</td></tr>
                        </table>
                        <p class="detailed-desc">Un grand format gourmand conçu pour servir jusqu'à 4 boules généreuses avec toppings.</p>
                        <a href="https://wa.me/212661177624?text=Bonjour,%20je%20souhaite%20commander%20des%20Pots%20à%20Glace%204%20Boules." target="_blank" class="btn-whatsapp">
                            <i class="fa-brands fa-whatsapp"></i> Commander
                        </a>
                    </div>
                </div>

                <!-- Pot 5 Boules -->
                <div class="detailed-card fade-in-up" style="transition-delay: 0.3s;">
                    <div class="detailed-image">
                        <span style="color:var(--text-secondary); font-size:4rem;">🍨</span>
                    </div>
                    <div class="detailed-info">
                        <h3>Pot à Glace Kraft/Blanc</h3>
                        <div class="capacity-subtitle">Pour 5 Boules (750 ml)</div>
                        <table class="spec-table">
                            <tr><td>Capacité:</td><td>24 oz</td></tr>
                            <tr><td>Matériau:</td><td>Carton glacé premium</td></tr>
                            <tr><td>Options:</td><td>Couvercle plat ou dôme</td></tr>
                        </table>
                        <p class="detailed-desc">Le format familial par excellence pour partager une sélection de vos meilleures saveurs.</p>
                        <a href="https://wa.me/212661177624?text=Bonjour,%20je%20souhaite%20commander%20des%20Pots%20à%20Glace%205%20Boules." target="_blank" class="btn-whatsapp">
                            <i class="fa-brands fa-whatsapp"></i> Commander
                        </a>
                    </div>
                </div>
"""

# Insert new glaciers products before the closing tag of the detailed-product-grid
grid_end = r'<!-- Tableau des Mesures -->'
if grid_end in html:
    parts = html.split(grid_end, 1)
    # The grid div closes right before the section closes, which is before Tableau
    # Let's target the exact closing divs more safely:
    # We find the string: '            </div>\n        </div>\n    </section>\n\n    <!-- Tableau'
    insert_target = '            </div>\n        </div>\n    </section>'
    if insert_target in parts[0]:
        sub_parts = parts[0].rsplit('            </div>\n        </div>\n    </section>', 1)
        html = sub_parts[0] + new_glaciers + '            </div>\n        </div>\n    </section>' + sub_parts[1] + grid_end + parts[1]

with open(glaciers_path, "w", encoding="utf-8") as f:
    f.write(html)


# --- 2. RESTAURANTS ---
rest_path = os.path.join(base_dir, "restaurants.html")
with open(rest_path, "r", encoding="utf-8") as f:
    html = f.read()

# Remove 'Boîte Traiteur Premium'
traiteur_pattern = re.compile(r'<!-- Boîte Traiteur Premium -->.*?</div>\s*</div>\s*</div>', re.DOTALL)
html = traiteur_pattern.sub('', html)

# New Restaurant Product (Sushi)
new_rest = """
                <!-- Barquette Sushi -->
                <div class="detailed-card fade-in-up">
                    <div class="detailed-image">
                        <span style="color:var(--text-secondary); font-size:4rem;">🍣</span>
                    </div>
                    <div class="detailed-info">
                        <h3>Barquettes pour Sushi</h3>
                        <div class="capacity-subtitle">Présentation Élégante & Sécurisée</div>
                        <table class="spec-table">
                            <tr><td>Format:</td><td>Rectangulaire (plusieurs tailles)</td></tr>
                            <tr><td>Couvercle:</td><td>PET transparent anti-buée</td></tr>
                            <tr><td>Finition:</td><td>Carton ou plastique premium</td></tr>
                        </table>
                        <p class="detailed-desc">Mettez en valeur vos assortiments de sushis avec une boîte esthétique assurant un maintien parfait.</p>
                        <a href="https://wa.me/212661177624?text=Bonjour,%20je%20souhaite%20commander%20des%20Barquettes%20à%20Sushi." target="_blank" class="btn-whatsapp">
                            <i class="fa-brands fa-whatsapp"></i> Commander
                        </a>
                    </div>
                </div>
"""

# We just insert it at the very top of the grid 
grid_start = r'<!-- Detailed Products Grid -->\s*<div class="detailed-product-grid">'
match = re.search(grid_start, html)
if match:
    insert_pos = match.end()
    html = html[:insert_pos] + "\n" + new_rest + html[insert_pos:]

with open(rest_path, "w", encoding="utf-8") as f:
    f.write(html)


# --- 3. CAFES ---
cafe_path = os.path.join(base_dir, "cafe.html")
with open(cafe_path, "r", encoding="utf-8") as f:
    html = f.read()

new_cafe = """
                <!-- Porte-Gobelets 2 -->
                <div class="detailed-card fade-in-up" style="transition-delay: 0.8s;">
                    <div class="detailed-image">
                        <span style="color:var(--text-secondary); font-size:4rem;">☕☕</span>
                    </div>
                    <div class="detailed-info">
                        <h3>Porte-Gobelets (2 Tasses)</h3>
                        <div class="capacity-subtitle">Transport Sécurisé</div>
                        <table class="spec-table">
                            <tr><td>Capacité:</td><td>2 emplacements</td></tr>
                            <tr><td>Matériau:</td><td>Carton moulé rigide</td></tr>
                            <tr><td>Compatibilité:</td><td>Du 4 oz au 16 oz</td></tr>
                        </table>
                        <p class="detailed-desc">L'accessoire indispensable pour la vente à emporter, évitant les renversements et les brûlures.</p>
                        <a href="https://wa.me/212661177624?text=Bonjour,%20je%20souhaite%20commander%20des%20Porte-Gobelets%202%20Tasses." target="_blank" class="btn-whatsapp">
                            <i class="fa-brands fa-whatsapp"></i> Commander
                        </a>
                    </div>
                </div>

                <!-- Porte-Gobelets 4 -->
                <div class="detailed-card fade-in-up" style="transition-delay: 0.9s;">
                    <div class="detailed-image">
                        <span style="color:var(--text-secondary); font-size:4rem;">📦</span>
                    </div>
                    <div class="detailed-info">
                        <h3>Porte-Gobelets (4 Tasses)</h3>
                        <div class="capacity-subtitle">Format Groupe</div>
                        <table class="spec-table">
                            <tr><td>Capacité:</td><td>4 emplacements</td></tr>
                            <tr><td>Matériau:</td><td>Carton moulé très haute résistance</td></tr>
                            <tr><td>Design:</td><td>Empilable pour optimiser l'espace</td></tr>
                        </table>
                        <p class="detailed-desc">Parfait pour les commandes multiples. Maintient fermement jusqu'à 4 gobelets de tailles variées.</p>
                        <a href="https://wa.me/212661177624?text=Bonjour,%20je%20souhaite%20commander%20des%20Porte-Gobelets%204%20Tasses." target="_blank" class="btn-whatsapp">
                            <i class="fa-brands fa-whatsapp"></i> Commander
                        </a>
                    </div>
                </div>
"""

# Insert at the end of the grid in cafe.html
target_grid_end = '            </div>\n        </div>\n    </section>\n\n\n    <!-- Tableau'
if target_grid_end in html:
    html = html.replace(target_grid_end, new_cafe + '\n' + target_grid_end)
else:
    # Alternative target if formatting differs
    target_grid_end_2 = '            </div>\n        </div>\n    </section>\n\n    <!-- Tableau'
    if target_grid_end_2 in html:
        html = html.replace(target_grid_end_2, new_cafe + '\n' + target_grid_end_2)
    else:
        # One last fallback
        target_grid_end_3 = '            </div>\n        </div>\n    </section>'
        sub_parts = html.rsplit(target_grid_end_3, 1)
        html = sub_parts[0] + new_cafe + '\n' + target_grid_end_3 + sub_parts[1]

with open(cafe_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Catalog updates generated successfully.")
