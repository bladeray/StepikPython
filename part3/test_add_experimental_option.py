from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)

class TestMainPage1():

    def test_guest_should_see_login_link(self):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")