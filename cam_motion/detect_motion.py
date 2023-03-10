import glob
import os
import cv2
import time
from threading import Thread
from emailer import send_email

video = cv2.VideoCapture(0)
# give cam time to load
time.sleep(1)

first_frame = None
status_list = []
cycle_count = 1


def clean_image_folder():
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)


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
    thresh_frame = \
    cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    dilate_frame = cv2.dilate(thresh_frame, None, iterations=2)
    # cv2.imshow("test video", dilate_frame)

    contours, check = cv2.findContours \
        (dilate_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue
        x, y, width, height = cv2.boundingRect(contour)
        green_rectangle = cv2.rectangle \
            (frame, (x, y), (x + width, y + height), (0, 255, 0), 3)

        if green_rectangle.any():
            status = 1
        cv2.imwrite(f"images/{cycle_count}.png", frame)
        cycle_count = cycle_count + 1
        all_images = glob.glob("images/*.png")
        get_middle_image = int(len(all_images) / 2)
        all_images[get_middle_image]
        image_to_email = all_images[get_middle_image]

    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[0] == 1 and status_list[1] == 0:
        send_email(image_to_email)

    # clean_image_folder()
    cv2.imshow("video", frame)





    # creates a kb exit when type 'q'
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
video.release()
