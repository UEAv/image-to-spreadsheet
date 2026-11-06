# 📄 AI-Powered Portrait Extractor
<img width="1919" height="808" alt="2026-11-05 10 37 06" src="https://github.com/user-attachments/assets/1751a7b8-7737-40ac-a5c8-89fc79ec03ff" />
<img width="1913" height="834" alt="2026-11-05 10 31 24" src="https://github.com/user-attachments/assets/8fa0ca63-e57e-4ab8-84bd-5737ea448e6e" />
<img width="1911" height="831" alt="2026-11-05 10 57 29" src="https://github.com/user-attachments/assets/d3ead852-ec18-4c0d-9ccd-0be4e5abb544" />
<img width="1920" height="839" alt="2026-11-05 10 56 22" src="https://github.com/user-attachments/assets/9f1a4b32-486b-4e7b-bd0b-36cacaecad68" />


An end-to-end Python pipeline and interactive web application that processes portrait images, extracts names using Optical Character Recognition (OCR), estimates age demographics using facial analysis AI, and exports the cleaned data to formatted Excel spreadsheets.

## ✨ Features
* **Intelligent OCR Extraction:** Utilizes `EasyOCR` to detect text in images.
* **Smart Noise Filtering:** Custom text-cleaning algorithms use regex and blacklist filtering to ignore timestamps, metadata, and random noise.
* **Multi-Pass Preprocessing:** Applies automated OpenCV transformations (Grayscale, Upscaling, Thresholding) to recover text from blurry or low-resolution images.
* **AI Age Estimation:** Integrates the `DeepFace` neural network to analyze facial features and categorize subjects as "Young" or "Old".
* **Automated Batch Processing:** Safely processes entire folders of images with built-in error handling.
* **Interactive Web App:** Includes a fully functional `Streamlit` frontend for drag-and-drop processing and one-click Excel downloads.
* **Formatted Exports:** Automatically sizes columns and freezes headers in the output `.xlsx` files using `pandas` and `openpyxl`.

## 🛠️ Tech Stack
* **Language:** Python
* **Computer Vision & AI:** EasyOCR, DeepFace, OpenCV
* **Data Manipulation:** Pandas, OpenPyXL, Regex
* **Frontend:** Streamlit

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
   cd your-repo-name
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install easyocr deepface opencv-python pandas openpyxl streamlit werkzeug
   ```

## 🚀 Usage

### Option 1: Web Interface (Recommended)
Launch the interactive Streamlit web application:
```bash
streamlit run app.py
```
* Upload `.jpg` or `.png` images directly in the browser.
* View extracted records in an interactive table.
* Download the results as a formatted Excel report.

### Option 2: Backend Batch Processing
Process an entire folder of images head-less via the terminal:
1. Place your target images inside `data/samples/`.
2. Run the batch processor:
   ```bash
   python src/batch_processing.py
   ```
3. Retrieve your final spreadsheet from the `outputs/` folder.

## 📂 Project Structure
```text
📦 AI-Powered-Image-Extractor
 ┣ 📂 data/samples/       # Folder for input images
 ┣ 📂 outputs/            # Generated Excel and CSV reports
 ┣ 📂 src/                # Core backend modules
 ┃ ┣ 📜 age_estimation.py # DeepFace facial analysis logic
 ┃ ┣ 📜 batch_processing.py # Multi-pass pipeline coordinator
 ┃ ┣ 📜 export.py         # Spreadsheet formatting and export
 ┃ ┣ 📜 name_extraction.py # Regex cleaning and blacklist rules
 ┃ ┗ 📜 preprocessing.py  # OpenCV image enhancements
 ┣ 📜 app.py              # Streamlit web application frontend
 ┗ 📜 README.md           # Project documentation
```
