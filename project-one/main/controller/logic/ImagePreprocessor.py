import os
import random
import cv2
import numpy as np

from tensorflow.keras.preprocessing.image import img_to_array
from imutils import paths
from main.controller.logic import ImageLogic


class ImagePreprocessor:

    def preprocessing_user_image(self, image_name):
        image_logic = ImageLogic()
        if not image_name:
            raise ValueError('Not Image Name was given')
        user_image = image_logic.get_image_with_name(image_name[0])

        if not user_image:
            raise ValueError("no User Image was found with that name: " + image_name.__str__())

        print("[INFO] loading User image...")
        data = []

        random.seed(42)
        image = np.asarray(bytearray(user_image[0].image.read()))
        image = cv2.resize(image, (64, 64))
        image = img_to_array(image)
        data.append(image)

        data = np.array(data, dtype="float") / 255.0

        return data

    def preprocessing_training_dataset(self, random_seed):
        # initialize the data and labels
        print("[INFO] loading Training images...")
        data = []
        labels = []

        # grab the image paths and randomly shuffle them
        imagePaths = sorted(list(paths.list_images("main/trainingData")))
        random.seed(random_seed)
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
            if label == "AlrightThenKeepYourSecrets":
                label = 1
            elif label == "AncientAliens":
                label = 2
            elif label == "BadLuckBrian":
                label = 3
            elif label == "BitchPlease":
                label = 4
            elif label == "BrentRambo":
                label = 5
            elif label == "CashMeOutside":
                label = 6
            elif label == "ChubbyBubblesGirl":
                label = 7
            elif label == "CondescendingWonka":
                label = 8
            elif label == "ConfusedBlackGirl":
                label = 9
            elif label == "ConfusedMathLady":
                label = 10
            elif label == "ConfusedTravolta":
                label = 11
            elif label == "ConspiracyKeanu":
                label = 12
            elif label == "DistractedBoyfriend":
                label = 13
            elif label == "FreeRealEstate":
                label = 14
            elif label == "GoodGuyGreg":
                label = 15
            elif label == "HideThePainHarold":
                label = 16
            elif label == "IsThisAPigeon":
                label = 17
            elif label == "LazyCollegeSenior":
                label = 18
            elif label == "MatrixMorpheus":
                label = 19
            elif label == "MeAndTheBoys":
                label = 20
            elif label == "OneDoesNotSimply":
                label = 21
            elif label == "OverlyAttachedGirlfriend":
                label = 22
            elif label == "Picard":
                label = 23
            elif label == "SaltBae":
                label = 24
            elif label == "SideEyeingChloe":
                label = 25
            elif label == "Stonks":
                label = 26
            elif label == "ThatEscalatedQuickly":
                label = 27
            elif label == "Trololo":
                label = 28
            elif label == "WomanYellingAtCat":
                label = 29
            elif label == "YouKnowIHadToDoItToEm":
                label = 30
            else:
                label = 0
            labels.append(label)
        # scale the raw pixel intensities to the range [0, 1]
        data = np.array(data, dtype="float") / 255.0
        labels = np.array(labels)

        return data, labels

