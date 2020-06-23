from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from main.controller.forms import UploadImageForm
from main.controller.logic import ImageLogic
from main.controller.logic import ImagePreprocessor
from main.controller.secondImageClassificator import Agents
from main.controller.secondImageClassificator import AgentTrainer

imageLogic = ImageLogic()
p = ImagePreprocessor()
a = Agents()
aT = AgentTrainer()


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

    return render(request, 'templates/future.html', context)


def train_agent_two(request):
    random_seed = request.POST.get('randomSeedTrainAgentTwo')
    agent = aT.compile_neural_network()
    trained_agent = aT.train_agent(agent, random_seed)
    aT.save_history_graph_to_disk(trained_agent)

    return HttpResponseRedirect(reverse('main:future'))


def delete_images(request):
    image_names = request.POST.getlist("deleteImageBox")
    imageLogic.delete_images(image_names)
    return HttpResponseRedirect(reverse('main:future'))


def get_context():
    image_names = imageLogic.get_all_image_names()
    context = {
        'image_names': image_names,
        'upload_image_form': UploadImageForm,
    }
    return context
