#Classic method for finding edges

import cv2
import numpy as np


image = cv2.imread("day3/images/cat.jpg")
scale = 50
width = int(image.shape[1] * scale/100)
height = int(image.shape[0] * scale /100)
image = cv2.resize(image, (width, height))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (3,3), 0)

edges = cv2.Canny(blurred, 100, 200)


#convert to 3 channels
gray_3ch = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
blurred_3ch = cv2.cvtColor(blurred, cv2.COLOR_GRAY2BGR)
edges_3ch = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)


all = np.hstack([image, gray_3ch, blurred_3ch, edges_3ch])
cv2.imshow("All", all)
cv2.waitKey(0)
cv2.destroyAllWindows()