from banco.transacao import Transacao

class Deposito(Transacao):

    def __init__(self,valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self,conta):
        sucessoTransacao = conta.depositar(self.valor)

        if sucessoTransacao:
            conta.historico.adicionarTransacao(self)