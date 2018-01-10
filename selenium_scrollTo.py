'''
scrollTo is a Javascript method ie. the execute_script
syntax browser.execute_script("window.scrollTo(xpos, ypos);")
'''

import time
from selenium import webdriver

browser = webdriver.Firefox()

browser.get("https://www.labri.fr/perso/nrougier/teaching/matplotlib/")
    
browser.execute_script("window.scrollTo(0, 500);")
