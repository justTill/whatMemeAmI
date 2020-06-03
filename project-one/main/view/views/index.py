from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from main.controller.forms import UploadImageForm
from main.controller.logic import ImagePreprocessor

preprocessor = ImagePreprocessor()


def index(request):
    template = loader.get_template('./templates/index.html')
    image_names = preprocessor.get_all_image_names()
    context = {
        'image_names': image_names,
        'upload_image_form': UploadImageForm,
    }
    return HttpResponse(template.render(context, request))


def save_new_user_image(request):
    context = {}
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.clean()
            form.save()
            return HttpResponseRedirect(reverse('main:index'))
        else:
            context['upload_image_form'] = form
    return render(request, 'templates/index.html', context)


def classify_image(request):
    image_name = request.POST.getlist('imageName')
    button = request.POST.get('button')
    if image_name:
        if button == 'agent_one':
            pass  # Do Image Classification with agent one an get result and show it
        elif button == 'agent_two':
            pass  # Do Image Classification with agent two an get result and show it
    return HttpResponseRedirect(reverse('main:index'))
