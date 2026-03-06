import os
from PIL import Image

def make_white_transparent(image):
    image = image.convert("RGBA")
    data = image.getdata()
    new_data = []
    for item in data:
        # If the pixel is mostly white, make it transparent
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            new_data.append((255, 255, 255, 0))
        else:
            # We can also handle anti-aliased edge blends roughly by making them semi-transparent
            # or just keep them solid if they aren't fully white. Let's keep it simple.
            # To be safer with slight off-whites:
            # blending:
            avg = sum(item[:3])/3
            if avg > 240:
                new_data.append((item[0], item[1], item[2], max(0, 255 - int((avg-240)*17)))) # rough fade
            else:
                new_data.append(item)
    image.putdata(new_data)
    return image

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website\assets"
# The logo file
logo_path = os.path.join(base_dir, "logo.png")
# The generated blank cups
cups_src = r"C:\Users\Laptop\.gemini\antigravity\brain\cb36bf15-5e39-4f5f-bcd3-73268ecf66ea\gobelet_blank_2cups_1772666097659.png"

# Load images
logo = Image.open(logo_path)
cups = Image.open(cups_src)

# Process logo (remove white background)
logo = make_white_transparent(logo)

# The generated image is nominally 1024x1024 or 512x512.
# Let's see dimensions
cups_w, cups_h = cups.size

# Assuming two cups side-by-side:
# Left cup center is roughly x = cups_w * 0.3
# Right cup center is roughly x = cups_w * 0.7
# Both cups y center is roughly y = cups_h * 0.6
logo_target_width = int(cups_w * 0.3)
# Keep aspect ratio
ratio = logo_target_width / logo.size[0]
logo_target_height = int(logo.size[1] * ratio)
logo = logo.resize((logo_target_width, logo_target_height), Image.Resampling.LANCZOS)

# Create a composite
result = cups.convert("RGBA")

# Paste left
paste_x = int(cups_w * 0.3) - (logo_target_width // 2)
paste_y = int(cups_h * 0.6) - (logo_target_height // 2)
result.paste(logo, (paste_x, paste_y), logo)

# Paste right
paste_x2 = int(cups_w * 0.7) - (logo_target_width // 2)
result.paste(logo, (paste_x2, paste_y), logo)

# Save the final result
out_path = os.path.join(base_dir, "gobelet_branded_master.png")
result.save(out_path)
print("✅ Created gobelet_branded_master.png")
