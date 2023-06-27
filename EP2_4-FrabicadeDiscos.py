"""
Uma fábrica de discos voadores produz diversos modelos que são entregues para clientes na galáxia. Nesta fábrica, os discos voadores são vendidos em pacotes com três unidades. Portanto, não é possível comprar apenas um disco voador nesta fábrica. Ao solicitar os três discos voadores, devem ser especificados os modelos dos discos. Dependendo dos modelos solicitados, o prazo de entrega pode ser diferente:

Quando os três discos voadores solicitados são do mesmo modelo (tem o mesmo código), o prazo de entrega é de 5 dias;
Quando dois discos voadores são do mesmo modelo (tem o mesmo código) e o outro é de outro modelo (outro código), o prazo de entrega é de 15 dias;
Quando os três discos voadores são de modelos diferentes (três códigos diferentes), o prazo de entrega é de 30 dias.


O gerente da fábrica escreveu um programa para calcular o prazo de entrega dependendo dos modelos solicitados pelo cliente, mas faltou implementar a função/método para calcular o prazo de entrega:



"""


def obter_prazo_entrega(d1, d2, d3):
    p = 0
    if d1 == d2 == d3:
        p = 5
    elif d1 == d2 or d2 == d3 or d1 == d3:
        p = 15
    else:
        p = 30
    return p


d1 = int(input("digite o codigo do disco 1 "))
d2 = int(input("digite o codigo do disco 2 "))
d3 = int(input("digite o codigo do disco 3 "))
prazo_entrega = obter_prazo_entrega(d1, d2, d3)
print("Disco1 =", d1)
print("Disco2 =", d2)
print("Disco3 =", d3)
print("Prazo de entrega =", prazo_entrega)
