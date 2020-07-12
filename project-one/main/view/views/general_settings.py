from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from main.controller.imageClassificator import AgentTrainer
from main.controller.logic import ImageLogic
import tensorflow as tf

imageLogic = ImageLogic()
aT = AgentTrainer()


def general_settings(request):
    template = loader.get_template('./templates/settings.html')
    context = get_context()
    return HttpResponse(template.render(context, request))


def delete_images(request):
    image_names = request.POST.getlist("deleteImageBox")
    imageLogic.delete_images(image_names)
    return HttpResponseRedirect(reverse('main:settings'))


def train_agent_one(request):
    random_seed = request.POST.get('randomSeedTrainAgentOne')
    random_seed = random_seed if random_seed else 1
    tf.random.set_seed(int(random_seed))
    agent = aT.compile_neural_network_with_RMSprop()
    trained_agent = aT.train_agent(agent, random_seed, "main/trainedAgents/agent_RMSprop.h5")
    aT.save_history_graph_to_disk(trained_agent, "main/view/static/images/RMSprop_agent_plot.png")
    return HttpResponseRedirect(reverse('main:settings'))


def train_agent_two(request):
    random_seed = request.POST.get('randomSeedTrainAgentTwo')
    random_seed = random_seed if random_seed else 1
    tf.random.set_seed(int(random_seed))
    agent = aT.compile_neural_network_with_adam()
    trained_agent = aT.train_agent(agent, random_seed, "main/trainedAgents/agent_Adam2.h5")
    aT.save_history_graph_to_disk(trained_agent, "main/view/static/images/adam_agent_plot2.png")
    return HttpResponseRedirect(reverse('main:settings'))


def get_context():
    image_names = imageLogic.get_all_image_names()
    context = {
        'image_names': image_names,
    }
    return context
