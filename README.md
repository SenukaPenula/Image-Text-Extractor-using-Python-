# Image Text Extractor 📷➡️📝

A modern, responsive GUI application that extracts text from images using Optical Character Recognition (OCR) technology. Built with Python and Tkinter, this application provides a user-friendly interface for converting text within images to editable text format.

![Application Preview](preview.png)

## Features ✨

- Modern, responsive GUI interface
- Support for multiple image formats (PNG, JPG, JPEG, BMP, GIF)
- Real-time image preview with responsive scaling
- Text extraction using Tesseract OCR
- Save extracted text to files
- Clean and intuitive user interface with modern theming
- Responsive design that adapts to window resizing

## Prerequisites 📋

Before installing the application, make sure you have:

1. Python 3.8 or higher installed
2. Tesseract OCR installed on your system

### Installing Tesseract OCR

#### Windows:
1. Download the Tesseract installer from the [official GitHub release page](https://github.com/UB-Mannheim/tesseract/wiki)
2. Run the installer and note down the installation path (default is `C:\Program Files\Tesseract-OCR`)
3. Add Tesseract to your system's PATH environment variable

#### Linux:
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

#### macOS:
```bash
brew install tesseract
```

## Installation 🔧

1. Clone the repository:
```bash
git clone https://github.com/yourusername/image-text-extractor.git
cd image-text-extractor
```

2. Create and activate a virtual environment (recommended):
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

3. Install required Python packages:
```bash
pip install -r requirements.txt
```

### Requirements.txt content:
```
Pillow==10.0.0
pytesseract==0.3.10
ttkthemes==3.2.2
```

## Usage 💻

1. Start the application:
```bash
python main.py
```

2. Use the interface to:
   - Click "Select Image" to choose an image file
   - View the image preview in the left panel
   - Click "Convert to Text" to extract text from the image
   - View the extracted text in the right panel
   - Click "Save" to save the extracted text to a file

## Configuration ⚙️

The application uses Tesseract OCR, which should be properly installed on your system. You may need to modify the Tesseract path in the code if it's installed in a different location:

```python
# In main.py, modify this line according to your Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## Project Structure 📁

```
image-text-extractor/
│
├── main.py                 # Main application file
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── venv/                  # Virtual environment (created during installation)
```

## Troubleshooting 🔍

1. **Tesseract not found error:**
   - Verify Tesseract is properly installed
   - Check if the path in `pytesseract.pytesseract.tesseract_cmd` matches your installation
   - Ensure Tesseract is added to your system's PATH

2. **Image preview not showing:**
   - Verify the image format is supported
   - Check if Pillow is properly installed
   - Ensure the image file isn't corrupted

3. **UI theme issues:**
   - Make sure ttkthemes is properly installed
   - Try using a different theme by modifying the theme name in `ThemedTk(theme="arc")`

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for the OCR engine
- [Pillow](https://python-pillow.org/) for image processing
- [ttkthemes](https://ttkthemes.readthedocs.io/) for modern UI themes

---
Made with ❤️ by Senuka Penula
