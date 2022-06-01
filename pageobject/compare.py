from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobject.base_page import BasePage


class ComparePage(BasePage):
    def get_url(self) -> str:
        return 'http://54.183.112.233/index.php?route=product/compare'

    def get_name_in_comparison(self, name) -> str:
        return self.driver.find_element(By.LINK_TEXT, name).text

    def get_button_remove(self) -> WebElement:
        button_remove = self.driver.find_elements(By.LINK_TEXT, 'Remove')
        return button_remove[0]

    def remove(self):
        self.get_button_remove().click()

    def get_alert_text(self) -> str:
        warning_text = self.driver.find_element(By.CLASS_NAME, 'alert-dismissible')
        return warning_text.text


