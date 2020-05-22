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
* Busca exatamente tudo

Para selecionar por lista, basta separar a busca por ,(virgula) e 
é possivel fazer combinações de seletores.
    navegador.find_elements_by_css_selector('label[for],*[type]='t'])
Encontrará qualquer tag LABEL que contenha o atributo FOR, juntamente a 
quaisquer tags (*) que tenha o atributo TYPE com o valor que termine em T
"""
chrome = Chrome()
url = 'https://selenium.dunossauro.live/aula_06_a.html'
chrome.get(url)
sleep(2)

# Buscando pelo atributo TYPE de forma exata (=)
# nome = chrome.find_element_by_css_selector('[type="text"]')
# nome.send_keys('Wagner')
# senha = chrome.find_element_by_css_selector('[type="password"]')
# senha.send_keys('123456')
# btn = chrome.find_element_by_css_selector('[type="submit"]')
# btn.click()

# Buscando pelo atributo NAME de forma exata (=)
# nome = chrome.find_element_by_css_selector('[name="nome"]')
# nome.send_keys('Wagner')
# senha = chrome.find_element_by_css_selector('[name="senha"]')
# senha.send_keys('123456')
# btn = chrome.find_element_by_css_selector('[name="l0c0"]')
# btn.click()

# Buscando pelo atributo NAME de forma que contenha a palavra (*=)
# nome = chrome.find_element_by_css_selector('[name*="ome"]')
# nome.send_keys('Wagner')
# senha = chrome.find_element_by_css_selector('[name*="nha"]')
# senha.send_keys('123456')
# btn = chrome.find_element_by_css_selector('[name*="l0"]')
# btn.click()

# Buscando pelo atributo NAME com a palavra exata (|=)
# nome = chrome.find_element_by_css_selector('[name|="nome"]')
# nome.send_keys('Wagner')
# senha = chrome.find_element_by_css_selector('[name|="senha"]')
# senha.send_keys('123456')
# btn = chrome.find_element_by_css_selector('[name|="l0c0"]')
# btn.click()

# Buscando pelo atributo NAME que se inicia com a palavra (^=)
nome = chrome.find_element_by_css_selector('[name^="n"]')
nome.send_keys('Wagner')
senha = chrome.find_element_by_css_selector('[name^="s"]')
senha.send_keys('123456')
btn = chrome.find_element_by_css_selector('[name^="l"]')
btn.click()