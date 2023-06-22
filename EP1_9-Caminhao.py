caixa = int(input('Digite o valor que deseja sacar: R$ '))
n50 = n20 = n10 = n1 = 0
while True:
    if caixa >= 500:
        caixa -= 500
        n50 += 1
    else:
        if caixa >= 100:
            caixa -= 100
            n20 += 1
        else:
            if caixa >= 25:
                caixa -= 25
                n10 += 1
            else:
                if caixa >= 1:
                    caixa -= 1
                    n1 += 1
    if caixa == 0:
        break
print(f'{n50} Quantidade de caixas de 500kg')
print(f'{n20} Quantidade de caixas de 100kg')
print(f'{n10} Quantidade de caixas de 25kg')
print(f'{n1} Quantidade de caixas de 1kg')