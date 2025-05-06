
import cv2
import numpy as np

image = cv2.imread("images/cat.jpg")

#show the image
cv2.imshow("OpenCV Test", image)

#wait until a key is pressed
cv2.waitKey(0)

#close window
cv2.destroyAllWindows()

cv2.imwrite("saved_copy.jpg", image)