import numpy as np
import glob
from scipy import misc

def crop_image(image):
    row_indices = [i for i in range(image.shape[0]) if np.all(image[i, :] == 255)]
    image = np.delete(image, row_indices, 1)

    col_indices = [i for i in range(image.shape[1]) if np.all(image[:, i] == 255)]
    image = np.delete(image, col_indices, 0)
    return image


def compose_dataset(datafile):
    dataset = np.ones([287, 79, 59, 3])
    i = 0
    for image_path in glob.glob(datafile + '/*.png'):

        image = misc.imread(image_path, mode='RGB')
        image = crop_image(image)

        enlarged_image = np.ones([79, 59, 3]) * 255

        y = image.shape[0]
        x = image.shape[1]

        enlarged_image[:y, :x, :] = image
        dataset[i, :, :, :] = enlarged_image
        i += 1

    return dataset
