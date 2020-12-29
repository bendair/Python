import numpy
from cv2 import cv2

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    cv2.imshow("Tracking",img)

    if cv2.waitkey(1) & 0xff == ord('q'):
        break