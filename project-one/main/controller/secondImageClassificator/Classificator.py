from main.controller.logic import ImagePreprocessor
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2

class Classificator:

    def classifiy_image_from_user(self, user_image_name, seed):
        preprocessor = ImagePreprocessor()
        user_image_data = preprocessor.preprocessing_user_image(user_image_name)
        model = load_model("main/trainedAgents/secondAgent/agentTwo.h5")

        test = model.predict(user_image_data)[0]
        print(test)
        return 0  # Not a Meme
