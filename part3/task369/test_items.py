import time


def test_add_to_card_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    time.sleep(30)

    button = browser.find_element_by_css_selector("button.btn-add-to-basket")

    assert button is not None
