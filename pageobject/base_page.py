from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    url = 'http://tutorialsninja.com/demo/index.php?route=product/product&product_id=42'
    '''Родительский класс PageObject'''

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_url(self) -> str:
        '''Обязательно реализовать в дочерних классах'''
        raise NotImplementedError

    def open(self):
        '''Открыть страницу логина'''
        self.driver.implicitly_wait(10)
        self.driver.get(self.get_url())
