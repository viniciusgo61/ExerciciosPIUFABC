#EP1_8
"""
Um determinado método para encriptar números de 4 dígitos consiste em adicionar
1 em cada dígito do número. Por exemplo:

O número 1234 ficaria 2345 após a encriptação;
O número 9092 ficaria 0103 após a encriptação
 """
entrada = 9092

milhar = (entrada%10000)//1000
centena = (entrada%1000)//100
dezena = (entrada%100)//10
unidade = entrada%10

if milhar==9:
  milhar=0
else:
  milhar += 1
if centena==9:
  centena=0;
else:
  centena += 1
if dezena==9:
  dezena=0
else:
  dezena += 1
if unidade==9:
  unidade=0
else:
  unidade += 1

print('%d%d%d%d' %(milhar, centena, dezena, unidade));