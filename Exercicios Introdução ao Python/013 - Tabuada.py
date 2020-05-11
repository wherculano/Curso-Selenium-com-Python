"""
Faça um programa que: Dada uma lista [1,2,3,...,9,10] e um número inteiro,
imprima a tabuada desse numero.
"""
numero = int(input('Numero: '))
lista_de_numeros = list(range(1,11))

print('#'*30)
print(f' Tabuada do {numero} '.center(30, '#'))
print('#'*30)
for num in lista_de_numeros:
    print(f'{numero} x {num} = {numero*num}')
