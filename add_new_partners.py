import os
import glob
import shutil
import re

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
brain_dir = r"C:\Users\Laptop\.gemini\antigravity\brain\cb36bf15-5e39-4f5f-bcd3-73268ecf66ea"
index_path = os.path.join(base_dir, "index.html")

media_files = glob.glob(os.path.join(brain_dir, "media__*.*"))
media_files.sort(key=os.path.getmtime, reverse=True)
newest_5 = media_files[:5]
newest_5.sort(key=os.path.getmtime)  # oldest to newest of the 5

partners = [
    ("Café De la Gare", "partner-12"),
    ("Dahab Café", "partner-13"),
    ("Shawarma Avenue", "partner-14"),
    ("Cafe Fast", "partner-15"),
    ("Kool Coffee", "partner-16")
]

new_partner_entries = []

for i, src_file in enumerate(newest_5):
    name, base_filename = partners[i]
    ext = os.path.splitext(src_file)[1]
    dest_filename = f"{base_filename}{ext}"
    dest_path = os.path.join(base_dir, "assets", dest_filename)
    shutil.copy2(src_file, dest_path)
    new_partner_entries.append((name, dest_filename))
    print(f"Copied {name} logo to {dest_filename}")

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
    ("Adoro Cafe", "partner-10.png")
]
all_partners.extend(new_partner_entries)

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

print("Marquees updated with 5 new partners!")
