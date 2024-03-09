import cv2

img = cv2.imread("./images/goat.jpg")

# COnverting to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# All values below 80 -> 0 and all above 80 -> 255
ret, thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)
# Just a blur to really differentiate the object from the background
thresh = cv2.blur(thresh, (10, 10))
ret, thresh = cv2.threshold(thresh, 80, 255, cv2.THRESH_BINARY)

# Adaptive threshold helps to automate finding a threshold for complicated images

cv2.imshow("frame", img)
cv2.imshow("threshold", thresh)
cv2.waitKey(0)