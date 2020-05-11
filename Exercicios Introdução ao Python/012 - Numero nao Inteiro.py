"""
Faça um programa que receba uma string, com um número de ponto flutuante
e imprima qual a parte dele que não é inteira.
n = '3.14'
>>> 14
"""
num_decimal = input('Digite um número decimal: ').split('.')[1]
print(f'A parte não inteira do numero é {num_decimal}')
