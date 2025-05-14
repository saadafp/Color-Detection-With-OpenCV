import cv2
import numpy as np
from PIL import Image

cap = cv2.VideoCapture("D:\AI\OpenCV/traffic light.mp4.")

# Getting original video dimensions, creat fourcc code and creat VideoWriter
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("TrafficLight.mp4", fourcc, fps, (width, height))

font = cv2.FONT_HERSHEY_SIMPLEX

while (True):
    ret, frame = cap.read()
    if not ret:
        break  # Exit loop if no frame is returned (end of video)

    #frame = cv2.resize(frame, (320, 240))  # Reduce size for speed
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    green_lower_limit = np.array([40, 50, 50])  # H: 40, S: 50, V: 50
    green_upper_limit = np.array([90, 255, 255])  # H: 90, S: 255, V: 255

    #Red appears at both ends of the hue circle (0–10 and 170–180 degrees in OpenCV's scale),
    #so you need to mask both ranges and combine them
    red_lower_limit = np.array([0, 70, 50])
    red_upper_limit = np.array([10, 255, 255])
    red_lower_limit2 = np.array([170, 70, 50])
    red_upper_limit2 = np.array([180, 255, 255])

    yellow_lower_limit = np.array([20, 100, 100])
    yellow_upper_limit = np.array([35, 255, 255])

    green_mask = cv2.inRange(hsv_frame, green_lower_limit, green_upper_limit)
    green_res = cv2.bitwise_and(frame, frame, mask=green_mask)
    green_mask_ = Image.fromarray(green_mask)
    green_bbox = green_mask_.getbbox()

    red1_mask = cv2.inRange(hsv_frame, red_lower_limit, red_upper_limit)
    red1_res = cv2.bitwise_and(frame, frame, mask=red1_mask)
    red1_mask_ = Image.fromarray(red1_mask)
    red1_bbox= red1_mask_.getbbox()

    red2_mask = cv2.inRange(hsv_frame, red_lower_limit2, red_upper_limit2)
    red2_res = cv2.bitwise_and(frame, frame, mask=red2_mask)
    red2_mask_ = Image.fromarray(red2_mask)
    red2_bbox = red2_mask_.getbbox()

    yellow_mask = cv2.inRange(hsv_frame, yellow_lower_limit, yellow_upper_limit)
    yellow_res = cv2.bitwise_and(frame, frame, mask=yellow_mask)
    yellow_mask_ = Image.fromarray(yellow_mask)
    yellow_bbox = yellow_mask_.getbbox()


    if green_bbox is not None:
        gx1, gy1, gx2, gy2 = green_bbox
        green_rectangle = cv2.rectangle(frame, (gx1, gy1), (gx2, gy2), (255, 0, 0), 2)
        frame = cv2.putText(frame, "Green : GO!", (40, 40), font, 1, (255, 0, 0), 2)


    if red1_bbox is not None:
        rx1, ry1, rx2, ry2 = red1_bbox
        red1_rectangle = cv2.rectangle(frame, (rx1, ry1), (rx2, ry2), (255, 0, 0), 2)


    if red2_bbox is not None:
        rrx1, rry1, rrx2, rry2 = red2_bbox
        red2_rectangle = cv2.rectangle(frame, (rrx1, rry1), (rrx2, rry2), (255, 0, 0), 2)


    if yellow_bbox is not None:
        yx1, yy1, yx2, yy2 = yellow_bbox
        yellow_rectangle = cv2.rectangle(frame, (yx1, yy1), (yx2, yy2), (255, 0, 0), 2)


    out.write(frame)
    cv2.imshow('Original frame', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
out.release()
cap.release()


