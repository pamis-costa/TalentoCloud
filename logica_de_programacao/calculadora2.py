def calculadora():
    while True:
        # menu 
        print("\nEscolha uma operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        try:
            opcao = int(input("Digite o número da operação desejada: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            continue

        if opcao == 0:
            print("Encerrando o programa...")
            break
        elif opcao in [1, 2, 3, 4]:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, insira números válidos.")
                continue

            if opcao == 1:
                resultado = num1 + num2
                print(f"Resultado da soma: {resultado}")
            elif opcao == 2:
                resultado = num1 - num2
                print(f"Resultado da subtração: {resultado}")
            elif opcao == 3:
                resultado = num1 * num2
                print(f"Resultado da multiplicação: {resultado}")
            elif opcao == 4:
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida.")
                else:
                    resultado = num1 / num2
                    print(f"Resultado da divisão: {resultado}")
        else:
            print("Essa opção não existe. Tente novamente.")

calculadora()
