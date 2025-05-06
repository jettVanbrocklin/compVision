
import cv2
import numpy as np

image = cv2.imread("images/cat.jpg")
#image = cv2.imread('heeps://via.placeholder.com/300')

#image = 255 * np.ones((300,300,3), dtype="uint8")

#show the image
cv2.imshow("OpenCV Test", image)

#wait until a key is pressed
cv2.waitKey(0)

#close window
cv2.destroyAllWindows()

cv2.imwrite("image_copy.jpg", image)