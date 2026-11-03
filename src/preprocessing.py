import cv2

def preprocess_image_for_ocr(image_path):
    """
    Loads an image and returns a dictionary of preprocessed versions
    to improve OCR accuracy on various text types.
    """
    img = cv2.imread(image_path)
    if img is None:
        return None
        
    # 1. Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. Resized (Upscaled for small text)
    resized = cv2.resize(gray, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
    
    # 3. Thresholded (High contrast for blurry/faded text)
    _, thresh = cv2.threshold(resized, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return {
        "original": img,
        "grayscale": gray,
        "resized": resized,
        "thresholded": thresh
    }

if __name__ == "__main__":
    # Quick test if run directly
    test_img = "data/samples/1.jpg"
    processed_images = preprocess_image_for_ocr(test_img)
    if processed_images:
        print(f"Successfully generated {len(processed_images)} image variations for {test_img}")