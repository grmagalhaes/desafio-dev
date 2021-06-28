from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse


def index(request):
    template = loader.get_template('app/index.html')
    context = {
        'loja_id': 2,
    }
    return HttpResponse(template.render(context, request))
