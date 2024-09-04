from banco.historico import Historico
class Conta:
    def __init__(self, numero,cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()


    @property
    def saldo(self):
        return self._saldo

    @classmethod
    def nova_conta(cls,cliente, numero):
        return cls(numero, cliente)


    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia

    
    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    
    def sacar(self,valor):
        saldo = self.saldo
        execedeu_saldo = valor >saldo

        if execedeu_saldo:
            print("OPERAÇÃO FALHOU, VOCE NAO POSSUI SALDO SUFICIENTE")
        elif valor>0:
            print("SAQUE REALIZADO COM SUCESSO")
            return True

        else:
            print("OPERAÇÃO FALHOU, O VALOR INFORMADO É INVALIDO")
            return False



    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True
    