import cv2 as cv
import numpy as np

def set_label(image, label, contour, color=(0, 255, 0), thickness=3):
    """ 도형의 이름을 이미지에 표시하는 함수 """
    (text_width, text_height), baseline = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.7, 1)
    x, y, width, height = cv.boundingRect(contour)

    pt_x = x + int((width - text_width) / 2)
    pt_y = y + int((height + text_height) / 2)
    cv.rectangle(image, (pt_x, pt_y + baseline), (pt_x + text_width, pt_y - text_height), (200, 200, 200), cv.FILLED)
    cv.putText(image, label, (pt_x, pt_y), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1, 8)

def process_image(input_image):
    """ 이미지 전처리 및 마스크 생성을 위한 함수 """
    img_gray = cv.cvtColor(input_image, cv.COLOR_BGR2GRAY)
    img_gray = cv.equalizeHist(img_gray)  # 히스토그램 평활화

    ret, img_binary = cv.threshold(img_gray, 100, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    return img_gray, img_binary
