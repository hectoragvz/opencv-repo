import os
import cv2

# Comment: read image
# image_path = os.path.join("./images/goat.jpg")
img = cv2.imread("./images/goat.jpg")

# Comment: Write image
# cv2.imwrite("./images/goat_out2.jpg", img)

# Comment: Visualize an image
# cv2.imshow("image_view", img)
# cv2.waitKey(0) # wait until a key is pressed to stop showing an image - parameter means the miliseconds to keep the frame open (0) forever


# Comment: read video
""" video = cv2.VideoCapture("./images/cancelo.gif")
# Comment: Visualize the video
ret = True
while ret:
  # ret is true if we are still missing frames to read
  ret, frame = video.read()
  if ret:
    cv2.imshow("frame", frame)
    cv2.waitKey(40)

video.release()
cv2.destroyAllWindows() """

# Comment: Read webcam
webcam = cv2.VideoCapture(0)
# Comment: visualize webcam
while True:
  ret, frame = webcam.read()
  cv2.imshow("frame", frame)
  if cv2.waitKey(40) & 0xFF == ord("q"): # Go out if q is pressed
    break

webcam.release()
cv2.destroyAllWindows()