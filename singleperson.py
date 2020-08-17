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
import time

driver = webdriver.Chrome()
driver.get('https://www.keybr.com/')

close_btn = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/a')
close_btn.click()
time.sleep(2)

for j in range(5):
    div_of_letters = driver.find_element_by_class_name('TextInput-fragment')
    all_letters_span = div_of_letters.find_elements_by_tag_name('span')
    letters = ''
    for i in all_letters_span:
        letter = i.text
        if i.get_attribute('class') == 'TextInput-item TextInput-item--special':
            letter = ' '
        letters+=letter
    if j == 0:
        div_of_letters.click()
    time.sleep(1.5)
    for i in letters:
        # div_of_letters.send_keys(i)
        actions = ActionChains(driver)
        actions.send_keys(i)
        time.sleep(0.06)
        actions.perform()


