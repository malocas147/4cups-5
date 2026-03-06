from PIL import Image, ImageDraw, ImageFont
import os
import re

# 1. Generate text-based logos
brands = [
    "Oliveri", "Cafe Carrion", "Picks", "La Grillardiere", 
    "Nouri", "Zushi", "Blueberry", "Al Itkane", 
    "Gelato Lab", "Adoro Cafe", "Wok 4you"
]

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
assets_dir = os.path.join(base_dir, "assets")

# Create a simple placeholder logo for each brand
try:
    # Try to load Arial or generic font
    font = ImageFont.truetype("arial.ttf", 40)
except:
    font = ImageFont.load_default()

for i, brand in enumerate(brands, 1):
    # Create image with transparent background
    img = Image.new('RGBA', (300, 100), (255, 255, 255, 0))
    d = ImageDraw.Draw(img)
    
    # Calculate text bounding box
    bbox = d.textbbox((0, 0), brand, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    x = (300 - text_w) / 2
    y = ((100 - text_h) / 2) - 10 # Slight visual adjustment
    
    # Draw text in dark grey
    d.text((x, y), brand, font=font, fill=(50, 50, 50, 255))
    
    # Save to assets
    filename = f"partner-{i}.png"
    img.save(os.path.join(assets_dir, filename))

print(f"✅ Generated {len(brands)} placeholder logos.")

# 2. Update index.html to include all 11 logos
idx_path = os.path.join(base_dir, "index.html")
with open(idx_path, "r", encoding="utf-8") as f:
    idx = f.read()

# Build marquee content for 11 logos
def build_marquee_content():
    content = ""
    # We repeat them a few times to ensure seamless infinite looping.
    # Total 22 items
    for i in range(22):
        n = (i % 11) + 1
        brand_name = brands[(i % 11)]
        content += f"""                    <div class="flex-shrink-0 w-48 h-24 bg-background border border-border rounded-xl shadow-sm flex items-center justify-center p-4">
                        <img src="assets/partner-{n}.png" alt="Logo {brand_name}" class="max-w-full max-h-full object-contain grayscale opacity-60 hover:grayscale-0 hover:opacity-100 transition-all duration-300">
                    </div>\n"""
    return content

new_inner = build_marquee_content()

pattern1 = re.compile(
    r'(<div class="flex animate-marquee gap-6">).*?(</div>\s*</div>)',
    re.DOTALL
)
# Make sure we don't accidentally match the reverse marquee, wait, the closing tags are tricky. 
# It's better to just replace by matching the <div class="flex animate-marquee gap-6"> and the next </div></div>.
# But there might be nested divs.
# The previous script successfully replaced it, so let's use the same logic.

def replace_marquee(html_content, class_name, offset=0):
    content = ""
    for i in range(22):
        n = ((i + offset) % 11) + 1 
        brand_name = brands[((i + offset) % 11)]
        content += f"""                    <div class="flex-shrink-0 w-48 h-24 bg-background border border-border rounded-xl shadow-sm flex items-center justify-center p-4">
                        <img src="assets/partner-{n}.png" alt="Logo {brand_name}" class="max-w-full max-h-full object-contain grayscale opacity-60 hover:grayscale-0 hover:opacity-100 transition-all duration-300">
                    </div>\n"""
    
    patt = re.compile(rf'(<div class="{class_name}">).*?(</div>\s*</div>)', re.DOTALL)
    return patt.sub(rf'\1\n{content}                \2', html_content)


idx = replace_marquee(idx, "flex animate-marquee gap-6", offset=0)
idx = replace_marquee(idx, "flex animate-marquee-reverse gap-6", offset=5)

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(idx)

print("✅ index.html: Marquee updated with 11 partners.")
