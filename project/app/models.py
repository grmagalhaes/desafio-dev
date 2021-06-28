from django.db import models


# Create your models here.


class Tipo:
    def __init__(self):
        self._tipos = [
            {'tipo': 1, 'nome': 'Debito', 'natureza': 'Entrada', 'sinal': '+'},
            {'tipo': 2, 'nome': 'Boleto', 'natureza': 'Saída', 'sinal': '-'},
            {'tipo': 3, 'nome': 'Financiamento', 'natureza': 'Saída', 'sinal': '-'},
            {'tipo': 4, 'nome': 'Credito', 'natureza': 'Entrada', 'sinal': '+'},
            {'tipo': 5, 'nome': 'Recebimento Empréstimo', 'natureza': 'Entrada', 'sinal': '+'},
            {'tipo': 6, 'nome': 'Vendas', 'natureza': 'Entrada', 'sinal': '+'},
            {'tipo': 7, 'nome': 'Recebimento TED', 'natureza': 'Entrada', 'sinal': '+'},
            {'tipo': 8, 'nome': 'Recebimento DOC', 'natureza': 'Entrada', 'sinal': '+'},
            {'tipo': 9, 'nome': 'Aluguel', 'natureza': 'Saída', 'sinal': '-'},
        ]

    def get_tipo(self, tipo):
        for item in self._tipos:
            if item['tipo'] == tipo:
                return item
        return None


class Loja(models.Model):
    nome = models.CharField(max_length=19)
    representante = models.CharField(max_length=14)

    objects = models.Manager()

    def retorna_saldo(self, loja_id):

        tipos = Tipo()
        transacoes = Transacao.objects.filter(loja_id=loja_id)

        saldo = 0.0
        if transacoes is not None:
            for transacao in transacoes:
                tipo = tipos.get_tipo(transacao.tipo)
                if tipo['sinal'] == '+':
                    saldo += transacao.valor
                else:
                    saldo -= transacao.valor
        return saldo



class Transacao(models.Model):
    tipo = models.IntegerField(default=0)
    data = models.DateField()
    valor = models.FloatField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.TimeField()
    loja_id = models.ForeignKey(Loja, on_delete=models.CASCADE)

    objects = models.Manager()

