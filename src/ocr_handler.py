import cv2 as cv
import pytesseract

# Tesseract 실행 경로 설정 (Windows 사용 시 필요)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_masked_image(original_image, mask):
    """ 마스크가 적용된 이미지에서 텍스트를 추출하는 함수 """
    text_only = cv.bitwise_and(original_image, original_image, mask=mask)  # 원본 이미지에서 마스크 적용
    extracted_text = pytesseract.image_to_string(text_only, lang='eng')  # OCR 수행
    return extracted_text
