import cv2

img = cv2.imread("./images/goat.jpg")

k_size = 7 # Size of the average pixels
blur_img = cv2.blur(img, (k_size, k_size))
blur_img2 = cv2.GaussianBlur(img, (k_size, k_size), 0)
blur_img3 = cv2.medianBlur(img, k_size)

# Removing the noise of an image can be done with the median blur


cv2.imshow("frame", img)
cv2.imshow("blur", blur_img3)
cv2.waitKey(0)

cv2.destroyAllWindows()