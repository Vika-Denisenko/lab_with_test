from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, text_to_be_present_in_element, \
    visibility_of
from selenium.webdriver.support.wait import WebDriverWait

from pageobject.base_page import BasePage


class ComparePage(BasePage):
    def get_url(self) -> str:
        return 'http://54.183.112.233/index.php?route=product/compare'

    def get_name_in_comparison(self, name) -> str:
        search_name = self.driver.find_element(By.LINK_TEXT, name)
        WebDriverWait(self.driver, timeout=5).until(visibility_of(search_name))
        return search_name.text

    def get_button_remove(self) -> WebElement:
        button_remove = self.driver.find_element(By.CLASS_NAME, 'btn-danger')
        return button_remove

    def remove(self):
        WebDriverWait(self.driver, timeout=10).until(element_to_be_clickable(self.get_button_remove()))
        self.get_button_remove().click()

    def get_alert_text(self) -> str:
        warning_text = self.driver.find_element(By.CLASS_NAME, 'alert-dismissible')
        return warning_text.text
