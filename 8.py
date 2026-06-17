print("=================================")
print("      QUIZ BÁSICO DE PYTHON      ")
print("=================================")

nome = input("Digite seu nome: ")
print("Olá,", nome)

print("Responda com sim ou nao.")
gosta_python = input("Você gosta de Python? ")

if gosta_python == "sim":
    print("Ótimo! Python é uma linguagem muito popular.")
if gosta_python == "nao":
    print("Tudo bem! Você pode aprender no seu ritmo.")

idade = input("Digite sua idade: ")

if idade >= "18":
    print("Você já é maior de idade.")
if idade < "18":
    print("Você ainda é menor de idade.")

cor = input("Qual é sua cor favorita? ")
print("Sua cor favorita é:", cor)

animal = input("Qual é seu animal favorito? ")
print("Seu animal favorito é:", animal)

comida = input("Qual é sua comida favorita? ")
print("Sua comida favorita é:", comida)

print("Agora vamos fazer mais perguntas.")

estuda = input("Você estuda programação? ")
if estuda == "sim":
    print("Parabéns! Continue estudando.")
if estuda == "nao":
    print("Sem problemas, começar também é importante.")

joga = input("Você gosta de jogos? ")
if joga == "sim":
    print("Legal! Jogos podem ajudar a praticar lógica.")
if joga == "nao":
    print("Tudo bem, existem muitas outras coisas legais.")

cidade = input("Em que cidade você mora? ")
print("Você mora em:", cidade)

linguagem = input("Qual linguagem você quer aprender? ")
print("Você quer aprender:", linguagem)

print("Obrigado por participar do quiz!")
print("Nome:", nome)
print("Idade:", idade)
print("Cor favorita:", cor)
print("Animal favorito:", animal)
print("Fim do programa.")