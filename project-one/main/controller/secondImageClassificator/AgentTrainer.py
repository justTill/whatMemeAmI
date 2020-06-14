from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split

# Number of learning reps
EPOCHS = 25

# Learningrate -> how strong are the result weighted
INIT_LR = 1e-3

# How many Images a taken for each learning repetitions
BS = 32

# image generator for data augmentation -> for additional test images
aug = ImageDataGenerator(rotation_range=30, width_shift_range=0.1,
                         height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
                         horizontal_flip=True, fill_mode="nearest")


class AgentTrainer:

    def split_data_with_labels_into_test_and_training_set(self, data, labels):
        # Split data 75% training 25% testing
        (training_data, test_data, training_labels, test_labels) = train_test_split(data,
                                                                                    labels, test_size=0.25,
                                                                                    random_state=42)
        # convert the labels from integers to vectors
        training_labels = to_categorical(training_labels, num_classes=4)
        test_labels = to_categorical(test_labels, num_classes=4)

        return training_data, test_data, training_labels, test_labels
