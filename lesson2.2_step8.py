from selenium import webdriver
import os
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name1 = browser.find_element_by_name("firstname")
    name1.send_keys("Evgheni")

    name2 = browser.find_element_by_name("lastname")
    name2.send_keys("Duscov")

    mail = browser.find_element_by_name("email")
    mail.send_keys("xxxx@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    element = browser.find_element_by_css_selector("#file")
    element.send_keys(file_path)

    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()
finally:
    time.sleep(10)
    browser.quit()





