import cv2
import numpy as np
import pytesseract
import pandas as pd


def clean_text(text):
    """텍스트 정제: 특수문자 제거 및 A로 시작하는 문자열만 반환"""
    text = text.replace("<", "").replace(">", "").replace("|", "").replace(")", "").replace(",", "").replace("»", "").replace(" ", "").strip()
    return text if text.startswith("A") else ""


def detect_arrows(image_path, output_path='output.png', excel_path='output.xlsx', min_contour_area=500):
    # 이미지 로드 (컬러)
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 이진화 (흰색 마스킹 영역 추출)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # 컨투어 찾기
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    results = {}  # {텍스트: (FROM/TO, 영역 크기)}

    # 이미지의 가로 중간 좌표 계산
    img_center_x = image.shape[1] // 2  # 가로 너비의 절반

    for contour in contours:
        if cv2.contourArea(contour) < min_contour_area:
            continue  # 일정 크기 이하의 작은 영역은 무시

        # 컨투어의 중심 좌표 계산 (무게 중심)
        M = cv2.moments(contour)
        if M["m00"] == 0:
            continue  # 면적이 0이면 스킵
        cX = int(M["m10"] / M["m00"])  # x 중심 좌표

        # y좌표별 x의 최댓값과 최솟값 저장
        y_indices = contour[:, :, 1].flatten()
        x_indices = contour[:, :, 0].flatten()

        y_unique = np.unique(y_indices)
        x_max_list = []
        x_min_list = []

        for y in y_unique:
            x_vals = x_indices[y_indices == y]
            x_max_list.append(np.max(x_vals))
            x_min_list.append(np.min(x_vals))

        # 차이 계산
        max_diff = max(x_max_list) - min(x_max_list)
        min_diff = max(x_min_list) - min(x_min_list)

        # 🔥 중심을 기준으로 왼쪽과 오른쪽을 구분하여 방향 결정
        if cX < img_center_x:
            direction = "TO" if max_diff > min_diff else "FROM"  # 왼쪽 영역
        else:
            direction = "TO" if max_diff < min_diff else "FROM"  # 오른쪽 영역

        # 색상 지정 (TO = 빨강, FROM = 초록)
        color = (0, 0, 255) if direction == "TO" else (0, 255, 0)

        # 외곽선 및 텍스트 추가
        cv2.drawContours(image, [contour], -1, color, 2)
        x, y, w, h = cv2.boundingRect(contour)
        cv2.putText(image, direction, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        # 영역 내부의 글자 추출 및 정제
        roi = gray[y:y + h, x:x + w]
        extracted_text = clean_text(pytesseract.image_to_string(roi, config='--psm 6'))

        if extracted_text:
            area_size = w * h  # 영역 크기 계산

            # 중복된 텍스트가 있다면 더 작은 영역의 방향(FROM/TO) 유지
            if extracted_text not in results or area_size < results[extracted_text][1]:
                results[extracted_text] = (direction, area_size)

    # 결과 이미지 저장
    cv2.imwrite(output_path, image)

    # 엑셀 저장
    df = pd.DataFrame([(text, info[0]) for text, info in results.items()], columns=['Document no', 'Connection'])
    df.to_excel(excel_path, index=False)

    print(f"추출된 데이터가 {excel_path}에 저장되었습니다.")
