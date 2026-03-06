import re, os

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"

# ============================================================
# 1. fast-food.html: Remove the original 4 products
# ============================================================
ff_path = os.path.join(base_dir, "fast-food.html")
with open(ff_path, "r", encoding="utf-8") as f:
    ff = f.read()

# Remove from "<!-- Boîte Burger XL -->" up to (but not including) "<!-- Porte-sauce 30ml -->"
start_marker = "                <!-- Boîte Burger XL -->"
end_marker = "                <!-- Porte-sauce 30ml -->"

start_idx = ff.find(start_marker)
end_idx = ff.find(end_marker)

if start_idx != -1 and end_idx != -1:
    ff = ff[:start_idx] + ff[end_idx:]
    print("✅ fast-food.html: 4 old products removed")
else:
    print(f"⚠️ Could not find markers. start={start_idx}, end={end_idx}")

with open(ff_path, "w", encoding="utf-8") as f:
    f.write(ff)

# ============================================================
# 2. cafe.html: Fix the empty gap
#    The gap is caused by the personnalisation-cup placeholder image
#    section that was inserted (with the onerror fallback text)
#    - let's find any empty sections or sections with no real content
# ============================================================
cafe_path = os.path.join(base_dir, "cafe.html")
with open(cafe_path, "r", encoding="utf-8") as f:
    cafe = f.read()

# The empty section is likely an old section-header div with no products
# or a div left from the couvercles insertion that has an extra closing tags pattern
# Let's check for the pattern where the rfind insertion may have added extra closing divs

# Look for the double closing pattern that the rfind approach may have inserted
# The insertion was: couvercles_html + "\n            </div>\n        </div>\n    </section>"
# So we might have extra </div></div></section>

# Count and fix extra closing tags by looking for ...
# Actually the issue is more likely that there's an empty section 
# (the one at the top of the products section that has no products)
# Let's look for a section-header that is followed immediately by </div></div></section>
bad_pattern = re.compile(
    r'(<div class="section-header [^"]*"[^>]*>.*?</div>\s*)\n\s*\n\s*</div>\s*\n\s*</div>\s*\n\s*</section>',
    re.DOTALL
)

# More direct approach: look for the duplicate closing tag from our earlier insert
# Our insert added couvercles before "\n            </div>\n        </div>\n    </section>"
# Check if there's a double occurrence of this pattern
closing_pattern = "\n            </div>\n        </div>\n    </section>"
count = cafe.count(closing_pattern)
print(f"Found {count} occurrences of closing pattern in cafe.html")

# Also look for the placeholder image section that might create visual gap
# Remove any empty detailed-product-grid divs or sections with only the header and no cards
# Pattern: section > container > section-header > empty detailed-product-grid > /div/div/section
empty_grid_pattern = re.compile(
    r'\s*<!-- Detailed Products Grid -->\s*\n\s*<div class="detailed-product-grid">\s*\n\s*</div>',
    re.DOTALL
)
if empty_grid_pattern.search(cafe):
    cafe = empty_grid_pattern.sub('', cafe)
    print("✅ cafe.html: Removed empty detailed-product-grid")

# Also look for any section that has just a section-header and nothing else
# caused by the failed insertion
orphan_section = re.compile(
    r'\s*<!-- Specific Products -->\s*\n\s*<section class="products">\s*\n'
    r'\s*<div class="container">\s*\n'
    r'\s*<div class="section-header[^"]*"[^>]*>\s*\n'
    r'.*?</div>\s*\n'
    r'\s*</div>\s*\n\s*</section>',
    re.DOTALL
)

# More targeted: remove duplicate section-header blocks
# The issue is more subtle - let's just check for the specific empty block

# Check if there's an empty section between hero and products
# by looking for <section class="products"> that is followed by only headers
sections = cafe.split('<section class="products">')
print(f"Found {len(sections)-1} 'products' sections in cafe.html")

with open(cafe_path, "w", encoding="utf-8") as f:
    f.write(cafe)

print("✅ Done!")
