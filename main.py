import cv2
import keyboard
import numpy as np

vid = cv2.VideoCapture(0)
bg = cv2.imread("bangkok.jpeg")

while True:

    ret, frame = vid.read()
    print(frame)
    frame = cv2.resize(frame, (640, 480))
    bg = cv2.resize(bg, (640, 480))

    u_black = np.array([50,50,50])
    l_black = np.array([0,0,0])

    mask = cv2.inRange(frame, l_black, u_black)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    f = frame - res
    f = np.where(f == 0, bg, f)

    cv2.imshow("video", frame)
    cv2.imshow("mask", f)

    if keyboard.is_pressed('q'):
        break

vid.release()
cv2.destroyAllWindows()
