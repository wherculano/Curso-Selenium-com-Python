from selenium.webdriver import Chrome
from time import sleep

def find_by_text(browser, tag, text):
    """
    Encontrar o elemento com o texto `texto`.
    Argumentos:
     - browser = Instancia do browser [firefox, chrome, ...]
     - text = conteúdo que deve estar na tag
     - tag = tag onde o texto será procurado
    """
    elements = browser.find_elements_by_tag_name(tag)
    for element in elements:
        if text == element.text:
            return element


url = 'http://selenium.dunossauro.live/aula_04_b.html'
chrome = Chrome()
chrome.get(url)
sleep(2)

nome_das_caixas = ['um','dois','tres','quatro']
for caixa in nome_das_caixas:
    find_by_text(chrome, 'div',caixa).click()

for _ in nome_das_caixas:
    sleep(0.5)
    # Voltar no Histórico
    chrome.back()

for _ in nome_das_caixas:
    sleep(0.5)
    # Acançar no Histórico
    chrome.forward()
