
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from keras.preprocessing import image
# from matplotlib.colors import ListedColormap

import tensorflow as tf
# import matplotlib.pyplot as plt
# import segmentation_models as sm

test_datagen = ImageDataGenerator(rescale=1./255)
