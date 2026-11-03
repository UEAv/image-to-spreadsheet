import easyocr
import json
import os
import numpy as np

# A small helper to convert numpy numbers so JSON can read them
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

print("Loading OCR model into memory...")
reader = easyocr.Reader(['en'])
im = 36

# FIXED: Added 'f' before the string and wrapped 'im' in curly braces
image_path = f"data/samples/{im}.jpg"  
print(f"\nProcessing {image_path}...\n")

results = reader.readtext(image_path)

ocr_data = []
for (bbox, text, prob) in results:
    ocr_data.append({
        "text": text,
        "confidence": float(prob),
        "bounding_box": bbox
    })

# Create an outputs folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# FIXED: Added 'f' before the string and wrapped 'im' in curly braces
output_path = f"outputs/raw_ocr_{im}.json"
with open(output_path, "w") as f:
    json.dump(ocr_data, f, indent=4, cls=NpEncoder)

# FIXED: Added closing quotation mark and parenthesis
print(f"\nSuccess! Raw OCR results saved to {output_path}")