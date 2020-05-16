from django.urls import path
from django.conf.urls import url
from main.view.views import index

app_name = 'main'

urlpatterns = [
    path('', index, name='index')
]
