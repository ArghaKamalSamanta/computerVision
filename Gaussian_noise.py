import cv2
import numpy as np
from random import seed
from random import randint


def create_noise(shape):
    h, w = shape
    noise = np.full((h, w), 255)
    # seeding random no generator
    seed(1)
    for i in range(h):
        for j in range(w):
            noise[i, j] = randint(0, 255)  # randomly choosing integers from [0, 255] according to Gaussian distribution

    return noise


img = cv2.imread("dog.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
Shape = img.shape
Noise = create_noise(Shape)
noisy_img = Noise/2 + img/2
cv2.namedWindow("Noisy image", cv2.WINDOW_NORMAL)
cv2.imshow("Noisy image", noisy_img.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
