from django.db import models


class UserImage(models.Model):
    name = models.CharField(unique=True, max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return "Imagename = " + self.name
