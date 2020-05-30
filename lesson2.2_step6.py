from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    browser.execute_script("window.scrollBy(0, 100);")

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(math.log(abs(12*math.sin(int(x))))))

    check_box = browser.find_element_by_id("robotCheckbox")
    check_box.click()

    radio_box = browser.find_element_by_id("robotsRule")
    radio_box.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
