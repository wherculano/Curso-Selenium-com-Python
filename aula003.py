# from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
from time import sleep

# firefox = Firefox()
chrome = Chrome()
url = 'https://curso-python-selenium.netlify.app/aula_03.html'

chrome.get(url)
sleep(2)
a = chrome.find_element_by_tag_name('a')

for click in range(10):
    p = chrome.find_elements_by_tag_name('p')
    a.click()    
    print(f'Valor de P: {p[-1].text} -> Valor do Click: {click}')
    print(f'Os valores de P são iguais ao Click: {p[-1].text == str(click)}')

chrome.quit()
