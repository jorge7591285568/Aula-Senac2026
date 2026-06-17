"""
PROGRAMA DE EXPLICAÇÃO SOBRE PYTHON
===================================
Este programa ensina os conceitos fundamentais de Python com exemplos práticos
"""

from turtle import home


def explicacao_python():
    """
    Função principal que explica o que é Python e seus conceitos básicos
    """
    
    print("=" * 60)
    print("   BEM-VINDO AO CURSO INTRODUTIVO DE PYTHON!")
    print("=" * 60)
    print()
    
    # O que é Python
    print("### O QUE É PYTHON? ###")
    print()
    print("  Python é uma linguagem de programação:")
    print("  • Interpretada (não executa código compilado)")
    print("  • De alto nível (fácil de entender)")
    print("  • Multipropósito (web, dados, automação, IA)")
    print("  • Com sintaxe simples e legível")
    print("  • Criada por Guido van Rossum em 1991")
    print()
    print("Nome vem do show 'Monty Python's Flying Circus', não de serpente!")
    print()
    
    # Exemplo 1: Variáveis e Tipos
    print("### 1. VARIÁVELES E TIPOS DE DADOS ###")
    print()
    
    # String
    nome = "Python"
    print(f"String: nome = '{nome}'")
    print(f"  Tipo: {type(nome)}")
    print()
    
    # Inteiro
    idade = 33
    print(f"Inteiro: idade = {idade}")
    print(f"  Tipo: {type(idade)}")
    print()
    
    # Float
    pi = 3.14159
    print(f"Float: pi = {pi}")
    print(f"  Tipo: {type(pi)}")
    print()
    
    # Booleano
    é_facil = True
    print(f"Booleano: é_facil = {é_facil}")
    print(f"  Tipo: {type(é_facil)}")
    print()
    
    # Exemplo 2: Estruturas de Dados
    print("### 2. ESTRUTURAS DE DADOS ###")
    print()
    
    # Lista
    listas = [1, 2, 3, 4, 5]
    print(f"Lista: {listas}")
    print(f"  Primeiro elemento: {listas[0]}")
    print(f"  Adicionar 6: {listas + [6]}")
    print()
    
    # Dicionário
    dicionario = {"nome": "Python", "versao": 3.12, "ano": 2026}
    print(f"Dicionário: {dicionario}")
    print(f"  Nome: {dicionario['nome']}")
    print(f"  Versão: {dicionario['versao']}")
    print()
    
    # Exemplo 3: Estruturas Condicionais
    print("### 3. ESTRUTURAS CONDICIONAIS (if/else) ###")
    print()
    
    nota = 85
    print(f"Nota: {nota}")
    
    if nota >= 90:
        classificacao = "A"
    elif nota >= 80:
        classificacao = "B"
    elif nota >= 70:
        classificacao = "C"
    else:
        classificacao = "D"
    
    print(f"classificacao: {classificacao}")
    print("  Syntax: if/elif/else com indentação!")
    print()
    
    # Exemplo 4: Loops
    print("### 4. LOOPS (for/while) ###")
    print()
    
    print("Loop FOR - contar de 1 a 5:")
    for i in range(1, 6):
        print(f" {i}", end="")
    print()
    print()
    
    print("Loop WHILE - contador de 3 a 0:")
    contador = 3
    while contador > 0:
        print(f"  {contador}", end="")
        contador -= 1
    print()
    print()
    
    # Exemplo 5: Funções
    print("### 5. FUNÇÕES ###")
    print()
    
    def saudacao(nome, linguagem="Python"):
        """Função que retorna uma mensagem de saudação"""
        return f"Olá®, {nome}! Bem-vindo a {linguagem}!"
    
    mensagem = saudacao("Estudante")
    print(f"Função: saudacao('Estudante')")
    print(f"  Resultado: '{mensagem}'")
    print()
    
    def calcular_area(largura, altura):
        """Calcula área de um retângulo"""
        return largura * altura
    
    area = calcular_area(5, 3)
    print(f"Função: calcular_area(5, 3)")
    print(f"  Área: {area}")
    print()
    
    # Exemplo 6: List Comprehension
    print("### 6. LIST COMPREHENSION (feature poderosa!) ###")
    print()
    
    numeros = [1, 2, 3, 4, 5]
    quadrados = [x**2 for x in numeros]
    
    print(f"Números: {numeros}")
    print(f"Quadrados: {quadrados}")
    print("  Syntax: [expressao for item in lista]")
    print()
    
    # Exemplo 7: Manipulação de Erros
    print("### 7. MANIPULAÇÃO DE ERROS (try/except) ###")
    print()
    
    def dividir(a, b):
        """Divide dois números com tratamento de erro"""
        try:
            resultado = a / b
            return resultado
        except ZeroDivisionError:
            return "Erro: divisão por zero!"
        except TypeError:
            return "Erro: tipos inválidos!"
    
    print(f"dividir(10, 2) = {dividir(10, 2)}")
    print(f"dividir(10, 0) = {dividir(10, 0)}")
    print(f"dividir(10, 'a') = {dividir(10, 'a')}")
    print()
    
    # Por que Python?
    print("### POR QUE APRENDER PYTHON? ###")
    print()
    print("✓ Fácil de aprender (sintaxe simples)")
    print("✓ Popular (milhões de usuários)")
    print("✓ Versátil (web, dados, IA, automação)")
    print("✓ Grande ecossistema (bibliotecas)")
    print("✓ Bom para iniciantes e profissionais")
    print("✓ Carreiras bem remuneradas")
    print()
    
    # Recursos para aprender
    print("### RECURSOS PARA APRENDER PYTHON ###")
    print()
    print("• Documentação oficial: python.org")
    print("• Curso gratuito: Coursera, edX, freeCodeCamp")
    print("• Praticar: HackerRank, LeetCode, Codewars")
    print("• Bibliotecas populares:")
    print("  - NumPy/Pandas (dados)")
    print("  - Requests (web)")
    print("  - Flask/Django (web)")
    print("  - TensorFlow/PyTorch (IA)")
    print("  - Matplotlib/Seaborn (visualização)")
    print()
    
    print("=" * 60)
    print("   AGORA VOCÊ SABE O BÁSICO DE PYTHON!")
    print("   Continue praticando e explorando!")
    print("=" * 60)

# Executar o programa
if __name__ == "__main__":
    explicacao_python()