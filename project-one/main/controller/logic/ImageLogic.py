from main.model.persistence import ImageDAO


class ImageLogic:

    def get_image_with_name(self, name):
        image_dao = ImageDAO()
        return image_dao.get_image_with_name(name)

    def get_all_image_names(self):
        image_dao = ImageDAO()
        return image_dao.get_image_names()

    def delete_images(self, image_names):
        image_dao = ImageDAO()
        [image_dao.delete_image_if_exist(name) for name in image_names]
