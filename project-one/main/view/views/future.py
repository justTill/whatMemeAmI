from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from main.controller.forms import UploadImageForm
from main.controller.logic import ImageLogic
from main.controller.logic import ImagePreprocessor
from main.controller.secondImageClassificator import Agents
from main.controller.secondImageClassificator import Classificator

imageLogic = ImageLogic()
p = ImagePreprocessor()
a = Agents()
classificator = Classificator()


def future(request):
    template = loader.get_template('./templates/future.html')
    context = get_context()
    return HttpResponse(template.render(context, request))


def save_new_user_image(request):
    context = {}
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.clean()
            form.save()
            return HttpResponseRedirect(reverse('main:future'))
        else:
            context['upload_image_form'] = form
    return render(request, 'templates/future.html', context)


def classify_image(request):
    image_name = request.POST.get('imageNames')
    button = request.POST.get('button')
    context = get_context()
    if image_name:
        if button == 'agent_one':
            print("try")
        elif button == 'agent_two':
            data = classificator.classifiy_image_from_user(image_name)
            label = data["label"]
            percentage = data["percentage"]
            context.update(({
                "predicted_class": label,
                "percentage": percentage * 100
            }))
    else:
        context.update(({
            "agent_error": "Pleas enter an Image name"
        }))

    return render(request, 'templates/future.html', context)


def get_context():
    image_names = imageLogic.get_all_image_names()
    context = {
        'image_names': image_names,
        'upload_image_form': UploadImageForm,
    }
    return context
