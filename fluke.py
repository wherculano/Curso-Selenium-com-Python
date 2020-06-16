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
answer(chrome,"plate apple")

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

#13 Select the pickles beside the bento
# O correto seria "bento ~ pickle", mas o input não reconheceu o ~ 
answer(chrome,"bento + pickle.small, pickle.small + pickle")

#14 Select the apple directly on a plate
answer(chrome,"plate > apple")

#15 Select the top orange
answer(chrome,"orange:first-child")

#16 Select the apple and the pickle on the plates
answer(chrome,"plate apple:only-child, plate pickle:only-child")

#17 Select the small apple and the pickle
answer(chrome,"apple:only-child, pickle.small")

#18 Select the 3rd plate
answer(chrome,"plate:nth-child(3)")

#19 Select the 1st bento
answer(chrome,"bento:nth-last-child(3)")

#20 Select first apple
answer(chrome,"apple:first-of-type")

#21 Select all even plates
answer(chrome,"plate:nth-of-type(even)")

#22 Select every 2nd plate, starting from the 3rd
answer(chrome, "plate:nth-of-type(2n+3)")

#23 Select the apple on the middle plate
answer(chrome, "plate apple.small:only-of-type")

#24 Select the last apple and orange
answer(chrome, "orange:last-of-type, apple:last-of-type")

#25 Select the empty bentos
answer(chrome, "bento:empty")

#26 Select the big apples
answer(chrome, "apple:not(.small)")
