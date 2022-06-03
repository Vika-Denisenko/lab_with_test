from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, text_to_be_present_in_element, \
    title_is, text_to_be_present_in_element_attribute
from selenium.webdriver.support.wait import WebDriverWait

from pageobject.base_page import BasePage


class CartPage(BasePage):
    def get_url(self) -> str:
        return 'http://54.183.112.233/index.php?route=checkout/cart'

    def get_name(self, name) -> str:
        return self.driver.find_element(By.LINK_TEXT, name).text

    def total_sum(self) -> str:
        total_sum = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/table/tbody/tr[4]/td[2]')
        return total_sum.text

    def get_remove_button(self) -> WebElement:
        remove_button = self.driver.find_element(By.CSS_SELECTOR, '[data-original-title="Remove"]')
        
        return remove_button

    def remove_cart(self):

        WebDriverWait(self.driver, timeout=5).until(element_to_be_clickable(self.get_remove_button()))
        self.get_remove_button().click()

    def get_content_text(self) -> str:
        contents = self.driver.find_elements(By.ID, 'content')
        cont_text = ''
        for el in contents:
            cont_text += el.text
        return cont_text
