import cv2
import numpy as np

cap = cv2.VideoCapture(0)

lower = np.array([90,150, 50])
upper = np.array([130,255,255])
trail_points = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)


    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    output = frame.copy()
    if contours:
        largest = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest)

        if area > 500:
            x, y, w, h = cv2.boundingRect(largest)
            cx, cy = x + w//2, y+h//2
        
            #save point
            trail_points.append((cx, cy))
            cv2.rectangle(output, (x, y), (x+w,y+h), (0,255,0), 2)
            cv2.circle(output, (cx,cy), 5, (0,0,255), -1)
    for i in range(1, len(trail_points)):
        cv2.line(output, trail_points[i-1], trail_points[i], (0,0,255), 2)

    
    cv2.imshow("Webcam Feed", output)
    cv2.imshow("Thresh", thresh)
    cv2.imshow("Detected Color", result)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()