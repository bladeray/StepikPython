import os
import time

from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

firstName = browser.find_element_by_name("firstname")
firstName.send_keys("Eugene")

lastName = browser.find_element_by_name("lastname")
lastName.send_keys("Sukhikh")

email = browser.find_element_by_name("email")
email.send_keys("raycut@yandex.ru")

file = browser.find_element_by_id("file")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
file.send_keys(file_path)

button = browser.find_element_by_css_selector("button")
button.click()

time.sleep(10)

