from django.template import loader

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from .transactions import parse_cnab
from .transactions import salva_dados
from .transactions import gera_tabela


def index(request):
    context = dict()
    print(gera_tabela)
    context = {'tabela': gera_tabela()}
    return render(request, 'app/index.html', {'tabela': gera_tabela()})


def model_form_upload(request):
    loader.get_template('app/index.html')
    context = dict()

    if request.method == 'POST':
        cnab = request.FILES['cnab']

        registros = parse_cnab(cnab)

        if registros:
            retorno = salva_dados(registros)
            if retorno:
                context = {'msg': 'Processamento realizado com sucesso'}
            else:
                context = {'msg': 'Erro ao processar arquivo'}
        else:
            context = {'msg': 'Erro ao processar arquivo'}

        context.update({'tabela': gera_tabela()})
        return render(request, 'app/index.html', context)
    else:
        context.update({'tabela': gera_tabela()})
        return render(request, 'app/index.html', context)
