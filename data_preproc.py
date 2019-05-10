import numpy as np
import re
from os import listdir, path, mkdir
from skimage import io


def pad(im, d_max):
    ''' Pad image im to the square whose side length is d_max.

    Args:
        im (ndarray): numerical representation of image
        d_max (int): side length of the square
    '''
    shape = im.shape
    shift_x = int(np.floor((d_max - shape[0])/2))
    shift_y = int(np.floor((d_max - shape[1])/2))
    if shift_x > 0:
        zeros = np.zeros((shift_x, shape[1], shape[2]), dtype=int)
        im = np.concatenate((zeros, im), axis=0)
        zeros = np.zeros((d_max - shape[0] - shift_x, shape[1], shape[2]), dtype=int)
        im = np.concatenate((im, zeros), axis=0)
    if shift_y > 0:
        zeros = np.zeros((im.shape[0], shift_y, shape[2]), dtype=int)
        im = np.concatenate((zeros, im), axis=1)
        zeros = np.zeros((im.shape[0], d_max - shift_y - shape[1], im.shape[2]), dtype=int)
        im = np.concatenate((im, zeros), axis=1)
    return im


def pad_images(image_files):
    ''' Pad images to the square whose side equals to the biggest dimension among the images.

    Args:
        image_files (list of str): list containing file path to image
    '''
    d_max = 0
    im_list = []
    new_images = []
    for f in image_files:
        im = io.imread(f)
        if max(im.shape) > d_max:
            d_max = max(im.shape)
        im_list.append(im)
    for im in im_list:
        new_images.append(pad(im, d_max))
    return new_images


def save_images(images):
    ''' Save images to processed_data directory.

    Args:
        images (list of ndarray): list of numerical representation of image
    '''

    if not path.isdir('./processed_data'):
        mkdir('./processed_data')
    for i in range(len(images)):
        file_path = './processed_data/sample_{}.png'.format(i+1)
        io.imsave(file_path, images[i].astype(np.uint8))

if __name__ == '__main__':
    dir_path = './data'
    regex = re.compile('.+\.png')
    image_files = [dir_path + '/' + image for image in listdir(dir_path) if regex.match(image)]
    images = pad_images(image_files)
    save_images(images)
