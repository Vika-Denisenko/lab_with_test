from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ProductCanonPage:

    url='http://tutorialsninja.com/demo/index.php?route=product/product&product_id=42'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        '''Открыть страницу логина'''
        self.driver.get(self.url)

    def get_name_str(self) -> str:
        name_str = self.driver.find_elements(By.TAG_NAME, 'h1')[1]
        name_str = name_str.text
        return name_str

    def get_brand_and_product_code(self) -> str:
        '''Получаем строку с брандом и продукт кодом(не нравится мне код, но по другому не придумала как сделать'''
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

