
# ================================================#
# CÓDIGO PYTHON COM TODOS OS COMANDOS PRINCIPAIS  #
# ================================================#

# 1. COMENTÁRIOS
# Comentário de linha única (usa #)
# Este é um comentário simples

"""
Comentário de múltiplas linhas
usando aspas triplas duplas
(para docstrings ou blocos longos)
"""

'''
Aspas triplas simples também funcionam
para comentários de múltiplas linhas
'''

# 2. VARIÁVEIS E TIPOS DE DADOS
# Variáveis não precisam de declaração de tipo (tipagem dinâmica)

# Tipos numéricos
numero_inteiro = 10           # int (inteiro)
numero_float = 10.5           # float (ponto flutuante)
numero_complexo = 3 + 4j      # complex (complexo)

# Tipos de texto
texto = "Olá, mundo!"         # str (string)
texto_simples = 'Python'      # str também com aspas simples

# Tipos booleanos
verdadeiro = True             # bool (verdadeiro)
falso = False                 # bool (falso)

# Tipo None (nulo)
nulo = None                   # NoneType (nulo)

# Sequências
lista = [1, 2, 3, 4, 5]       # list (lista - ordenada, mutável)
tupla = (1, 2, 3, 4, 5)       # tuple (tupla - ordenada, imutável)
conjunto = {1, 2, 3, 4, 5}    # set (conjunto - não ordenado, único)
dicionario = {'a': 1, 'b': 2} # dict (dicionário - key-value)

# 3. OPERADORES
# Operadores aritméticos
soma = 10 + 5                 # + (adição)
subtracao = 10 - 5            # - (subtração)
multiplicacao = 10 * 5        # * (multiplicação)
divisao = 10 / 5              # / (divisão)
divisao_inteira = 10 // 3     # // (divisão inteira)
potencia = 10 ** 2            # ** (exponenciação)
resto = 10 % 3                # % (resto da divisão)

# Operadores de comparação
igual = 10 == 5               # == (igual)
diferente = 10 != 5           # != (diferente)
maior = 10 > 5                # > (maior que)
menor = 10 < 5                # < (menor que)
maior_igual = 10 >= 5         # >= (maior ou igual)
menor_igual = 10 <= 5         # <= (menor ou igual)

# Operadores lógicos
and_result = True and False   # and (e lógico)
or_result = True or False     # or (ou lógico)
not_result = not True         # not (negação)

# Operadores de atribuição
x = 10                        # = (atribuição simples)
x += 5                        # += (adição e atribuição)
x -= 5                        # -= (subtração e atribuição)
x *= 5                        # *= (multiplicação e atribuição)
x /= 5                        # /= (divisão e atribuição)

# Operadores de identidade
e_igual = x is 10           # is (é o mesmo objeto?)
nao_e_igual = x is not 10   # is not (não é o mesmo objeto?)

# Operadores de pertinência
esta_na_lista = 3 in lista    # in (está na sequência?)
nao_esta = 10 not in lista    # not in (não está na sequência?)

# 4. ESTRUTURAS DE CONTROLE

# if, elif, else (condicionais)
idade = 18

if idade < 12:
    print("Criança")
elif idade < 18:
    print(" adolescentes ")
else:
    print("Adulto")

# Operador ternário (if em uma linha)
mensagem = "Aprovado" if idade >= 18 else "Reprovado"

# while (loop enquanto)
contador = 0
while contador < 5:
    print(contador)
    contador += 1
    if contador == 3:
        break  # break: sai do loop imediatamente

# for (loop para)
for i in range(5):
    print(i)

# for com lista
for item in lista:
    print(item)

# for com dicionário
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")

# continue (continua o loop mesmo após encontrar)
for i in range(10):
    if i == 5:
        continue  # continue: ignora o resto e continua o loop
    print(i)

# pass (não faz nada - placeholder)
def funcao_nao_implementada():
    pass  # pass: ocupa espaço sem executar nada

# 5. FUNÇÕES

# Definição de função simples
def saudacao():
    return "Olá!"

# Função com argumentos
def somar(a, b):
    return a + b

# Função com argumento default
def multiplicar(a, b=2):
    return a * b

# Função com argumentos arbitrários
def soma_tudo(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total

# Função com keyword arguments
def imprime_info(**info):
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

# Função com tipo de retorno especificado
def retornar_inteiro(x: int) -> int:
    return x

# Chamada de funções
print(saudacao())
print(somar(5, 3))
print(multiplicar(5))
print(soma_tudo(1, 2, 3, 4, 5))
imprime_info(nome="João", idade=25)

# 6. CLASSES E OBJETO

# Definição de classe
class Pessoa:
    # Construtor (método inicializador)
    def __init__(self, nome, idade):
        self.nome = nome  # self: referência ao objeto atual
        self.idade = idade
    
    # Método da classe
    def apresentar(self):
        return f"Olá, sou {self.nome} e tenho {self.idade} anos"
    
    # Método estático
    @staticmethod
    def metodo_statico():
        return "Método estático"
    
    # Método da classe
    @classmethod
    def metodo_classe(cls):
        return f"Método da classe {cls.__name__}"

# Criando objeto (instância)
pessoa1 = Pessoa("Maria", 30)
print(pessoa1.apresentar())

# Acesso a atributos
print(pessoa1.nome)
print(pessoa1.idade)

# Modificação de atributos
pessoa1.idade = 31
print(pessoa1.apresentar())

# Métodos estáticos e de classe
print(Pessoa.metodo_statico())
print(Pessoa.metodo_classe())

# Herança
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)  # super(): chama o construtor da pai
        self.curso = curso
    
    # Sobrescrita de método
    def apresentar(self):
        return f"Sou {self.nome}, {self.idade} anos e estudo {self.curso}"

estudante1 = Estudante("João", 20, "Engenharia")
print(estudante1.apresentar())

# 7. PROCESSAMENTO DE LISTAS E SEQUÊNCIAS

# List comprehension (lista compacta)
lista_dobro = [x * 2 for x in lista]
print(lista_dobro)

# List comprehension com condição
lista_even = [x for x in lista if x % 2 == 0]
print(lista_even)

# Dict comprehension
dicionario_dobro = {k: v * 2 for k, v in dicionario.items()}
print(dicionario_dobro)

# Set comprehension
set_quad = {x**2 for x in [1, 2, 3, 4, 5]}
print(set_quad)

# Map (aplica função a cada elemento)
def dobro(x):
    return x * 2

lista_map = list(map(dobro, lista))
print(lista_map)

# Filter (filtra elementos)
lista_filter = list(filter(lambda x: x > 2, lista))
print(lista_filter)

# Lambda (função anônima)
lambda_soma = lambda a, b: a + b
print(lambda_soma(5, 3))

# Reduce (reduz a sequência a um valor)
from functools import reduce
soma_reduce = reduce(lambda x, y: x + y, lista)
print(soma_reduce)

# 8. MANEJO DE EXCEÇÕES

# try, except, else, finally
try:
    resultado = 10 / 0  # Isso vai gerar erro
except ZeroDivisionError:
    print("Erro: divisão por zero!")
except Exception as e:
    print(f"Erro genérico: {e}")
else:
    print("Nenhum erro ocorreu")
finally:
    print("Executa sempre (final do try-except)")

# raise (levantar exceção)
def verificar_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    return idade

# try com raise
try:
    verificar_idade(-5)
except ValueError as e:
    print(f"Erro: {e}")

# 9. MODULOS E IMPORTS

# Import módulo inteiro
import math
print(math.sqrt(16))  # Raiz quadrada

# Import com alias
import numpy as np

# Import função específica
from math import pi, sin
print(pi)
print(sin(0))

# Import de classe
from datetime import datetime
print(datetime.now())

# Import relativo (para pacotes)
# from .mymodule import funcao

# 10. ENTRADA E SAÍDA (I/O)

# print() - saída
print("Texto na tela")
print(f"Valor formatado: {numero_inteiro}")

# input() - entrada
# nome = input("Digite seu nome: ")  # Descomente para testar
# print(f"Olá, {nome}")

# 11. MANEJO DE ARQUIVOS

# open() - abre arquivo
# Modo 'w' (write) - escrever
with open("exemplo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write(" Segunda linha")

# Modo 'r' (read) - ler
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Ler linha por linha
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())  # strip() remove espaços extras

# 12. FUNÇÕES ÚTILES E MÉTODOS

# len() - tamanho
print(len(lista))  # 5

# range() - sequência
for i in range(1, 10, 2):  # início, fim, passo
    print(i)

# enumerate() - índice e valor
for indice, valor in enumerate(lista):
    print(f"{indice}: {valor}")

# zip() - combina listas
lista2 = ['a', 'b', 'c']
for num, char in zip(lista, lista2):
    print(f"{num}: {char}")

# sorted() - ordena
lista_ordenada = sorted([3, 1, 4, 2, 5])
print(lista_ordenada)

# reversed() - reverte
lista_reversa = list(reversed(lista))
print(lista_reversa)

# any() e all()
print(any([False, True, False]))  # True (algum é True)
print(all([True, True, True]))    # True (todos são True)

# isinstance() - verificar tipo
print(isinstance(numero_inteiro, int))  # True
print(isinstance(texto, str))           # True

# type() - tipo de variável
print(type(numero_inteiro))
print(type(texto))

# str(), int(), float() - conversão
texto_num = "123"
print(int(texto_num))    # 123
print(float(texto_num))  # 123.0

# list(), tuple(), set(), dict() - conversão de tipos
print(list("abc"))       # ['a', 'b', 'c']
print(tuple([1, 2, 3]))  # (1, 2, 3)
print(set([1, 2, 2, 3])) # {1, 2, 3}

# 13. MÉTODOS DE LISTA
lista.append(6)           # adiciona ao final
lista.extend([7, 8])      # adiciona múltiplos
lista.insert(0, 0)        # adiciona em posição
lista.remove(0)           # remove primeiro elemento igual
valor = lista.pop()       # remove e retorna último
lista.clear()             # remove todos
#lista.index(2)            # retorna índice
lista.count(2)            # conta ocorrências
lista.sort()              # ordena
lista.reverse()           # reverte
lista.copy()              # copia lista

# 14. MÉTODOS DE STRING
texto = "  Olá, Mundo!  "
print(texto.upper())           # OLÁ, MUNDO!
print(texto.lower())           # ola, mundo!
print(texto.strip())           # "Olá, Mundo!" (remove espaços)
print(texto.replace("Mundo", "Python"))  # "Olá, Python!"
print(texto.split(","))        # ['  Olá', ' Mundo!  ']
print(texto.find("Mundo"))     # índice onde encontra
print(texto.startswith("Olá")) # True
print(texto.endswith("!"))     # True
print(texto.isalnum())         # False (tem espaços e pontuação)
print(texto.isalpha())         # False
print(texto.isdigit())         # False
print(texto.isspace())         # False

# 15. MÉTODOS DE DICIONÁRIO
dicionario.keys()              # retorna chaves
dicionario.values()            # retorna valores
dicionario.items()             # retorna (chave, valor)
dicionario.get('a')            # retorna valor (sem erro se não existe)
dicionario.update({'c': 3})    # adiciona/Atualiza
dicionario.pop('a')            # remove e retorna valor
dicionario.popitem()           # remove último (chave, valor)
dicionario.clear()             # remove todos
dicionario.copy()              # copia

# 16. OPERADOR DE DECOMPOSIÇÃO (UNPACKING)
a, b, c = [1, 2, 3]  # unpacking de lista
print(a, b, c)       # 1, 2, 3

primeiro, *resto = [1, 2, 3, 4]  # * captura resto
print(primeiro, resto)           # 1, [2, 3, 4]

# 17. GENERATORS (Geradores)
def gerador():
    for i in range(5):
        yield i  # yield: retorna valor e mantém estado

for num in gerador():
    print(num)

# 18. DECORADORES
def meu_decorador(funcao):
    def wrapper():
        print("Antes da função")
        funcao()
        print("Depois da função")
    return wrapper

@meu_decorador
def funcao_decorada():
    print("Função executando")

funcao_decorada()

# 19. ASSERT (verificação)
x = 10
assert x == 10, "x deve ser 10"  # levanta erro se falso

# 20. WALRUS OPERATOR (:=) - Python 3.8+
while (n := len(lista)) < 10:
    lista.append(n)
    # n é atribuído e usado na mesma expressão

# ============================================#
# FINAL DO CÓDIGO                             #
# ============================================#
print("Todos os comandos Python foram demonstrados!")