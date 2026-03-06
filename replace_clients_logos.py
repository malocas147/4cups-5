import os
import re

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
idx_path = os.path.join(base_dir, "index.html")

with open(idx_path, "r", encoding="utf-8") as f:
    idx = f.read()

# Build the generic HTML for logos
def build_marquee_content():
    content = ""
    # We create 6 unique placeholders, and repeat them to ensure seamless infinite looping.
    # We do 2 sets of 6 = 12 items.
    for i in range(12):
        n = (i % 6) + 1
        content += f"""                    <div class="flex-shrink-0 w-48 h-24 bg-background border border-border rounded-xl shadow-sm flex items-center justify-center p-4">
                        <img src="assets/client-logo-{n}.png" alt="Logo Partenaire {n}" class="max-w-full max-h-full object-contain grayscale opacity-60 hover:grayscale-0 hover:opacity-100 transition-all duration-300">
                    </div>\n"""
    return content

new_inner = build_marquee_content()

# Replace first marquee
pattern1 = re.compile(
    r'(<div class="flex animate-marquee gap-6">).*?(</div>\s*</div>)',
    re.DOTALL
)
idx = pattern1.sub(r'\1\n' + new_inner + r'                \2', idx)

# Replace second marquee
pattern2 = re.compile(
    r'(<div class="flex animate-marquee-reverse gap-6">).*?(</div>\s*</div>)',
    re.DOTALL
)
# Make a slightly shifted pattern for reverse
def build_marquee_reverse_content():
    content = ""
    for i in range(12):
        n = ((i + 3) % 6) + 1 # Offset by 3 so the second row looks different 
        content += f"""                    <div class="flex-shrink-0 w-48 h-24 bg-background border border-border rounded-xl shadow-sm flex items-center justify-center p-4">
                        <img src="assets/client-logo-{n}.png" alt="Logo Partenaire {n}" class="max-w-full max-h-full object-contain grayscale opacity-60 hover:grayscale-0 hover:opacity-100 transition-all duration-300">
                    </div>\n"""
    return content

new_inner2 = build_marquee_reverse_content()
idx = pattern2.sub(r'\1\n' + new_inner2 + r'                \2', idx)

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(idx)

print("✅ index.html: Marquee names replaced by logo placeholders")
