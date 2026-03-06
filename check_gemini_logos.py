import os
from PIL import Image

files = [
    'Gemini_Generated_Image_g4yblog4yblog4yb.png',
    'Gemini_Generated_Image_qt1koyqt1koyqt1k.png',
    'Gemini_Generated_Image_c3zz7qc3zz7qc3zz.png'
]

downloads_dir = r"C:\Users\Laptop\Downloads"

for fn in files:
    p = os.path.join(downloads_dir, fn)
    if os.path.exists(p):
        img = Image.open(p).convert('RGBA')
        colors = img.getcolors(100000)
        if colors:
            colors.sort(key=lambda x: x[0], reverse=True)
            print(f"{fn}: {[c[1] for c in colors[:3]]}")
        else:
            print(f"{fn}: Too many colors")
    else:
        print(f"{fn}: Not found")
