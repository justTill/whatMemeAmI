from django.urls import path
from django.conf.urls import url
from main.view.views import index, save_new_user_image, classify_image, delete_images, random_agent

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    url(r'^save_new_user_image', save_new_user_image, name='save_new_user_image'),
    url(r'^classify_image', classify_image, name='classify_image'),
    url(r'^delete_images', delete_images, name='delete_images'),
    url(r'^random_agent', random_agent, name='random_agent'),
]
