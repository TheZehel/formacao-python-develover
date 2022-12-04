def primeiro_e_ultimo_iguais(listanumeros):
    print("Pegando Lista: ", listanumeros)

    primeiro_numero = listanumeros[0]
    ultimo_numero = listanumeros[-1]

    if primeiro_numero == ultimo_numero:
        return True
    else:
        return False

numero_x = [10, 20, 30, 40, 10]
print("O resultado é: ", primeiro_e_ultimo_iguais(numero_x))

numero_y = [75, 65, 35, 75, 30]
print ("O resultado é: ", primeiro_e_ultimo_iguais(numero_y))