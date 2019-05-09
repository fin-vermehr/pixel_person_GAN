# from utils import Logger
from data_preproc import compose_dataset
import os
import numpy as np
import errno
import torchvision.utils as vutils
from tensorboardX import SummaryWriter
from IPython import display
from matplotlib import pyplot as plt
import torch

def pixel_data():
    dataset = compose_dataset('data')
    return dataset

# Load data
data = pixel_data()

# Create loader with data, so that we can iterate over it
data_loader = torch.utils.data.DataLoader(data, batch_size=100, shuffle=True)
