import cv2
import numpy as np

#resizing an image

image = cv2.imread("images/cat.jpg")

resized = cv2.resize(image, (300,300))

cv2.imshow("Resized Cat", resized)
cv2.imshow("Original Cat", image)
cv2.waitKey(0)
cv2.destroyAllWindows

#Proportional Resizing
scale_percent = 50
width = int(image.shape[1] * scale_percent/100)
height = int(image.shape[0] * scale_percent /100)
resized = cv2.resize(image, (width, height))
cv2.imshow("Resized Cat", resized)
cv2.imshow("Original Cat", image)
cv2.waitKey(0)
cv2.destroyWindow("Resized Cat")




#Cropping an Image
#crop a region: [startY:endY, startX:endX]
cropped = image[50:200, 100:300]

cv2.imshow("Cropped", cropped)
cv2.waitKey(0)
cv2.destroyWindow("Cropped")



#Flipping an Image

#Horizontal (mirror)
flipped_horizontal = cv2.flip(image,1)

#Vertical (Upside Down)
flipped_vertical = cv2.flip(image, 0)

#Both Axis
flipped_both = cv2.flip(image, -1)

cv2.imshow("Mirrored", flipped_horizontal)
cv2.imshow("UpsideDown", flipped_vertical)
cv2.imshow("both", flipped_both)
cv2.waitKey(0)
cv2.destroyWindow("Mirrored")
cv2.destroyWindow("UpsideDown")
cv2.destroyWindow("both")



#Rotate an Image

(h, w) = image.shape[:2]
center = (w // 2, h // 2)

#rotate 45 degrees counter clockwise
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow("Rotated", rotated)
cv2.waitKey(0)
cv2.destroyWindow("Rotated")

