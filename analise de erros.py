peso = float(input("digite o seu peso(Kg):"))
altura = float(input("digite a sua altura:"))


def condiçao():

    Imc = peso / altura**2
    print(f"Seu IMC é: {Imc:.2f}")

    if Imc <=18:
        print("sua condiçao: abaixo do peso.")
    elif 18.5 <= Imc < 25.0:
        print("sua condiçao: peso ideal")
    elif 25.0 <= Imc < 30.0:
        print("sua condiçao: sobrepeso")
    elif 30.0<=Imc <= 35.0:
        print("sua condiçao: obsidade grau I")
    elif 35.0 <=Imc <= 40.0:
        print("sua condiçao: obsidade grau II")
    else:
        print("sua condiçao: obsidade grau III")
condiçao()