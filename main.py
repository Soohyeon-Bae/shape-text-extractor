from pdf_handler import remove_text_from_pdf
from image_processor import process_image, set_label
from ocr_handler import extract_text_from_masked_image
from utils import create_mask_from_contours
from pdf2image import convert_from_path
import cv2 as cv
import numpy as np

if __name__ == "__main__":
    input_pdf_path = 'data/input/test_PID.pdf'
    output_pdf_path = 'data/output/output.pdf'

    # 1. 원본 PDF를 이미지로 변환
    images_original = convert_from_path(input_pdf_path)
    img_original = cv.cvtColor(np.array(images_original[0]), cv.COLOR_RGB2BGR)

    # 2. PDF에서 텍스트 제거 후 저장
    remove_text_from_pdf(input_pdf_path, output_pdf_path)

    # 3. 텍스트 제거된 PDF를 이미지로 변환
    images_removed_text = convert_from_path(output_pdf_path)
    img_color = cv.cvtColor(np.array(images_removed_text[0]), cv.COLOR_RGB2BGR)

    # 4. 이미지 전처리
    img_gray, img_binary = process_image(img_color)

    # 5. 컨투어 검출
    contours, hierarchy = cv.findContours(img_binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # 6. 마스크 생성
    mask = create_mask_from_contours(contours, img_original)

    # 7. OCR 수행
    extracted_text = extract_text_from_masked_image(img_original, mask)

    # 8. 최종 결과 저장
    cv.imwrite('data/output/img_original.png', img_original)
    cv.imwrite('data/output/pentagon_text_area.png', mask)  # 마스크 이미지 저장

    # 9. OCR 결과 출력
    print("🔴 오각형 내부의 텍스트 추출 결과:")
    print(extracted_text)
