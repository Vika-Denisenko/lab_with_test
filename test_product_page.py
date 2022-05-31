import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageobject.product_apple_page import ProductApplePage


class ProductPageTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self) -> None:
        self.driver.close()

    def test_name(self):
        product_page = ProductApplePage(self.driver)
        product_page.open()
        actual_name = product_page.get_name_str()

        self.assertEqual(
            'Apple Cinema 30"',
            actual_name
        )

    def test_brand(self):
        product_page = ProductApplePage(self.driver)
        product_page.open()
        actual_brand = product_page.get_brand_and_product_code()
        self.assertIn(
            'Brand: Apple',
            actual_brand
        )

    def test_product_code(self):
        product_page = ProductApplePage(self.driver)
        product_page.open()
        actual_product_code = product_page.get_brand_and_product_code()
        self.assertIn(
            'Product Code: Product 15',
            actual_product_code
        )

    def test_price(self):
        product_page = ProductApplePage(self.driver)
        product_page.open()
        self.assertEqual(
            '$110.00',
            product_page.get_price()
        )


    def test_description(self):
        product_page = ProductApplePage(self.driver)
        product_page.open()

        self.assertIn(
            'The 30-inch Apple Cinema HD Display delivers an amazing 2560 x 1600 pixel resolution',
            product_page.get_description()
        )
