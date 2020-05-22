from selenium.webdriver import Chrome
from time import sleep
"""
Atributo Operador Valor
= Exatamente igual
*= Deve ocorrer em
|= Deve ser exatamente ou iniciar
^= Iniciado em
$= Terminado em
~= Um deve ser exatamemte igual
"""
chrome = Chrome()
url = 'https://selenium.dunossauro.live/aula_06_a.html'
chrome.get(url)
sleep(2)

nome = chrome.find_element_by_css_selector('input').send_keys('Wagner')
