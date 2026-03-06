import os
from PIL import Image

files_to_check = [
    r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website\assets\partner-5.png",
    r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website\assets\partner-5-v2.png",
    r"C:\Users\Laptop\.gemini\antigravity\brain\cb36bf15-5e39-4f5f-bcd3-73268ecf66ea\media__1772669359534.png",
    r"C:\Users\Laptop\.gemini\antigravity\brain\cb36bf15-5e39-4f5f-bcd3-73268ecf66ea\media__1772674007048.png"
]

for f in files_to_check:
    if os.path.exists(f):
        img = Image.open(f).convert('RGBA')
        colors = img.getcolors(1000000)
        colors.sort(key=lambda x: x[0], reverse=True)
        print(f"File: {os.path.basename(f)}")
        print(f"  Top colors: {[c[1] for c in colors[:5]]}")
        print(f"  Size: {img.size}")
    else:
        print(f"File NOT FOUND: {f}")
        
