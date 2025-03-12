tela_inicial ="""
Bem vindo ao Banco Dio.me!

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair

Escolha uma opção acima [1], [2], [3] ou [4]:
""" 

saldo = 0
limite = 500
extrato = ""
numero_operacoes = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(tela_inicial)
    
    if opcao == "1":
        while True:
            try:
                valor_deposito = float(input("Digite o valor do depósito: ")) # Tenta converter para float
                if valor_deposito > 0:
                    saldo += valor_deposito
                    extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
                    print(f"\nDepósito de R${valor_deposito:.2f} realizado com sucesso!\n")
                    break # Sai do loop interno
                else:
                    print("Valor inválido! O depósito deve ser maior que zero.")
            except ValueError:
                print("Valor inválido! Por favor, insira somente número.")
    
    elif opcao == "2":
        valor_saque = float(input("Digite o valor do saque: ")) # Tenta converter para float
        
        excedeu_saldo = valor_saque > saldo 
        excedeu_limite = valor_saque > limite
        excedeu_saque = numero_operacoes >= LIMITE_SAQUES
        
        if excedeu_saldo or excedeu_limite:
            print("\nSaque não autorizado! Verifique seu saldo e/ou limite de saque.\n")      
        
        elif excedeu_saque:
            print("\nSaque não autorizado! Limite de saques diários excedido.\n")
                      
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_operacoes += 1     
            print(f"\nSaque de R${valor_saque:.2f} realizado com sucesso\n")
            
        else:
            print("\nValor inválido! O saque deve ser maior que zero.\n")

    elif opcao == "3":
        print("\n########## Extrato ##########\n")
        print("Não foram realizadas operações." if extrato == "" else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print(f"Limite de saque diário: R$ {limite:.2f}")
        print(f"Operações realizadas: {numero_operacoes}")
        print("\n##############################\n")
    
    elif opcao == "4":
        print("\nObrigado por utilizar o Banco Dio.me! Volte sempre.\n")
        break
    
    else:
        print("\nOpção inválida! Por favor, escolha uma opção válida.\n")
            
        