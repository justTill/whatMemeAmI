from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import losses
from .Agents import Agents
import os
from main.controller.logic import ImagePreprocessor

# Number of learning repetitions
EPOCHS = 25

# Learningrate -> how strong are the result weighted
INIT_LR = 1e-4

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

    def compile_neural_network(self):
        # initialize the model
        print("[INFO] compiling model...")
        agent_builder = Agents()
        # build our neural network together
        agent = agent_builder.build_neural_network_agent(width=28, height=28, depth=1, classes=31)
        # we use the Adam optimizer
        # lr = learningrate = INIT_LR => 1e-4
        # decay = learningrate slowly goes down the further we train the agent
        optimizer = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
        # compile our model: with the optimize, loss function and we want accurate metrics
        agent.compile(optimizer=optimizer,
                      loss=losses.SparseCategoricalCrossentropy(),
                      metrics=["accuracy"])

        return agent

    def train_agent(self, agent, random_seed):
        image_processor = ImagePreprocessor()
        image_data, image_labels = image_processor.preprocessing_training_dataset(random_seed)

        training_data, test_data, training_labels, test_labels = self.split_data_with_labels_into_test_and_training_set(
            image_data, image_labels)

        # train the agent
        print("[INFO] training network...")
        # x = augmented versions of the training data with labels (data from which our agent learn)
        # validation_data = after learning we test our agent with these data, and we can check if the agent was right
        # steps_per_epoch = number of training reps
        # epochs = we do this 25 times
        # verbose = visualisation of training progress for each epoch
        trained_agent = agent.fit(x=aug.flow(training_data, training_labels, batch_size=BS),
                                  validation_data=(test_data, test_labels), steps_per_epoch=len(training_data) // BS,
                                  epochs=EPOCHS, verbose=1)

        return trained_agent

    def save_trained_agent_to_disk(self, trained_agent):
        trained_agent.save("../../trainedAgents/secondAgent", save_format="h5")
