# Create your views here.

from django.shortcuts import render
from .transactions import parse_cnab
from .transactions import salva_dados
from .transactions import gera_tabela
from .transactions import purge


def index(request):
    return render(request, 'app/index.html', {'tabela': gera_tabela()})


def model_form_upload(request):
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


def purge_all(request):
    purge()
    context = {'msg': 'Base de dados limpa com sucesso'}
    return render(request, 'app/index.html', context)
