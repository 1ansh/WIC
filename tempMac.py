import cv2
import numpy as np

cap = cv2.VideoCapture(0)
template = cv2.imread('temp.png',0)
w, h = template.shape[::-1]
while(True):
        ret, img_rgb = cap.read()
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where( res >= threshold)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

        cv2.imshow('Detected',img_rgb)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
