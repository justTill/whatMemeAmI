# set the matplotlib backend so figures can be saved in the background
import argparse
import os
import random

import cv2
import matplotlib
import numpy as np

matplotlib.use("Agg")
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.utils import to_categorical
from imutils import paths


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
        # construct the argument parser and parse the arguments
        ap = argparse.ArgumentParser()
        # points to the directory containing the training images
        ap.add_argument("-d", "--dataset", required=True,
                        help="main/trainingData")
        # points to the directory where trained image classifier is saved
        ap.add_argument("-m", "--model", required=True,
                        help="main/classifier")
        args = vars(ap.parse_args())

        # Number of learning reps
        EPOCHS = 25

        # Learningrate -> how strong are the result weighted
        INIT_LR = 1e-3

        # How many Images a taken for each learning rep
        BS = 32

        # initialize the data and labels
        print("[INFO] loading images...")
        data = []
        labels = []

        # grab the image paths and randomly shuffle them
        imagePaths = sorted(list(paths.list_images(args["dataset"])))
        random.seed(42)
        random.shuffle(imagePaths)

        # loop over the input images
        for imagePath in imagePaths:
            # load the image, pre-process it, and store it in the data list
            image = cv2.imread(imagePath)
            image = cv2.resize(image, (64, 64))
            image = img_to_array(image)
            data.append(image)
            # extract the class label from the image path and update the
            # labels list
            label = imagePath.split(os.path.sep)[-2]
            if label == "badLuckBrian":
                lable = 1
            elif label == "hideThePain":
                lable = 2
            elif label == "oneDoesNotSimply":
                lable = 3
            else:
                lable = 0
            labels.append(label)

            # scale the raw pixel intensities to the range [0, 1]
            data = np.array(data, dtype="float") / 255.0
            labels = np.array(labels)
            # partition the data into training and testing splits using 75% of
            # the data for training and the remaining 25% for testing
            (trainX, testX, trainY, testY) = train_test_split(data,
                                                              labels, test_size=0.25, random_state=42)
            # convert the labels from integers to vectors
            trainY = to_categorical(trainY, num_classes=4)
            testY = to_categorical(testY, num_classes=4)

            # construct the image generator for data augmentation -> for additional test images
            aug = ImageDataGenerator(rotation_range=30, width_shift_range=0.1,
                                     height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
                                     horizontal_flip=True, fill_mode="nearest")
            print(trainX)
