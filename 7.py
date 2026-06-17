print("=== Jogo rápido ===")

nome = input("Digite seu nome: ")
resposta = input("Você gosta de programar? (sim/nao): ")

print("Olá,", nome)

if resposta == "sim":
    print("Que bom! Programar é muito legal.")
if resposta == "nao":
    print("Tudo bem! Você pode aprender aos poucos.")

idade = input("Digite sua idade: ")

print("Obrigado por participar!")
print("Seu nome é:", nome)
print("Sua resposta foi:", resposta)
print("Sua idade foi:", idade)
print("Programa encerrado.")
