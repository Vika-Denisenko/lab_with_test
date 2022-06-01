import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageobject.product_page import ProductPage


class ProductPageTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.url_list = ['33', '47']
        self.product_name = []
        self.product_page = ProductPage(self.driver, self.url_list[0])
        self.product_page.open()
        self.product_page.send_qty(2)
        self.product_name.append(self.product_page.get_name())
        self.product_page.cart()

    def tearDown(self) -> None:
        self.driver.close()

    def test_product(self):
        actual_name = self.product_page.get_name()
        self.assertEqual(
            'Apple Cinema 30"',
            actual_name
        )