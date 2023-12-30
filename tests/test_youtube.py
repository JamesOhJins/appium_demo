import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from ..pages.youtube_page import YoutubePage
import time
import json



appium_server_url = 'http://localhost:4723'

def load_device_config(name):
    with open('config.json', 'r') as config_file:
        all_configs = json.load(config_file)
        for config in all_configs:
            if name in config:
                return config[name]
    return None
    
device_config = load_device_config("note_20_ultra")
capabilities_options = UiAutomator2Options().load_capabilities(device_config)

@pytest.fixture(scope="class")
def driver_init(request):
    appium_driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)
    request.cls.driver = appium_driver
    yield appium_driver
    appium_driver.quit()

@pytest.mark.usefixtures("driver_init")
class TestYoutubeApp:
    def setup_method(self, method):
        self.calculator = YoutubePage(self.driver)

    def test_search(self):
        self.calculator.press_digit(9)

        self.calculator.press_multiply()
        self.calculator.press_digit(7)
        
        self.calculator.press_equals()
        result = self.calculator.get_result()
        
        assert result == "63 계산 결과", f"Test failed: Expected result '63 계산 결과', but got {result}"

    def test_complex(self):
        self.calculator.press_digit(6)

        self.calculator.press_add()
        self.calculator.press_digit(7)
        
        self.calculator.press_multiply()
        self.calculator.press_digit(1)
        self.calculator.press_digit(2)
        
        self.calculator.press_divide()
        self.calculator.press_digit(2)
        
        self.calculator.press_subtract()
        self.calculator.press_digit(1)
        self.calculator.press_digit(8)

        self.calculator.press_equals()
        result = self.calculator.get_result()
       
        assert result == "30 계산 결과", f"Test failed: Expected result '30 계산 결과', but got {result}"
