from django.template import loader

# Create your views here.

from django.http import HttpResponse
from .transactions import parse_cnab
from .transactions import salva_dados


def index(request):
    template = loader.get_template('app/index.html')
    context = {
        'loja_id': 2,
    }
    return HttpResponse(template.render(context, request))


def model_form_upload(request):
    template = loader.get_template('app/index.html')
    context = {}

    if request.method == 'POST':
        cnab = request.FILES['cnab']

        registros = parse_cnab(cnab)
        print(registros)

        if registros is not None:
            retorno = salva_dados(registros)
            if retorno:
                context = {'msg:': 'Processamento realizado com sucesso'}
            else:
                context = {'msg:': 'Erro ao processar arquivo'}
        else:
            context = {'msg:': 'Erro ao processar arquivo'}

        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))
