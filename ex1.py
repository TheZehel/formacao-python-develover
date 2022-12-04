salario_recebido=float(input("\n informe o seu salario: "))
total=float(input("Informe o total dos seu gastos: "))

if(salario_recebido >=total):
    print("Seus custos estão dentro do orçamento")
else:
    print("Seus gastos estão fora do orçamento")