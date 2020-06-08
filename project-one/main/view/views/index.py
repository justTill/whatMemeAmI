from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from main.controller.forms import UploadImageForm
from main.controller.logic import ImageLogic
from main.controller.logic import ImagePreprocessor
from main.controller.secondImageClassificator import Agents

imageLogic = ImageLogic()
p = ImagePreprocessor()
a = Agents()


def index(request):
    template = loader.get_template('./templates/index.html')
    context = get_context()
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
    random_seed = request.POST.get('randomSeed')
    seed = random_seed if random_seed else 1
    button = request.POST.get('button')
    context = get_context()
    if image_name:
        if button == 'agent_one':
            try:
                print("try")
            except ValueError as error:
                error_message = error.__str__()
                context.update(({
                    "agent_error": error_message
                }))
        elif button == 'agent_two':
            try:
                print("try")
            except ValueError as error:
                error_message = error.__str__()
                context.update(({
                    "agent_error": error_message
                }))
    else:
        context.update(({
            "agent_error": "Pleas enter an Image name"
        }))

    return render(request, 'templates/index.html', context)


def random_agent(request):
    random_seed = request.POST.get('randomSeed')
    seed = random_seed if random_seed else 1
    context = get_context()
    image = imageLogic.get_image_with_name("Dominik")
    try:
        results = a.random_agent(seed)
        context.update({
            "image_label": results[0],
            "guess_label": results[1],
            "percentage": results[2],
            'img_classified': "images/" + results[0] + ".jpg",
            'img_class_predicted': "images/" + results[1] + ".jpg"
        })
    except ValueError as error:
        error_message = error.__str__()
        context.update(({
            "agent_error": error_message
        }))
    return render(request, 'templates/index.html', context)


def delete_images(request):
    image_names = request.POST.getlist("deleteImageBox")
    imageLogic.delete_images(image_names)
    return HttpResponseRedirect(reverse('main:index'))


def get_context():
    image_names = imageLogic.get_all_image_names()
    context = {
        'image_names': image_names,
        'upload_image_form': UploadImageForm,
    }
    return context
