from transacao import Transacao
from conta import Conta


class Saque(Transacao):

    def __init__(self,valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self,conta):
        sucessoTransacao = conta.sacar(self.valor)

        if sucessoTransacao:
            conta.historico.adicionarTransacao(self)