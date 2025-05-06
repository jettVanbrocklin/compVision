import cv2
import numpy as np


image = cv2.imread("images/cat.jpg")

#show the image
cv2.imshow("OpenCV Test", image)

#wait until a key is pressed
cv2.waitKey(0)

#close window
cv2.destroyAllWindows()


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow("Grayscale", gray)
cv2.imshow("HSV", hsv)

cv2.waitKey(0)

cv2.destroyAllWindows()

