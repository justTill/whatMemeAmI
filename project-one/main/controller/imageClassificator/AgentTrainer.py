import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from .Agents import Agents
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.optimizers import RMSprop
from main.controller.logic import ImagePreprocessor

# Number of learning repetitions
EPOCHS = 150

# Learningrate -> how strong are the result weighted
INIT_LR = 1e-3

# How many Images a taken for each learning repetitions
BS = 64

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
        training_labels = to_categorical(training_labels, num_classes=25)
        test_labels = to_categorical(test_labels, num_classes=25)

        return training_data, test_data, training_labels, test_labels

    def compile_neural_network_with_adam(self):
        # initialize the model
        print("[INFO] compiling model...")
        tf.random.set_seed(42)
        agent_builder = Agents()
        # build our neural network together
        agent = agent_builder.build_neural_network_agent(width=224, height=224, depth=1, classes=25)
        # we use the Adam optimizer
        # lr = learningrate
        # decay = learningrate slowly goes down the further we train the agent
        optimizer = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
        # compile our model: with the optimize, loss function and we want accurate metrics
        agent.compile(optimizer=optimizer,
                      loss="categorical_crossentropy",
                      metrics=["accuracy"])

        return agent

    def compile_neural_network_with_RMSprop(self):
        # initialize the model
        print("[INFO] compiling model...")
        tf.random.set_seed(42)
        agent_builder = Agents()
        # build our neural network together
        agent = agent_builder.build_neural_network_agent(width=224, height=224, depth=1, classes=25)
        # lr = learningrate
        # decay = learningrate slowly goes down the further we train the agent
        optimizer = RMSprop(learning_rate=INIT_LR)
        # compile our model: with the optimize, loss function and we want accurate metrics
        agent.compile(optimizer=optimizer,
                      loss="categorical_crossentropy",
                      metrics=["accuracy"])

        return agent

    def train_agent(self, agent, random_seed, path):
        image_processor = ImagePreprocessor()
        image_data, image_labels = image_processor.preprocessing_training_dataset(random_seed)

        training_data, test_data, training_labels, test_labels = self.split_data_with_labels_into_test_and_training_set(
            image_data, image_labels)

        # train the agent
        print("[INFO] training network...")
        # x = augmented versions of the training data with labels (data from which our agent learn)
        # validation_data = after learning we test our agent with these data, and we can check if the agent was right
        # steps_per_epoch = number of training reps
        # epochs = we do this 35 times
        # verbose = visualisation of training progress for each epoch

        training_labels = tf.convert_to_tensor(training_labels)
        test_labels = tf.convert_to_tensor(test_labels)
        history_of_the_training = agent.fit(x=aug.flow(training_data, training_labels, batch_size=BS),
                                            validation_data=(test_data, test_labels),
                                            steps_per_epoch=len(training_data) // BS,
                                            epochs=EPOCHS, verbose=1)


        self.save_agent_to_disk(agent, path)
        return history_of_the_training

    def save_history_graph_to_disk(self, history, path):
        # specify the diagram appearance
        plt.style.use("ggplot")
        plt.figure()
        plt.plot(np.arange(0, EPOCHS), history.history["loss"], label="train_loss")
        plt.plot(np.arange(0, EPOCHS), history.history["val_loss"], label="val_loss")
        plt.plot(np.arange(0, EPOCHS), history.history["accuracy"], label="train_acc")
        plt.plot(np.arange(0, EPOCHS), history.history["val_accuracy"], label="val_acc")

        plt.title("Training Loss and Accuracy on Meme Classification")
        plt.xlabel("Epoch #")
        plt.ylabel("Loss/Accuracy")
        plt.legend(loc="lower left")
        plt.savefig(path)

    def save_agent_to_disk(self, agent, path):
        agent.save(path, save_format="h5")
