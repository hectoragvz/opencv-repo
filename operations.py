import os
import cv2

# Show an image to work with
img = cv2.imread("./images/goat.jpg")
print(f"Original: {img.shape}")
# cv2.imshow("image_view", img)
# cv2.waitKey(0)

# Resizing an image
resized_img = cv2.resize(img, (320, 213)) #width height
print(f"Resized: {resized_img.shape}") #height width

# Cropping an image
cropped_img = img[120:240, 120:340]

cv2.imshow("image_view", img)
cv2.imshow("cropped", cropped_img)

cv2.waitKey(0)