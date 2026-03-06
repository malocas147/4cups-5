import os

# Create the assets directory for the image if it doesn't exist
# Actually I will just put the image file in the correct location or assume it's there
# I see the image path in the user prompt is "image.png" but there might be a better name
# I'll just use the base64 or ask the user to upload it to assets.
# But wait, the image was attached to the prompt. I will just reference a placeholder 'assets/personnalisation.png' 
# or use the image path if I can find it. 

index_path = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

personnalisation_html = """
        <!-- Personnalisation Section -->
        <section id="personnalisation" class="py-24 bg-background">
            <div class="container">
                <div class="grid lg:grid-cols-2 gap-16 items-center">
                    
                    <!-- Image -->
                    <div class="relative order-2 lg:order-1">
                        <!-- Decorative background blob -->
                        <div class="absolute -right-8 -bottom-8 w-64 h-64 bg-accent/10 rounded-full blur-3xl"></div>
                        <div class="absolute -left-8 -top-8 w-64 h-64 bg-primary/10 rounded-full blur-3xl"></div>
                        
                        <div class="relative bg-secondary/30 rounded-3xl p-8 md:p-12 overflow-hidden group">
                           <div class="absolute bottom-0 left-0 right-0 h-1/2 bg-[#7aa0b8] rounded-t-[50%] z-0 translate-y-12"></div>
                            <img src="assets/personnalisation-cup.jpg" alt="Exemple de gobelet personnalisé 4cups" 
                                class="relative z-10 w-full max-w-md mx-auto aspect-[4/5] object-contain drop-shadow-2xl group-hover:scale-105 transition-transform duration-700"
                                onerror="this.src='https://placehold.co/600x800/f8fafc/1e293b?text=Image+Gobelet'"
                            />
                        </div>
                    </div>

                    <!-- Content -->
                    <div class="order-1 lg:order-2">
                        <span class="inline-block px-4 py-1.5 rounded-full bg-accent/10 text-accent text-sm font-body font-medium mb-4">
                            Sur-mesure
                        </span>
                        
                        <h2 class="text-3xl md:text-5xl font-heading font-bold text-foreground mb-6 leading-tight">
                            Personnalisez <span class="text-primary italic">Vos Emballages</span>
                        </h2>
                        
                        <p class="text-lg text-muted-foreground font-body mb-10 leading-relaxed">
                            Créez une présentation unique qui reflète parfaitement l'identité de votre marque et marque les esprits de vos clients.
                        </p>
                        
                        <div class="space-y-6">
                            <!-- Point 1 -->
                            <div class="flex items-start gap-4">
                                <div class="flex-shrink-0 w-12 h-12 rounded-xl bg-primary/10 flex items-center justify-center text-primary">
                                    <i data-lucide="palette" class="w-6 h-6"></i>
                                </div>
                                <div>
                                    <h3 class="text-xl font-heading font-bold text-foreground mb-1">Ajout de logos</h3>
                                    <p class="text-muted-foreground font-body">Intégration parfaite de votre identité visuelle.</p>
                                </div>
                            </div>
                            
                            <!-- Point 2 -->
                            <div class="flex items-start gap-4">
                                <div class="flex-shrink-0 w-12 h-12 rounded-xl bg-accent/10 flex items-center justify-center text-accent">
                                    <i data-lucide="droplet" class="w-6 h-6"></i>
                                </div>
                                <div>
                                    <h3 class="text-xl font-heading font-bold text-foreground mb-1">Choix de couleurs</h3>
                                    <p class="text-muted-foreground font-body">Une palette illimitée pour respecter votre charte graphique.</p>
                                </div>
                            </div>
                            
                            <!-- Point 3 -->
                            <div class="flex items-start gap-4">
                                <div class="flex-shrink-0 w-12 h-12 rounded-xl bg-primary/10 flex items-center justify-center text-primary">
                                    <i data-lucide="ruler" class="w-6 h-6"></i>
                                </div>
                                <div>
                                    <h3 class="text-xl font-heading font-bold text-foreground mb-1">Formats sur mesure</h3>
                                    <p class="text-muted-foreground font-body">Des dimensions exactes adaptées à vos produits.</p>
                                </div>
                            </div>
                            
                            <!-- Point 4 -->
                            <div class="flex items-start gap-4">
                                <div class="flex-shrink-0 w-12 h-12 rounded-xl bg-accent/10 flex items-center justify-center text-accent">
                                    <i data-lucide="sparkles" class="w-6 h-6"></i>
                                </div>
                                <div>
                                    <h3 class="text-xl font-heading font-bold text-foreground mb-1">Design personnalisé</h3>
                                    <p class="text-muted-foreground font-body">Un accompagnement pour un rendu à votre image.</p>
                                </div>
                            </div>
                        </div>

                        <div class="mt-10">
                            <a href="#contact" class="inline-flex items-center gap-2 px-8 py-3.5 rounded-full bg-foreground text-background font-body font-semibold text-sm hover:bg-foreground/90 transition-colors">
                                Demander une maquette
                                <i data-lucide="arrow-right" class="w-4 h-4"></i>
                            </a>
                        </div>
                    </div>

                </div>
            </div>
        </section>

"""

content = content.replace(
    "<!-- About Section -->\n        <section id=\"apropos\"",
    personnalisation_html + "<!-- About Section -->\n        <section id=\"apropos\""
)

# Alternative line endings
content = content.replace(
    "<!-- About Section -->\r\n        <section id=\"apropos\"",
    personnalisation_html + "<!-- About Section -->\r\n        <section id=\"apropos\""
)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Added Personnalisation section to index.html")
