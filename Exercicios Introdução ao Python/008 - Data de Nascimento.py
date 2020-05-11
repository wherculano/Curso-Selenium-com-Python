"""
Faça um programa que receba uma data de nascimento (dd/mm/aaaa)
e imprima: 'Você nasceu em <dia> de <mês> de <ano>'
"""

dia, mes, ano = map(int, input('Data de Nascimento [dd/mm/aaaa]: ').split('/'))

print(f'Você nasceu no dia {dia} de {mes} de {ano}')
