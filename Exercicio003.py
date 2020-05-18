from selenium.webdriver import Chrome
from time import sleep
from urllib.parse import urlparse

def pegar_link(navegador, link):
    """
    navegador - instancia do navegador
    link - link ou parte do link que deseja buscar
    """
    main = navegador.find_element_by_id('main')
    ancora = main.find_elements_by_tag_name('a')

    for a in ancora:
        if link in a.get_attribute('href'):
            return a

def pegar_por_tag(navegador, tag):
    """
    navegador - instancia do navegador
    tag - tag a ser procurada
    """
    main = navegador.find_element_by_id('main')
    elemento = main.find_elements_by_tag_name(tag)
    return elemento


def pegar_titulo(navegador):
    """Retorna o Título da Página"""
    return navegador.title

def fazer_conta(n1, n2, operador):
    if operador == '+':
        return float(n1) + float(n2)
    elif operador == '-':
        return float(n1) - float(n2)
    elif operador == '/':
        if n2 != 0:
            return float(n1) / float(n2)
    elif operador == '*':
        return float(n1) * float(n2)

chrome = Chrome()
url = 'https://selenium.dunossauro.live/exercicio_03.html'
chrome.get(url)
sleep(2)

## HOME ##
home = pegar_link(chrome, 'page_1')
home.click()

## Pagina 1 ##
#pagina1 = pegar_link(chrome, 'page_1')
# pagina1.click()
p_pagina1 = pegar_por_tag(chrome, 'p')
n1, operador, n2, *_ = p_pagina1[1].text.split()
result_da_conta = str(fazer_conta(n1, n2, operador))
li_pagina1 = pegar_por_tag(chrome, 'li')
for texto in li_pagina1:
    a = texto.find_element_by_tag_name('a') 
    if not texto.text in result_da_conta:
        a.click()
        break
sleep(20)

## Pagina 2 ## 
#pagina2 = pegar_link(chrome, 'page_2')
# pagina2.click()
titulo = pegar_titulo(chrome)
li_pagina2 = pegar_por_tag(chrome, 'li')
for texto in li_pagina2:
    link = texto.find_element_by_tag_name('a')
    if texto.text == titulo:
        link.click()
    break
sleep(5)

## Pagina 3 ##
#pagina3 = pegar_link(chrome, 'page_3')
# pagina3.click()
pagina = urlparse(chrome.current_url)
li_pagina3 = pegar_por_tag(chrome,'li')
for texto in li_pagina3:
    ancora = texto.find_element_by_tag_name('a')
    if texto.text in pagina.path:
        ancora.click()
        break
sleep(5)

## Pagina 4 ##
chrome.refresh()
