class Cliente:

    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizarTransacao(self,conta, transacao):
        transacao.registrar(conta)

    def adicionarConta(self,conta):
        self.contas.append(conta)