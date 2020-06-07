from django.urls import path
from django.conf.urls import url
from main.view.views import index, save_new_user_image, classify_image

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    url(r'^save_new_user_image', save_new_user_image, name='save_new_user_image'),
    url(r'^classify_image', classify_image, name='classify_image'),
]
