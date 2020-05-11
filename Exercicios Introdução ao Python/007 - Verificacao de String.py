"""
Faça um programa que recebba uma string e responda se ela tem alguma vogal,
se sim, quais são? E também diga se ela é uma frase ou não.
"""
string = input('Digite alguma palavra: ')
vogais = 'aeiou'
contador_vogais = set([vog for vog in string if vog in vogais])

print(f'As vogais encontradadas foram: {contador_vogais}')
print('Provavelmente é uma frase' if ' ' in string else 'Não é uma frase')
