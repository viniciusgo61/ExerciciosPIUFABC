"""
Exercite a formatação de saídas. 
Seu programa irá receber 3 valores, 
então deverá imprimir o primeiro formatado 
com nenhuma casa decimal, o segundo com duas casas e o terceiro 
com três casas, seguindo o mesmo estilo da saída de exemplo.

"""
a=2
b=1.41421
c=3.14159

print("primeiro numero = {}".format(a))
print("{:.2f} eh o segundo numero".format(b))
print("Finalmente {:.3f} eh o terceiro numero".format(c))