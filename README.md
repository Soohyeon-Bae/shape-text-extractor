# PDF Text Extractor
This project provides a set of tools to extract text from shapes within PDF documents. It utilizes PyMuPDF for PDF handling, OpenCV for image processing, and Tesseract for Optical Character Recognition (OCR).

## Features
Remove text from PDF files
Convert PDF pages to images
Process images to detect shapes
Extract text from specified shapes using OCR

## Directory Structure

pdf-text-extractor/

│── 📂 data/                      
│   ├──📂 input/
│   │  └── your_pdf_file.pdf  
│   └──📂 output/  
│      └── output_pdf_file.pdf      
│
│── 📂 src/                      # Source code directory
│   ├── __init__.py
│   ├── pdf_handler.py        # Functions for handling PDF files
│   ├── image_processor.py     # Functions for image processing
│   ├── ocr_handler.py        # Functions for OCR operations
│   └── utils.py              # Utility functions
│
├── main.py                   # Main script to run the extraction process
├── requirements.txt          # List of required Python packages
└── README.md                 # Project documentation


## Installation
1. Clone the repository:
````
git clone https://github.com/yourusername/pdf-text-extractor.git
cd pdf-text-extractor
````

2. Install the required packages:
````
pip install -r requirements.txt
````
3. Make sure to install Tesseract OCR on your system. Follow the installation instructions for your operating system: Tesseract Installation Guide.

## Usage
1. Place your PDF files in the data/your_pdf_file_path/ directory.
2. Run the main script:
````
python main.py
````
3. The output will be saved in the data/output/ directory.
   
## Contributing
Feel free to submit issues or pull requests to improve this project. Contributions are welcome!

## License
This project is licensed under the MIT License.

Make sure to replace yourusername with your actual GitHub username in the clone command. Let me know if you need any modifications or additional sections!


