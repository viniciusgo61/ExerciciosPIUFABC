"""
Faça um programa que calcule o conceito final de um aluno em uma disciplina. 
O programa irá receber, respectivamente, as notas de três testes, um a um, e a nota de duas provas, 
uma a uma.

A seguir, defina e imprima a Nota Final (NF)
formatada com duas casas decimais e o Conceito Final do aluno
de acordo com a definição a seguir:

NF=0.2T+0.4P1+0.4P2

T
 é a média aritmética dos três testes;
P1
 é a nota da primeira prova;
P2
 é a nota da segunda prova.


Cálculo do Conceito Final (CF)
:
9.0≤NF≤10.0⟹CF=A

7.5≤NF<9.0⟹CF=B

6.0≤NF<7.5⟹CF=C

5.0≤NF<6.0⟹CF=D

NF<5.0⟹CF=F


"""
n1 = float(input("Digite o valor da sua nota do teste 1: "))
n2 = float(input("Digite o valor da sua nota do teste 2: "))
n3 = float(input("Digite o valor da sua nota do teste 3: "))
n4 = float(input("Digite o valor da sua nota de P1 : "))
n5 = float(input("Digite o valor da sua nota de P2 : "))
t=(n1+n2+n3)/3
nf=(0.2*t)+(0.4*n4)+(0.4*n5)
print('{:.2f}'.format(nf))
if 9<=nf<=10:
    print("CF=A")
elif 7.5<= nf< 9.0:
    print("CF=B")
elif 6.0<= nf< 7.5:
    print("CF=C")
elif 5.0<=nf< 6.0:
    print("CF=D")
elif nf< 5.0:
    print("CF=F")