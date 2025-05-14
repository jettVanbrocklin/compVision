import cv2
import numpy as np

image = cv2.imread("day5/images/bird.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#Define blue range in hsv
lower_blue = np.array([100,150,50])
upper_blue = np.array([130, 255, 255])

#create a mask
mask = cv2.inRange(hsv, lower_blue, upper_blue)

#apply the mask
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Original", image)
cv2.imshow("Mask", mask)
cv2.imshow("DetectedBlue", result)
cv2.waitKey(0)
cv2.destroyAllWindows()