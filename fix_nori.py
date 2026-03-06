import os
import re

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# We need to find the <div class="flex animate-marquee gap-6"> ... </div> block and rebuild it perfectly.
# The user wants to KEEP the new "Nori" (which is partner-5-v2.png) and REMOVE the old "Nori".
# Wait, let's verify if there is an old Nori image named differently like partner-nori.png or something.
# The partner list: Oliveri, Cafe Carrion, Picks, La Grillardiere, Nori, Zushi, Blueberry, Al Itkane, Gelato Lab, Adoro Cafe, Wok 4you.
# Let's list the partners and their files:
partners = [
    ("Oliveri", "partner-1.svg"),
    ("Cafe Carrion", "partner-2.png"),
    ("Picks", "partner-3.jpg"),
    ("La Grillardiere", "partner-4.png"),
    ("Nori", "partner-5-v2.png"),  # The good one
    ("Zushi", "partner-6.png"),
    ("Blueberry", "partner-7.png"),
    ("Al Itkane", "partner-8.webp"),
    ("Gelato Lab", "partner-9.jpg"),
    ("Adoro Cafe", "partner-10.png"),
    ("Wok 4you", "partner-11.png"),
]

# We will replace the entire marquee content.
marquee_start = html.find('<div class="flex animate-marquee gap-6">')
if marquee_start == -1:
    print("Could not find marquee start")
    exit(1)

marquee_end = html.find('</div>\n            </div>\n\n            <!-- Second Support -->\n', marquee_start)
if marquee_end == -1:
    # Try another way
    marquee_end = html.find('</div>\n            </div>\n\n        </section>', marquee_start)

if marquee_end == -1:
    print("Could not find marquee end")
    # Let's just create a regex to replace the content of <div class="flex animate-marquee gap-6">...</div>
    marquee_end = html.find('</div>\n            </div>', marquee_start)

new_marquee_content = '<div class="flex animate-marquee gap-6">\n'
# Multiply by 3 for infinite scroll effect
for _ in range(3):
    for name, img_file in partners:
        new_marquee_content += f'''                    <div
                        class="flex-shrink-0 w-48 h-24 bg-background border border-border rounded-xl shadow-sm flex items-center justify-center p-4">
                        <img src="assets/{img_file}" alt="Logo {name}"
                            class="max-w-full max-h-full object-contain transition-all duration-300">
                    </div>\n'''

new_marquee_content += '                </div>'

# We replace from marquee_start to marquee_end with new_marquee_content
# Let's find exactly the end of the <div class="flex animate-marquee gap-6"> element.
# It ends right before "</div>\n            </div>" for the container.

# We can use regex to replace everything inside:
html = re.sub(
    r'<div class="flex animate-marquee gap-6">.*?</div>\n            </div>',
    new_marquee_content + '\n            </div>',
    html,
    flags=re.DOTALL
)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Rebuilt marquee with only the GOOD logos.")

