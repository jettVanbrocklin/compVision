#Smoothing reduces noise and detail -- very useful before detecting edges or contours

import cv2
import numpy as np

image = cv2.imread("day3/images/cat.jpg")
blurred = cv2.GaussianBlur(image, (5,5), 0)

cv2.imshow("Blurred", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

#MedianBlur
#Great for removing salt-and-pepper noise
median = cv2.medianBlur(image, 5)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

