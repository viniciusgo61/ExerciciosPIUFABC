"""
Faça um programa que, dados os coeficientes a,b,c
 , resolva a equação de segundo grau:
ax2+bx+c=0


Caso a equação não tenha solução, o programa deverá exibir "Sem solucao real!" (sem utilizar acento e cedilha), seguido pelo valor de Δ
, formatado com duas casas decimais.
Caso a equação tenha solução única, o programa deverá exibir apenas essa solução, formatada com duas casas decimais.
Caso a equação tenha duas soluções, o programa deverá exibi-las em linhas separadas, em ordem crescente, formatadas com duas casas decimais.


"""
import math
print('Lembre-se: a ≠ 0 e a, b, c ∈ ℝ e quando não estiver o valor de c, ele equivale a 0, o mesmo com o valor de b')
a = int(input("Digite o valor de A"))
b = int(input("Digite o valor de B"))
c = int(input("Digite o valor de C"))
delta = (b**2 - 4*a*c)
x1 = (-b+ delta**(1.0/2.0)) / (2.0*a)
x2 = (-b- delta**(1.0/2.0)) / (2.0*a)

if delta == 0: 

    print('A raiz dessa função é {}'.format(delta))
    print('ela possui duas raizes iguais no valor de {:.2f}'.format(x1))
if delta > 0:
    print('A raiz dessa função é {}'.format(delta))
    print('\nValor de x1: {:.2f}'.format(x1))
    print('Valor de x2: {:.2f}'.format(x2))
if delta < 0:
    print('Sem solucao real !')
    print('Delta = {:.2f}'.format(delta))