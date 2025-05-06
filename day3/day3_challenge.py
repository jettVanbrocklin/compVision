import cv2
import numpy as np


image = cv2.imread("day3/images/yak.jpg")
scale = 50
width = int(image.shape[1] * scale/100)
height = int(image.shape[0] * scale /100)
image = cv2.resize(image, (width, height))


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (9,9), 0)

edge = cv2.Canny(blur, 25, 200)
_, binary = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

#contours, _ = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#draw contours and bounding boxes
output = image.copy()
for cnt in contours:
    if cv2.contourArea(cnt) > 500: #filter noise
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(output, (x,y), (x+w, y+h), (0,255,0), 2)

gray_3ch = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
blur_3ch = cv2.cvtColor(blur, cv2.COLOR_GRAY2BGR)
edge_3ch = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
binary_3ch = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

stacked = np.hstack([ gray_3ch,edge_3ch,binary_3ch,output ])
cv2.imshow("Stacked", stacked)
cv2.waitKey(0)
cv2.destroyAllWindows()

