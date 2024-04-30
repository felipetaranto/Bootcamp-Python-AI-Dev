# DESAFIO SISTEMA BANCÁRIO - BOOTCAMP PYTHON AI BACKEND DEVELOPER
"""
OPERAÇÕES:
    * DEPÓSITO
        - DEVE SER POSSÍVEL DEPOSITAR APENAS VALORES INTEIROS E POSITIVOS
        - TODOS OS DEPÓSITOS DEVEM SER ARMAZENADOS EM UMA VARIÁVEL E EXIBIDOS NA OPERAÇÃO EXTRATO
    * SAQUE
        - DEVE PERMITIR 3 SAQUES DIÁRIOS COM LIMITE MÁXIMO DE R$500.00 POR SAQUE
        - CASO O USUÁRIO NÃO TENHA SALDO EM CONTA, O SISTEMA DEVERÁ EXIBIR UMA MENSAGEM INFORMANDO QUE NÃO SERÁ POSSÍVEL SACAR O VALOR POR FALTA DE SALDO
    * EXTRATO
        - VALORES DEVEM SER EXIBIDOS NO PADRÃO R$ XXXX.XX
        - DEVE LISTAR AS OPERAÇÕES DE DEPOSITO E SAQUE INDIVIDUALMENTE IDENTIFICANDO SEU TIPO E MOSTRANDO O VALOR
        - DEVE EXIBIR O SALDO ATUAL
"""

menu = """

    Sistema Bancário
    Menu:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    Opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    # DESPÓSITO
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Falha na operação: O valor informado é inválido.")

    # SAQUE
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha na operação: você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Falha na operação: o valor do saque excede o limite.")
        elif excedeu_saques:
            print("Falha na operação: número máximo de saques diários atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
        else:
            print("Falha na operação: o valor informado é inválido.")

    # EXTRATO
    elif opcao == "e":
        print("================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print(f"\nSaques diários disponíveis: {3-numero_saques}")
        print("=========================================")

    # SAIR
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
