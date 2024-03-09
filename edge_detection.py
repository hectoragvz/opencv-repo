import cv2
import numpy as np

img = cv2.imread("./images/goat.jpg")

# Canny detector
edges = cv2.Canny(img, 100, 200)

# Dilate the generated image (thikcer edged)
img_edge_dilate = cv2.dilate(edges, np.ones((5, 5), dtype=np.int8))


cv2.imshow("img", img)
cv2.imshow("edges", img_edge_dilate)
cv2.waitKey(0)