from selenium.webdriver import Chrome
from time import sleep


def answer(browser, command):
    input_type = browser.find_element_by_class_name("input-strobe")
    input_type.send_keys(command)
    browser.find_element_by_class_name("enter-button").click()
    sleep(2)


url = "https://flukeout.github.io/"
chrome = Chrome()
chrome.get(url)
sleep(2)

#1 Select the plates
answer(chrome, "plate")

#2 Select the bento boxes
answer(chrome, "bento")
