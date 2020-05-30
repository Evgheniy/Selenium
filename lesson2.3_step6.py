from selenium import webdriver
import math
import time

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("trollface.btn.btn-primary")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(math.log(abs(12*math.sin(int(x))))))

    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

finally:
    time.sleep(10)
    browser.quit()






