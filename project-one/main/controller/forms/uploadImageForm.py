from django.forms import ModelForm
from django import forms
from main.model.models import UserImage


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserImage
        fields = ['name', 'image']

    def clean(self):
        name = self.cleaned_data['name']
        if UserImage.objects.filter(name=name):
            raise forms.ValidationError("this image name ist already taken, please choose another name")
