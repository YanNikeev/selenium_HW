"""Test the functionality of all buttons on the main page."""
import random
import pytest
from conftest import chrome_driver
from defaults import Defaults
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from string import digits, punctuation

CONSONANTS = 'аеёиоуыэюя'
ALPHABET = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
RANDOM_LENGTH = 150


def expected_text(text: str, add_chars=''):
    """
    Convert input text into expected shortened version.

    Parameters:
        add_chars: chars that could be in the expected data
        text: text for editing
    Returns:
        return: shortened text
    """
    return ''.join([
        char for char in text.lower()
        if char in CONSONANTS + add_chars or char == '\n'
    ])


@pytest.fixture(scope='function', autouse=True)
def new_tab():
    """
    Update the browser tab.

    Yields:
        yield: new tab in browser
    """
    yield
    chrome_driver.refresh()


@pytest.fixture
def buttons():
    """
    Return all the buttons on the page except selection button.

    Returns:
        return: buttons objects
    """
    return [
        item for item in chrome_driver.find_elements(By.XPATH, '//button')
        if item.text != 'Выделить результат'
    ]


def test_buttons_default_data(buttons):
    """
    Check the buttons' functionality using the predefined data.

    Parameters:
        buttons: contains buttons objects (except selection button)
    """
    text = Defaults.input_text
    for button in buttons:
        if button.text == 'Оставить только гласные':
            expected = expected_text(text)
        elif button.text == 'Ну и ещё пробелы':
            expected = expected_text(text, ' ')
        elif button.text == 'Оставить ещё и .,-!?':
            expected = expected_text(text, ' .,-!?')
        button.click()
        actual = chrome_driver.find_element(By.ID, 'text_output').text
        assert actual == expected


def test_buttons_random_data(buttons):
    """
    Check the buttons' functionality using some random data.

    Parameters:
        buttons: contains buttons objects (except selection button)
    """
    random_text = ''.join(random.choices(
        ALPHABET + ALPHABET.upper() + digits + punctuation + '   ' + '\n', k=RANDOM_LENGTH)
    )
    chrome_driver.find_element(By.ID, 'text_input').clear()
    chrome_driver.find_element(By.ID, 'text_input').send_keys(random_text)
    for button in buttons:
        if button.text == 'Оставить только гласные':
            expected = expected_text(random_text)
        elif button.text == 'Ну и ещё пробелы':
            expected = expected_text(random_text, ' ')
        elif button.text == 'Оставить ещё и .,-!?':
            expected = expected_text(random_text, ' .,-!?')
        button.click()
        actual = chrome_driver.find_element(By.ID, 'text_output').text
        assert actual == expected


def test_buttons_empty_data(buttons):
    """
    Check the buttons' functionality using the empty input field.

    Parameters:
        buttons: contains buttons objects (except selection button)
    """
    chrome_driver.find_element(By.ID, 'text_input').clear()
    for button in buttons:
        button.click()
        actual = chrome_driver.find_element(By.ID, 'text_output').text
        assert actual == ''


@pytest.mark.parametrize(
    'edit_button', [0, 1, 2],
    ids=['Consonants', 'Add spaces', 'Add .,-!?'],
)
@pytest.mark.parametrize('data_type', ['default', 'random'])
def test_selection_button_after_editing(data_type, buttons, edit_button):
    """
    Check selection button's functionality after editing the input data.

    Parameters:
        data_type: use default or random data for test
        buttons: contains buttons objects (except selection button)
        edit_button: button for editing input data before test
    """
    action = ActionChains(chrome_driver)
    text_input = chrome_driver.find_element(By.ID, 'text_input')

    if data_type == 'random':
        text = ''.join(random.choices(
            ALPHABET + ALPHABET.upper() + digits + punctuation + '   ' + '\n', k=RANDOM_LENGTH)
        )
        text_input.clear()
        text_input.send_keys(text)
    buttons[edit_button].click()
    expected_selection = chrome_driver.find_element(By.ID, 'text_output').text
    button = [item for item in chrome_driver.find_elements(By.XPATH, '//button')
              if item.text == 'Выделить результат'][0]
    button.click()

    action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    text_input.clear()
    text_input.click()
    action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    selected = text_input.get_attribute('value')

    assert selected == expected_selection


@pytest.mark.parametrize('data_type', ['default', 'random'])
def test_selection_button_no_editing(data_type, buttons):
    """
    Check selection button's functionality with no pre-editing.

    Parameters:
        data_type: use default or random data for test
        buttons: contains buttons objects (except selection button)
    """
    action = ActionChains(chrome_driver)
    text_input = chrome_driver.find_element(By.ID, 'text_input')

    if data_type == 'random':
        text = ''.join(random.choices(
            ALPHABET + ALPHABET.upper() + digits + punctuation + '   ' + '\n', k=RANDOM_LENGTH)
        )
        text_input.clear()
        text_input.send_keys(text)
    expected_selection = chrome_driver.find_element(By.ID, 'text_output').text
    button = [item for item in chrome_driver.find_elements(By.XPATH, '//button')
              if item.text == 'Выделить результат'][0]
    button.click()

    action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    text_input.clear()
    text_input.click()
    action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    selected = text_input.get_attribute('value')

    assert selected == expected_selection





