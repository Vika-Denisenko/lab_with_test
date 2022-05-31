from selenium.webdriver.common.by import By

from pageobject.base_page import BasePage


class ProductCanonPage(BasePage):

    def get_url(self) -> str:
        return 'http://54.183.112.233/index.php?route=product/product&product_id=42'


    def get_name_str(self) -> str:
        name_str = self.driver.find_element(By.TAG_NAME, 'h1')
        return name_str.text

    def get_brand_and_product_code(self) -> str:
        '''Получаем строку с брэндом и продукт кодом(не нравится мне код, но по другому не придумала как сделать'''
        brand_and_product_code = self.driver.find_elements(By.CLASS_NAME, 'list-unstyled')
        brand_and_product_text=''
        for brand in brand_and_product_code:
            brand_and_product_text += brand.text
        return brand_and_product_text

    def get_price(self) -> str:
        prices = self.driver.find_elements(By.TAG_NAME, 'h2')
        return prices[1].text

    def get_description(self) -> str:
        text_description = self.driver.find_element(By.ID, 'tab-description')
        return text_description.text

