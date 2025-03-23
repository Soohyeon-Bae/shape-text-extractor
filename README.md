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
│── 📂 src/                              
│   ├── __init__.py           
│   ├── pdf_handler.py             
│   ├── image_processor.py                
│   ├── ocr_handler.py                
│   └── utils.py                     
│        
├── main.py                      
├── requirements.txt                  
└── README.md                        


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

## References
This project references the following materials:

- [[파이썬] 파이썬 + OpenCV활용 이미지에서 도형 인식]([blog_link](https://blog.naver.com/sharedrecord/222576941770)) - Author: 기록과 공유  
  This post explains the basic idea and implementation method of the project.

## License
This project is licensed under the MIT License.

Make sure to replace yourusername with your actual GitHub username in the clone command. Let me know if you need any modifications or additional sections!


