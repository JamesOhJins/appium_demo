from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        """This method wraps Appium's `find_element()` for easier usage."""
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        """This method wraps Appium's `find_elements()` for easier usage."""
        return self.driver.find_elements(*locator)

    def is_element_present(self, by):
        """Check if an element is present on the page."""
        try:
            self.find_element(by)
            return True
        except Exception:
            return False

    def send_keys(self, text, element=None):
        """Send keys to an element."""
        if element:
            element.send_keys(text)
        else:
            self.driver.send_keys(text)

    def press_keycode(self, keycode):
        """Press a specific keycode."""
        self.driver.press_keycode(keycode)

    def get_text(self, element):
        """Get text from an element."""
        return element.text

    def is_element_displayed(self, element):
        """Check if an element is displayed on the screen."""
        return self.is_element_present(element) and self.get_text(element).strip() != ""

    def launch_app(self):
        """Launch the app."""
        self.driver.launch_app()