from selenium.webdriver import Chrome
from time import sleep
from urllib.parse import urlparse
import json



chrome = Chrome()
url = 'https://selenium.dunossauro.live/exercicio_04.html'
chrome.get(url)
sleep(5)

def preencher_formulario(navegador, nome, email, senha, telefone):
    navegador.find_element_by_name('nome').send_keys(nome)
    navegador.find_element_by_name('email').send_keys(email)
    navegador.find_element_by_name('senha').send_keys(senha)
    navegador.find_element_by_name('telefone').send_keys(telefone)
    navegador.find_element_by_name('btn').click()


dados = {
    'nome':'Wagner',
    'email':'wag@ner.com',
    'senha':'123456',
    'telefone':'(00)00000-0000',
}

dict_elementos = {
    '%40':'@',
    '%28':'(',
    '%29':')'
}

dict_url = {}

preencher_formulario(chrome,**dados)
sleep(5)

url_parseada = urlparse(chrome.current_url)
list_query = url_parseada.query.split('&')

for texto in list_query:
    atributo, valor = texto.split('=')
    if atributo != 'btn':
        dict_url[atributo] = valor

for cod, decod in dict_elementos.items():
    for chave, valor in dict_url.items():
        dict_url[chave] = valor.replace(cod, decod)

textarea = chrome.find_element_by_tag_name('textarea')
dict_text = json.loads(textarea.text.replace('\'','\"'))

assert dict_text == dict_url
