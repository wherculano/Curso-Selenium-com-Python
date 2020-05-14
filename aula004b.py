from selenium.webdriver import Chrome
from time import sleep

def pegar_por_tag_e_texto(navegador, tag, texto):
    """
    Encontrar o elemento com o texto `texto`.
    Argumentos:
     - navegador = Instancia do browser [firefox, chrome, ...]
     - texto = conteúdo que deve estar na tag
     - tag = tag onde o texto será procurado
    """        
    elementos = navegador.find_elements_by_tag_name(tag)
    for elemento in elementos:
        if elemento.text == texto:
            return elemento
    

def pegar_por_href(navegador, link):
    """Encontrar o elemento `a` com o link `link`.
        Argumentos:
        - browser = Instancia do browser [firefox, chrome, ...]
        - link = link (ou parte dele) que será procurado em toda as tags `a`
    """
    elementos = chrome.find_elements_by_tag_name('a')
    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento



url = 'http://selenium.dunossauro.live/aula_04_a.html'
chrome = Chrome()
chrome.get(url)
sleep(2)

elemento_ddg_1 = pegar_por_tag_e_texto(chrome, 'a', 'DuckDuckGo')
# print(elemento_ddg_1.text) # DuckDuckGo
# print(elemento_ddg_1.get_attribute('href')) # https://ddg.gg
elemento_ddg_2 = pegar_por_href(chrome, 'ddg')
# faz a mesma coisa que o elemento_ddg_1
