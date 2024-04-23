from selenium.webdriver.common.by import By


class GoogleSearchPageLocators(object):
    SEARCH_INPUT = (By.CSS_SELECTOR, '[aria-label=Search]')
    COOKIE_POPUP = (By.XPATH, '//div[h1[contains(., "Before you continue to Google")]]')
    ACCEPT_ALL_BTN = (By.XPATH, '//button[div[contains(., "Accept all")]]')


class GoogleResultPageLocators(object):
    RESULT_LINKS = (By.CSS_SELECTOR, 'div.MjjYud > div:not([data-initq]) a > h3')
    SEARCH_INPUT = (By.CSS_SELECTOR, '[aria-label=Search]')