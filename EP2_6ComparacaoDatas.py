"""

Escreva uma função/método para comparar duas datas. A função/método possui os parâmetros d1, m1, a1, d2, m2, a2 (números inteiros representando o dia(d), mês(m) e ano(a) da data1 e da data2) e deverá retornar um valor inteiro conforme definido a seguir:

Retorna -1 se a data1 é a mais antiga;
Retorna 0 se as duas datas são iguais;
Retorna 1 se as data2 é a mais antiga.

"""
def comparar_datas(d1, m1, a1, d2, m2, a2):
    if a1 < a2:
        return -1
    elif a1 > a2:
        return 1
    elif m1 < m2:
        return -1
    elif m1 > m2:
        return 1
    elif d1 < d2:
        return -1
    elif d1 > d2:
        return 1
    else:
        return 0
        
r=comparar_datas(5,2,2009,2,3,2010)
print(r)