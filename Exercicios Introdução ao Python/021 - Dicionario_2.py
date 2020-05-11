"""
Dada uma lista de entradas de usuarios de numeros inteiros,
construa um dicionario com a lista padrao,a lista com os valores elevados ao quadrado e a lista dos valores elevados ao cubo.
"""
entrada = [1,5,2,4,7,8,9,3,6]

dct = {
	'lista': entrada,
	'quadrado': [n**2 for n in entrada],
	'cubo': [n**3 for n in entrada]
}

print(dct)
