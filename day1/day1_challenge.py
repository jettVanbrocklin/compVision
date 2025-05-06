import cv2
import numpy as np



badge = 255 * np.ones((200,400,3), dtype="uint8")

cv2.imshow("blankId", badge)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.putText(badge, "Jett Vanbrocklin", (210, 170), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 2)
cv2.imshow("Added Name", badge)
cv2.waitKey(0)
cv2.destroyAllWindows()

profile = cv2.imread("images/cat.jpg")
profile = cv2.resize(profile, (200,200))
badge[0:200, 0:200] = profile
cv2.imshow("Added Picture", badge)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.rectangle(badge, (0,0), (200,200), (80,175,50), 3)
cv2.imshow("Added Border", badge)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.circle(badge, (300,50), 30, (80,175,50), -1)
cv2.imshow("Added logo", badge)
cv2.waitKey(0)
cv2.destroyAllWindows()