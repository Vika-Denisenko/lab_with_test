from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobject.base_page import BasePage


class CartPage(BasePage):
    def get_url(self) -> str:
        return 'http://54.183.112.233/index.php?route=checkout/cart'

    def get_name(self, name) -> str:
        return self.driver.find_element(By.LINK_TEXT, name).text

    def field_total(self) -> str:
        field_total = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/table/tbody/tr[4]/td[2]')
        return field_total.text

    def get_remove_button(self) -> WebElement:
        remove_button = self.driver.find_elements(By.CLASS_NAME, 'fa-times-circle')
        return remove_button[0]

    def remove_cart(self):
        self.get_remove_button().click()

    def get_content_text(self)-> str:
        contents = self.driver.find_elements(By.ID, 'content')
        cont_text = ''
        for el in contents:
            cont_text += el.text
        return cont_text
