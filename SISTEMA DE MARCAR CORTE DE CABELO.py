
lista_h ={

    11: "- horario✅",
    12: "- horario✅",
    13: "- horario✅",
    14: "- horario✅",
    15: "- horario✅",
    16: "- horario✅",
    0:   "-sair",
}
lista_pessoas = []

print("Bem vindo a barbearia, esses são os horários disponiveis:")

while True:
    for temp,hora in lista_h.items():
        print(f"{temp} {hora}")
    try:
        pergunta = int(input ("escolha um desses horarios:"))
    except ValueError:
        print("digite o horario certo.")
        continue
    
    if pergunta == 0:
        print("saindo do sistema...")
        break
    elif lista_h[pergunta] == "- horário ❌":
        print("Esse horário já foi reservado. Por favor, escolha outro.")
        continue

    elif pergunta == 11:
        print ("qual você quer mandar meu chefe:")
        listas={
            1: "- corte R$ 35",
            2: "- barba R$ 25",
            3: "- pintar R$ 60",
            4: "- pézinho do cabelo R$ 15",
            0:   "-sair"

        }
        for num,preç in listas.items():
         print(f"{num} {preç}")
       
        nome = input("digite o seu nome:")
        escolha= int(input("escolha uma dessas opções:"))

        if escolha == 1:
            print(f"[corte: R$ 35] já está marcado, {nome}")
        elif escolha ==2:
                print(f"[barba: R$ 25] já está marcado, {nome}") 
        elif escolha ==3:
                print(f"[pintar: R$ 60] já está marcado ,{nome}")
        elif escolha ==4:
                print(f"[pézinho do cabelo: R$ 15] já está marcado ,{nome}")
        elif escolha ==0:
                print("saindo...")
                continue
        
        pessoa = {'nome':nome , 'escolha':escolha, 'horario':pergunta}
        lista_pessoas.append(pessoa)
        print(f" cadastrado com sucesso! {nome}")
        print(f"nome:{pessoa['nome']} | horario:{pessoa['horario']}")

        lista_h[pergunta]= "- horário ❌"

    elif pergunta ==12:
         print ("qual você quer mandar meu chefe:")
         listas={
            1: "- corte R$ 35",
            2: "- barba R$ 25",
            3: "- pintar R$ 60",
            4: "- pézinho do cabelo R$ 15",
            0:   "-sair"

        }
         for num,preç in listas.items():
          print(f"{num} {preç}")
       
         nome = input("digite o seu nome:")
         escolha= int(input("escolha uma dessas opções:"))

         if escolha == 1:
            print(f"[corte: R$ 35] já está marcado, {nome}")
         elif escolha ==2:
                print(f"[barba: R$ 25] já está marcado, {nome}") 
         elif escolha ==3:
                print(f"[pintar: R$ 60] já está marcado ,{nome}")
         elif escolha ==4:
                print(f"[pézinho do cabelo: R$ 15] já está marcado ,{nome}")
         elif escolha ==0:
                print("saindo...")
                continue
        
         pessoa = {'nome':nome , 'escolha':escolha, 'horario':pergunta}
         lista_pessoas.append(pessoa)
         print(f" cadastrado com sucesso! {nome}")
         print(f"nome:{pessoa['nome']} | horario:{pessoa['horario']}")

         lista_h[pergunta]= "- horário ❌"

    elif pergunta == 13:
         print ("qual você quer mandar meu chefe:")
         listas={
            1: "- corte R$ 35",
            2: "- barba R$ 25",
            3: "- pintar R$ 60",
            4: "- pézinho do cabelo R$ 15",
            0:   "-sair"

        }
         for num,preç in listas.items():
          print(f"{num} {preç}")
       
         nome = input("digite o seu nome:")
         escolha= int(input("escolha uma dessas opções:"))

         if escolha == 1:
            print(f"[corte: R$ 35] já está marcado, {nome}")
         elif escolha ==2:
                print(f"[barba: R$ 25] já está marcado, {nome}") 
         elif escolha ==3:
                print(f"[pintar: R$ 60] já está marcado ,{nome}")
         elif escolha ==4:
                print(f"[pézinho do cabelo: R$ 15] já está marcado ,{nome}")
         elif escolha ==0:
                print("saindo...")
                continue
        
         pessoa = {'nome':nome , 'escolha':escolha, 'horario':pergunta}
         lista_pessoas.append(pessoa)
         print(f" cadastrado com sucesso! {nome}")
         print(f"nome:{pessoa['nome']} | horario:{pessoa['horario']}")

         lista_h[pergunta]= "- horário ❌"

    elif pergunta == 14:
         print ("qual você quer mandar meu chefe:")
         listas={
            1: "- corte R$ 35",
            2: "- barba R$ 25",
            3: "- pintar R$ 60",
            4: "- pézinho do cabelo R$ 15",
            0:   "-sair"

        }
         for num,preç in listas.items():
          print(f"{num} {preç}")
       
         nome = input("digite o seu nome:")
         escolha= int(input("escolha uma dessas opções:"))

         if escolha == 1:
            print(f"[corte: R$ 35] já está marcado, {nome}")
         elif escolha ==2:
                print(f"[barba: R$ 25] já está marcado, {nome}") 
         elif escolha ==3:
                print(f"[pintar: R$ 60] já está marcado ,{nome}")
         elif escolha ==4:
                print(f"[pézinho do cabelo: R$ 15] já está marcado ,{nome}")
         elif escolha ==0:
                print("saindo...")
                continue
        
         pessoa = {'nome':nome , 'escolha':escolha, 'horario':pergunta}
         lista_pessoas.append(pessoa)
         print(f" cadastrado com sucesso! {nome}")
         print(f"nome:{pessoa['nome']} | horario:{pessoa['horario']}")

         lista_h[pergunta]= "- horário ❌"
    
    elif pergunta == 15:
        print ("qual você quer mandar meu chefe:")
        listas={
            1: "- corte R$ 35",
            2: "- barba R$ 25",
            3: "- pintar R$ 60",
            4: "- pézinho do cabelo R$ 15",
            0:   "-sair"

        }
        for num,preç in listas.items():
         print(f"{num} {preç}")
       
        nome = input("digite o seu nome:")
        escolha= int(input("escolha uma dessas opções:"))

        if escolha == 1:
            print(f"[corte: R$ 35] já está marcado, {nome}")
        elif escolha ==2:
                print(f"[barba: R$ 25] já está marcado, {nome}") 
        elif escolha ==3:
                print(f"[pintar: R$ 60] já está marcado ,{nome}")
        elif escolha ==4:
                print(f"[pézinho do cabelo: R$ 15] já está marcado ,{nome}")
        elif escolha ==0:
                print("saindo...")
                continue
        
        pessoa = {'nome':nome , 'escolha':escolha, 'horario':pergunta}
        lista_pessoas.append(pessoa)
        print(f" cadastrado com sucesso! {nome}")
        print(f"nome:{pessoa['nome']} | horario:{pessoa['horario']}")

        lista_h[pergunta]= "- horário ❌"
    
    elif pergunta == 16:
        print ("qual você quer mandar meu chefe:")
        listas={
            1: "- corte R$ 35",
            2: "- barba R$ 25",
            3: "- pintar R$ 60",
            4: "- pézinho do cabelo R$ 15",
            0:   "-sair"

        }
        for num,preç in listas.items():
         print(f"{num} {preç}")
       
        nome = input("digite o seu nome:")
        escolha= int(input("escolha uma dessas opções:"))

        if escolha == 1:
            print(f"[corte: R$ 35] já está marcado, {nome}")
        elif escolha ==2:
                print(f"[barba: R$ 25] já está marcado, {nome}") 
        elif escolha ==3:
                print(f"[pintar: R$ 60] já está marcado ,{nome}")
        elif escolha ==4:
                print(f"[pézinho do cabelo: R$ 15] já está marcado ,{nome}")
        elif escolha ==0:
                print("saindo...")
                continue
        
        pessoa = {'nome':nome , 'escolha':escolha, 'horario':pergunta}
        lista_pessoas.append(pessoa)
        print(f" cadastrado com sucesso! {nome}")
        print(f"nome:{pessoa['nome']} | horario:{pessoa['horario']}")

        lista_h[pergunta]= "- horário ❌"
    
    
    

    
    
        





    
        