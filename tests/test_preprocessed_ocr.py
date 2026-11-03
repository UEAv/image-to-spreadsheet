import easyocr
import os

im = 40  # Using the image number from your generated files

print("Loading OCR model...")
reader = easyocr.Reader(['en'])

# Define the paths for the 4 versions of the image
image_paths = {
    "Original": f"data/samples/{im}.jpg",
    "Grayscale": f"outputs/{im}_step1_gray.jpg",
    "Resized": f"outputs/{im}_step2_resized.jpg",
    "Thresholded": f"outputs/{im}_step3_thresh.jpg"
}

print(f"\n--- Comparing OCR Results for Image {im} ---")

for name, path in image_paths.items():
    if not os.path.exists(path):
        print(f"Skipping {name}: File not found at {path}")
        continue
        
    results = reader.readtext(path)
    
    print(f"\n[{name} Image]:")
    if not results:
        print("  No text detected.")
    
    for (bbox, text, prob) in results:
        # Only print the results if it has a decent confidence or looks like a name
        if len(text) > 2 and prob > 0.1:
            print(f"  Extracted: '{text}' | Confidence: {prob:.4f}")