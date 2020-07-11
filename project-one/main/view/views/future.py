from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from main.controller.forms import UploadImageForm
from main.controller.logic import ImageLogic
from main.controller.logic import ImagePreprocessor
from main.controller.imageClassificator import Agents
from main.controller.imageClassificator import Classificator

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
            classify_image_from_user_with_agent(image_name, 'main/trainedAgents/agent_RMSprop.h5', context)

        elif button == 'agent_two':
            classify_image_from_user_with_agent(image_name, 'main/trainedAgents/agent_Adam.h5', context)

    return render(request, 'templates/future.html', context)


def classify_image_from_user_with_agent(image_name, agent_path, context):
    data, heatmap_created = classificator.classifiy_image_from_user(image_name, agent_path)
    process_classified_data(data, context)

    context.update(({
        "user_image": imageLogic.get_image_with_name(image_name).get().image.url
    }))

    if heatmap_created:
        context.update(({
            "heatmap_path": "./mediafiles/images/userImageWithHeatmap.png"
        }))


def process_classified_data(data, context):
    max_label = data["max_label"]
    max_percentage = data["max_percentage"]
    context.update(({
        "predicted_class": max_label,
        "max_percentage": round((max_percentage * 100), 3),
        "predicted_class_image_path": "images/" + max_label + ".jpg",
    }))
    if max_percentage <= 0.7:
        second_label = data["second_label"]
        second_percentage = data["second_percentage"]
        context.update(({
            "second_predicted_class": second_label,
            "second_percentage": round((second_percentage * 100), 3),
            "second_predicted_class_image_path": "images/" + second_label + ".jpg",
        }))


def get_context():
    image_names = imageLogic.get_all_image_names()
    context = {
        'image_names': image_names,
        'upload_image_form': UploadImageForm,
    }
    return context
