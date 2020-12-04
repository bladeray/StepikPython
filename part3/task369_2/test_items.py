import time

import pytest
from selenium import webdriver
import selenium.common.exceptions as exceptions



def test_should_be_add_to_basket_button(browser):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    button = None
    try:
        button = browser.find_element_by_css_selector('button.btn-add-to-basket')
    except exceptions.NoSuchElementException:
        assert button is not None, "Should be a 'add-to-basket' button"
