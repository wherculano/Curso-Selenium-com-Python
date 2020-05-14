from selenium.webdriver import Chrome
from pprint import pprint
from time import sleep

"""
1. Pegar todos os links de aulas
    {'nome da aula': 'link da aula'}
2. Navegar até o exercício 3
    achar a url do exercício 3 e ir até lá
"""

def pegar_links(navegador, elemento):
    """
    Pega todos os links dentro de um elemento
    - browser = a instância do navegador
    - element = webelement [aside, main, body, ul, ol]
    """
    resultado = {}
    elementos = navegador.find_element_by_tag_name(elemento)
    ancoras = elementos.find_elements_by_tag_name('a')
    for a in ancoras:
        resultado[a.text] = a.get_attribute('href')
    return resultado

chrome = Chrome()
url = 'http://selenium.dunossauro.live/aula_04.html'
chrome.get(url)

"""Parte 1"""
sleep(2)
aulas = pegar_links(chrome, 'aside')
pprint(aulas)

# chrome.get(aulas['Aula 3'])  # Ir para a aula 3
# chrome.get(aulas['Aula 4'])  # Ir para a aula 4

"""Parte 2"""
exercicios = pegar_links(chrome, 'main')
pprint(exercicios)

chrome.get(exercicios['Exercício 3'])
