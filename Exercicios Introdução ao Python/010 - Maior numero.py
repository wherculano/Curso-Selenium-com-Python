"""
Faça um programa que leia 5 numeros e informe o maior
"""
numeros = [int(input(f'Digite o {num}º numero: ')) for num in range(1,6)]
print(f'O maior número digitado foi: {max(numeros)}')
