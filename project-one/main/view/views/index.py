from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from main.controller.forms import UploadImageForm
from main.controller.logic import ImageLogic
from main.controller.secondImageClassificator import AgentTrainer

imageLogic = ImageLogic()
aT = AgentTrainer()


def index(request):
    template = loader.get_template('./templates/index.html')
    context = get_context()
    agent = aT.compile_neural_network()
    trained_agent = aT.train_agent(agent, 42)
    aT.save_trained_agent_to_disk(trained_agent)
    return HttpResponse(template.render(context, request))


def get_context():
    image_names = imageLogic.get_all_image_names()
    context = {
        'image_names': image_names,
        'upload_image_form': UploadImageForm,
    }
    return context

