# set the matplotlib backend so figures can be saved in the background
import matplotlib
matplotlib.use("Agg")
# import the necessary packages
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.utils import to_categorical
from pyimagesearch.lenet import LeNet
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import random
import cv2
import os


class SecondImagePreprocessor:

    """
    Implement keras Preprocessing Image with Image from User
    """
    def preprocessing_image_from_user(self):
        pass

    """
    Implement keras Preprocessing but for Images in traningData Folder
    """
    def preprocessing_training_dataset(self):
        pass