from main.model.models import UserImage


class ImageDAO:

    def get_image_with_name(self, name):
        return UserImage.objects.all().filter(name=name)

    def get_image_names(self):
       return [image.name for image in UserImage.objects.all()]

    def delete_image_if_exist(self, name):
        image = self.get_image_with_name(name)
        if image:
            image.delete()
