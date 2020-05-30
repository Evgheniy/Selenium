from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select





try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a_element = browser.find_element_by_id("num1")
    a = a_element.text

    b_element = browser.find_element_by_id("num2")
    b = b_element.text

    list1 = browser.find_element_by_id("dropdown")
    list1.click()

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(int(a)+int(b)))  # ищем элемент с текстом "Python"



    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
