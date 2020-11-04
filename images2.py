import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
import os
import numpy as np
from numpy import unravel_index


def grayscale(image):
    h, w, _ = image.shape
    for y in range(h):
        for x in range(w):
            image2[y, x] = sum(image[y, x] * [0.2126, 0.7152, 0.0722])
    return image2


for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith('.png'):
            image = plt.imread(filename)
            image2 = image.copy()
            image3 = grayscale(image2)
            smallest = np.amin(image3)
            biggest = np.amax(image3)
            maxi = unravel_index(image3.argmax(), image3.shape)
            mini = unravel_index(image3.argmin(), image3.shape)
            image3[maxi[0],maxi[1],:]=[0,1,0]
            image3[mini[0], mini[1], :] = [0, 0,1]
            mpimg.imsave(filename[:8] + "gray.png", image3)
        else:
            continue
