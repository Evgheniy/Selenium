from selenium import webdriver
import math
import time

try:
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_id("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
