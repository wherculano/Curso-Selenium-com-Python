"""
Faça um programa, com uma funçao, que dado uma lista e uma posiçao da mesma,
faça o quartil dessa posição.
funçoes embutidas que podem ajudar:
	* p_index = int(p * len(lista))
>>> quartil(1, [6, 47, 49, 15, 42, 41, 7, 39, 43, 40, 36])
15
>>> quartil(2, [6, 47, 49, 15, 42, 41, 7, 39, 43, 40, 36])
40
>>> quartil(3, [6, 47, 49, 15, 42, 41, 7, 39, 43, 40, 36])
43
>>> quartil(1, [7,15,36,39,40,41])
15
>>> quartil(2, [7,15,36,39,40,41])
37.5
>>> quartil(3, [7,15,36,39,40,41])
40
"""
def quartil(indice, lista):
	lista.sort()
	tam = len(lista)
	if indice == 1:
		return lista[int(1/4*tam)]
	elif indice == 2:
		if tam % 2 == 0:
			return (lista[int(tam/2)-1] + lista[int(tam/2)])/2
		else:
			return lista[int(tam/2)]
	elif indice == 3:
		return lista[int(3/4*tam)]

entrada = [40, 41, 39, 36, 15, 7]
for i in range(1,4):
	print(quartil(i, entrada))
