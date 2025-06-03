import random


senha = [
    "Precisa conter um número",
    "Precisa conter pelo menos uma letra minúscula",
    "Precisa conter pelo menos uma letra maiúscula",
    "Precisa ter pelo menos 8 caracteres"
]
erros = []
pessoas_login = []
pessoas_login_completo =[]


print("Para você criar uma senha precisa cumprir esses critérios:")

for criterio in senha:
    print(f"- {criterio}")

nome = input("Digite o seu nome: ")

senhas = input("Digite uma senha que esteja dentro dos critérios: ")

if not len(senhas) >= 8:
    erros.append("- Precisa ter pelo menos 8 caracteres.")
if not any(c.isupper() for c in senhas):
    erros.append("- Precisa conter pelo menos uma letra maiúscula.")
if not any(c.islower() for c in senhas):
    erros.append("- Precisa conter pelo menos uma letra minúscula.")
if not any(c.isdigit() for c in senhas):
    erros.append("- Precisa conter um número.")

if not erros:
    print(f"Parabéns {nome}, sua senha foi cadastrada com sucesso ✅")
else:
    print("Senha fraca.")
    print("Motivos:")
    for erro in erros:
        print(erro)

pessoas = {'nome': nome, 'senhas': senhas}
pessoas_login.append(pessoas)

print(" cadastrado com sucesso!")
print(f"{pessoas['nome']} | senha:******** ")


print("agora vamos fazer o login:")

while True:
    email = input("digite o seu email:")
    if  "@" in email and "." in email.split("@")[-1]:
        print("✅,email registrado com sucesso!.")

        print("digite o codigo que será gerado para confirmar o seu email")
        codigo = ''.join(str(random.randint(0, 9)) for _ in range(4))
        print(f"{codigo}")
        verificar = input("digite o codigo:")


        if verificar == codigo:
                print("login de email concluido.")
        else:
                print("codigo digitado errado, tente novamente")

                continue
        
    else:
        print("erro em digitar o seu email.")

    pessoas2 = {'nome': nome, 'senhas': senhas , 'email':email}
    pessoas_login_completo.append(pessoas2)

    print(" cadastrado com sucesso!")
    print(f"{pessoas2['nome']} | senha:******** | email:{pessoas2['email']}")   


        
