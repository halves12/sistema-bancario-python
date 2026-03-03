
menu = """
Bem-vindo ao Sistema Bancário!
Escolha uma opção:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("informe o valor do depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("informe o valor do saque:"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques =  numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Falhou! saldo insuficiente.")
        elif excedeu_limite:
            print("Operação Falhou! o valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação Falhou! número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

    elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

            input("\nAperte [Enter] para voltar ao menu.")

            
    elif opcao == "q":
           break
