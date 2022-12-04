def multiplication_or_sum(num1, num2):
    #calcula o produto entre dois numeros
    product = num1 * num2
    #verifica se o numero é menor ou igual a 1000
    if product <= 1000:
        return product
    else:
        #o numero é menor do que 1000, executa a soma
        return num1 + num2

#primeira condição
result = multiplication_or_sum(20, 30)
print("O resultado é", result)

#segunda condição
result = multiplication_or_sum(40, 30)
print("O resultado é", result)