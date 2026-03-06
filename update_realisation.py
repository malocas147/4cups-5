import re

with open('c:/Users/Laptop/.gemini/antigravity/scratch/4cups-website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the flex containers inside realisations to have realisation-slider class
# and also the group to have realisation-card class.
# Add the buttons exactly before the slider.

# Item 1
item_start_pattern = r'class="group relative rounded-2xl overflow-hidden cursor-pointer shadow-md bg-white border border-border.*?"'
html = re.sub(item_start_pattern, lambda m: m.group(0).replace('group', 'group realisation-card'), html)

slider_pattern = r'class="flex overflow-x-auto snap-x snap-mandatory hide-scrollbar w-full h-\[350px\]"'
html = re.sub(slider_pattern, lambda m: m.group(0).replace('flex', 'flex realisation-slider scroll-smooth'), html)

buttons_html = '''
                        <!-- Navigation Arrows -->
                        <button class="realisation-prev absolute left-2 top-1/2 -translate-y-1/2 z-30 w-10 h-10 rounded-full bg-white/90 shadow-md flex items-center justify-center text-foreground opacity-0 group-hover:opacity-100 transition-opacity duration-300 hover:bg-white focus:outline-none">
                            <i data-lucide="chevron-left" class="w-6 h-6"></i>
                        </button>
                        <button class="realisation-next absolute right-2 top-1/2 -translate-y-1/2 z-30 w-10 h-10 rounded-full bg-white/90 shadow-md flex items-center justify-center text-foreground opacity-0 group-hover:opacity-100 transition-opacity duration-300 hover:bg-white focus:outline-none">
                            <i data-lucide="chevron-right" class="w-6 h-6"></i>
                        </button>
'''

# Insert buttons before the slider
html = html.replace('<div\n                            class="flex realisation-slider', buttons_html + '\n                        <div\n                            class="flex realisation-slider')
html = html.replace('<div class="flex realisation-slider scroll-smooth overflow-x-auto', buttons_html + '\n                        <div class="flex realisation-slider scroll-smooth overflow-x-auto')
# Wait, let's just make sure the replacement works correctly. The previous re.sub of `flex` to `flex realisation-slider scroll-smooth` was done.
html = html.replace('class="flex realisation-slider scroll-smooth overflow-x-auto snap-x snap-mandatory hide-scrollbar w-full h-[350px]"', 'class="flex realisation-slider scroll-smooth overflow-x-auto snap-x snap-mandatory hide-scrollbar w-full h-[350px]"')

# Let's use re to insert buttons right before the matched slider.
# A more robust approach:
html_parts = html.split('<div class="flex realisation-slider scroll-smooth overflow-x-auto snap-x snap-mandatory hide-scrollbar w-full h-[350px]">')
if len(html_parts) > 1:
    html = (buttons_html + '\n                        <div class="flex realisation-slider scroll-smooth overflow-x-auto snap-x snap-mandatory hide-scrollbar w-full h-[350px]">').join(html_parts)

# Add the script just before </body>
script_html = '''
    <script>
        document.addEventListener("DOMContentLoaded", () => {
            const cards = document.querySelectorAll(".realisation-card");
            
            cards.forEach(card => {
                const slider = card.querySelector(".realisation-slider");
                const prevBtn = card.querySelector(".realisation-prev");
                const nextBtn = card.querySelector(".realisation-next");
                let autoScrollInterval;
                
                const scrollNext = () => {
                    if (!slider) return;
                    const maxScrollLeft = slider.scrollWidth - slider.clientWidth;
                    if (slider.scrollLeft >= maxScrollLeft - 10) {
                        slider.scrollTo({ left: 0, behavior: "smooth" });
                    } else {
                        slider.scrollBy({ left: slider.clientWidth, behavior: "smooth" });
                    }
                };

                const scrollPrev = () => {
                    if (!slider) return;
                    if (slider.scrollLeft <= 10) {
                        slider.scrollTo({ left: slider.scrollWidth, behavior: "smooth" });
                    } else {
                        slider.scrollBy({ left: -slider.clientWidth, behavior: "smooth" });
                    }
                };

                if (nextBtn) nextBtn.addEventListener("click", (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    scrollNext();
                    resetInterval();
                });
                
                if (prevBtn) prevBtn.addEventListener("click", (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    scrollPrev();
                    resetInterval();
                });

                const startInterval = () => {
                    autoScrollInterval = setInterval(scrollNext, 2000); // 2 seconds
                };

                const resetInterval = () => {
                    clearInterval(autoScrollInterval);
                    startInterval();
                };

                card.addEventListener("mouseenter", () => clearInterval(autoScrollInterval));
                card.addEventListener("mouseleave", startInterval);
                
                // Touch events for mobile
                card.addEventListener("touchstart", () => clearInterval(autoScrollInterval), {passive: true});
                card.addEventListener("touchend", startInterval, {passive: true});

                startInterval();
            });
        });
    </script>
'''
if 'const cards = document.querySelectorAll(".realisation-card");' not in html:
    html = html.replace('</body>', script_html + '\n</body>')

with open('c:/Users/Laptop/.gemini/antigravity/scratch/4cups-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
