import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


urls = ["https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"]


@pytest.mark.parametrize('url', urls)
def test_guest_should_see_login_link(browser, url):
    browser.get(url)

    textarea = browser.find_element_by_css_selector(".textarea")
    answer = math.log(int(time.time()))
    textarea.send_keys(answer.__str__())

    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()

    message = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert message == "Correct!"
