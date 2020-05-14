from selenium.webdriver import Chrome
from urllib.parse import urlparse

chrome = Chrome()
url = 'http://selenium.dunossauro.live/aula_04_a.html'
chrome.get(url)

url_parseada = urlparse(chrome.current_url)
print(url_parseada.scheme) # https
print(url_parseada.netloc) # selenium.dunossauro.live
print(url_parseada.path) # aula_04_a.html
