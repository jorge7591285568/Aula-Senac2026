

# ============================================
# SISTEMA DE CADASTRO E LOGIN COM CORES
# ============================================

from colorama import init, Fore, Style

# Inicializa o colorama para funcionar bem no terminal
init(autoreset=True)

# Listas para guardar usuários e senhas
usuarios = []
senhas = []

# Função para imprimir títulos bonitos
def titulo(texto):
    print(Fore.CYAN + Style.BRIGHT + "=" * 40)
    print(Fore.CYAN + Style.BRIGHT + texto.center(40))
    print(Fore.CYAN + Style.BRIGHT + "=" * 40)

# Função para mensagens de sucesso
def sucesso(texto):
    print(Fore.GREEN + Style.BRIGHT + texto)

# Função para mensagens de erro
def erro(texto):
    print(Fore.RED + Style.BRIGHT + texto)

# Função para mensagens de aviso
def aviso(texto):
    print(Fore.YELLOW + Style.BRIGHT + texto)

# Exibe o título inicial
titulo("SISTEMA DE CADASTRO")

# Laço principal do menu
while True:
    print()
    print(Fore.MAGENTA + "1 - Cadastrar usuário")
    print(Fore.MAGENTA + "2 - Fazer login")
    print(Fore.MAGENTA + "3 - Listar usuários")
    print(Fore.MAGENTA + "4 - Sair")

    opcao = input(Fore.BLUE + "Escolha uma opção: ")

    if opcao == "1":
        titulo("CADASTRO")

        nome = input("Digite seu nome: ")
        email = input("Digite seu e-mail: ")
        idade = input("Digite sua idade: ")
        usuario = input("Escolha um nome de usuário: ")
        senha = input("Crie uma senha: ")
        confirmar_senha = input("Confirme sua senha: ")

        # Validação dos campos
        if nome == "":
            erro("O nome não pode ficar vazio.")
        elif email == "":
            erro("O e-mail não pode ficar vazio.")
        elif idade == "":
            erro("A idade não pode ficar vazia.")
        elif usuario == "":
            erro("O nome de usuário não pode ficar vazio.")
        elif senha == "":
            erro("A senha não pode ficar vazia.")
        elif senha != confirmar_senha:
            erro("As senhas não coincidem.")
        elif usuario in usuarios:
            erro("Esse usuário já existe.")
        else:
            usuarios.append(usuario)
            senhas.append(senha)
            sucesso("Cadastro realizado com sucesso!")

    elif opcao == "2":
        titulo("LOGIN")

        login_usuario = input("Digite seu usuário: ")
        login_senha = input("Digite sua senha: ")

        if login_usuario in usuarios:
            indice = usuarios.index(login_usuario)
            if senhas[indice] == login_senha:
                sucesso("Login realizado com sucesso!")
                print(Fore.GREEN + "Bem-vindo,", login_usuario)
            else:
                erro("Senha incorreta.")
        else:
            erro("Usuário não encontrado.")

    elif opcao == "3":
        titulo("USUÁRIOS CADASTRADOS")

        if len(usuarios) == 0:
            aviso("Nenhum usuário cadastrado.")
        else:
            for u in usuarios:
                print(Fore.WHITE + "- " + u)

    elif opcao == "4":
        titulo("SAINDO")
        aviso("Obrigado por usar o sistema.")
        break

    else:
        erro("Opção inválida. Tente novamente.")

    print()
    print(Fore.WHITE + "-" * 40)
    print(Fore.WHITE + "Voltando ao menu principal...")
    print(Fore.WHITE + "-" * 40)

print(Fore.CYAN + Style.BRIGHT + "Programa encerrado.")