from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class SearchPage:
    url = 'http://tutorialsninja.com/demo/index.php?route=product/search'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        '''Открыть страницу логина'''
        self.driver.get(self.url)

    def get_search_field(self) -> WebElement:
        search_field = self.driver.find_element(By.CLASS_NAME, 'input-lg')
        return search_field

    def enter_word(self, word: str):
        search_field = self.get_search_field()
        search_field.send_keys(word)

    def clear_search(self):
        search_field = self.get_search_field()
        search_field.clear()

    def get_search_button(self) -> WebElement:
        return self.driver.find_element(By.CLASS_NAME, 'btn-default')

    def get_search_criteria(self) -> WebElement:
        return self.driver.find_element(By.ID, 'input-search')

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

