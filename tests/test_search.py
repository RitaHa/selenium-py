from pages.result import GoogleResultPage
from pages.search import GoogleSearchPage


def test_google_search(browser):
    search_page = GoogleSearchPage(browser)
    result_page = GoogleResultPage(browser)
    phrase = "Carbonara"
    #     Given the Google home page is displayed
    search_page.open()
    #     When the user close Cookies popup
    assert search_page.close_cookies_popup() == False
    #     When the user searches for "Carbonara"
    search_page.search(phrase)
    #     Then the search result title contains "Carbonara"
    assert phrase in result_page.title()
    #     And the search result query is "Carbonara"
    assert phrase == result_page.search_input_value()
    #     And the search result links pertain to "Carbonara"
    for title in result_page.result_link_titles():
        assert phrase.lower() in title.lower()