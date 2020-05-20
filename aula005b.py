from selenium.webdriver import Chrome
from time import sleep

chrome = Chrome()
url = 'https://selenium.dunossauro.live/aula_05_b.html'
chrome.get(url)
sleep(2)

topico = chrome.find_element_by_class_name('topico')
print(topico.text)

linguagens = chrome.find_elements_by_class_name('linguagens')

# criando uma tupla com os valores H2 e P de cada DIV
for linguagem in linguagens:
    print(
            (
            linguagem.find_element_by_tag_name('h2').text,
            linguagem.find_element_by_tag_name('p').text
            )
        )
