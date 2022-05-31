from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobject.base_page import BasePage


class SearchPage(BasePage):
    def get_url(self) -> str:
        return 'http://54.183.112.233/index.php?route=product/search'

    def get_search_field(self) -> WebElement:
        search_field = self.driver.find_element(By.CLASS_NAME, 'input-lg')
        return search_field

    def get_search_criteria(self) -> WebElement:
        return self.driver.find_element(By.ID, 'input-search')

    def get_search_checkbox(self) -> WebElement:
        return self.driver.find_element(By.ID, 'description')

    def enter_word(self, word: str):
        search_field = self.get_search_field()
        search_field.send_keys(word)

    def clear_search(self):
        search_field = self.get_search_field()
        search_field.clear()

    def enter_word_in_field_criteria(self, word: str):
        criteria_field = self.get_search_criteria()
        criteria_field.send_keys(word)

    def click_checkbox(self):
        self.get_search_checkbox().click()

    def get_search_button(self) -> WebElement:
        return self.driver.find_element(By.CLASS_NAME, 'btn-default')

    def get_button_after_criteria(self) -> WebElement:
        return self.driver.find_element(By.ID, 'button-search')

    def search_basic(self):
        self.get_search_button().click()

    def search_advanced(self):
        self.get_button_after_criteria().click()

    def get_search_description(self) -> WebElement:
        return self.driver.find_element(By.ID, 'description')

    def get_name_product(self, name) -> str:
        name_product = self.driver.find_element(By.LINK_TEXT, name)
        return name_product.text

    def get_price_product(self, price) -> str:
        price_product = self.driver.find_element(By.CLASS_NAME, price)
        return price_product.text

    def get_price_sony(self) -> str:
        price_product = self.get_price_product('price')
        price_sony = price_product[:price_product.find('\n')]
        return price_sony

    def get_expected_text(self) -> str:
        expected_text = self.driver.find_element(By.ID, 'content').text
        return expected_text
