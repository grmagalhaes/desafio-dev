from .models import Loja
from .models import Transacao
from .models import Tipo


def parse_cnab(arquivo):
    # parse do arquivo CNAB.TXT
    registros = []
    try:
        for item in arquivo.readlines():
            texto = item.decode('utf-8')
            registros.append({
                'tipo': int(texto[0:1]),
                'data': texto[1:9][0:4] + "-" + texto[1:9][4:6] + "-" + texto[1:9][6:8],
                'valor': float(texto[9:19]) / 100,
                'cpf': texto[19:30],
                'cartao': texto[30:42],
                'hora': texto[42:48][0:2] + ":" + texto[42:48][2:4] + ":" + texto[42:48][4:6],
                'representante': texto[48:62].strip(),
                'loja': texto[62:81].replace('\r', '').strip(),
            })
    except Exception:
        registros = []

    return registros


def salva_dados(registros):
    for registro in registros:

        loja_id = None
        try:
            loja_id = Loja.objects.get(nome=registro['loja'])
        except Exception:
            pass

        if not loja_id:
            loja = Loja()
            loja.nome = registro['loja']
            loja.representante = registro['representante']
            loja.save()
            loja_id = Loja.objects.get(nome=registro['loja'])

        try:
            transacao = Transacao()
            transacao.tipo = registro['tipo']
            transacao.valor = registro['valor']
            transacao.data = registro['data']
            transacao.cpf = registro['cpf']
            transacao.cartao = registro['cartao']
            transacao.hora = registro['hora']
            transacao.loja_id = loja_id
            transacao.save()

            loja = Loja()
            print(f'saldo: {loja.retorna_saldo(loja_id)}')

        except ValueError:
            return False

    return True


def gera_tabela():
    lojas = Loja.objects.all().order_by('id')
    tabela = []
    tipo = Tipo()

    for loja in lojas:
        loja_id = Loja.objects.get(nome=loja.nome)
        transacoes = Transacao.objects.filter(loja_id=loja_id)

        for transacao in transacoes:
            detalhes_tipo = tipo.get_tipo(transacao.tipo)
            tabela.append({'loja': loja.nome, 'representante': loja.representante,
                           'descricao': detalhes_tipo['nome'],
                           'natureza': detalhes_tipo['natureza'],
                           'data': transacao.data, 'valor': '{:.2f}'.format(transacao.valor),
                           'cpf': transacao.cpf, 'cartao': transacao.cartao, 'hora': transacao.hora
                          })

        tabela.append({'loja': loja.nome, 'representante': '',
                       'descricao': '',
                       'natureza': '',
                       'data': '', 'valor': '',
                       'cpf': '', 'cartao': 'Saldo', 'hora': '{:.2f}'.format(loja.retorna_saldo(loja_id))})

    return tabela

def purge():
    Transacao.objects.all().delete()
    Loja.objects.all().delete()
    return True
