import os
import re

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
files_to_update = ["cafe.html", "restaurants.html", "fast-food.html", "glaciers.html"]

for filename in files_to_update:
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
        
    # Replace WhatsApp number globally
    html = html.replace("212000000000", "212661177624")
    
    # Identify the Features Section block
    features_pattern = re.compile(r'<!-- Features Section -->.*?</section>', re.DOTALL)
    
    match = features_pattern.search(html)
    if match:
        features_block = match.group(0)
        
        # Remove it from its original place
        html = html.replace(features_block, "")
        
        # Insert it before the Contact Section
        contact_pattern = r'<!-- Contact Section -->'
        
        # Find where the contact section begins
        if contact_pattern in html:
            # Add some spacing to make it clean
            new_features_block = "\n    " + features_block + "\n\n    "
            
            # Split and insert
            parts = html.split(contact_pattern, 1)
            html = parts[0] + new_features_block + contact_pattern + parts[1]
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"Updated {filename} successfully.")
        else:
            print(f"Could not find Contact Section in {filename}")
    else:
        print(f"Could not find Features Section in {filename}")
