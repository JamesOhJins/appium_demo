from appium import webdriver
from .base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class YoutubePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_box = self.find_element('xpath', '//*[@name="SearchEditText"]')

    def search(self, keyword):
        self.send_keys(keyword, self.search_box)
        self.press_keycode(32)  # Enter keycode for search

    def get_video_title(self):
        title = self.find_element('xpath', '//h3[@class="yt-uix-tile-title"]').text
        return title

    def is_search_result_visible(self, keyword):
        search_result_xpath = f'//*[contains(@text,"{keyword}")]'
        return self.is_element_present(AppiumBy.XPATH, search_result_xpath)