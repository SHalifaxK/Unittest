from selenium import webdriver
import time

#firefox selain objecti
selain = webdriver.Firefox()
#haetaan googlen suomen sivut
selain.get("http://www.google.fi")
#haetaan elementti nimen perusteella (hakukentta)
hakukentta = selain.find_element_by_name("q")
#kirjoitetaan hakukenttaan Selenium
hakukentta.send_keys("Selenium")
#Simuloidaan enterin painallusta
hakukentta.submit()
'''odotetaan 10s muuten selain ei löydä elementtia r ja ohjelma tuottaa vaaria tuloksia, 
elementin haku tapahtuu sleepin jalkeen'''
time.sleep(10)
tulokset = selain.find_elements_by_class_name("r") # find_elements_by_class_name palauttaa listan
#tulostetaan vielä yhden sivun haun tulosten maara
print len(tulokset)

# Parenpi vaihtoehto
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://www.google.fi")
elem = driver.find_element_by_name("q")
elem.send_keys("Selenium")
elem.submit()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "r"))
    )
    el = driver.find_elements_by_class_name("r")
    print len(el)
finally:
    driver.quit()
'''
