from .models import Loja
from .models import Transacao


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
