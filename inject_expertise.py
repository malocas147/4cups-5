import os
import re

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

new_section_html = """
        <!-- Expertise Section -->
        <section class="py-24 bg-background border-t border-border">
            <div class="container">
                <div class="text-center mb-16">
                    <span class="inline-block px-4 py-1.5 rounded-full bg-primary/10 text-primary text-sm font-body font-medium mb-4">Notre Différence</span>
                    <h2 class="font-heading text-3xl md:text-5xl font-bold text-foreground mb-4">Qu'est-ce qui nous distingue ?</h2>
                    <p class="text-xl md:text-2xl font-semibold text-primary max-w-3xl mx-auto italic mb-4">
                        "Le premier Fabricant de gobelets en carton personnalisés au Maroc"
                    </p>
                </div>
                
                <div class="grid md:grid-cols-3 gap-8">
                    <!-- Feature 1 -->
                    <div class="bg-card border border-border rounded-2xl p-8 hover:shadow-lg transition-shadow duration-300 relative overflow-hidden group text-center">
                        <div class="absolute -right-8 -top-8 w-32 h-32 bg-primary/5 rounded-full group-hover:scale-150 transition-transform duration-500"></div>
                        <div class="w-16 h-16 rounded-2xl bg-primary/10 flex items-center justify-center mb-6 mx-auto relative z-10">
                            <i data-lucide="award" class="w-8 h-8 text-primary"></i>
                        </div>
                        <h3 class="font-heading text-xl font-semibold text-foreground mb-3 relative z-10">Notre Expertise</h3>
                        <p class="font-body text-muted-foreground leading-relaxed relative z-10">Pionniers dans la fabrication d'emballages personnalisés au Maroc avec un savoir-faire inégalé et des installations de pointe.</p>
                    </div>

                    <!-- Feature 2 -->
                    <div class="bg-card border border-border rounded-2xl p-8 hover:shadow-lg transition-shadow duration-300 relative overflow-hidden group text-center">
                        <div class="absolute -right-8 -top-8 w-32 h-32 bg-primary/5 rounded-full group-hover:scale-150 transition-transform duration-500"></div>
                        <div class="w-16 h-16 rounded-2xl bg-primary/10 flex items-center justify-center mb-6 mx-auto relative z-10">
                            <i data-lucide="shield-check" class="w-8 h-8 text-primary"></i>
                        </div>
                        <h3 class="font-heading text-xl font-semibold text-foreground mb-3 relative z-10">Qualité Supérieure</h3>
                        <p class="font-body text-muted-foreground leading-relaxed relative z-10">Des matériaux rigoureusement sélectionnés et certifiés alimentaires pour des gobelets robustes, étanches et premium.</p>
                    </div>

                    <!-- Feature 3 -->
                    <div class="bg-card border border-border rounded-2xl p-8 hover:shadow-lg transition-shadow duration-300 relative overflow-hidden group text-center">
                        <div class="absolute -right-8 -top-8 w-32 h-32 bg-primary/5 rounded-full group-hover:scale-150 transition-transform duration-500"></div>
                        <div class="w-16 h-16 rounded-2xl bg-primary/10 flex items-center justify-center mb-6 mx-auto relative z-10">
                            <i data-lucide="zap" class="w-8 h-8 text-primary"></i>
                        </div>
                        <h3 class="font-heading text-xl font-semibold text-foreground mb-3 relative z-10">Processus Efficace</h3>
                        <p class="font-body text-muted-foreground leading-relaxed relative z-10">Une chaîne de production optimisée garantissant des délais de livraison extrêmement rapides et un service client réactif.</p>
                    </div>
                </div>
            </div>
        </section>
"""

# Insert right after: <!-- Social Proof / Instagram Reels Carousel Section -->
# Actually, the user approved "avant les vidéos Instagram"
# Let's find "<!-- Social Proof / Instagram Reels Carousel Section -->"
target_marker = "<!-- Social Proof / Instagram Reels Carousel Section -->"

if target_marker in html:
    parts = html.split(target_marker, 1)
    html = parts[0] + new_section_html + "\n        " + target_marker + parts[1]
    
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Successfully injected Expertise section.")
else:
    print("Could not find the target section marker.")
