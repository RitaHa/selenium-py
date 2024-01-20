from elements.locators import GoogleResultPageLocators
from elements.pages.base_page import BasePage


class GoogleResultPage(BasePage):

    def result_link_titles(self):
        links = self.driver.find_elements(*GoogleResultPageLocators.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.driver.find_element(*GoogleResultPageLocators.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.driver.title
