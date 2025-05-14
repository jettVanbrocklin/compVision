import cv2
import numpy as np

canvas = 255 * np.ones((300,300,3), dtype="uint8")

cv2.circle(canvas, (150,150), 50, (0,255,0), -1)
cv2.rectangle(canvas, (50,100), (100, 150), (0,200, 200), -1)

cv2.imshow("Original", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

hsv = cv2.cvtColor(canvas, cv2.COLOR_BGR2HSV)

lower_green = np.array([35, 150,50])
upper_green = np.array([85,255,255])

mask = cv2.inRange(hsv, lower_green, upper_green)

result = cv2.bitwise_and(canvas, canvas, mask=mask)

cv2.imshow("Mask", mask)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()