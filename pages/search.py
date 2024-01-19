from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class GoogleSearchPage(BasePage):
    URL = 'https://www.google.com/'
    SEARCH_INPUT = (By.CSS_SELECTOR, 'textarea[type=search]')
    COOKIE_POPUP = (By.XPATH, '//div[h1[contains(text(), "Before you continue to Google")]]')
    ACCEPT_ALL_BTN = (By.XPATH, '//button[div[contains(text(), "Accept all")]]')

    def open(self):
        self.driver.get(self.URL)

    def search(self, phrase):
        search_input = (self.driver.find_element(*self.SEARCH_INPUT))
        search_input.send_keys(phrase + Keys.RETURN)

    def close_cookies_popup(self):
        cookies_popup = (self.driver.find_element(*self.COOKIE_POPUP))
        accept_all_btn = (self.driver.find_element(*self.ACCEPT_ALL_BTN))
        accept_all_btn.click()
        return cookies_popup.is_displayed()




