"""
Faça um programa que itera em uma string e toda vez que uma vogal aparecer
na sua string, print o seu nome entre elas
"""
vogais = 'aeiou'
string = 'bananas'
nome = input('Nome: ')
for letra in string:
    if letra in vogais:
        print(nome)
    else:
        print(letra)
