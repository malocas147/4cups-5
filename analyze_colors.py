from PIL import Image

def analyze(path):
    print(f"\nAnalyzing {path}")
    img = Image.open(path).convert('RGB')
    colors = img.getcolors(img.size[0]*img.size[1])
    colors.sort(key=lambda x: x[0], reverse=True)
    for count, color in colors[:10]:
        print(f"Count: {count}, Color: {color}")

analyze(r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website\assets\partner-10.png")
analyze(r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website\assets\partner-11.png")
