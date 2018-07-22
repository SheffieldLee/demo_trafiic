import cv2
import numpy as np
import filter
import getcentroid

cap = cv2.VideoCapture('test.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
    # 运用我们的滤波器
    fgmask = filter.filter_mask(fgmask)
    # 寻找视频中的轮廓
    im, contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        contour_valid = (w >= 35) and (h >= 35)

        if not contour_valid:
            continue

        # 画出矩形
        cv2.rectangle(frame, (x, y), (x + w - 1, y + h - 1), (0, 0, 255), 1)
        # 画出质心
        centroid = getcentroid.get_centroid(x, y, w, h)
        cv2.circle(frame, centroid, 2, (255, 0, 0), -1)

    cv2.imshow('frame', frame)
    cv2.imshow('fgmask', fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()