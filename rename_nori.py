import os

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace('src="assets/partner-5.png"', 'src="assets/partner-5-v2.png"')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Updated index.html to use partner-5-v2.png to bypass cache.")
