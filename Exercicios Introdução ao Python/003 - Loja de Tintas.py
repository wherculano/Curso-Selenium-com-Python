"""
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
que a tinta é vendida em latas de 18 litros que custam R$80.
Informe ao usuário  a quantidade de latas de tinta a serem compradas e o preço total.
"""
from math import ceil
# o método ceil é usado para arredondar um numero para cima

metros_quadrados = float(input('Informe os metros quadrados da área a ser pintada: '))
valor_lata = 80
cobertura_por_metro_quadrado = 3
litros_na_lata = 18

quantidade_litros = metros_quadrados / cobertura_por_metro_quadrado

# caso a quantidade de latas seja um numero decimal (1.123), será arredondado para 2
quantidade_latas = ceil(quantidade_litros /litros_na_lata)

valor = valor_lata if quantidade_litros <= litros_na_lata else quantidade_latas * valor_lata 

print(f'Você precisará de {quantidade_litros:.2f} litros de tinta e isso custará R${valor:.2f}.')
