"""
Crie um programa com selenium que:
    - Gere um dicionário, onde a chave é a tag h1:
        * O valor deve ser um novo dicionário
        * Cada chave do valor deverá ser o valor de 'atributo'
        * Cada valor deve ser o texto contido no elemento
{'H1':
    {
        'texto1':'texto',
        'texto2':'texto',
        'texto3':'texto',
    }
}
"""
from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

# Criando o 'navegador'
firefox = Firefox()
# Acessando a URL
firefox.get(url)
# Esperando 2 segundos para dar tempo da pagina carregar
sleep(2)

dct = dict()

# Pegando elemento h1
h1 = firefox.find_element_by_tag_name('h1')
dct[h1.tag_name] = {}

# Pegando todos os elementos (tag) 'p'
p = firefox.find_elements_by_tag_name('p')

for item in p:
    # Atualizando o Dicionario com uma nova chave e um novo valor
    # dct[nome do atributo] = valor do atributo
    dct[h1.tag_name].update({item.get_attribute('atributo'): item.text})

print(dct)
