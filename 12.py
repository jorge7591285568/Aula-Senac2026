# ============================================
# MENU COMPLETO: CADASTRO E LOGIN DE USUÁRIO
# ============================================

usuarios = []
senhas = []

print("===================================")
print("   SISTEMA DE CADASTRO E LOGIN     ")
print("===================================")

while True:
    print("\nMENU PRINCIPAL")
    print("1 - Cadastrar usuário")
    print("2 - Fazer login")
    print("3 - Listar usuários")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n=== CADASTRO ===")
        nome = input("Digite seu nome: ")
        email = input("Digite seu e-mail: ")
        idade = input("Digite sua idade: ")
        usuario = input("Escolha um nome de usuário: ")
        senha = input("Crie uma senha: ")
        confirmar_senha = input("Confirme sua senha: ")

        if nome == "":
            print("O nome não pode ficar vazio.")
        elif email == "":
            print("O e-mail não pode ficar vazio.")
        elif idade == "":
            print("A idade não pode ficar vazia.")
        elif usuario == "":
            print("O nome de usuário não pode ficar vazio.")
        elif senha == "":
            print("A senha não pode ficar vazia.")
        elif senha != confirmar_senha:
            print("As senhas não coincidem.")
        else:
            usuarios.append(usuario)
            senhas.append(senha)
            print("Cadastro realizado com sucesso!")

    elif opcao == "2":
        print("\n=== LOGIN ===")
        login_usuario = input("Digite seu usuário: ")
        login_senha = input("Digite sua senha: ")

        if login_usuario in usuarios:
            indice = usuarios.index(login_usuario)
            if senhas[indice] == login_senha:
                print("Login realizado com sucesso!")
                print("Bem-vindo,", login_usuario)
            else:
                print("Senha incorreta.")
        else:
            print("Usuário não encontrado.")

    elif opcao == "3":
        print("\n=== USUÁRIOS CADASTRADOS ===")
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.")
        else:
            for u in usuarios:
                print("-", u)

    elif opcao == "4":
        print("Saindo do sistema...")
        print("Obrigado por usar o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")

    print("\n-----------------------------------")
    print("Voltando ao menu principal...")
    print("-----------------------------------")

print("Programa encerrado.")