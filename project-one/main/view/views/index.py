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
    button = request.POST.get('button')
    context = get_context()
    if image_name and random_seed:
        if button == 'agent_one':
            pass  # Do Image Classification with agent one an get result and show it
        elif button == 'agent_two':
            try:
                results = a.random_agent(random_seed)
                context.update({
                    "image_label": results[0],
                    "guess_label": results[1],
                    "percentage": results[2]
                })
            except ValueError as error:
                errorMessage = error.__str__()
                print(errorMessage)

    return render(request, 'templates/index.html', context)


def get_context():
    image_names = imageLogic.get_all_image_names()
    context = {
        'image_names': image_names,
        'upload_image_form': UploadImageForm,
    }
    return context
