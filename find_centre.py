from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def find_centre_gaus(array):
    return

image = Image.open('gaussian_2point88uW.jpg')
image_array = np.array(image)

print(image_array.shape)
