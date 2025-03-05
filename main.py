from src.pdf_handler import remove_text_from_pdf
from src.image_processor import process_image
from src.ocr_handler import extract_text_from_image

if __name__ == "__main__":
    input_pdf_path = 'data/input/test_PID.pdf'
    output_pdf_path = 'data/output/output.pdf'

    # PDF에서 텍스트 제거
    remove_text_from_pdf(input_pdf_path, output_pdf_path)

    # 처리된 이미지에서 텍스트 추출
    extracted_text = extract_text_from_image(output_pdf_path)

    print("추출된 텍스트:")
    print(extracted_text)
