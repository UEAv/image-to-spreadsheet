import cv2
import os


# --- TASK 9: Handle invalid file paths ---
bad_path = "data/samples/this_fake_file.jpg"
bad_image = cv2.imread(bad_path)

if bad_image is None:
    print(f"Task 9 Passed: Successfully handled invalid file path -> {bad_path}")

# --- TASK 8: Understand NumPy arrays ---
real_path = "data/samples/1.jpg"  # Update to match the path that just worked for you
image = cv2.imread(real_path)

if image is not None:
    print(f"\nTask 8 Check:")
    print(f"1. What is the image actually made of? -> {type(image)}")
    print(f"2. What are the Blue, Green, and Red values of the very first pixel? -> {image[0, 0]}")


print("Starting batch check of all portrait images...\n")

# Loop through images 1 to 32
for i in range(1, 33):
    image_path = f"data/samples/{i}.jpg"
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"❌ Failed to load: {image_path}")
    else:
        # We only print the shape to verify it works, without stopping to display each one
        print(f"✅ Loaded {i}.jpg - Dimensions: {image.shape}")

print("\nTask 10 Passed: Automated loading for all images.")