import json
import os

im = 30  # Make sure this matches your test image number
input_path = f"outputs/raw_ocr_{im}.json"

if not os.path.exists(input_path):
    print(f"Error: {input_path} not found.")
    exit()

with open(input_path, "r") as f:
    ocr_data = json.load(f)

print(f"--- Analyzing OCR Data for Image {im} ---")

likely_names = []

# Expanded blacklist covering metadata, dates, system stamps, and generic labels
ignore_words = {
    "age", "verified", "id", "date", "no", "name", "timestamp", "time", 
    "camera", "iso", "shutter", "aperture", "lens", "mm", "metadata", 
    "system", "stamp", "scan", "artifact", "error", "img", "jpeg", "jpg", 
    "png", "file", "size", "kb", "mb", "resolution", "px", "pixel", 
    "student", "staff", "employee", "member", "card", "profile", "user",
    "class", "grade", "department", "dept", "title", "position", "role"
}

for item in ocr_data:
    text = item["text"].strip()
    confidence = item["confidence"]

    # Rule 1: Basic length and confidence filter
    if len(text) <= 2 or confidence < 0.4:
        continue
        
    # Rule 2: Ignore text containing numbers (filters out dates, times, specs)
    if any(char.isdigit() for char in text):
        print(f"[Ignored - Contains Numbers]: {text}")
        continue
        
    # Rule 3: Check against the expanded blacklist (Whole words only!)
    text_words = set(text.lower().split()) # Split text into individual words
    # If there is any overlap between the text's words and our ignore list
    if text_words.intersection(ignore_words):
        print(f"[Ignored - Blacklisted Word]: {text}")
        continue
        
    # Rule 4: Names typically have at least two words (First Last)
    if len(text.split()) < 2:
        print(f"[Ignored - Only One Word]: {text}")
        continue

    # If it passes all rules, it's highly likely to be the name
    likely_names.append(text)

# Output the results
print("\n✅ Extracted Name(s):")
if likely_names:
    for name in likely_names:
        print(f"- {name}")
else:
    print("No valid names found based on current rules.")