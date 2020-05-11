"""
Monte um dicionario com as seguintes chaves:
	lista, somatorio, maior e menor valor
"""

def dicionario(lst):
	dct = dict() #criacao do dicionario
	dct['lista'] = lst #criacao chave e valor
	dct['somatorio'] = sum(lst)
	dct['maior valor'] = max(lst)
	dct['menor valor'] = min(lst)
	return dct

lista = [1,5,2,6,8,3,7,4]
print(dicionario(lista))
	