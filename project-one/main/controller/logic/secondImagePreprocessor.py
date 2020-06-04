from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras import backend as K


class SecondImagePreprocessor:

    """
    width = The width of our input images
    height = The height of the input images
    depth = The number of channels in our input images ( 3 for RGB)
    classes = The total number of classes we want to recognize
    """
    @staticmethod
    def build_neural_network_architecture(width, height, depth, classes):
        # We use the Sequential class since we will be sequentially adding layers to the model
        model = Sequential()
        inputShape = (height, width, depth)

        # We are adding 20 convolution filter which are 5x5 and "slide" over the image and sum up the 25 values too one
        model.add(Conv2D(20, (5, 5), padding="same",
                         input_shape=inputShape))
        # iterate through the image with an 2x2 pixel pattern and get the highest pixel value
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        # same procedure, but with 50 convolution filter
        model.add(Conv2D(50, (5, 5), padding="same"))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        # now convert the MaxPooling2D to a single vector(Flatten)
        model.add(Flatten())
        # apply fully connected layers
        model.add(Dense(500))
        # another relu activation
        model.add(Activation("relu"))

        # connect the output values with all existing classes
        model.add(Dense(classes))
        # classifier: will give us the probability for each class
        model.add(Activation("softmax"))

        # return the constructed network architecture
        return model

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

    def preprocess_image(self):
        pass
