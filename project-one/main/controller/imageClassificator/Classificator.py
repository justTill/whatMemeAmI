from main.controller.logic import ImagePreprocessor
from tensorflow.keras.models import load_model
from .Agents import Agents


class Classificator:

    def classifiy_image_from_user(self, user_image_name,path):
        preprocessor = ImagePreprocessor()
        user_image_data = preprocessor.preprocessing_user_image(user_image_name)
        model = load_model(path)

        percentage_of_classes = model.predict(user_image_data)[0]

        return self.get_highest_labels_with_percentage(percentage_of_classes)

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

        return {"max_label": max_label, "max_percentage": max_percentage, "second_label": second_label, "second_percentage": second_highest_percentage}
