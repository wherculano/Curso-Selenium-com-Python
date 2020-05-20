from selenium.webdriver import Chrome
from time import sleep

chrome = Chrome()
url = 'https://selenium.dunossauro.live/aula_05_c.html'
chrome.get(url)
sleep(2)


def melhor_filme(navegador, filme='Nome do Filme', email='example@domain.com', telefone='(xx)xxxx-xxxx'):
    """Preenche o formulario do melhor filme de 2020"""
    navegador.find_element_by_name('filme').send_keys(filme)
    navegador.find_element_by_name('email').send_keys(email)
    navegador.find_element_by_name('telefone').send_keys(telefone)
    navegador.find_element_by_name('enviar').click()


melhor_filme(chrome, 'Matrix', 'w@gn.er','(99)98765-4321')
