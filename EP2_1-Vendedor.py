"""

Uma empresa contratou diversos vendedores. Para cada um deles, a empresa paga um salário fixo mais 20% de comissão sobre o total de vendas realizadas pelo vendedor. Por exemplo, um vendedor com salário fixo de 2000,00 e que vendeu 3500,00, receberá 2700,00 (sendo 700,00 de comissão).

Neste mês, a empresa definiu como meta que os vendedores devem vender o suficiente para pelo menos obter uma comissão de 50% de seu salário fixo. Por exemplo, para o caso do vendedor que recebe 2000,00 de salário, ele deve vender pelo menos o suficiente para obter 1000,00 de comissão.

Escreva um programa que leia o salário fixo do vendedor e o total de vendas realizadas no mês. O programa então irá imprimir o valor da comissão e o texto "Atingiu meta de vendas" (se a meta de vendas foi atingida) ou "Nao atingiu meta de vendas" (se a meta de vendas não foi atingida).

"""
SalFixo=float(input("digite o salario fixo do vendedor :"))
TotVendas=int(input("digite o total de vendas :"))
comissao=TotVendas * 0.2
m=TotVendas * (50/100)
SalTot=SalFixo + comissao
meta=0
if meta >0:
    print("{:.2f} Atingiu meta de vendas".format(SalTot))
else:
    print("{:.2f} Não atingiu meta de vendas".format(SalTot))

