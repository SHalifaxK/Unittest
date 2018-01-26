
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import logging
logging.basicConfig(level=logging.INFO)

selain = webdriver.Firefox()
#selain.add_argument('--incognito')
selain.get('https://yle.fi/aihe/tekstitv')

try:
    WebDriverWait(selain,10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'ydd-content')))
    linkit = selain.find_elements_by_class_name('yle-ttv-link-init-processed')
    for link in linkit:
        print link.text
        
finally:
    print 'done fetching info'
	
print 'Where do you want to go? Give a page number'
page = input()
logging.info('You want to view info on page ' + str(page))
time.sleep(5)
selain.quit()
