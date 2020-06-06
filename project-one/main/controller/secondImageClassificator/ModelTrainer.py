from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split

# Number of learning reps
EPOCHS = 25

# Learningrate -> how strong are the result weighted
INIT_LR = 1e-3

# How many Images a taken for each learning rep
BS = 32

# image generator for data augmentation -> for additional test images
aug = ImageDataGenerator(rotation_range=30, width_shift_range=0.1,
                         height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
                         horizontal_flip=True, fill_mode="nearest")


class ModelTrainer:

    def split_data_with_labels_into_test_and_training_set(self, data, labels):
        # Split data 75% training 25% testing
        (trainX, testX, trainY, testY) = train_test_split(data,
                                                          labels, test_size=0.25, random_state=42)
        # convert the labels from integers to vectors
        trainY = to_categorical(trainY, num_classes=4)
        testY = to_categorical(testY, num_classes=4)

        return trainX, testX, trainY, testY