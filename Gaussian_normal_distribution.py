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


Shape = (200, 200)
Noise = create_noise(Shape)
cv2.namedWindow("Noise", cv2.WINDOW_NORMAL)
cv2.imshow("Noise", Noise.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
