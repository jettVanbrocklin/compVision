import cv2
import numpy as np


canvas = 255 * np.ones((300,300,3), dtype="uint8")


cv2.circle(canvas, (50,50), 20, (255, 55, 55), -1)
cv2.circle(canvas, (50,100), 20, (255, 55, 55), -1)
cv2.circle(canvas, (100,50), 20, (255, 55, 55), -1)
cv2.circle(canvas, (100,100), 20, (255, 55, 55), -1)

cv2.rectangle(canvas, (140, 80), (200, 200), (255, 0, 0), -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()


gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.imwrite("shapes.jpg", canvas)