import os
import re

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"

new_frite_card = """
                <!-- Barquette Frite -->
                <div class="detailed-card fade-in-up">
                    <div class="detailed-image">
                        <span style="color:var(--text-secondary); font-size:4rem;">🍟</span>
                    </div>
                    <div class="detailed-info">
                        <h3>Barquette à Frites</h3>
                        <div class="capacity-subtitle">Idéal pour Frites & Snacks</div>
                        <table class="spec-table">
                            <tr><td>Format:</td><td>Standard ou Grand</td></tr>
                            <tr><td>Matériau:</td><td>Carton ingraissable premium</td></tr>
                            <tr><td>Design:</td><td>Prise en main ergonomique</td></tr>
                        </table>
                        <p class="detailed-desc">Emballage pratique et résistant aux graisses, conçu pour maintenir la chaleur et le croustillant de vos frites.</p>
                        <a href="https://wa.me/212661177624?text=Bonjour,%20je%20souhaite%20commander%20des%20Barquettes%20à%20Frites." target="_blank" class="btn-whatsapp">
                            <i class="fa-brands fa-whatsapp"></i> Commander
                        </a>
                    </div>
                </div>
"""

def inject_product(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # We will inject at the end of the detailed-product-grid
    target_grid_end = '            </div>\n        </div>\n    </section>\n\n    <!--'
    if target_grid_end in html:
        html = html.replace(target_grid_end, new_frite_card + '\n' + target_grid_end)
    else:
        target_grid_end_fallback = '            </div>\n        </div>\n    </section>'
        parts = html.rsplit(target_grid_end_fallback, 1)
        if len(parts) == 2:
            html = parts[0] + new_frite_card + '\n' + target_grid_end_fallback + parts[1]
            
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated {os.path.basename(filepath)}")

inject_product(os.path.join(base_dir, "restaurants.html"))
inject_product(os.path.join(base_dir, "fast-food.html"))
