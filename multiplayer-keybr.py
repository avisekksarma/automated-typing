import logging
logger = logging.getLogger(__name__)
filehandler = logging.FileHandler('selenium-test.log')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(lineno)d:%(name)s:%(message)s')
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()
driver.get('https://www.keybr.com/')

close_btn = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/a')
close_btn.click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/nav/div/div[6]/a').click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "Ticker"))
    )
except:
    logger.info('Selenium quitted due to timeout.')
    driver.quit()

for j in range(2):
    while True:
        if element.text == 'GO!':
            logger.info(j)
            break
    
    div_of_letters = driver.find_element_by_class_name('TextInput-fragment')
    all_letters_span = div_of_letters.find_elements_by_tag_name('span')
    letters = ''
    for k in all_letters_span:
        letter = k.text
        if k.get_attribute('class') == 'TextInput-item TextInput-item--special':
            letter = ' '
        letters+=letter
    logger.info(j)
    logger.info(letters)
    for i in letters:
        # div_of_letters.send_keys(i)
        actions = ActionChains(driver)
        actions.send_keys(i)
        time.sleep(0.01)
        actions.perform()
    logger.info(j)
    time.sleep(2.5)

