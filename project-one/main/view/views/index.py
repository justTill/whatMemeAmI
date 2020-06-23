from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from main.controller.logic import ImageLogic

imageLogic = ImageLogic()


def index(request):
    template = loader.get_template('./templates/index.html')
    context = get_context()
    return HttpResponse(template.render(context, request))


def get_context():
    image_names = imageLogic.get_all_image_names()
    context = {
        'image_names': image_names,
    }
    return context


def general_settings(request):
    template = loader.get_template('./templates/settings.html')
    context = get_context()
    return HttpResponse(template.render(context, request))


def delete_images(request):
    image_names = request.POST.getlist("deleteImageBox")
    imageLogic.delete_images(image_names)
    return HttpResponseRedirect(reverse('main:settings'))
