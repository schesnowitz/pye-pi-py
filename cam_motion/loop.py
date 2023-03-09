import cv2
import time


video = cv2.VideoCapture(0)
# give cam time to load
time.sleep(1)
while True:

    # shooting at 1fps
    # time.sleep(1)
    check, frame = video.read()
    cv2.imshow("test video", frame)
    # creates a kb exit when type 'q'
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
video.release()