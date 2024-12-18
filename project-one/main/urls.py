from django.urls import path
from django.conf.urls import url
from main.view.views import index, submission, future, save_new_user_image, classify_image, delete_images, random_agent, train_agent_two, general_settings, train_agent_one

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    url(r'^submission', submission, name='submission'),
    url(r'^settings', general_settings, name='settings'),
    url(r'^future', future, name='future'),
    url(r'^save_new_user_image', save_new_user_image, name='save_new_user_image'),
    url(r'^classify_image', classify_image, name='classify_image'),
    url(r'^delete_images', delete_images, name='delete_images'),
    url(r'^random_agent', random_agent, name='random_agent'),
    url(r'^train_agent_one', train_agent_one, name='train_agent_one'),
    url(r'^train_agent_two', train_agent_two, name='train_agent_two'),
]
