"""
Faça um programa que peça uma nota entre 0 e 10.
Mostre uma mensagem caso o valor seja inválido e continue pedindo
até que o usuário informe um valor válido.
"""

while True:
    numero = int(input('Digite um numero entre 0 e 10: '))
    if 0 < numero <= 10:
        print(f'Você digitou o numero: {numero}')
        break
