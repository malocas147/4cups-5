import os
import re

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
idx_path = os.path.join(base_dir, "index.html")

with open(idx_path, "r", encoding="utf-8") as f:
    idx = f.read()

# 1. Add Instagram posts
reel4 = """
                        <!-- Reel 4 -->
                        <div class="snap-center shrink-0 w-[300px] md:w-[320px]">
                            <div class="relative w-full aspect-[9/16] rounded-[2rem] overflow-hidden shadow-xl bg-muted/20 border border-border/50 bg-white">
                                <iframe src="https://www.instagram.com/p/DVCCHjfAIE2/embed" width="100%" height="100%" frameborder="0" scrolling="no" allowtransparency="true" class="absolute inset-0 w-full h-full object-cover"></iframe>
                            </div>
                        </div>"""

reel5 = """
                        <!-- Reel 5 -->
                        <div class="snap-center shrink-0 w-[300px] md:w-[320px]">
                            <div class="relative w-full aspect-[9/16] rounded-[2rem] overflow-hidden shadow-xl bg-muted/20 border border-border/50 bg-white">
                                <iframe src="https://www.instagram.com/p/DOjOKfxDT6C/embed" width="100%" height="100%" frameborder="0" scrolling="no" allowtransparency="true" class="absolute inset-0 w-full h-full object-cover"></iframe>
                            </div>
                        </div>"""

# Insert right after Reel 3
pattern = re.compile(
    r'(<!-- Reel 3 -->\s*<div class="snap-center shrink-0 w-\[300px\] md:w-\[320px\]">.*?</div>\s*</div>)',
    re.DOTALL
)
idx = pattern.sub(r'\1\n' + reel4 + '\n' + reel5, idx)

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(idx)

# 2. Update all contact forms to post to FormSubmit

files_to_update = ["index.html", "cafe.html", "restaurants.html", "fast-food.html", "glaciers.html"]
email_dest = "4cupsmaroc@gmail.com"

# Currently the form tag is something like <form class="space-y-6">
# We want to change it to: <form action="https://formsubmit.co/4cupsmaroc@gmail.com" method="POST" class="space-y-6">

form_pattern = re.compile(r'<form class="space-y-6">')
new_form_tag = f'<form action="https://formsubmit.co/{email_dest}" method="POST" class="space-y-6">\n                                <!-- Optional Settings for FormSubmit -->\n                                <input type="hidden" name="_captcha" value="false">\n                                <input type="hidden" name="_next" value="#">'

# Alternatively, wait, the user's form has no action attribute. Let's make sure.
form_pattern_2 = re.compile(r'<form(?! action)[^>]*class="space-y-6"[^>]*>')

for filename in files_to_update:
    filepath = os.path.join(base_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace the form tag
        # The form has a <button type="submit"> which is standard.
        if '<form class="space-y-6">' in content:
            new_content = content.replace('<form class="space-y-6">', new_form_tag)
            
            # Also ensure fields have `name` attributes, which FormSubmit requires
            new_content = re.sub(r'id="name"', r'id="name" name="nom"', new_content)
            new_content = re.sub(r'id="email"', r'id="email" name="email"', new_content)
            new_content = re.sub(r'id="phone"', r'id="phone" name="telephone"', new_content)
            new_content = re.sub(r'id="message"', r'id="message" name="message"', new_content)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"✅ {filename}: form updated with FormSubmit")

