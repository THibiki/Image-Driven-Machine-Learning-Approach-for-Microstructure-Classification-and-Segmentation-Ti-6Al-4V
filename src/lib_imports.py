"""
----------------------------------ABOUT-----------------------------------
Author: Arun Baskaran
--------------------------------------------------------------------------
"""


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import os.path

from tensorflow.keras.layers import Reshape
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import SGD
from tensorflow.keras import regularizers

from scipy import ndimage as ndi
from skimage.segmentation import watershed
from skimage.morphology import disk
from skimage.feature import peak_local_max
from PIL import Image
from skimage import exposure, data, morphology
from skimage.color import label2rgb
from skimage.feature import hog
from skimage.filters import sobel
import random
