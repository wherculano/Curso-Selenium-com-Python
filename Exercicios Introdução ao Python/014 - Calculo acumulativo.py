"""
Faça um programa que dada a entrada de uma lista
ele faça o calculo acumulativo da mesma.
Entrada - [1,2,3,4]
Saida - [1,3,6,10]
"""
entrada = [1,2,3,4]
saida = []
for item in entrada:
    soma = item
    for i in range(item):
        soma += i
    saida.append(soma)

print(saida)
