import cv2 as cv
import os
import time
import numpy as np
from src.process import process_pdf
from src.detector import detect_arrows

if __name__ == "__main__":
    input_pdf_path = 'data/input/your_pdf_file'
    output_pdf_path = 'data/output/text_removed_pdf_file'

    # PDF 처리 및 텍스트 추출
    img_original, overlay, img_overlayed, mask, text_only, extracted_text = process_pdf(input_pdf_path, output_pdf_path)

    # 12. 최종 결과 저장
    cv.imwrite('data/output/img_original.png', img_original)
    cv.imwrite('data/output/overlay.png', overlay)
    cv.imwrite('data/output/overlay_result.png', img_overlayed)

    # 🔥 text_only 저장 및 검증
    if isinstance(text_only, np.ndarray):
        cv.imwrite('data/output/pentagon_text_area.png', text_only)
    else:
        raise TypeError(f"⚠️ text_only의 타입이 잘못됨: {type(text_only)}")

    # 파일 저장 확인
    time.sleep(1)  # 파일 기록 완료 대기
    if not os.path.exists('data/output/pentagon_text_area.png'):
        raise FileNotFoundError("⚠️ pentagon_text_area.png 파일이 저장되지 않았습니다!")

    # 13. OCR 결과 출력
    print("🔴 오각형 내부의 텍스트 추출 결과:")
    print(extracted_text)

    # 🔥 detect_arrows 실행 (화살표 방향 검출 및 엑셀 저장)
    time.sleep(1)  # 파일이 사용 가능할 때까지 대기
    detect_arrows('data/output/pentagon_text_area.png', 'data/output/arrow_result.png', 'data/output/arrow_data.xlsx', min_contour_area=3000)
