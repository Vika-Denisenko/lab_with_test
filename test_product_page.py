import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageobject.product_page import ProductPage


class ProductPageTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.product_apple = '42'
        self.product_page = ProductPage(self.driver, self.product_apple)
        self.product_page.open()

    def tearDown(self) -> None:
        self.driver.close()

    def test_product(self):
        actual_name = self.product_page.get_name()
        self.assertEqual(
            'Apple Cinema 30"',
            actual_name
        )

        actual_brand = self.product_page.get_brand_and_product_code()
        self.assertIn(
            'Brand: Apple',
            actual_brand
        )

        self.assertIn(
            'Product Code: Product 15',
            actual_brand
        )

        self.assertEqual(
            '$110.00',
            self.product_page.get_price()
        )

        self.assertIn(
            'The 30-inch Apple Cinema HD Display delivers an amazing 2560 x 1600 pixel resolution',
            self.product_page.get_description()
        )
