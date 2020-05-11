"""
Faça um programa que peça 2 numeros inteiros e um numero float.
Calcule e mostr:
* O produto do dobro do primeiro com a metade do segundo
* A soma do triplo do primeiro com o terceiro
* O terceiro elevado ao cubo
"""

a = int(input('1º número: '))
b = int(input('2º número: '))
c = float(input('3º número: '))

item_1 = (a*2) * (b/2)
item_2 = (a*3) + c
item_3 = c**3

print(f'O produto do dobro de {a} com a metade de {b} = {item_1}')
print(f'A soma do triplo de {a} com {c} = {item_2}')
print(f'{c} elevado ao cubo = {item_3}')
