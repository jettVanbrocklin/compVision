import cv2
import numpy as np


#creating a blank canvas

canvas = np.zeros((300,300,3), dtype = "uint8")
cv2.imshow("Blank Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()





#Rectangle (image, top-left, bottom-right, color(BGR), thickness)
cv2.rectangle(canvas, (0,0), (50,50), (255,0,0), 2)
cv2.imshow("Rectangle", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Circle (image, center, radius, color, thickness) 
cv2.circle(canvas, (150,150), 50, (0, 255, 0), -1) #filled circle
cv2.imshow("Added Circle", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Line (image, start_point, end_point, color, thickness)
cv2.line(canvas, (150,150), (50,50), (0, 0, 255), 5)
cv2.imshow("Added Circle", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Text (image, string, bottom-left corner, font, font scale, color, thickness)
cv2.putText(canvas, "OpenCV!", (100, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
cv2.imshow("Text", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

