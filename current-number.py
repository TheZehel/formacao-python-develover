print("Mostrando a sequencia de numeros em um rage(10)")
numero_anterior = 0

#loop de 1 a 10
for i in range(1, 11):
    x_soma = numero_anterior + i
    print("Numero atual", i, "Numero anterior", numero_anterior, "Soma: ", x_soma)
    #mudando o numero anterior
    #definindo o numero atual
    numero_anterior = i