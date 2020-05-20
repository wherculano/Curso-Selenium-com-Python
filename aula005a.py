from selenium.webdriver import Chrome
from time import sleep

chrome = Chrome()
url = 'https://selenium.dunossauro.live/aula_05_a.html'
chrome.get(url)
sleep(2)

div_py = chrome.find_element_by_id('python')
print(div_py.text)

div_hk = chrome.find_element_by_id('haskell')
print(div_hk.text)

chrome.quit()