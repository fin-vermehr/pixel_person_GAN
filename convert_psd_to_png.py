import glob
from PIL import Image

for image_path in glob.glob('data_psd' + '/*.psd'):
    myImage = Image.open(image_path)
