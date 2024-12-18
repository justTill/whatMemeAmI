import os
import random
import cv2
import numpy as np

from tensorflow.keras.preprocessing.image import img_to_array
from imutils import paths
from main.controller.logic import ImageLogic


class ImagePreprocessor:

    def preprocessing_user_image(self, image_name):
        # get the user Image with the specified name
        image_logic = ImageLogic()
        if not image_name:
            raise ValueError('Not Image Name was given')
        user_image = image_logic.get_image_with_name(image_name)
        if not user_image:
            raise ValueError("no User Image was found with that name: " + image_name.__str__())

        print("[INFO] loading User image...")
        image = cv2.imread("."+user_image.get().image.url, cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(image, (224, 224))
        image = image.astype("float") / 255.0
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)

        return image

    def preprocessing_training_dataset(self, random_seed):
        print("[INFO] loading Training images...")
        data = []
        labels = []

        # grab the image paths and randomly shuffle them
        image_paths = sorted(list(paths.list_images("main/trainingData")))
        random.seed(random_seed)
        random.shuffle(image_paths)

        # loop over the images paths
        for path in image_paths:
            # load the image, pre-process it, and store it in the data list
            image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(image, (224, 224))
            image = img_to_array(image)
            data.append(image)
            # extract the class label from the image path and update the
            # labels list
            label_name = path.split(os.path.sep)[-2]
            labels.append(self.get_label_number(label_name))

        # scale the raw pixel intensities to the range [0, 1]
        data = np.array(data, dtype="float") / 255.0
        labels = np.array(labels)

        return data, labels

    def get_label_number(self, label_name):
        if label_name == "AlrightThenKeepYourSecrets":
            return 1
        elif label_name == "AncientAliens":
            return 2
        elif label_name == "BadLuckBrian":
            return 3
        elif label_name == "BitchPlease":
            return 4
        elif label_name == "CashMeOutside":
            return 5
        elif label_name == "ChubbyBubblesGirl":
            return 6
        elif label_name == "CondescendingWonka":
            return 7
        elif label_name == "ConfusedBlackGirl":
            return 8
        elif label_name == "ConfusedMathLady":
            return 9
        elif label_name == "ConfusedTravolta":
            return 10
        elif label_name == "ConspiracyKeanu":
            return 11
        elif label_name == "DistractedBoyfriend":
            return 12
        elif label_name == "FreeRealEstate":
            return 13
        elif label_name == "GoodGuyGreg":
            return 14
        elif label_name == "HideThePainHarold":
            return 15
        elif label_name == "IsThisAPigeon":
            return 16
        elif label_name == "LazyCollegeSenior":
            return 17
        elif label_name == "MatrixMorpheus":
            return 18
        elif label_name == "OneDoesNotSimply":
            return 19
        elif label_name == "OverlyAttachedGirlfriend":
            return 20
        elif label_name == "Picard":
            return 21
        elif label_name == "SaltBae":
            return 22
        elif label_name == "SideEyeingChloe":
            return 23
        elif label_name == "Stonks":
            return 24
        elif label_name == "WomanYellingAtCat":
            return 25
        else: # NotAMeme
            return 0
