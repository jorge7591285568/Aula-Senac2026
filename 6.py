print("Bem-vindo ao Python!")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

ano_atual = 2026
ano_nascimento = ano_atual - idade

print("Seu nome é:", nome)
print("Você tem", idade, "anos")
print("Você nasceu em:", ano_nascimento)

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

soma = 5 + 3
subtracao = 10 - 4

print("5 + 3 =", soma)
print("10 - 4 =", subtracao)
print("Fim do programa.")