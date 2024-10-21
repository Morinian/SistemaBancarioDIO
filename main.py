
extrato = 500
sair = 0 

while sair == 0:
    print("-----------------------------")
    print("Bem vindo ao sistema bancário")
    print("1) Sacar")
    print("2) Depositar")
    print("3) Visualizar Extrato")
    print("4) Sair")
    print("-----------------------------")

    escolha = int(input("Escolha a opção:"))

    if escolha == 1:
        sacar = float(input("Qual o valor ?"))    

        if extrato >= sacar:
            extrato = extrato - sacar
    elif escolha == 2:
        deposito = float(input("Qual o valor ?"))    
        extrato = extrato + deposito

    elif escolha == 3:
        print(f"Seu extrato é : {extrato}")
    elif escolha == 4:
        sair = 1
    else:
        print("Opção inválida. Tente novamente.")


