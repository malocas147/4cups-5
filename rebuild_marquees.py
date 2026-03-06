import os
import re

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

partners = [
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
    ("Wok 4you", "partner-11.png"),
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

# The first marquee
marquee1 = build_marquee(partners, "flex animate-marquee gap-6")
# The second marquee (starts from half to look different)
partners_reverse = partners[5:] + partners[:5]
marquee2 = build_marquee(partners_reverse, "flex animate-marquee-reverse gap-6")

# Replace marquee 1
html = re.sub(
    r'<div class="flex animate-marquee gap-6">.*?</div>\s*</div>\s*<div class="relative mt-6">',
    marquee1 + '\n            </div>\n\n            <div class="relative mt-6">',
    html,
    flags=re.DOTALL
)

# Replace marquee 2
html = re.sub(
    r'<div class="flex animate-marquee-reverse gap-6">.*?</div>\s*</div>\s*</section>',
    marquee2 + '\n            </div>\n        </section>',
    html,
    flags=re.DOTALL
)


with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Marquees rebuilt successfully.")
