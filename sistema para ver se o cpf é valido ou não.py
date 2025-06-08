def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit,cpf))

    if len(cpf) !=11 or cpf == cpf[0] *11:
        return False

    soma1 = sum(int(cpf[i]) * (10-i) for i in range(9))
    digito1= (soma1 * 10) % 11
    digito1= digito1 if digito1 < 10 else 0

    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma2 * 10) % 11
    digito2 = digito2 if digito2 < 10 else 0

    return cpf[-2:]== f"{digito1}{digito2}"

cpf = (input("digite um cpf:"))

if validar_cpf(cpf):
    print("cpf valido!")
else:
    print("cpf invalido!")