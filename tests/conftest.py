import json

import pytest
import selenium.webdriver


@pytest.fixture
def config(scope='session'):
    with open('config.json') as config_file:
        config = json.load(config_file)
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0
    return config


@pytest.fixture
def browser(config):
    if config['browser'] == 'Firefox':
        driver = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        driver = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        driver = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')
    driver.implicitly_wait(config['implicit_wait'])
    yield driver
    driver.quit()
