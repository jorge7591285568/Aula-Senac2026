print("===================================")
print("       CADASTRO DE USUÁRIO         ")
print("===================================")

nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
idade = input("Digite sua idade: ")
cidade = input("Digite sua cidade: ")
usuario = input("Escolha um nome de usuário: ")
senha = input("Crie uma senha: ")
confirmar_senha = input("Confirme sua senha: ")

print("===================================")
print("          VALIDANDO DADOS          ")
print("===================================")

if nome == "":
    print("O nome não pode ficar vazio.")
elif email == "":
    print("O e-mail não pode ficar vazio.")
elif idade == "":
    print("A idade não pode ficar vazia.")
elif cidade == "":
    print("A cidade não pode ficar vazia.")
elif usuario == "":
    print("O nome de usuário não pode ficar vazio.")
elif senha == "":
    print("A senha não pode ficar vazia.")
else:
    print("Campos principais preenchidos com sucesso.")

if senha == confirmar_senha:
    print("As senhas coincidem.")
elif senha != confirmar_senha:
    print("As senhas não coincidem.")
else:
    print("Erro na validação da senha.")

print("===================================")
print("            RESUMO FINAL           ")
print("===================================")

print("Nome:", nome)
print("E-mail:", email)
print("Idade:", idade)
print("Cidade:", cidade)
print("Usuário:", usuario)

if idade >= "18":
    print("Cadastro aprovado para maior de idade.")
elif idade == "17":
    print("Cadastro em análise: quase maior de idade.")
else:
    print("Cadastro aprovado para menor de idade com responsável.")

if "@" in email:
    print("E-mail com formato aparentemente válido.")
elif "." in email:
    print("E-mail pode estar correto, mas vale revisar.")
else:
    print("E-mail inválido.")

if len(usuario) >= 5:
    print("Nome de usuário aceitável.")
elif len(usuario) >= 3:
    print("Nome de usuário curto, mas ainda aceitável.")
else:
    print("Nome de usuário muito pequeno.")

print("===================================")
print("      CADASTRO CONCLUÍDO          ")
print("===================================")
print("Obrigado por se cadastrar!")