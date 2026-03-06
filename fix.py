with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()
import re
pattern = r'(<!-- Navigation Arrows -->.*?</button>\s*<button.*?</button>\s*)(\s*<!-- Navigation Arrows -->.*?</button>\s*<button.*?</button>\s*)'
text = re.sub(pattern, r'\g<1>', text, flags=re.DOTALL)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
