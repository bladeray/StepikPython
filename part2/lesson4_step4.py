import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
browser.find_element_by_id("book").click()

element_x = browser.find_element_by_id("input_value").text

browser.find_element_by_id("answer").send_keys(func(element_x))

browser.find_element_by_id("solve").click()

time.sleep(10)
