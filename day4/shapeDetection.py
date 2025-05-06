import cv2
import numpy as np

image = cv2.imread("day4/images/shapes.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

thresh = cv2.bitwise_not(thresh)
#Looking for white shapes, not black shapes, that is why I bitwise not the entire thresh canvas
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

output = image.copy()

gray_3ch = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
thresh_3ch = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)

stack = np.hstack([gray_3ch, thresh_3ch])


#approximate the shapes
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 500: #skips small stuff
        continue


    #Get bounding box
    x, y, w, h = cv2.boundingRect(cnt)

    #approximate the shape
    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

    #identify shape
    corners = len(approx)
    shape = "Undefined"
    if corners == 3:
        shape = "Triangle"
    if corners == 4:
        shape = "Rectangle"
    if corners > 5:
        shape = "Circle"

    cv2.drawContours(output, [approx], -1, (0,255, 0), 2)
    cv2.putText(output, shape, (x,y + h +10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0, 255), 2)


cv2.imshow("Stack", stack)
cv2.imshow("Contours", output)
cv2.waitKey(0)
cv2.destroyAllWindows()