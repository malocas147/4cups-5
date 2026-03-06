import os
import re

html_files = ["cafe.html", "restaurants.html", "fast-food.html", "glaciers.html", "index.html"]
base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"

for fname in html_files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Add `list-none m-0 p-0` to any `ul` inside the <nav> block
    # and to mobile menu if present
    content = content.replace('<ul class="hidden md:flex items-center gap-8">', '<ul class="hidden md:flex items-center gap-8 list-none m-0 p-0">')
    content = content.replace('<ul class="flex flex-col gap-4 px-6 py-6 border-t border-border">', '<ul class="flex flex-col gap-4 px-6 py-6 border-t border-border list-none m-0 p-0">')
    
    # Let's forcefully change the mobile button ID and menu to avoid conflict with the old CSS and JS since we don't want the old toggler
    content = content.replace('id="mobile-menu-btn"', 'id="tailwind-mobile-btn"')
    content = content.replace('id="mobile-menu"', 'id="tailwind-mobile-menu"')
    
    # We will also embed a tiny script inside to handle the tailwind mobile menu properly in case the old script JS fails to do so for the new nav
    # Only append if not already appended
    if "/* Tailwind Mobile Menu Logic */" not in content and "tailwind-mobile-btn" in content:
        script_block = """
    <script>
        // /* Tailwind Mobile Menu Logic */
        document.addEventListener("DOMContentLoaded", () => {
            const mobileBtn = document.getElementById("tailwind-mobile-btn");
            const mobileMenu = document.getElementById("tailwind-mobile-menu");
            if(mobileBtn && mobileMenu) {
                const icon = mobileBtn.querySelector("i");
                let isOpen = false;
                mobileBtn.addEventListener("click", () => {
                    isOpen = !isOpen;
                    if (isOpen) {
                        mobileMenu.classList.remove("hidden");
                        if(icon) icon.setAttribute("data-lucide", "x");
                    } else {
                        mobileMenu.classList.add("hidden");
                        if(icon) icon.setAttribute("data-lucide", "menu");
                    }
                    if(typeof lucide !== 'undefined') lucide.createIcons();
                });
            }
        });
    </script>
</body>
"""
        content = content.replace("</body>", script_block)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Done fixing lists and mobile menu")
