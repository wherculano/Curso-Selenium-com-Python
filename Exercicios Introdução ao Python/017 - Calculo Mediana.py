"""
Faça um programa, com uma funçao, que calcula a mediana de uma lista.
funçoes embutidas que podem ajudar:
	* sorted(lista)
>>> mediana([3,1,8])
3
>>> mediana([6,4,7,2])
5
>>> mediana([6,7,2,1,8])
6
"""

def mediana(lista):
	lista.sort()
	meio = len(lista)//2
	if len(lista)%2==0:
		return (lista[meio]+lista[meio-1])//2
	else:
		return lista[meio]

lst = [3,2,4,1]
print(mediana(lst))
