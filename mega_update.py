import os
import re

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"

# ============================================================
# 1. index.html: Move Personnalisation section AFTER À propos
#    and fix "4 étapes" -> "5 étapes"
# ============================================================

idx_path = os.path.join(base_dir, "index.html")
with open(idx_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix "4 étapes" -> "5 étapes"
content = content.replace(
    "Votre emballage personnalisé en 4 étapes",
    "Votre emballage personnalisé en 5 étapes"
)

# Extract the Personnalisation section block
perso_start = content.find("<!-- Personnalisation Section -->")
perso_end = content.find("<!-- About Section -->")
perso_block = content[perso_start:perso_end]

# Remove it from its current location
content_without = content[:perso_start] + content[perso_end:]

# Find where About section ends and Étapes section begins
# About section ends with </section> before ProcessSteps
# We insert after the About section closing tag
process_comment = "<!-- ProcessSteps Section -->"
insert_pos = content_without.find(process_comment)

# Insert the Personnalisation block just before ProcessSteps
content_new = content_without[:insert_pos] + perso_block + "\n        " + content_without[insert_pos:]

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(content_new)

print("✅ index.html: Personnalisation moved, '5 étapes' fixed")

# ============================================================
# 2. cafe.html: Add Couvercles pour Gobelets section
# ============================================================

cafe_path = os.path.join(base_dir, "cafe.html")
with open(cafe_path, "r", encoding="utf-8") as f:
    cafe = f.read()

couvercles_html = """
                <!-- Couvercles pour Gobelets -->
                <div class="detailed-card fade-in-up" style="transition-delay: 0.4s;">
                    <div class="detailed-image">
                        <span style="color:var(--text-secondary); font-size:4rem;">🪄</span>
                    </div>
                    <div class="detailed-info">
                        <h3>Couvercle 72mm</h3>
                        <div class="capacity-subtitle">Pour Gobelets 4 oz</div>
                        <table class="spec-table">
                            <tr><td>Hauteur:</td><td>8 mm</td></tr>
                            <tr><td>Ø Haut:</td><td>72 mm</td></tr>
                            <tr><td>Ø Base:</td><td>72 mm</td></tr>
                        </table>
                        <p class="detailed-desc">Couvercle adapté aux gobelets 4 oz. Fermeture sécurisée anti-renversement.</p>
                        <a href="https://wa.me/212661177624?text=Bonjour,%20je%20souhaite%20commander%20des%20Couvercles%2072mm."
                            target="_blank" class="btn-whatsapp">
                            <i class="fa-brands fa-whatsapp"></i> Commander
                        </a>
                    </div>
                </div>

                <!-- Couvercle 80mm -->
                <div class="detailed-card fade-in-up" style="transition-delay: 0.5s;">
                    <div class="detailed-image">
                        <span style="color:var(--text-secondary); font-size:4rem;">🪄</span>
                    </div>
                    <div class="detailed-info">
                        <h3>Couvercle 80mm</h3>
                        <div class="capacity-subtitle">Pour Gobelets 6 oz</div>
                        <table class="spec-table">
                            <tr><td>Hauteur:</td><td>8 mm</td></tr>
                            <tr><td>Ø Haut:</td><td>80 mm</td></tr>
                            <tr><td>Ø Base:</td><td>80 mm</td></tr>
                        </table>
                        <p class="detailed-desc">Couvercle adapté aux gobelets 6 oz. Ajustement parfait pour vos boissons chaudes.</p>
                        <a href="https://wa.me/212661177624?text=Bonjour,%20je%20souhaite%20commander%20des%20Couvercles%2080mm."
                            target="_blank" class="btn-whatsapp">
                            <i class="fa-brands fa-whatsapp"></i> Commander
                        </a>
                    </div>
                </div>

                <!-- Couvercle 96mm -->
                <div class="detailed-card fade-in-up" style="transition-delay: 0.6s;">
                    <div class="detailed-image">
                        <span style="color:var(--text-secondary); font-size:4rem;">🪄</span>
                    </div>
                    <div class="detailed-info">
                        <h3>Couvercle 96mm</h3>
                        <div class="capacity-subtitle">Pour Gobelets 8 oz / 12 oz</div>
                        <table class="spec-table">
                            <tr><td>Hauteur:</td><td>8 mm</td></tr>
                            <tr><td>Ø Haut:</td><td>96 mm</td></tr>
                            <tr><td>Ø Base:</td><td>96 mm</td></tr>
                        </table>
                        <p class="detailed-desc">Couvercle adapté aux gobelets 8 à 12 oz. Idéal pour cafés allongés et lattes.</p>
                        <a href="https://wa.me/212661177624?text=Bonjour,%20je%20souhaite%20commander%20des%20Couvercles%2096mm."
                            target="_blank" class="btn-whatsapp">
                            <i class="fa-brands fa-whatsapp"></i> Commander
                        </a>
                    </div>
                </div>

                <!-- Couvercle 110mm -->
                <div class="detailed-card fade-in-up" style="transition-delay: 0.7s;">
                    <div class="detailed-image">
                        <span style="color:var(--text-secondary); font-size:4rem;">🪄</span>
                    </div>
                    <div class="detailed-info">
                        <h3>Couvercle 110mm</h3>
                        <div class="capacity-subtitle">Pour Gobelets 16 oz / 20 oz</div>
                        <table class="spec-table">
                            <tr><td>Hauteur:</td><td>8 mm</td></tr>
                            <tr><td>Ø Haut:</td><td>110 mm</td></tr>
                            <tr><td>Ø Base:</td><td>110 mm</td></tr>
                        </table>
                        <p class="detailed-desc">Couvercle grand format pour les grandes boissons. Parfait pour les smoothies et frappés.</p>
                        <a href="https://wa.me/212661177624?text=Bonjour,%20je%20souhaite%20commander%20des%20Couvercles%20110mm."
                            target="_blank" class="btn-whatsapp">
                            <i class="fa-brands fa-whatsapp"></i> Commander
                        </a>
                    </div>
                </div>
"""

# Insert before the closing </div></div></section> of the detailed-product-grid
# Find the last </div> closing of the detailed-product-grid
close_marker = "            </div>\n        </div>\n    </section>\n\n    <!-- Contact Section -->"
close_marker2 = "            </div>\r\n        </div>\r\n    </section>\r\n\r\n    <!-- Contact Section -->"

if close_marker in cafe:
    cafe = cafe.replace(close_marker, couvercles_html + close_marker, 1)
elif close_marker2 in cafe:
    cafe = cafe.replace(close_marker2, couvercles_html + close_marker2, 1)
else:
    # Fallback: find the Contact Section comment
    cafe = cafe.replace(
        "    <!-- Contact Section -->",
        couvercles_html + "\n            </div>\n        </div>\n    </section>\n\n    <!-- Contact Section -->",
        1
    )

# Actually let's do a simpler approach: add before the `<!-- Contact Section -->` part that closes the products
# Find end of products section
idx_end_grid = cafe.rfind("            </div>\n        </div>\n    </section>")
if idx_end_grid == -1:
    idx_end_grid = cafe.rfind("            </div>\r\n        </div>\r\n    </section>")

contact_pos = cafe.find("<!-- Contact Section -->")
# We insert the new cards before the closing divs of products section
# but only in the products section range
products_close = cafe.rfind("</div>", 0, contact_pos)
products_close = cafe.rfind("</div>", 0, products_close)
products_close = cafe.rfind("</div>", 0, products_close)

# Simpler: insert before </div>\n    </section>\n that comes before Contact
# Let's find the specific marker: the detailed-product-grid closing div
pos = cafe.find("    <!-- Contact Section -->")
insert_here = cafe.rfind("\n            </div>\n        </div>\n    </section>", 0, pos)
if insert_here == -1:
    insert_here = cafe.rfind("\r\n            </div>\r\n        </div>\r\n    </section>", 0, pos)

if insert_here != -1:
    cafe = cafe[:insert_here] + couvercles_html + cafe[insert_here:]
    print("✅ cafe.html: Couvercles added via rfind method")
else:
    print("⚠️ cafe.html: Could not find insertion point, trying alternative")
    # Try adding at the specific grid close
    cafe = cafe.replace(
        "\n            </div>\n        </div>\n    </section>\n",
        couvercles_html + "\n            </div>\n        </div>\n    </section>\n",
        1
    )

with open(cafe_path, "w", encoding="utf-8") as f:
    f.write(cafe)

print("✅ cafe.html updated")

# ============================================================
# 3. fast-food.html: Add Porte-sauces + Barquettes sections
# ============================================================

ff_path = os.path.join(base_dir, "fast-food.html")
with open(ff_path, "r", encoding="utf-8") as f:
    ff = f.read()

new_products_html = """
                <!-- Porte-sauce 30ml -->
                <div class="detailed-card fade-in-up" style="transition-delay: 0.4s;">
                    <div class="detailed-image">
                        <span style="color:var(--text-secondary); font-size:4rem;">🥣</span>
                    </div>
                    <div class="detailed-info">
                        <h3>Porte-sauce 30ml</h3>
                        <div class="capacity-subtitle">Petits contenants kraft</div>
                        <table class="spec-table">
                            <tr><td>Contenance:</td><td>30 ml</td></tr>
                            <tr><td>Hauteur:</td><td>30 mm</td></tr>
                            <tr><td>Ø Haut:</td><td>50 mm</td></tr>
                            <tr><td>Ø Base:</td><td>38 mm</td></tr>
                        </table>
                        <p class="detailed-desc">Petits contenants papier kraft pour ketchup, mayonnaise et sauces. Eco-responsable.</p>
                        <a href="https://wa.me/212661177624?text=Bonjour,%20je%20souhaite%20commander%20des%20Porte-sauces%2030ml."
                            target="_blank" class="btn-whatsapp">
                            <i class="fa-brands fa-whatsapp"></i> Commander
                        </a>
                    </div>
                </div>

                <!-- Porte-sauce 60ml -->
                <div class="detailed-card fade-in-up" style="transition-delay: 0.5s;">
                    <div class="detailed-image">
                        <span style="color:var(--text-secondary); font-size:4rem;">🥣</span>
                    </div>
                    <div class="detailed-info">
                        <h3>Porte-sauce 60ml</h3>
                        <div class="capacity-subtitle">Format moyen</div>
                        <table class="spec-table">
                            <tr><td>Contenance:</td><td>60 ml</td></tr>
                            <tr><td>Hauteur:</td><td>35 mm</td></tr>
                            <tr><td>Ø Haut:</td><td>60 mm</td></tr>
                            <tr><td>Ø Base:</td><td>45 mm</td></tr>
                        </table>
                        <p class="detailed-desc">Format idéal pour les sauces en portion individuelle. Parfait pour hamburgers et wraps.</p>
                        <a href="https://wa.me/212661177624?text=Bonjour,%20je%20souhaite%20commander%20des%20Porte-sauces%2060ml."
                            target="_blank" class="btn-whatsapp">
                            <i class="fa-brands fa-whatsapp"></i> Commander
                        </a>
                    </div>
                </div>

                <!-- Porte-sauce 90ml -->
                <div class="detailed-card fade-in-up" style="transition-delay: 0.6s;">
                    <div class="detailed-image">
                        <span style="color:var(--text-secondary); font-size:4rem;">🥣</span>
                    </div>
                    <div class="detailed-info">
                        <h3>Porte-sauce 90ml</h3>
                        <div class="capacity-subtitle">Grand format</div>
                        <table class="spec-table">
                            <tr><td>Contenance:</td><td>90 ml</td></tr>
                            <tr><td>Hauteur:</td><td>40 mm</td></tr>
                            <tr><td>Ø Haut:</td><td>68 mm</td></tr>
                            <tr><td>Ø Base:</td><td>50 mm</td></tr>
                        </table>
                        <p class="detailed-desc">Grand format pour les accompagnements généreux. Idéal pour les plats à partager.</p>
                        <a href="https://wa.me/212661177624?text=Bonjour,%20je%20souhaite%20commander%20des%20Porte-sauces%2090ml."
                            target="_blank" class="btn-whatsapp">
                            <i class="fa-brands fa-whatsapp"></i> Commander
                        </a>
                    </div>
                </div>

                <!-- Barquette Alimentaire 500ml -->
                <div class="detailed-card fade-in-up" style="transition-delay: 0.7s;">
                    <div class="detailed-image">
                        <span style="color:var(--text-secondary); font-size:4rem;">🥡</span>
                    </div>
                    <div class="detailed-info">
                        <h3>Barquette 500ml</h3>
                        <div class="capacity-subtitle">Barquette Alimentaire Kraft</div>
                        <table class="spec-table">
                            <tr><td>Contenance:</td><td>500 ml</td></tr>
                            <tr><td>Hauteur:</td><td>45 mm</td></tr>
                            <tr><td>Ø Haut:</td><td>150×100 mm</td></tr>
                            <tr><td>Ø Base:</td><td>130×80 mm</td></tr>
                        </table>
                        <p class="detailed-desc">Barquette kraft résistante pour plats à emporter. Excellente tenue à la chaleur.</p>
                        <a href="https://wa.me/212661177624?text=Bonjour,%20je%20souhaite%20commander%20des%20Barquettes%20500ml."
                            target="_blank" class="btn-whatsapp">
                            <i class="fa-brands fa-whatsapp"></i> Commander
                        </a>
                    </div>
                </div>

                <!-- Barquette 750ml -->
                <div class="detailed-card fade-in-up" style="transition-delay: 0.8s;">
                    <div class="detailed-image">
                        <span style="color:var(--text-secondary); font-size:4rem;">🥡</span>
                    </div>
                    <div class="detailed-info">
                        <h3>Barquette 750ml</h3>
                        <div class="capacity-subtitle">Format Standard</div>
                        <table class="spec-table">
                            <tr><td>Contenance:</td><td>750 ml</td></tr>
                            <tr><td>Hauteur:</td><td>55 mm</td></tr>
                            <tr><td>Ø Haut:</td><td>170×120 mm</td></tr>
                            <tr><td>Ø Base:</td><td>150×100 mm</td></tr>
                        </table>
                        <p class="detailed-desc">Format standard pour les plats principaux. Compatibilité micro-ondes disponible sur demande.</p>
                        <a href="https://wa.me/212661177624?text=Bonjour,%20je%20souhaite%20commander%20des%20Barquettes%20750ml."
                            target="_blank" class="btn-whatsapp">
                            <i class="fa-brands fa-whatsapp"></i> Commander
                        </a>
                    </div>
                </div>

                <!-- Barquette 1000ml -->
                <div class="detailed-card fade-in-up" style="transition-delay: 0.9s;">
                    <div class="detailed-image">
                        <span style="color:var(--text-secondary); font-size:4rem;">🥡</span>
                    </div>
                    <div class="detailed-info">
                        <h3>Barquette 1000ml</h3>
                        <div class="capacity-subtitle">Grand Format</div>
                        <table class="spec-table">
                            <tr><td>Contenance:</td><td>1000 ml</td></tr>
                            <tr><td>Hauteur:</td><td>65 mm</td></tr>
                            <tr><td>Ø Haut:</td><td>190×130 mm</td></tr>
                            <tr><td>Ø Base:</td><td>170×110 mm</td></tr>
                        </table>
                        <p class="detailed-desc">Grand format pour les repas généreux et plateaux partagés. Idéal pour la restauration collective.</p>
                        <a href="https://wa.me/212661177624?text=Bonjour,%20je%20souhaite%20commander%20des%20Barquettes%201000ml."
                            target="_blank" class="btn-whatsapp">
                            <i class="fa-brands fa-whatsapp"></i> Commander
                        </a>
                    </div>
                </div>

                <!-- Barquette Ouverte S -->
                <div class="detailed-card fade-in-up" style="transition-delay: 1.0s;">
                    <div class="detailed-image">
                        <span style="color:var(--text-secondary); font-size:4rem;">🍟</span>
                    </div>
                    <div class="detailed-info">
                        <h3>Barquette ouverte S</h3>
                        <div class="capacity-subtitle">Barquette Frites & Snacks</div>
                        <table class="spec-table">
                            <tr><td>Contenance:</td><td>300 ml</td></tr>
                            <tr><td>Hauteur:</td><td>40 mm</td></tr>
                            <tr><td>Ø Haut:</td><td>130×90 mm</td></tr>
                            <tr><td>Ø Base:</td><td>110×70 mm</td></tr>
                        </table>
                        <p class="detailed-desc">Barquette ouverte pour frites et snacks. Format petit, idéal pour les portions individuelles.</p>
                        <a href="https://wa.me/212661177624?text=Bonjour,%20je%20souhaite%20commander%20des%20Barquettes%20ouvertes%20S."
                            target="_blank" class="btn-whatsapp">
                            <i class="fa-brands fa-whatsapp"></i> Commander
                        </a>
                    </div>
                </div>

                <!-- Barquette Ouverte M -->
                <div class="detailed-card fade-in-up" style="transition-delay: 1.1s;">
                    <div class="detailed-image">
                        <span style="color:var(--text-secondary); font-size:4rem;">🍟</span>
                    </div>
                    <div class="detailed-info">
                        <h3>Barquette ouverte M</h3>
                        <div class="capacity-subtitle">Barquette Frites & Snacks</div>
                        <table class="spec-table">
                            <tr><td>Contenance:</td><td>500 ml</td></tr>
                            <tr><td>Hauteur:</td><td>45 mm</td></tr>
                            <tr><td>Ø Haut:</td><td>150×100 mm</td></tr>
                            <tr><td>Ø Base:</td><td>130×80 mm</td></tr>
                        </table>
                        <p class="detailed-desc">Barquette ouverte taille medium pour frites et snacks. Design pratique pour consommation nomade.</p>
                        <a href="https://wa.me/212661177624?text=Bonjour,%20je%20souhaite%20commander%20des%20Barquettes%20ouvertes%20M."
                            target="_blank" class="btn-whatsapp">
                            <i class="fa-brands fa-whatsapp"></i> Commander
                        </a>
                    </div>
                </div>

                <!-- Barquette Ouverte L -->
                <div class="detailed-card fade-in-up" style="transition-delay: 1.2s;">
                    <div class="detailed-image">
                        <span style="color:var(--text-secondary); font-size:4rem;">🍟</span>
                    </div>
                    <div class="detailed-info">
                        <h3>Barquette ouverte L</h3>
                        <div class="capacity-subtitle">Grand Format</div>
                        <table class="spec-table">
                            <tr><td>Contenance:</td><td>750 ml</td></tr>
                            <tr><td>Hauteur:</td><td>55 mm</td></tr>
                            <tr><td>Ø Haut:</td><td>170×120 mm</td></tr>
                            <tr><td>Ø Base:</td><td>150×100 mm</td></tr>
                        </table>
                        <p class="detailed-desc">Grande barquette ouverte pour portions généreuses de frites et snacks à partager.</p>
                        <a href="https://wa.me/212661177624?text=Bonjour,%20je%20souhaite%20commander%20des%20Barquettes%20ouvertes%20L."
                            target="_blank" class="btn-whatsapp">
                            <i class="fa-brands fa-whatsapp"></i> Commander
                        </a>
                    </div>
                </div>
"""

# Insert before the closing of the detailed-product-grid in fast-food.html
contact_pos = ff.find("    <!-- Contact Section -->")
insert_here = ff.rfind("\n            </div>\n        </div>\n    </section>", 0, contact_pos)
if insert_here == -1:
    insert_here = ff.rfind("\r\n            </div>\r\n        </div>\r\n    </section>", 0, contact_pos)

if insert_here != -1:
    ff = ff[:insert_here] + new_products_html + ff[insert_here:]
    print("✅ fast-food.html: New products added via rfind method")
else:
    print("⚠️ Trying alternative for fast-food.html")
    ff = ff.replace("    <!-- Contact Section -->", new_products_html + "\n            </div>\n        </div>\n    </section>\n\n    <!-- Contact Section -->", 1)

with open(ff_path, "w", encoding="utf-8") as f:
    f.write(ff)

print("✅ fast-food.html updated")
print("\n🎉 All done!")
