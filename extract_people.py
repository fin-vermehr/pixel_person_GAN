import numpy as np
import glob
from scipy import misc
from skimage import filters, io
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

i = 0

for image_path in glob.glob('data_to_edit' + '/*.png'):
    image = io.imread(image_path, plugin='matplotlib', as_gray=True)
    print(image)
    print(image.shape)
    # image = misc.imread(image_path, mode='RGB')
    edges = filters.sobel(image)

    plt.imshow(edges, cmap='gray')
    if i == 2:
        plt.show()

        break

    i += 1
