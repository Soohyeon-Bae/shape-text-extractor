import numpy as np
import cv2 as cv

def create_mask_from_contours(contours, original_image):
    """ 컨투어를 기반으로 마스크를 생성하는 함수 """
    mask = np.zeros_like(original_image, dtype=np.uint8)

    for cnt in contours:
        epsilon = 0.007 * cv.arcLength(cnt, True)
        approx = cv.approxPolyDP(cnt, epsilon, True)

        if cv.isContourConvex(approx):
            temp_mask = np.zeros_like(mask, dtype=np.uint8)
            cv.drawContours(temp_mask, [approx], -1, (255, 255, 255), thickness=cv.FILLED)

            # 마스크 영역을 확장 (팽창)
            kernel = np.ones((15, 15), np.uint8)
            expanded_mask = cv.dilate(temp_mask, kernel, iterations=1)

            # 최종 마스크에 합치기
            mask = cv.bitwise_or(mask, expanded_mask)

    return mask
