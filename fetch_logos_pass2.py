import os
import urllib.request

brands_domains = {
    3: ["picks.ma", "picks.com", "picks-burger.com"], # Picks
    6: ["zushi.ma", "zushi.com"], # Zushi
    7: ["blueberry.ma", "blueberry.com"], # Blueberry
    8: ["zinecapitalinvest.ma", "alitkane.ma"], # Al Itkane
    9: ["gelatolab.ma", "gelatolab.com"], # Gelato Lab
    10: ["adorocafe.ma", "adoro.ma", "cafeadoro.com"], # Adoro Cafe
    11: ["wok4you.ma", "wok4you.com", "wok-4you.com"] # Wok 4you
}

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website\assets"

def download_logo(domain, save_path):
    # Try clearbit first
    url1 = f"https://logo.clearbit.com/{domain}"
    req = urllib.request.Request(url1, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                with open(save_path, 'wb') as f:
                    f.write(response.read())
                return True
    except Exception:
        pass
        
    # Try Google Favicon (high res) as fallback
    url2 = f"https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=http://{domain}&size=256"
    req = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                data = response.read()
                if len(data) > 1000: 
                    with open(save_path, 'wb') as f:
                        f.write(data)
                    return True
    except Exception:
        pass
        
    return False

success_count = 0
for idx, domains in brands_domains.items():
    save_path = os.path.join(base_dir, f"partner-{idx}.png")
    found = False
    for domain in domains:
        if download_logo(domain, save_path):
            print(f"✅ Found logo for partner {idx} using {domain}")
            success_count += 1
            found = True
            break

print(f"Fetch complete. Successfully updated {success_count}/7 logos.")
