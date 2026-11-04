import re

def clean_text(text):
    """Removes unwanted punctuation and normalizes whitespace."""
    # Keep only letters, numbers, basic spaces, and hyphens
    cleaned = re.sub(r'[^a-zA-Z\s\-]', '', text)
    # Remove extra spaces (e.g., "JORDAN    MILLER" -> "JORDAN MILLER")
    return " ".join(cleaned.split()).strip('- ')

def extract_name(ocr_results):
    """
    Takes raw OCR text results, filters out noise, cleans the string, 
    and returns the most likely name formatted in Title Case.
    """
    ignore_words = {
        "age", "verified", "id", "date", "no", "name", "timestamp", "time", 
        "camera", "iso", "shutter", "aperture", "lens", "mm", "metadata", 
        "system", "stamp", "scan", "artifact", "error", "img", "jpeg", "jpg", 
        "png", "file", "size", "kb", "mb", "resolution", "px", "pixel", 
        "student", "staff", "employee", "member", "card", "profile", "user",
        "class", "grade", "department", "dept", "title", "position", "role",
        "access", "secure"
    }

    likely_names = []
    
    for item in ocr_results:
        # Handle dict format from our JSON saves or direct EasyOCR tuples
        if isinstance(item, dict):
            text = item.get("text", "")
            confidence = item.get("confidence", 0.0)
        else:
            # Assuming EasyOCR raw output format: (bbox, text, confidence)
            text = item[1]
            confidence = item[2]

        text = clean_text(text)
        
        # Rule 1: Length and confidence
        if len(text) <= 2 or confidence < 0.4:
            continue
            
        # Rule 2: Ignore text with numbers
        if any(char.isdigit() for char in text):
            continue
            
        # Rule 3: Check blacklist for exact word matches
        text_words = set(text.lower().split())
        if text_words.intersection(ignore_words):
            continue
            
        # Rule 4: Names typically have at least two words
        if len(text.split()) < 2:
            continue

        # Cleanly format the name (e.g., "JORDAN MILLER" -> "Jordan Miller")
        likely_names.append(text.title())

    # Return the best match or "Unknown" if all rules fail
    if likely_names:
        return likely_names[0]
    return "Unknown"

if __name__ == "__main__":
    # Quick test using the noisy data we encountered earlier
    mock_ocr_data = [
        {"text": "DSC_8842!", "confidence": 0.90},
        {"text": "SECURE ACCESS", "confidence": 0.95},
        {"text": "- JoRDAN   MiLLeR -", "confidence": 0.88},
        {"text": "AGE 7", "confidence": 0.90}
    ]
    
    final_name = extract_name(mock_ocr_data)
    print(f"✅ Extraction Test: '{final_name}'")