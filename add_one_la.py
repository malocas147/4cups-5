import os
import shutil
import re

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
index_path = os.path.join(base_dir, "index.html")
new_logo_src = r"C:\Users\Laptop\.gemini\antigravity\brain\cb36bf15-5e39-4f5f-bcd3-73268ecf66ea\media__1772677233651.png"

# Copy the new logo
dest_filename = "partner-17.png"
dest_path = os.path.join(base_dir, "assets", dest_filename)
if os.path.exists(new_logo_src):
    shutil.copy2(new_logo_src, dest_path)
    print(f"Copied One La logo to {dest_filename}")
else:
    print(f"Source file not found: {new_logo_src}")

# Rebuild marquees with the new partner
all_partners = [
    ("Oliveri", "partner-1.svg"),
    ("Cafe Carrion", "partner-2.png"),
    ("Picks", "partner-3.jpg"),
    ("La Grillardiere", "partner-4.png"),
    ("Nori", "partner-5-v2.png"),
    ("Zushi", "partner-6.png"),
    ("Blueberry", "partner-7.png"),
    ("Al Itkane", "partner-8.webp"),
    ("Gelato Lab", "partner-9.jpg"),
    ("Adoro Cafe", "partner-10.png"),
    ("Café De la Gare", "partner-12.png"),
    ("Dahab Café", "partner-13.png"),
    ("Shawarma Avenue", "partner-14.png"),
    ("Cafe Fast", "partner-15.png"),
    ("Kool Coffee", "partner-16.png"),
    ("One Là!!!", "partner-17.png")
]

def build_marquee(partners_list, css_class):
    content = f'<div class="{css_class}">\n'
    for _ in range(3):
        for name, img_file in partners_list:
            content += f'''                    <div
                        class="flex-shrink-0 w-48 h-24 bg-background border border-border rounded-xl shadow-sm flex items-center justify-center p-4">
                        <img src="assets/{img_file}" alt="Logo {name}"
                            class="max-w-full max-h-full object-contain transition-all duration-300">
                    </div>\n'''
    content += '                </div>'
    return content

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace text: "personnalisation" -> "production" inside the specific paragraph
html = html.replace(
    'confient la personnalisation de leurs emballages.</p>',
    'confient la production de leurs emballages.</p>'
)

marquee1 = build_marquee(all_partners, "flex animate-marquee gap-6")
half = len(all_partners) // 2
partners_reverse = all_partners[half:] + all_partners[:half]
marquee2 = build_marquee(partners_reverse, "flex animate-marquee-reverse gap-6")

html = re.sub(
    r'<div class="flex animate-marquee gap-6">.*?</div>\s*</div>\s*<div class="relative mt-6">',
    marquee1 + '\n            </div>\n\n            <div class="relative mt-6">',
    html,
    flags=re.DOTALL
)

html = re.sub(
    r'<div class="flex animate-marquee-reverse gap-6">.*?</div>\s*</div>\s*</section>',
    marquee2 + '\n            </div>\n        </section>',
    html,
    flags=re.DOTALL
)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Marquees updated with 16 partners and text replaced.")
