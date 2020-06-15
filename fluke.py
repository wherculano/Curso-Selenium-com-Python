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

#3 Select the fancy plate
answer(chrome, "#fancy")

#4 Select the apple on the plate
answer("plate apple")

#5 Select the pickle on the fancy plate
answer(chrome,"#fancy pickle" )

#6 Select the small apples
answer(chrome,"apple.small")

#7 Select the small oranges
answer(chrome,"orange.small")

#8 Select the small oranges in the bentos
answer(chrome,"bento orange.small")

#9 Select all the plates and bentos
answer(chrome,"plate, bento")

#10 Select all the things!
answer(chrome,"*")

#11 Select everything on a plate
answer(chrome,"plate *")

#12 Select every apple that's next to a plate
answer(chrome,"plate + apple")
