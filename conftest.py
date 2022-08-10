"""Prepare webdriver and browser tab opening for the autotests."""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument('--headless')

chrome_driver = webdriver.Chrome(
    options=chrome_options,
    service=Service(ChromeDriverManager().install()),
)

main_page = 'https://rioran.github.io/ru_vowels_filter/main.html'


@pytest.fixture(scope='session', autouse=True)
def start_and_quit_driver():
    """
    Open the start page before and quit webdriver after tests execution.

    Yields:
        :yield:
    """
    chrome_driver.get(main_page)
    yield
    chrome_driver.quit()
