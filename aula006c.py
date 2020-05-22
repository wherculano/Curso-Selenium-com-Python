from selenium.webdriver import Chrome
from time import sleep

chrome = Chrome()
url = 'https://selenium.dunossauro.live/aula_06_a.html'
chrome.get(url)
sleep(2)

"""
Irmaõs adjacentes (mesmo nível de hierarquia) -> A+B
Todos os irmãos adjacentes -> A~B
Filhos (a partir de uma tag, pegue seu filho) -> A>B
Descendentes (a partir de uma tag, pegue tudo oq achar) -> A B
"""

# procurando todas as DIVs com a classe from-group
divs = chrome.find_elements_by_css_selector('div.form-group')

# procurando os BRs que são "IRMÃOS" adjacentes das DIVs
irmao_br = chrome.find_elements_by_css_selector('div.form-group + br')

# procurando os BRs que são "FILHOS das DIVs
filho = chrome.find_elements_by_css_selector('div.form-group > #dentro-nome')

# procurando todas as LABELs que estão dentro do FORM
labels = chrome.find_elements_by_css_selector('form label') 

# procurando todas as DIVs irmãs adjacentes de H2
div = chrome.find_elements_by_css_selector('h2 ~ div')
