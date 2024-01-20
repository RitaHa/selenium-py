from selenium.webdriver import Keys

from elements.locators import GoogleSearchPageLocators
from elements.pages.base_page import BasePage


class GoogleSearchPage(BasePage):
    URL = 'https://www.google.com/'

    def open(self):
        self.driver.get(self.URL)

    def search(self, phrase):
        search_input = (self.driver.find_element(*GoogleSearchPageLocators.SEARCH_INPUT))
        search_input.send_keys(phrase + Keys.RETURN)

    def close_cookies_popup(self):
        cookies_popup = (self.driver.find_element(*GoogleSearchPageLocators.COOKIE_POPUP))
        accept_all_btn = (self.driver.find_element(*GoogleSearchPageLocators.ACCEPT_ALL_BTN))
        accept_all_btn.click()
        return cookies_popup.is_displayed()




