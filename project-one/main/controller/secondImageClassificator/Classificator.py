from main.controller.logic import ImagePreprocessor
from tensorflow.keras.models import load_model
from .Agents import Agents


class Classificator:

    def classifiy_image_from_user(self, user_image_name):
        preprocessor = ImagePreprocessor()
        user_image_data = preprocessor.preprocessing_user_image(user_image_name)
        model = load_model("main/trainedAgents/secondAgent/agentTwo.h5")

        percentage_of_classes = model.predict(user_image_data)[0]

        return self.get_highest_label_with_percentage(percentage_of_classes)

    def get_highest_label_with_percentage(self, percentage_of_classes):
        max_percentage = max(percentage_of_classes)
        label = 0
        for i in range(0, len(percentage_of_classes)):
            if percentage_of_classes[i] == max_percentage:
                agents = Agents()
                label = agents.get_label_name(i)

        return {"label": label, "percentage": max_percentage}
