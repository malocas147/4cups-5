import os

base_dir = r"c:\Users\Laptop\.gemini\antigravity\scratch\4cups-website"
cafe_path = os.path.join(base_dir, "cafe.html")

with open(cafe_path, "r", encoding="utf-8") as f:
    cafe = f.read()

# The duplicate starts at "<!-- Couvercles pour Gobelets -->" (second set, delay 0.4s)
# and ends before the closing pattern \n            </div>\n        </div>\n    </section>
# (which appears twice - the real one and a duplicate)

# The first good set ends at Couvercle 110mm (delay 0.7s) and its closing </div>
# The second set starts with the comment "<!-- Couvercles pour Gobelets -->"

# The pattern from the rfind was inserted BEFORE the closing divs, meaning:
# [correct couvercles 0.4..0.7] + [duplicate couvercles 0.4..0.7] + [closing divs]

# Let's find the second occurrence of "<!-- Couvercles pour Gobelets -->"
first_occ = cafe.find("<!-- Couvercles pour Gobelets -->")
second_occ = cafe.find("<!-- Couvercles pour Gobelets -->", first_occ + 1)

print(f"First occurrence at char {first_occ}")
print(f"Second occurrence at char {second_occ}")

if second_occ != -1:
    # Find the closing divs after the second set
    # Pattern: "\n            </div>\n        </div>\n    </section>"
    closing_after_second = cafe.find("\n            </div>\n        </div>\n    </section>", second_occ)
    if closing_after_second == -1:
        closing_after_second = cafe.find("\r\n            </div>\r\n        </div>\r\n    </section>", second_occ)
    
    print(f"Closing pattern after second set at char {closing_after_second}")
    
    # Remove everything from second_occ up to (but not including) the closing pattern
    if closing_after_second > second_occ:
        cafe = cafe[:second_occ] + cafe[closing_after_second:]
        print("✅ Removed duplicate couvercle block from cafe.html")
    else:
        print("⚠️ Could not find proper range to remove")
else:
    print("No duplicate found, checking structure...")

with open(cafe_path, "w", encoding="utf-8") as f:
    f.write(cafe)

print("Done!")
