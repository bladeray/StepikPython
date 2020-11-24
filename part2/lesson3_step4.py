import math
import time

from selenium import webdriver


def func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_css_selector(".btn").click()

browser.switch_to.alert.accept()

element_x = browser.find_element_by_id("input_value").text

browser.find_element_by_id("answer").send_keys(func(element_x))

browser.find_element_by_css_selector(".btn").click()

time.sleep(10)
