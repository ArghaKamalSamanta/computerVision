import random
import cv2
import numpy as np


def add_noise(img):
    row, col = img.shape

    # Randomly choosing no. of impulse noise pixels
    noise_pixels = random.randint(1, row * col)
    for i in range(noise_pixels):
        # Randomly choosing a pixel for salt noise
        r = random.randint(0, row - 1)
        c = random.randint(0, col - 1)
        img[r][c] = 255

    return img


img = cv2.imread('dog.jpg', cv2.IMREAD_GRAYSCALE)
noisy_img = add_noise(img)
cv2.namedWindow("Noisy image", cv2.WINDOW_NORMAL)
cv2.imshow("Noisy image", noisy_img.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
