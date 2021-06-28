from django.test import TestCase
from .models import Tipo, Loja, Transacao
from datetime import datetime


# Create your tests here.


class DesafioTextCase(TestCase):

    def test_criacao_loja(self):
        Loja.objects.create(nome='Teste', representante='Gerson')
        registros = Loja.objects.filter(nome='Teste')
        self.assertEquals(registros[0].representante, 'Gerson')

    def test_criacao_transacao(self):
        Loja.objects.create(nome='Teste', representante='Gerson2')
        loja_id = Loja.objects.get(nome='Teste')
        self.assertEquals(loja_id.representante, 'Gerson2')

        Transacao.objects.create(loja_id=loja_id, valor=12.50, tipo=1, cartao='111122223333',
                                 data=datetime.now().date(), hora=datetime.now().time(), cpf='12345678909')
        transacao = Transacao.objects.last()
        self.assertEquals(transacao.cartao, '111122223333')

    def test_validacao_saldo(self):
        Loja.objects.create(nome='Teste', representante='Gerson2')
        loja_id = Loja.objects.get(nome='Teste')
        self.assertEquals(loja_id.representante, 'Gerson2')

        Transacao.objects.create(loja_id=loja_id, valor=12.50, tipo=1, cartao='111122223333',
                                 data=datetime.now().date(), hora=datetime.now().time(), cpf='12345678909')
        Transacao.objects.create(loja_id=loja_id, valor=7.50, tipo=2, cartao='111122223333',
                                 data=datetime.now().date(), hora=datetime.now().time(), cpf='12345678909')

        loja = Loja()
        self.assertEquals(loja.retorna_saldo(loja_id), 5.0)


