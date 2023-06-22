#EP1_10
"""
Escreva um programa que leia os valores VP, FN, FP e VN e então imprima o valor das métricas acurácia, precisão e sensibilidade.

"""

vp=40
fn=10
fp=15
vn=35

acuracia=(vp+vn)/(vp+vn+fp+fn)
precisao=vp/(vp+fp)
sensibilidade=vp/(vp+fn)
print('acuracia= {:.2f}'.format(acuracia))
print('precisao= {:.2f}'.format(precisao))
print('sensibilidade= {:.2f}'.format(sensibilidade))