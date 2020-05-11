"""
Faça um programa para a leitura de 2 notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
* A mensagem 'Aprovado' se a média alcançada for maior ou igual a 7;
* A mensagem 'Reprovado se a média for menor do que 7;
* A mensagem 'Aprovado com Distinção' se a média for igual a 10.
"""

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1+n2) / 2

if media == 10:
    print(f'Média: {media}\nAprovado com Distinção!')
elif media >= 7:
    print(f'Média: {media}\nAprovado!')
else:
    print(f'Média: {media}\nReprovado!')
