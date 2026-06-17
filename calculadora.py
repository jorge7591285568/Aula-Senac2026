def calculadora():
    print("=" * 30)
    print("CALCULADORA SIMPLES")
    print("=" * 30)

    num1 = float(input("Digite o primeiro número: "))

    print("\nEscolha a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operacao = input("Digite a opção: ")
    num2 = float( input("Digite o segundo número: "))


    print()
    if operacao == "1":
        resultado = num1 + num2
        print("Resultado:", resultado)

    elif operacao == "2":
        resultado = num1 - num2
        print("Resultado:", resultado)

    elif operacao == "3":
        resultado = num1 * num2
        print("Resultado:", resultado)

    elif operacao == "4":
        if num2 != 0:
            resultado = num1 / num2
            print()  
            print("Resultado:", resultado)
        else:
            print("Erro: não é possível dividir por zero.")
    else:
        print("Opção inválida.")
    
calculadora()
print()
