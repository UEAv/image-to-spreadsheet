import cv2
import os

im = 40  # Try to pick an image number that is slightly blurry or low-resolution
image_path = f"data/samples/{im}.jpg"

# Load original image
img = cv2.imread(image_path)
if img is None:
    print(f"Error: Could not load {image_path}")
    exit()

print(f"Applying preprocessing to image {im}...")

# Technique 1: Convert to Grayscale
# OCR engines work better without color distractions
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Technique 2: Resizing (Upscaling)
# Makes small text larger and easier to read
resized = cv2.resize(gray, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)

# Technique 3: Thresholding
# Converts the grayscale image to pure black and white (high contrast)
_, thresh = cv2.threshold(resized, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Save outputs to compare visually
os.makedirs("outputs", exist_ok=True)
cv2.imwrite(f"outputs/{im}_step1_gray.jpg", gray)
cv2.imwrite(f"outputs/{im}_step2_resized.jpg", resized)
cv2.imwrite(f"outputs/{im}_step3_thresh.jpg", thresh)

print("✅ Preprocessing complete! Check your 'outputs' folder to compare the three new images.")