"""
Faça um programa, com uma funçao, que calcula a média de uma lista.
funçoes embutidas que podem ajudar:
	* len(lista)
	* sum(lista)
>>> media([1,2,3])
2.0
"""

def media(lista):
	return sum(lista)/len(lista)


lst = [1,2,3]
print(media(lst))
