import pytest
import selenium.webdriver


@pytest.fixture
def browser():
    driver = selenium.webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
