from banco.cliente import Cliente
class PessoaFisica(Cliente):

    def __init__(self ,cpf, nome, data_nascimento,endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.nome = nome
    