"""
Escreva um programa que leia o valor da temperatura e mostre qual a mensagem que seria exibida. 
"""

t=float(input('digite o valor da temperatura : '))
if t<=-20:
    print('muito baixa')
elif t>-20 and t<=30:
    print('baixa')
elif t>30 and t <=200:
    print('normal')
elif t>200 and t <=250:
    print('alta')
else:
    print("muito alta")