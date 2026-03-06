from PIL import Image
import os

def clean_bg(path):
    print(f"Processing {path}...")
    img = Image.open(path).convert('RGBA')
    width, height = img.size
    pixels = img.load()
    
    # We will also try to smooth the edges slightly by not making it too harsh if needed,
    # but a simple replacement works for a white background container.
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            # Find light gray/white pixels that are typically part of a fake png checkerboard
            if r > 190 and g > 190 and b > 190 and max(r,g,b) - min(r,g,b) < 15:
                # Replace with pure white
                pixels[x, y] = (255, 255, 255, 255)
                
    img.save(path)
    print("Cleaned", path)

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website\assets"
clean_bg(os.path.join(base_dir, "partner-10.png"))
clean_bg(os.path.join(base_dir, "partner-11.png"))
