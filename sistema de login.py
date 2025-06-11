import json
import os
import re

def verificar_email(email):
    
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(padrao, email):
        return True
    else:
        return False


def carregar_dados(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        return []

def salvar_dados(arquivo, dados):
    with open(arquivo, "w") as f:
        json.dump(dados, f, indent=4)

ARQUIVO = "dados.json"
login = carregar_dados(ARQUIVO)

menu_opcoes = {
    1: "- login",
    2: "- cadastrar",
    3: "- esqueci a senha",
    4: "- sair"
}

while True:
    print("\n-- Bem-vindo ao sistema de entrada --")
    for chave, texto in menu_opcoes.items():
        print(f"{chave}: {texto}")

    try:
        opcao = int(input("Digite uma dessas opções: "))
    except ValueError:
        print("❌ Digite um número válido.")
        continue

    if opcao == 2:  
        apelido = input("Digite o seu apelido(digite 'sair'para voltar no nemu principal): ")
        if apelido == 'sair':
            continue
        while True:
            email = input("Digite o seu email: ")
            if verificar_email(email):
                print("✅ Email registrado com sucesso!")
            else:
                print("❌ Erro ao digitar o seu email. Tente novamente.")
                continue

            print("\nPara criar uma senha, ela precisa atender aos seguintes critérios:")
            requisitos = [
                "Precisa conter um número",
                "Precisa conter pelo menos uma letra minúscula",
                "Precisa conter pelo menos uma letra maiúscula",
                "Precisa ter pelo menos 8 caracteres"
            ]
            for item in requisitos:
                print(f"-- {item} --")

            senha_digitada = input("Digite uma senha: ")
            erros = [] 

            if len(senha_digitada) < 8:
                erros.append("- Precisa ter pelo menos 8 caracteres.")
            if not any(c.isupper() for c in senha_digitada):
                erros.append("- Precisa conter pelo menos uma letra maiúscula.")
            if not any(c.islower() for c in senha_digitada):
                erros.append("- Precisa conter pelo menos uma letra minúscula.")
            if not any(c.isdigit() for c in senha_digitada):
                erros.append("- Precisa conter um número.")

            if erros:
                print("❌ Senha fraca. Motivos:")
                for erro in erros:
                    print(erro)
                continue  

            print("✅ Senha registrada com sucesso!")

            data_nascimento = (input("digite a sua data de nascimento (DD/MM/AAAA):"))

            pessoa = {
                'apelido': apelido,
                'email': email,
                'senha': senha_digitada,
                'data_nascimento':data_nascimento
            }
            login.append(pessoa)
            salvar_dados(ARQUIVO, login)

            print("\n✅ Cadastro feito com sucesso!")
            print(f"\nApelido: {pessoa['apelido']} | Email: {pessoa['email']} | Data de nascimento: {pessoa['data_nascimento']} .")
            break 

    elif opcao == 4:
        print("\nEncerrando o programa.")
        break
    elif opcao == 1:
        log_email = input("digite o email:")
        log_senha = input("digite a sua senha:")

        usuario_logado = None
        for pessoa in login:
            if 'email' in pessoa and 'senha' in pessoa:
                if pessoa['email'] == log_email and pessoa['senha'] == log_senha:
                    usuario_logado = pessoa
                    break


        if usuario_logado:
            print(f"Login realizado com sucesso! Bem-vindo {usuario_logado['apelido']}.")
        else:
            print(" usuario não encontrado, Tente novamente.")
    elif opcao == 3:

     
        menu_opcoes2 = {
            1: "- redefinir senha.",
            2: "- recuperar senha.",
            3: "- sair"
        }

        print("\nescolha uma dessas opções:")

        for numerom , red_se in menu_opcoes2.items():
            print(f"{numerom}: {red_se}")

        opção = int(input("\ndigite uma dessas opções:"))


        if opção == 3:
            print("\nvoltando ao menu principal.")

        elif opção == 1:
            
            print("\npara redefinir a sua senha, coloque o seu email")

            email_recuperar_senha = input("\ndigite o seu email:")


            usuario_logado2 = None
            for pessoa in login:
                if 'email' in pessoa:
                    if pessoa['email'] == email_recuperar_senha:
                        usuario_logado2 = pessoa
                        break

            if not usuario_logado2:
                print("❌ Email não encontrado. Tente novamente.")
                continue
            
            print(f"\npara confirmar que é você {usuario_logado2['apelido']}, coloque a sua data de nascimento:")

            reconhecer_data = input("\ncoloque a sua data de nascimento (DD/MM/AAAA):")

            verificar_data_nascimento = None
            for pessoa in login:
                if 'data_nascimento' in pessoa:
                    if pessoa['data_nascimento'] == reconhecer_data:
                        verificar_data_nascimento = pessoa
                        break
            if not verificar_data_nascimento:
                print("❌ data de nascimento não encontrado. Tente novamente.")
                continue


            while True:
                if usuario_logado2:
                    usuario_troca_senha=input(f"\nolá {usuario_logado2['apelido']} , você realmente quer trocar a sua senha(s/n):")

                    if usuario_troca_senha == 's':

                        digitar_nova_senha = input(f"\ndigite a sua nova senha {usuario_logado2['apelido']}:")
                    
                        erros2 = [] 

                        if len(digitar_nova_senha) < 8:
                            erros2.append("- Precisa ter pelo menos 8 caracteres.")
                        if not any(c.isupper() for c in digitar_nova_senha):
                            erros2.append("- Precisa conter pelo menos uma letra maiúscula.")
                        if not any(c.islower() for c in digitar_nova_senha):
                            erros2.append("- Precisa conter pelo menos uma letra minúscula.")
                        if not any(c.isdigit() for c in digitar_nova_senha):
                            erros2.append("- Precisa conter um número.")

                        if erros2:
                            print("❌ \nSenha fraca. Motivos:")
                            for erro in erros2:
                                print(erro)
                            continue  

                        
                        else:
                            print("\n✅ nova senha registrada com sucesso!")
                            usuario_logado2['senha'] = digitar_nova_senha
                            salvar_dados(ARQUIVO, login)
                            print("✅ Senha redefinida com sucesso!")
                              
                            print(f"\n| Nova Senha: {usuario_logado2['senha']}.")
                            break 
                    if usuario_troca_senha == 'n':
                        print("voltando ao menu principal.")
                        break
        elif opção == 2:

            print("\nPara recuperar a sua senha, Coloque o seu email.")

            recurepar_senha= input("\ndigite o seu email:")

            usuario_logado3 = None
            for pessoa in login:
                if 'email' in pessoa:
                    if pessoa['email'] == recurepar_senha:
                        usuario_logado3 = pessoa
                        break

            if not usuario_logado3:
                print("❌ Email não encontrado. Tente novamente.")
                continue
            
            print(f"\npara confirmar que é você {usuario_logado3['apelido']}, coloque a sua data de nascimento:")

            reconhecer_data2 = input("\ncoloque a sua data de nascimento (DD/MM/AAAA):")

            verificar_data_nascimento2 = None
            for pessoa in login:
                if 'data_nascimento' in pessoa:
                    if pessoa['data_nascimento'] == reconhecer_data2:
                        verificar_data_nascimento2 = pessoa
                        break
            if not verificar_data_nascimento2:
                print("❌ data de nascimento não encontrado. Tente novamente.")
                continue
                
            if usuario_logado3:
                
                print(f"\n A sua senha é: {usuario_logado3['senha']}.")
                continue
