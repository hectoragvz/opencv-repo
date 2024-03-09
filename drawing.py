import cv2
import os

img = cv2.imread("./images/goat.jpg")
print(img.shape)

# Drawing a line
cv2.line(img, (100, 150), (300, 450), (255, 0, 0), 3)

# Drawing a rectangle
cv2.rectangle(img, (200, 350), (250, 600), (0, 0, 255), 3)

# Drawing a circle
cv2.circle(img, (300, 350), 15, (0, 255, 0), 10)

# Text
cv2.putText(img, "Hey Jude", (320, 220), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
