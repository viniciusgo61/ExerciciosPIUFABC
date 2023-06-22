#EP1_7
"""
Uma loja aplica descontos anunciando da seguinte forma: 10% + 10%.
 Ou seja, primeiro reduz o valor total em 10% e depois reduz mais 10% sobre o total já descontado.
  Escreva um programa que receba o valor de um produto e imprima o valor após o desconto 10% + 10%.

Por exemplo, para o valor 50, após o desconto, o valor será 40,50
"""

valor_total=50
desconto= valor_total * (19)/100
valor_com_desconto1 = valor_total - desconto
print("para o valor {},após o desconto, o valor será {:.2f}".format(valor_total,valor_com_desconto1))