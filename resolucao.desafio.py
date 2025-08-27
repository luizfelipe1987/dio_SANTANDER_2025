saldo = 0
opcao = 1
cont = 0
extrato = ""
print(

    """
    ============================ MENU ==================================

    1 - Depositar
    2 - Sacar
    3 - Extrato
    0 - Sair

    ====================================================================

    """
)

while opcao!=0:
    opcao = int(input("Informe a opção desejada: "))
    if opcao == 1:
        deposito = float(input("Informe o valor a ser depositado: "))
        if deposito <= 0:
            print("Informe um valor válido")
        else:
            saldo += deposito
            print (f"Valor depositado R$: {deposito: .2f}")
            extrato += f"Depósito no valor de R$: {deposito: .2f}\n"
    elif opcao == 2:
        if cont < 3:
            saque = float(input("Informe o valor a ser sacado: "))
            if 0 < saque <= saldo:
                saldo -= saque
                print(f"Valor sacado é R$: {saque: .2f}")
                cont += 1
                extrato += f" Saque no valor de R$: {saque: .2f}\n"
            elif saque > 500:
                print ("Limite máximo por saque é de R$500,00")
            else:
                print("Valor indiponível por falta de saldo")
        else:
            print ("Você atingiu o limite diário para saque!")

    elif opcao == 3:
        if extrato != '':
            print("\n ============ EXTRATO =========== \n")
            print(f"\n Seu extrato é:\n {extrato}\n")
            print(f"\n Seu saldo é R$:{saldo: .2f}")
            print("\n ================================")

    elif opcao == 0:
        print("Obrigado por utilizar nosso sistema!")
        break

    else:
        print("opção inválida.")

            




    