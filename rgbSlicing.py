import cv2  # Importing OpenCV package
import numpy as np

# Reading the image. OpenCV has in-built function called "imread" to read an image
# After reading, we have to store that image in a variable, say img
img = cv2.imread("rgb.png")

# As it's a colour image, let's "slice" it into red, green and blue channels
# Though it's called RGB, in OpenCV blue channel comes first and red at the last
r, g, b = img[:, :, 2], img[:, :, 1], img[:, :, 0]

red = np.zeros(img.shape, np.uint8)
red[:, :, 2] = r
green = np.zeros(img.shape, np.uint8)
green[:, :, 1] = g
blue = np.zeros(img.shape, np.uint8)
blue[:, :, 0] = b

# Let's see how the three channels look like
cv2.namedWindow("Red channel", cv2.WINDOW_NORMAL)
cv2.imshow("Red channel", red)
cv2.namedWindow("Green channel", cv2.WINDOW_NORMAL)
cv2.imshow("Green channel", green)
cv2.namedWindow("Blue channel", cv2.WINDOW_NORMAL)
cv2.imshow("Blue channel", blue)

cv2.waitKey(0)
cv2.destroyAllWindows()