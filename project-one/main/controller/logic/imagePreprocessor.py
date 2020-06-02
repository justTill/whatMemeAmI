from main.model.persistence import ImageDAO


class ImagePreprocessor:

    def get_image_with_name(self, name):
        image_dao = ImageDAO()
        return image_dao.get_image_with_names(name)

    def get_all_image_names(self):
        image_dao = ImageDAO()
        return image_dao.get_image_names();

    """
    Implement keras Preprocessing Image with Image from User
    """
    def preprocessing_image_from_user(self):
        pass

    """
    Implement keras Preprocessing but for Images in traningData Folder
    """
    def preporcessing_training_dataset(self):
        pass