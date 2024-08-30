from datetime import datetime
import textwrap

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

def depositar(saldo, valor,extrato, /): #essa / indica receber os argumentos por posicao (positional only)
    try:
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            gerar_trasacao
        else:
            print("Operação falhou! O valor informado é inválido.")
    except ValueError:
        print("Operação falhou! Valor inválido.")
    return saldo, extrato

def sacar(*, saldo,valor, limite, extrato, numero_saques, LIMITE_SAQUES): #esse * indica que tudo que vier depois recebe argumentos por nome (keyword only)
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    
    if  excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif  excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def gerar_trasacao():
    trasacao_realizada = datetime.now()
    print(trasacao_realizada)
    
    
    pass


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("usuario nao encontrado")

    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("="*100)
        print(textwrap.dedent(linha))


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente Números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(" Já existe usuario com esse CPF ")
        return 
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento dd-mm-aaaa: ")
    endereco = input("Informe o endereço ( rua - numero - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome":nome,"cpf": cpf,"data_nascimento":data_nascimento,"endereco":endereco,})

    print ("usuario criado com sucesso")

def filtrar_usuario(cpf ,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def main():
    AGENCIA = "0001"
    saldo = 10
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo,valor, extrato)


        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor= valor,
                limite = limite,
                extrato = extrato,
                numero_saques = numero_saques,
                LIMITE_SAQUES= LIMITE_SAQUES
            )


        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)


        elif opcao == "nc":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "lc":
            listar_contas(contas)
            

        elif opcao == "nu":
            criar_usuario(usuarios)


        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
