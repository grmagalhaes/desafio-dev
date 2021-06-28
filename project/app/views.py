from django.template import loader

# Create your views here.

from django.http import HttpResponse


def index(request):
    template = loader.get_template('app/index.html')
    context = {
        'loja_id': 2,
    }
    return HttpResponse(template.render(context, request))


def model_form_upload(request):
    template = loader.get_template('app/index.html')
    context = {'loja_id': 2}
    print('passou')

    if request.method == 'POST':
        cnab = request.FILES['cnab']

        registros = []
        for item in cnab.readlines():
            texto = item.decode('utf-8')
            registros.append({
                'tipo': texto[0:1],
                'data': texto[1:9][0:4] + "-" + texto[1:9][4:6] + "-" + texto[1:9][6:8],
                'valor': texto[9:19],
                'cpf': texto[19:30],
                'cartao': texto[30:42],
                'hora': texto[42:48][0:2] + ":" + texto[42:48][2:4] + ":" + texto[42:48][4:6],
                'representante': texto[48:62],
                'loja': texto[62:81],
            })

        print(registros)

        return HttpResponse(template.render(context, request))
    else:
        print('não é válido')
        return HttpResponse(template.render(context, request))
