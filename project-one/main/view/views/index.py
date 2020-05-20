from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from main.controller.forms import UploadImageForm


def index(request):
    template = loader.get_template('./templates/index.html')
    context = {
        'upload_image_form': UploadImageForm
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
