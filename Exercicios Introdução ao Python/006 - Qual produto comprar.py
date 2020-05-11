"""
Escreva um programa que pergunte o preço de 3 produtos e informe
qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""
preco_1 = float(input('Valor do produto 1: R$'))
preco_2 = float(input('Valor do produto 2: R$'))
preco_3 = float(input('Valor do produto 3: R$'))

if preco_1 >= preco_2  and preco_1 >= preco_3:
    if preco_2 > preco_3:
        print('Melhor você comprar o produto 3')
    else:
        print('Melhor você comprar o produto 2')
elif preco_2 >= preco_1  and preco_2 >= preco_3:
    if preco_1 > preco_3:
        print('Melhor você comprar o produto 3')
    else:
        print('Melhor você comprar o produto 1')
elif preco_3 >= preco_1  and preco_3 >= preco_2:
    if preco_1 > preco_2:
        print('Melhor você comprar o produto 2')
    else:
        print('Melhor você comprar o produto 1')


