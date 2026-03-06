import os
import re

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
idx_path = os.path.join(base_dir, "index.html")
files_to_update = ["index.html", "cafe.html", "restaurants.html", "fast-food.html", "glaciers.html"]
email_dest = "4cupsmaroc@gmail.com"

# In the actual HTML, the form starts with:
# <form class="lg:col-span-3 flex flex-col gap-5">
# Or something similar for contact forms.

new_form_attributes = f'action="https://formsubmit.co/{email_dest}" method="POST" '
hidden_inputs = '\n                        <input type="hidden" name="_captcha" value="false">\n                        <input type="hidden" name="_next" value="">'

for filename in files_to_update:
    filepath = os.path.join(base_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # 1. Inject action and method into any <form> tag that doesn't have an action
        # The form on index.html is <form class="lg:col-span-3 flex flex-col gap-5">
        if '<form class=' in content and 'action="https://formsubmit.co' not in content:
            # We will use regex to find all <form ...> without action
            content = re.sub(r'<form(?![^>]*action=)([^>]*)>', r'<form \1' + new_form_attributes + r'>' + hidden_inputs, content)
            
            # 2. Add 'name' attributes to inputs
            # Only do this if they don't already have one
            content = re.sub(r'<input([^>]*?)placeholder="Nom"([^>]*?)>', r'<input\1placeholder="Nom"\2 name="nom" id="nom">', content)
            content = re.sub(r'<input([^>]*?)placeholder="Email"([^>]*?)>', r'<input\1placeholder="Email"\2 name="email" id="email">', content)
            content = re.sub(r'<input([^>]*?)placeholder="Numéro de téléphone"([^>]*?)>', r'<input\1placeholder="Numéro de téléphone"\2 name="telephone" id="telephone">', content)
            # Textarea
            content = re.sub(r'<textarea([^>]*?)placeholder="Votre message \(optionnel\)\.\.\."([^>]*?)>', r'<textarea\1placeholder="Votre message (optionnel)..."\2 name="message" id="message">', content)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ {filename}: form updated with FormSubmit")
        else:
            print(f"⏭️ {filename}: no un-actioned form found or already updated.")
