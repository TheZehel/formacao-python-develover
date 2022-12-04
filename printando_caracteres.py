# recebendo input do tipo string
letra = input('Insira uma palavra: ')
print("String Original: ", letra)

#recebendo o cumprimento da string
tamanho = len(letra)

#iterar cada caractere de uma string
# start: 0 para começar com o primeiro caractere
# stop: tamanho-1 porque o índice começa com 0
# passo: 2 para obter os caracteres presentes no mesmo índice como 0, 2, 4

print("Mostrando apenas caracteres de indice par")
for i in range(0, tamanho - 1, 2):
    print("Index[", i, "]", letra[i])
