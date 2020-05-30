from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_tag_name("img")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    check1 = browser.find_element_by_id("robotCheckbox")
    check1.click()
    check2 = browser.find_element_by_id("robotsRule")
    check2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
