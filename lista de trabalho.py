

lista = {
    1: "- cadastrar livro",
    2: "- exibir todos os livros",
    3: "- buscar por autor",
    4: "- emprestar livro",
    5: "- devolver livro",
    6: "- sair"
}

livros = []
alugados = []

while True:
    print("\nEscolha uma opção:")

    for numero, item in lista.items():
        print(f"{numero}: {item}")

    try:
        escolha = int(input("Escolha um número: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if escolha == 6:
        print("Saindo do sistema...")
        break

    elif escolha == 1:
        tit = input("Digite o título: ")
        aut = input("Digite o nome do autor: ")
        ano = input("Digite o ano: ")
        quantidade = int(input("Digite a quantidade: "))
        
        

        pessoa = {'tit': tit, 'autor': aut, 'ano': ano, 'quantidade': quantidade}
        livros.append(pessoa)

        print("\nLivro cadastrado com sucesso!")
        print(f"Título: {pessoa['tit']} | Autor: {pessoa['autor']} | Ano: {pessoa['ano']} | Quantidade: {pessoa['quantidade']}")

    elif escolha == 2:
        if not livros:
            print("Nenhum livro cadastrado ainda.")
        else:
            print("\nEsses são todos os livros cadastrados:")
            for idx, livro in enumerate(livros, start=1):
                print(f"{idx}. Título: {livro['tit']} | Autor: {livro['autor']} | Ano: {livro['ano']} | Quantidade: {livro['quantidade']}")
    elif escolha == 3:
        autor= input("digite o nome do autor:")

        livros_autor = [livro for livro in livros if livro ['autor'] == autor]

        if not livros_autor:
            print("Nenhum livro cadastrado sobre esse autor.")
    
        print("\nEsses são os livros cadastrados por esse autor:")

        for idx, livro in enumerate(livros_autor, start=1):
            print(f"{idx}. Título: {livro['tit']} | Autor: {livro['autor']} | Ano: {livro['ano']} | Quantidade: {livro['quantidade']}")
    elif escolha == 4:       
        emprestar = input("digite o nome do livro:")

        emprestar_livro = [livro for livro in livros if livro ['tit'] == emprestar]

        if not emprestar_livro:
            print("Nenhum livro cadastrado sobre esse titulo.")

        print("\nesses são o/s livros cadastrados com esse titulo:")
        for idx, livro in enumerate(emprestar_livro, start=1):
            print(f"{idx}. Título: {livro['tit']} | Autor: {livro['autor']} | Ano: {livro['ano']} | Quantidade: {livro['quantidade']}")

        alugar = input("deseja pegar emprestado este livro(s/n):")
        if alugar == 's':
             for livro in emprestar_livro:
                if livro['quantidade'] > 0:
                    livro['quantidade'] -= 1
                    alugados.append(livro.copy())
                    print(f"Título: {livro['tit']} | Autor: {livro['autor']}| Ano: {livro['ano']} | emprestado!")
        else:
            print(f"O livro '{livro['tit']}' não está disponível para empréstimo.")
            continue
        
    elif escolha == 5:
        if not alugados:
            print("Nenhum livro foi emprestado.")
        else:
            print("Livros emprestados:")
            for idx, livro in enumerate(alugados, start=1):
                print(f"{idx}. Título: {livro['tit']} | Autor: {livro['autor']} | Ano: {livro['ano']}")

            devolver = input("Digite o título do livro que você quer devolver: ")

       
            livros_para_devolver = [livro for livro in alugados if livro['tit'] == devolver]

            if not livros_para_devolver:
                print("Nenhum livro emprestado com esse título.")
            else:
                for livro in livros_para_devolver:
               
                    for l in livros:
                        if l['tit'] == livro['tit']:
                            l['quantidade'] += 1
                            
                    alugados.remove(livro)
                    print(f"O livro '{livro['tit']}' foi devolvido com sucesso.")
    else:
        print("Opção inválida, tente novamente.")
        
    


    




