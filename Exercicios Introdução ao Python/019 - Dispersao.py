"""
Faça um programa, com uma funçao, que calcule a dispersão (amplitude) de uma lista.
funçoes embutidas que podem ajudar:
	* min(lista)
	*max(lista)
	
>>> dispersao([5,7,6,9])
4
"""
def dispersao(iteravel):
	return max(iteravel) - min(iteravel)

entrada = [5,7,6,9]
print(dispersao(entrada))
