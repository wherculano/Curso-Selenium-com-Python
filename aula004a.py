from selenium.webdriver import Chrome
from time import sleep

chrome = Chrome()
url = 'http://selenium.dunossauro.live/aula_04_a.html'
chrome.get(url)
sleep(2)

lista_nao_ordenada = chrome.find_element_by_tag_name('ul') # 1
li = lista_nao_ordenada.find_elements_by_tag_name('li') # 2
li[0].find_element_by_tag_name('a').text # 3
"""
1. buscamos `ul`
2. buscamos todos `li`
3. No primeiro `li`, buscamos `a` e pegamos o seu texto
ul
    li
        a
            DuckDuckGo
    li
        a
            Google
"""
