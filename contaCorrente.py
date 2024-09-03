from conta import Conta
from cliente import Cliente
from pessoaFisica import PessoaFisica
from saque import Saque

class ContaCorrente(Conta):


    def __init__(self, numero, cliente, limite = 500, limite_saque=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saque = limite_saque

   
    def sacar(self,valor):

        numero_saque = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )
        
        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saque >= self._limite_saque
    
        if  excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
       
        else:
            return super().sacar(valor)
        return False

    def __str__(self) -> str:
        return f"""\
            Agencia:{self.agencia}
            C/C:{self.numero}
            Titular:{self.cliente.nome}
            """
    