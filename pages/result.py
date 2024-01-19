from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class GoogleResultPage(BasePage):
    RESULT_LINKS = (By.CSS_SELECTOR, 'div[class="MjjYud"] > div:not([data-initq]) a > h3')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'textarea[type=search]')

    def result_link_titles(self):
        links = self.driver.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.driver.title
