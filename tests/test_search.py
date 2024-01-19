import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.result import GoogleResultPage
from pages.search import GoogleSearchPage


@pytest.mark.parametrize('phrase', ['Carbonara', 'Mascarpone', 'Arancini'])
def test_google_search(browser, phrase):
    search_page = GoogleSearchPage(browser)
    result_page = GoogleResultPage(browser)
    #     Given the Google home page is displayed
    search_page.open()
    #     When the user close Cookies popup
    assert search_page.close_cookies_popup() == False
    #     When the user searches for phrase
    search_page.search(phrase)
    #     Then the search result title contains phrase
    # WebDriverWait(browser, 10).until(expected_conditions.title_contains(phrase))
    # don't Implicit Wait vs Explicit Wait
    assert phrase in result_page.title()
    #     And the search result query is phrase
    assert phrase == result_page.search_input_value()
    #     And the search result links pertain to phrase
    for title in result_page.result_link_titles():
        assert phrase.lower() in title.lower()