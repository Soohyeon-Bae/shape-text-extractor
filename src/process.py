# src/process.py

from .pdf_handler import remove_text_from_pdf
from .image_preprocessor import process_image, set_label
from .ocr_handler import extract_text_from_masked_image
from .utils import create_mask_from_contours
from pdf2image import convert_from_path
import cv2 as cv
import numpy as np


def process_pdf(input_pdf_path, output_pdf_path):
    # 1. 원본 PDF를 이미지로 변환
    images_original = convert_from_path(input_pdf_path)
    img_original = cv.cvtColor(np.array(images_original[0]), cv.COLOR_RGB2BGR)

    # 2. PDF에서 텍스트 제거 후 저장
    remove_text_from_pdf(input_pdf_path, output_pdf_path)

    # 3. 텍스트 제거된 PDF를 이미지로 변환
    images_removed_text = convert_from_path(output_pdf_path)
    img_color = cv.cvtColor(np.array(images_removed_text[0]), cv.COLOR_RGB2BGR)

    # 4. 이미지 전처리 및 이진화
    img_gray, img_binary = process_image(img_color)

    # 5. 컨투어 검출
    contours, hierarchy = cv.findContours(img_binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # 6. 원본과 동일한 크기의 빈 투명 이미지 생성
    overlay = np.zeros_like(img_original, dtype=np.uint8)

    # 7. 마스크 이미지 생성
    mask = create_mask_from_contours(contours, img_gray.shape)

    # 8. 도형 정보를 출력하고 마스킹
    for cnt in contours:
        epsilon = 0.007 * cv.arcLength(cnt, True)
        approx = cv.approxPolyDP(cnt, epsilon, True)
        shape_name = ""

        if cv.isContourConvex(approx):
            size = len(approx)
            if size == 3:
                shape_name = "triangle"
            elif size == 4:
                shape_name = "rectangle"
            elif size == 5:
                shape_name = "pentagon"
                set_label(overlay, shape_name, cnt, color=(0, 0, 255), thickness=5)
            elif size == 6:
                shape_name = "hexagon"
            elif size == 8:
                shape_name = "octagon"
            elif size == 10:
                shape_name = "decagon"
            else:
                shape_name = str(size)

            # 컨투어 색상 및 두께 적용
            cv.polylines(overlay, [approx], isClosed=True, color=(0, 255, 0), thickness=3)
            set_label(overlay, shape_name, cnt)

    # 9. 원본 이미지와 컨투어 이미지를 중첩 (알파 블렌딩)
    alpha = 0.6
    img_overlayed = cv.addWeighted(img_original, 1, overlay, alpha, 0)

    # 10. 오각형 내부의 텍스트 추출
    text_only, extracted_text = extract_text_from_masked_image(img_original, mask)

    # 11. 결과 반환
    return img_original, overlay, img_overlayed, mask, text_only, extracted_text
