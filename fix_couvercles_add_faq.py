import os

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"

# ============================================================
# 1. Fix cafe.html couvercles layout
# ============================================================
cafe_path = os.path.join(base_dir, "cafe.html")
with open(cafe_path, "r", encoding="utf-8") as f:
    cafe = f.read()

# Find the start of the couvercles
start_couv = cafe.find("                <!-- Couvercles pour Gobelets -->")
# The end is the closing of the section/container
end_couv = cafe.find("    <!-- Contact Section -->", start_couv)
# Well, actually there's `</div>\n        </div>\n    </section>` before Contact, let's find that
end_couv_precise = cafe.rfind("            </div>\n        </div>\n    </section>", start_couv, end_couv)
if end_couv_precise == -1:
    end_couv_precise = cafe.rfind("            </div>\r\n        </div>\r\n    </section>", start_couv, end_couv)

# Extract the couvercles raw HTML (it's currently inside the table section)
couvercles_html = cafe[start_couv:end_couv_precise]

# We need to remove them from their current place
cafe_cleaned = cafe[:start_couv]

# And we will append them properly wrapped:
proper_couvercles_section = """
    </section>

    <!-- Section Couvercles -->
    <section class="products overflow-hidden" style="padding-top: 0;">
        <div class="container">
            <div class="section-header fade-in-up" style="margin-bottom: 2rem;">
                <h2>Gamme Couvercles - 4CUPS</h2>
                <p>Couvercles adaptés et sécurisés pour notre gamme de gobelets.</p>
                <div class="category-badges">
                    <div class="spec-badge">✅ Anti-renversement</div>
                    <div class="spec-badge">🌡️ Haute résistance thermique</div>
                </div>
            </div>

            <!-- Detailed Products Grid -->
            <div class="detailed-product-grid">
""" + couvercles_html + """
            </div>
        </div>
    </section>

"""

# Then we attach the rest of the file (from end_couv_precise + the closing tags we skipped over)
cafe_cleaned += proper_couvercles_section + cafe[end_couv_precise + len("\n            </div>\n        </div>\n    </section>"):]

with open(cafe_path, "w", encoding="utf-8") as f:
    f.write(cafe_cleaned)
print("✅ cafe.html: Couvercles wrapped in grid layout")


# ============================================================
# 2. Add FAQ section to index.html
# ============================================================
idx_path = os.path.join(base_dir, "index.html")
with open(idx_path, "r", encoding="utf-8") as f:
    idx = f.read()

faq_html = """
        <!-- FAQ Section -->
        <section id="faq" class="py-24 bg-secondary/50">
            <div class="container max-w-4xl mx-auto px-4">
                <div class="text-center mb-16">
                    <span class="inline-block px-4 py-1.5 rounded-full bg-primary/10 text-primary text-sm font-body font-medium mb-4">
                        Des questions ?
                    </span>
                    <h2 class="text-3xl md:text-5xl font-heading font-bold text-foreground mb-4">
                        Foire Aux Questions
                    </h2>
                    <p class="text-muted-foreground font-body text-lg">
                        Retrouvez les réponses aux questions les plus fréquentes sur nos produits et services.
                    </p>
                </div>

                <div class="space-y-4">
                    <!-- Q1 -->
                    <div class="bg-background border border-border rounded-xl p-6 shadow-sm hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-heading font-bold text-foreground mb-2 flex items-center justify-between">
                            Quel est le minimum de commande pour la personnalisation ?
                        </h3>
                        <p class="text-muted-foreground font-body leading-relaxed">
                            Pour la majorité de nos produits (gobelets, barquettes), le minimum de commande (MOQ) pour la personnalisation avec votre logo est de 10 000 pièces.
                        </p>
                    </div>

                    <!-- Q2 -->
                    <div class="bg-background border border-border rounded-xl p-6 shadow-sm hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-heading font-bold text-foreground mb-2 flex items-center justify-between">
                            Livrez-vous partout au Maroc ?
                        </h3>
                        <p class="text-muted-foreground font-body leading-relaxed">
                            Absolument ! Nous produisons localement à Casablanca (Bouskoura) et nous assurons la logistique sur l'ensemble du territoire marocain.
                        </p>
                    </div>

                    <!-- Q3 -->
                    <div class="bg-background border border-border rounded-xl p-6 shadow-sm hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-heading font-bold text-foreground mb-2 flex items-center justify-between">
                            Quels sont les délais de production ?
                        </h3>
                        <p class="text-muted-foreground font-body leading-relaxed">
                            Une fois le BAT (Bon À Tirer) validé et l'acompte réglé, le délai moyen de production est de 15 à 20 jours ouvrables. Vous serez tenu informé à chaque étape.
                        </p>
                    </div>

                    <!-- Q4 -->
                    <div class="bg-background border border-border rounded-xl p-6 shadow-sm hover:shadow-md transition-shadow">
                        <h3 class="text-xl font-heading font-bold text-foreground mb-2 flex items-center justify-between">
                            Vos emballages sont-ils recyclables / écologiques ?
                        </h3>
                        <p class="text-muted-foreground font-body leading-relaxed">
                            Oui, nos emballages en papier kraft et carton sont fabriqués à partir de matériaux durables et certifiés, répondant aux normes de respect de l'environnement.
                        </p>
                    </div>
                </div>
            </div>
        </section>
"""

# Insert FAQ right before the Contact section!
contact_idx = idx.find('        <section id="contact"')
if contact_idx != -1:
    idx_new = idx[:contact_idx] + faq_html + "\n" + idx[contact_idx:]
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(idx_new)
    print("✅ index.html: FAQ section added")
else:
    print("⚠️ Could not locate Contact section in index.html")
