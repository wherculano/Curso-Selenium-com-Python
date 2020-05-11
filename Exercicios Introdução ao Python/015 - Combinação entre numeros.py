"""
Faça um programa que dada a etrada de uma lista, o programa calcule
a combinatória de dois elementos e nos retorne as combinações em uma nova lista.
Entrada -> [1,2,3,4]
Saida -> [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
"""
entrada = [1,2,3,4]
saida = []

for indice_1, valor_1 in enumerate(entrada):
    for indice_2, valor_2 in enumerate(entrada):
        if indice_1 < indice_2:
            saida.append([valor_1, valor_2])

print(saida)
