from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from main.controller.logic import ImageLogic
from main.controller.logic import ImagePreprocessor
from main.controller.secondImageClassificator import Agents

imageLogic = ImageLogic()
p = ImagePreprocessor()
a = Agents()


def submission(request):
    template = loader.get_template('./templates/submission.html')
    context = get_context()
    return HttpResponse(template.render(context, request))


def random_agent(request):
    random_seed = request.POST.get('randomSeed')
    seed = random_seed if random_seed else 1
    context = get_context()
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
    return render(request, 'templates/submission.html', context)


def get_context():
    context = {
    }
    return context