import json
import os

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
produto = carregar_dados(ARQUIVO)

lista_h ={

    1: "- cadastrar produto",
    2: "- atualizar estoque",
    3: "- remover produto",
    4: "- consultar produto",
    5: "- lista de todos produtos ",
    0:   "-sair",
}
produto = []

if os.path.exists("dados.json"):
    with open("dados.json", "r") as f:
        try:
            produto = json.load(f)
            if not isinstance(produto, list):
                produto = []
        except json.JSONDecodeError:
            produto = []
print("Bem-vindo ao Sistema de Estoque!")

while True:
    for prod,est in lista_h.items():
        print(f"{prod} {est}")

    try:
        pergunta = int(input ("escolha uma opção:"))
    except ValueError:
        print("digite a opção certa.")
        continue
    
    if pergunta == 0:
        print("fechando o sistema...")
        break
    elif pergunta == 1:
        nome=input("digite o nome do produto:")
        codigo_do_produto=int(input("digite o codigo do produto:"))
        quantidade=int(input("digite a quantidade do produto:"))
        preço_unitario=float(input("digite o preço unitario do produto(R$):"))

        dados ={'nome':nome, 'codigo_do_produto':codigo_do_produto, 'quantidade':quantidade, 'preço_unitario':preço_unitario}
        produto.append(dados)

        salvar_dados(ARQUIVO,produto)
        
        print("cadastro feito com sucesso!!.")
        print(f"nome do produto:{dados['nome']} -- codigo do produto:{dados['codigo_do_produto']} --"
              f"quantidade:{dados['quantidade']} -- preço unitario:{dados['preço_unitario']}")

    elif pergunta == 2:
        listal ={

            6: "- Entrada de mercadoria (aumentar a quantidade)",
            7: "- saida de mercadoria(diminuir a quantidade)",
            8: "- sair"
        }

        print("escolha uma dessas opções:")
        for produt,estes in listal.items():
            print(f"{produt} {estes}")
        try:
            estoque=int(input("digite uma dessas opções:"))
        except ValueError:
            print("opção invalida!!.")
            continue
        if estoque in [6,7]:
            print ("essas são as mercadorias:")

            for idx, produ in enumerate(produto, start=1):
                print(f"{idx}. nome do produto:{produ['nome']} -- codigo do produto:{produ['codigo_do_produto']} --"
                      f"quantidade:{produ['quantidade']} -- preço unitario:{produ['preço_unitario']}")


            mercadoria=input("digite o nome da mercadoria:")

            encontrado = False
            for produ in produto:
                if produ['nome'].lower() == mercadoria.lower():
                    encontrado = True
                    try:
                        qtd = int(input("Digite a quantidade: "))
                    except ValueError:
                        print("Quantidade inválida!")
                        continue

                    if estoque == 6:  
                        produ['quantidade'] += qtd
                        print("Entrada de mercadoria realizada com sucesso!")
                    elif estoque == 7: 
                        if produ['quantidade'] >= qtd:
                            produ['quantidade'] -= qtd
                            print("Saída de mercadoria realizada com sucesso!")
                        else:
                            print("Quantidade insuficiente em estoque!")
                   
                    salvar_dados(ARQUIVO,produto)
                    continue
            if not encontrado:
                print("Produto não encontrado!")

            

        if estoque == 8:
            print("voltando pro menu")
            
        continue
    elif pergunta == 3:
        print("essas são as mercadorias:")

        for idx, produ in enumerate(produto, start=1):
            print(f"{idx}. nome do produto:{produ['nome']} -- codigo do produto:{produ['codigo_do_produto']} --"
                      f"quantidade:{produ['quantidade']} -- preço unitario:{produ['preço_unitario']}")

        remove_p = input("selecione qual produto você quer remover(digite o nome):")       

        encontrado = False
        for produ in produto:
            if produ['nome'].lower() == remove_p.lower():
                encontrado = True
                
                certeza = input("você tem certeza(s/n):")
               
                if certeza == 's':
                    produto.remove(produ)
                    salvar_dados(ARQUIVO,produto)
                    print("produto removido com sucesso!!.")
                elif certeza == 'n':
                    print("saindo do sistema de remover produto.")
                    continue

        if not encontrado:
            print("Produto não encontrado!")

        

    elif pergunta == 4:

        lista_consultar_produto ={

            9: "- por código",
            10: "- listar todos",
            11: "- sair"
        }
        print("você quer consultar os produtos por:")
        for consult,produtcs in lista_consultar_produto.items():
            print(f"{consult} {produtcs}")

        try:
            estoque_consult=int(input("digite uma dessas opções:"))
        except ValueError:
            print("opção invalida!!.")
            continue

        if estoque_consult == 9:
            try:
                codigo = int(input("digite o codigo do produto:"))
            except ValueError:
                print("codigo invalido! dever ser um numero.")

            encontrado = False
            for produ in produto:
                if produ['codigo_do_produto'] == codigo:
                    encontrado = True
                    try:
                        print("este é o produto:")
                        print(f" nome do produto:{produ['nome']} -- codigo do produto:{produ['codigo_do_produto']} --"
                                        f"quantidade:{produ['quantidade']} -- preço unitario:{produ['preço_unitario']}")

                    except ValueError:
                        print("codigo invalido!")
                        continue
                
        if estoque_consult == 10:

            print("esses são todos os produtos disponíveis:")

            for idx, produ in enumerate(produto, start=1):
                print(f"{idx}. nome do produto:{produ['nome']} -- codigo do produto:{produ['codigo_do_produto']} --"
                      f"quantidade:{produ['quantidade']} -- preço unitario:{produ['preço_unitario']}")

        if estoque_consult == 11:
            print("voltando ao menu principal.")
            continue

    elif pergunta == 5:
        print("esses são todos os produtos disponíveis:")

        for idx, produ in enumerate(produto, start=1):
                print(f"{idx}. nome do produto:{produ['nome']} -- codigo do produto:{produ['codigo_do_produto']} --"
                      f"quantidade:{produ['quantidade']} -- preço unitario:{produ['preço_unitario']}")

        