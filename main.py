from datetime import datetime
import textwrap

from contaCorrente import ContaCorrente
from pessoaFisica import PessoaFisica
from saque import Saque
from deposito import Deposito
from cliente import Cliente
from transacao import Transacao

def exibir_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar contas
    [nu] Novo Usuario
    [q] Sair

    => """
    return input(menu)

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("cliente nao possui conta")
        return
    #FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizarTransacao(conta, transacao)

def sacar(clientes): #esse * indica que tudo que vier depois recebe argumentos por nome (keyword only)
    
    cpf = input("informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("cliente nao encontrado")
        return 
    
    valor = float(input("informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return 
    cliente.realizarTransacao(conta,transacao)

def exibir_extrato(clientes):

    cpf = input("informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("cliente nao encontrado")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return 
    

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato =""
    if not transacoes:
        extrato = "nao foram realizadas movimentações"
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"
    
    print(extrato)
    print(f"\n Saldo:\n\t R$ {conta.saldo:.2f}")
    print("\n=======================================")

def gerar_trasacao():
    trasacao_realizada = datetime.now()
    print(trasacao_realizada)
    
    
    pass


def criar_conta( numero_conta, clientes, contas):
    cpf = input("informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("cliente nao encontrado")
        return 
    
    conta = ContaCorrente.nova_conta(cliente = cliente, numero = numero_conta) 
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n CONTA CRIADA COM SUCESSO")
    
def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def criar_cliente(clientes):
    cpf = input("informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Ja existe cliente com esse CPF")
        return 
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento dd-mm-aaaa: ")
    endereco = input("Informe o endereço ( rua - numero - bairro - cidade/sigla estado): ")
    
    cliente= PessoaFisica(nome=nome, cpf=cpf, data_nascimento=data_nascimento, endereco=endereco)

    clientes.append(cliente)
    
    print ("usuario criado com sucesso")

def filtrar_cliente(cpf ,clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def main():
    
    clientes = []
    contas = []
    

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)


        elif opcao == "e":
            exibir_extrato(clientes)


        elif opcao == "nc":
            numero_conta = len(contas) +1
            criar_conta(numero_conta, clientes, contas)

           
        elif opcao == "lc":
           listar_contas(contas)
            

        elif opcao == "nu":
            criar_cliente(clientes)


        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
