import cv2
import time
video = cv2.VideoCapture(0)

check1, frame1 = video.read()
time.sleep(1)
print(check1)
print(frame1)

check2, frame2 = video.read()
time.sleep(1)
print(check2)
print(frame2)