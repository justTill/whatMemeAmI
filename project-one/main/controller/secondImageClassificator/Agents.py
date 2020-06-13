import random

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from main.controller.logic import ImagePreprocessor


class Agents:
    """
    width = The width of our input images
    height = The height of the input images
    depth = The number of channels in our input images (3 for RGB)
    classes = The total number of classes we want to recognize
    """

    def build_neural_network_agent(self, width, height, depth, classes):
        # We use the Sequential class since we will be sequentially adding layers to the agent
        agent = Sequential()
        inputShape = (height, width, depth)

        # We are adding 20 convolution filter which are 5x5 and "slide" over the image and sum up the 25 values too one
        # The convolution filter finds feature points in our image
        agent.add(Conv2D(20, (5, 5), padding="same", input_shape=inputShape))

        agent.add(Activation("relu"))
        # iterate through the image with an 2x2 pixel pattern and get the highest pixel value
        agent.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        # same procedure, but with 50 convolution filter
        agent.add(Conv2D(50, (5, 5), padding="same"))
        agent.add(Activation("relu"))
        agent.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        # now convert the MaxPooling2D representation to a single vector(Flatten)
        agent.add(Flatten())
        # apply connections (fully connected layers)
        agent.add(Dense(512))
        # another relu activation
        agent.add(Activation("relu"))

        # connect the output values with all existing classes -> so we can calculate the probability for each class
        agent.add(Dense(classes))
        # classifier: will give us the probability for each class
        agent.add(Activation("softmax"))

        # return the constructed network architecture
        return agent

    def random_agent(self, random_seed):
        ip = ImagePreprocessor()
        data, labels = ip.preprocessing_training_dataset(random_seed)

        random_image_number = random.randrange(0, labels.size, 1)
        image_label = labels[random_image_number]
        random_label = random.randrange(0, 30, 1)

        image_label_name = self.get_label_name(image_label)
        guessed_label = self.get_label_name(random_label)
        percentage = self.get_percentage_of_label(labels, guessed_label)

        return image_label_name, guessed_label, percentage

    def get_label_name(self, label_number):
        if label_number == 1:
            return "AlrightThenKeepYourSecrets"
        elif label_number == 2:
            return "AncientAliens"
        elif label_number == 3:
            return "BadLuckBrian"
        elif label_number == 4:
            return "BitchPlease"
        elif label_number == 5:
            return "BrentRambo"
        elif label_number == 6:
            return "CashMeOutside"
        elif label_number == 7:
            return "ChubbyBubblesGirl"
        elif label_number == 8:
            return "CondescendingWonka"
        elif label_number == 9:
            return "ConfusedBlackGirl"
        elif label_number == 10:
            return "ConfusedMathLady"
        elif label_number == 11:
            return "ConfusedTravolta"
        elif label_number == 12:
            return "ConspiracyKeanu"
        elif label_number == 13:
            return "DistractedBoyfriend"
        elif label_number == 14:
            return "FreeRealEstate"
        elif label_number == 15:
            return "GoodGuyGreg"
        elif label_number == 16:
            return "HideThePainHarold"
        elif label_number == 17:
            return "IsThisAPigeon"
        elif label_number == 18:
            return "LazyCollegeSenior"
        elif label_number == 19:
            return "MatrixMorpheus"
        elif label_number == 20:
            return "MeAndTheBoys"
        elif label_number == 21:
            return "OneDoesNotSimply"
        elif label_number == 22:
            return "OverlyAttachedGirlfriend"
        elif label_number == 23:
            return "Picard"
        elif label_number == 24:
            return "SaltBae"
        elif label_number == 25:
            return "SideEyeingChloe"
        elif label_number == 26:
            return "Stonks"
        elif label_number == 27:
            return "ThatEscalatedQuickly"
        elif label_number == 28:
            return "Trololo"
        elif label_number == 29:
            return "WomanYellingAtCat"
        elif label_number == 30:
            return "YouKnowIHadToDoItToEm"
        else:
            return "NotAMeme"

    def get_percentage_of_label(self, labels, guessed_label):
        number_of_labels = {}

        for label in labels:
            label_name = self.get_label_name(label)
            if number_of_labels.__contains__(label_name):
                number_of_labels.update({label_name: number_of_labels[label_name] + 1})
            else:
                number_of_labels.update({label_name: 1})
        return number_of_labels[guessed_label] / labels.size * 100
