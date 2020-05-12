"""
Crie um programa com Selenium que:
    Jogue o jogo
    Quando você ganhar, o script deve parar de ser executado
"""
from selenium.webdriver import Chrome
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html#'

chrome = Chrome()
chrome.get(url)

sleep(2)

valor_esperado = chrome.find_elements_by_tag_name('p')[-1].text

clique = chrome.find_element_by_id('ancora')
clique.click()

valor_buscado = chrome.find_elements_by_tag_name('p')[-1].text

while True:
    if valor_buscado[-1] == valor_esperado[-1]:
        print('Achei o valor!')
        chrome.quit()
        break
    clique.click()
    valor_buscado = chrome.find_elements_by_tag_name('p')[-1].text
