import cv2
import numpy as np

cap = cv2.VideoCapture(0)

b_lower = np.array([90,150, 50])
b_upper = np.array([130,255,255])

r_lower = np.array([30, 150, 50])
r_upper = np.array([40, 150, 255])

while True:
    ret, frame = cap.read() #ret is the status, frame is the image
    if not ret: 
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #convert to hsv

    b_mask = cv2.inRange(hsv, b_lower, b_upper) #create a mask based on hsv range
    b_result = cv2.bitwise_and(frame, frame, mask=b_mask) #apply the mask
    b_gray = cv2.cvtColor(b_result, cv2.COLOR_BGR2GRAY)

    r_mask = cv2.inRange(hsv, r_lower, r_upper) #create a mask based on hsv range
    r_result = cv2.bitwise_and(frame, frame, mask=r_mask) #apply the mask
    r_gray = cv2.cvtColor(r_result, cv2.COLOR_BGR2GRAY)

    _, b_thresh = cv2.threshold(b_gray, 50, 255, cv2.THRESH_BINARY)
    b_contours ,_ = cv2.findContours(b_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    _, r_thresh = cv2.threshold(r_gray, 50, 255, cv2.THRESH_BINARY)
    r_contours ,_ = cv2.findContours(r_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    output = frame.copy()

    if(b_contours):
        largest_blue = max(b_contours, key = cv2.contourArea)
        if(cv2.contourArea(largest_blue < 500)):
            x, y, w, h = cv2.boundingRect(largest_blue)
            cv2.rectangle(output, (x, y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(output, "Blue", (x, y+h+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    if(r_contours):
        largest_red = max(r_contours, key = cv2.contourArea)
        if(cv2.contourArea(largest_red < 500)):
            x, y, w, h = cv2.boundingRect(largest_red)
            cv2.rectangle(output, (x, y), (x+w, y+h), (0,255, 255), 2)
            cv2.putText(output, "Red", (x, y+h+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Output", output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()