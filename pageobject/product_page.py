from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobject.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, driver: WebDriver, product_id: str):
        super().__init__(driver)
        self.product_id = product_id

    def get_url(self) -> str:
        return 'http://54.183.112.233/index.php?route=product/product&product_id='+self.product_id

    def get_name(self) -> str:
        name = self.driver.find_element(By.TAG_NAME, 'h1')
        return name.text

    def get_brand_and_product_code(self) -> str:
        '''Получаем строку с брэндом и продукт кодом(не нравится мне код, но по другому не придумала как сделать'''
        brand_and_product_code = self.driver.find_elements(By.CLASS_NAME, 'list-unstyled')
        brand_and_product_text = ''
        for brand in brand_and_product_code:
            brand_and_product_text += brand.text
        return brand_and_product_text

    def get_price(self) -> str:
        prices = self.driver.find_elements(By.TAG_NAME, 'h2')
        return prices[1].text

    def get_description(self) -> str:
        text_description = self.driver.find_element(By.ID, 'tab-description')
        return text_description.text

    def get_tab_review(self) -> WebElement:
        tab_review = self.driver.find_element(By.XPATH,  '/html/body/div[2]/div/div/div[1]/div[1]/ul[2]/li[3]/a')
        return tab_review

    def open_review(self):
        self.get_tab_review().click()

    def get_button_review(self) -> WebElement:
        return self.driver.find_element(By.ID, 'button-review')

    def review(self):
        self.get_button_review().click()

    def get_alert_text(self) -> str:
        warning_text = self.driver.find_element(By.CLASS_NAME, 'alert-dismissible')
        return warning_text.text

    def get_name_field(self) -> WebElement:
        return self.driver.find_element(By.ID, 'input-name')

    def get_review_field(self) -> WebElement:
        return self.driver.find_element(By.ID, 'input-review')

    def get_radio_button(self) -> WebElement:

        return self.driver.find_element(By.CSS_SELECTOR, '[value="3"]')

    def rating(self):
        self.get_radio_button().click()

    def enter_name(self, name: str):
        self.get_name_field().send_keys(name)

    def enter_review(self, review: str):
        self.get_review_field().send_keys(review)

    def compare(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-original-title="Compare this Product"]').click()

    def product_comparison(self):
        self.driver.find_element(By.LINK_TEXT, 'product comparison').click()

    def get_field_quantity(self) -> WebElement:
        return self.driver.find_element(By.ID, 'input-quantity')

    def clear_qty(self):
        self.get_field_quantity().clear()

    def send_qty(self, quantity):
        self.clear_qty()
        self.get_field_quantity().send_keys(quantity)

    def get_button_card(self) -> WebElement:
        return self.driver.find_element(By.ID, 'button-cart')

    def cart(self):
        self.get_button_card().click()

