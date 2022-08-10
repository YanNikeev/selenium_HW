"""Test main paige components existence."""
import pytest
from conftest import chrome_driver
from defaults import Defaults
from selenium.webdriver.common.by import By


def test_main_page_title():
    """Check the title on the main page."""
    assert chrome_driver.title == Defaults.title


@pytest.mark.parametrize(
    'field', [
        ('input', Defaults.input_text),
        ('output', Defaults.output_text),
    ],
    ids=['Default input', 'Default output'],
)
def test_default_fields_text(field):
    """
    Check input and output fields content.

    Parameters:
        field: contains field type and data
    """
    name, default_text = field
    actual_text = chrome_driver.find_element(By.ID, f'text_{name}').text
    assert actual_text == default_text


def test_buttons_on_the_page():
    """Check all buttons existence."""
    buttons = chrome_driver.find_elements(By.XPATH, '//button')
    assert len(buttons) == 4
