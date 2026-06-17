# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())
## Números e Operações Matemáticas
# Soma
5 + 5
# Subtração
#8–3
# Multiplicação
8 * 3
# Divisão
9 / 2
# Potência
6 ** 2  
# Módulo
10 % 3  
### Função Type
type(5)
type(5.0)
a = 'Eu sou uma string'
type(a)
### Operações com números float
3.1 + 6.4
4 + 4.0
# Resultado é um número float
4 / 2
# Resultado é um número inteiro
4 // 2
4 / 3.0
4 // 3.0
### Conversão
float(9)
int(6.0)
### Hexadecimal e Binário
hex(394)
hex(217)
bin(286)
bin(390)
### Funções abs, round e pow
# Retorna o valor absoluto
abs(-8)
# Retorna o valor absoluto
abs(8)
# Retorna o valor com arredondamento
round(3.14151922,2)
# Potência
pow(4,2)
# Potência
pow(5,3)
# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
lista = [1,2,3,4,5,6,7,8,9,10]
lista
# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
list1 = ['carros','viagem','diversao','comidas','dinheiro']
list1
# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
f1 = 'jorge '
f2 = 'mendes'
f3_f = f1 + f2
f3_f
# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a 
#função count do objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tup = (1,2,2,3,4,4,4,5)
tup.count(4)
# Exercício 5 - Crie um dicionário vazio e imprima na tela
dict3 = {}
dict3
# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dict = { 'k1':("ontem",1),'k2':("hoje",2),'k3':("amanha",3) }
dict
# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na 
# tela
dict['k4'] = ("dias da semana",7)
dict
# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 
#elementos numéricos. 
# Imprima o dicionário na tela.
dict2 = {'chave':'internet','chave1':'analisededados','chave2':[100,50]}
dict2
# Exercício 9 - Crie uma lista de 4 elementos.
# O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos,
# o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
list = ['string',(100,50),{'k1':'v1','k2':'v2'},50.25]
list
# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
frase[0:18]