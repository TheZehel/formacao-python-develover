num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo numero: "))
num3 = float(input("digite o terceiro numero: "))

if num1 > num2:
    if num1 < num3:
        mediana =num1
    elif num2 > num3:
        mediana = num2
    else:
        mediana = num3
else:
    if num1 > num3:
        mediana = num1
    elif num2< num3:
        mediana = num2
    else:
        mediana = num3
print("Mediana= ", mediana)