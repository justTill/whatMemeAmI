from main.model.models import UserImage


class ImageDAO:

    def get_image_with_name(self, name):
        return UserImage.objects.all().filter(name=name)

    def get_image_names(self):
       return [image.name for image in UserImage.objects.all()]
