from main.controller.logic import ImagePreprocessor
from tensorflow.keras.models import load_model
from .Agents import Agents
import numpy as np
import cv2
import tensorflow.keras.backend as K
import tensorflow as tf
import matplotlib.pyplot as plt
from main.controller.logic import ImageLogic


class Classificator:

    def classifiy_image_from_user(self, user_image_name, path):
        preprocessor = ImagePreprocessor()
        user_image_data = preprocessor.preprocessing_user_image(user_image_name)
        model = load_model(path)
        percentage_of_classes = model.predict(user_image_data)[0]
        heat_map_created = False
        try:
            self.create_heatmap_for_user_image(model, percentage_of_classes, user_image_data, user_image_name)
            heat_map_created = True
            print("could created heatmap")
        except:
            print("could not created heatmap: try again")
            try:
                self.create_heatmap_for_user_image(model, percentage_of_classes, user_image_data, user_image_name)
            except:
                print("second attempt to create heatmap failed")

        return self.get_highest_labels_with_percentage(percentage_of_classes), heat_map_created

    def get_highest_labels_with_percentage(self, percentage_of_classes):
        agents = Agents()
        sorted_percentages = percentage_of_classes.copy()
        sorted_percentages.sort()
        max_percentage = sorted_percentages[-1]
        second_highest_percentage = sorted_percentages[-2]
        max_label = 0
        second_label = 0
        for i in range(0, len(percentage_of_classes)):
            if percentage_of_classes[i] == max_percentage:
                max_label = agents.get_label_name(i)
            if percentage_of_classes[i] == second_highest_percentage:
                second_label = agents.get_label_name(i)

        return {"max_label": max_label, "max_percentage": max_percentage, "second_label": second_label,
                "second_percentage": second_highest_percentage}

    def create_heatmap_for_user_image(self, model, percentage, preprocessed_user_image_data, image_name):
        # to use K.gradients later
        tf.compat.v1.disable_eager_execution()
        #get Last conv layer from model
        last_conv_layer = model.get_layer('last_conv_layer')
        # index of the hightes percentage
        argmax = np.argmax([percentage])
        # get the output from that index
        output = model.output[:, argmax]
        # get the gradients
        grads = K.gradients(output, last_conv_layer.output)[0]
        # Each entry of this tensor is the mean intensity of the gradient over a specific feature map channel.
        pooled_grads = K.mean(grads, axis=(0, 1, 2))
        # Access the values we just defined
        iterate = K.function([model.input], [pooled_grads, last_conv_layer.output[0]])
        # These are the values of these two quantities
        pooled_grads_value, conv_layer_output_value = iterate([preprocessed_user_image_data])
        # Multiply each channel in the feature map by "how important this channel is"
        for i in range(50):
            conv_layer_output_value[:, :, i] *= pooled_grads_value[i]
        # plot the heatmap from those values
        heatmap = np.mean(conv_layer_output_value, axis=-1)
        heatmap = np.maximum(heatmap, 0)
        heatmap /= np.max(heatmap)
        plt.matshow(heatmap)
        # save the small heatmap
        plt.savefig("./mediafiles/images/pixelHeatmap.png")
        plt.close("all")
        # load the User image
        image_logic = ImageLogic()
        user_image = image_logic.get_image_with_name(image_name)
        img = cv2.imread("."+user_image.get().image.url)

        # resize the heatmap to user image size
        heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))
        # convert heatmap to RGB
        heatmap = np.uint8(255 * heatmap)
        # lay heatmap over user image
        heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
        # how intense should the colors be & and apply?
        hif = .8
        superimposed_img = heatmap * hif + img
        output_path = './mediafiles/images/userImageWithHeatmap.png'
        # save user image with heatmap
        cv2.imwrite(output_path, superimposed_img)
