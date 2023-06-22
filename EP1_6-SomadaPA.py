#EP1_6
"""
Faça um programa que calcula a soma dos termos de uma Progressão Aritmética (PA) finita.
Seu programa irá receber o primeiro termo da progressão, a1
, a razão da progressão, r
, e o número de termos, n
. Então, calcule e imprima a soma dos termos de a1
 até an
.

"""
a1=2
a2=4
a3=6
r=a3-a2
n=4

an=a1+((n-1)*r)
sn=(n*(a1+an))/2
print("a soma dos termos de uma PA é igual a : {}".format(sn))