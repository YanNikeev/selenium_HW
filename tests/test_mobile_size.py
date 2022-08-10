"""Test the buttons' positioning on the small screens."""
import pytest
from conftest import chrome_driver
from defaults import Defaults
from selenium.webdriver.common.by import By


@pytest.mark.parametrize(
    'device', [(Defaults.tablet_width, Defaults.tablet_height),
               (Defaults.mobile_width, Defaults.mobile_height)],
    ids=['Tablet', 'Mobile'],
)
def test_buttons_positions_mobile_width(device):
    """
    Check buttons locations with the small screen width.

    Parameters:
        device: type of the using mobile device
    """
    width, height = device
    chrome_driver.set_window_size(width, height)
    buttons = chrome_driver.find_elements(By.XPATH, '//button')
    locations = {button.location['x'] for button in buttons}
    assert len(locations) < 4, 'All buttons are in one line'
    assert len(locations) == 1, 'Not all buttons are placed under each other'
