import os
import cv2

# Showing an image
img = cv2.imread("./images/goat.jpg")

# Convert an image to a different color space
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("frame", img)
#cv2.imshow("colorspace", img_rgb)
#cv2.imshow("gray", img_bw)
cv2.imshow("hsv", img_hsv)

cv2.waitKey(0)