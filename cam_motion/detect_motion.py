import cv2
import time
from emailer import send_email

video = cv2.VideoCapture(0)
# give cam time to load
time.sleep(1)

first_frame = None
status_list = []
while True:
    status = 0
    check, frame = video.read()
    # set frames to BW as smaller
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                                        # amount of blur
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    # cv2.imshow("test video", gray_frame_gau)

    if first_frame is None:
        first_frame = gray_frame_gau
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)


    # if pixel has a value more than 30 we set it to 255
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    dilate_frame = cv2.dilate(thresh_frame, None, iterations=2)
    # cv2.imshow("test video", dilate_frame)

    contours, check = cv2.findContours(dilate_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue
        x, y, width, height = cv2.boundingRect(contour)
        green_rectangle = cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 255, 0), 3)

        if green_rectangle.any():
            status = 1


    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[0] == 1 and status_list[1] == 0:
        send_email()
    print(status_list)





    cv2.imshow("video", frame)





    # creates a kb exit when type 'q'
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
video.release()