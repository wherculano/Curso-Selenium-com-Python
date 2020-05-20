from selenium.webdriver import Chrome
from time import sleep
import json

chrome = Chrome()
url = 'https://selenium.dunossauro.live/aula_05.html'
chrome.get(url)
sleep(10)


def preencher_formulario(navegador, nome, email, senha, telefone):
    navegador.find_element_by_name('nome').send_keys(nome)
    navegador.find_element_by_name('email').send_keys(email)
    navegador.find_element_by_name('senha').send_keys(senha)
    navegador.find_element_by_name('telefone').send_keys(telefone)
    navegador.find_element_by_name('btn').click()

dados = {
    'nome': 'Wagner',
    'email': 'wag@ner.com', 
    'senha': '12345678', 
    'telefone': '(00)98765-4321'
}

# Passando os dados do dict para a função (** são elementos nomeados (chave:valor))
preencher_formulario(chrome,**dados)
sleep(10)

# Pegar o resultado
resultado = chrome.find_element_by_id('result').text
# Trocar as aspas simples por aspas duplas
resultado_arrumado = resultado.replace('\'', "\"")
# Transformar o resultado em um json/dict
dict_resultado = json.loads(resultado_arrumado)

# Verificando se o dict do resultado é igual aos dados enviados
assert dict_resultado == dados

