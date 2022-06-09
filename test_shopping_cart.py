import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageobject.cart_page import CartPage
from pageobject.product_page import ProductPage
from webdriver_factory import WebDriverFactory


class ProductPageTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = WebDriverFactory.get_driver()
        self.url_list = ['33', '47']
        self.qty_list = [2, 1]
        self.product_name = []
        self.sum = 0

    def tearDown(self) -> None:
        self.driver.close()

    def add_product_to_cart(self):
        '''Знаю хорошо бы было сделать словарями, а не списками'''
        for i in range(len(self.url_list)):
            self.product_page = ProductPage(self.driver, self.url_list[i])
            self.product_page.open()
            self.product_page.send_qty(self.qty_list[i])
            self.product_page.cart()
            self.name = self.product_page.get_name()
            self.product_name.append(self.name)
            self.sum += float(self.product_page.get_price())*self.qty_list[i]


    def test_add_success(self):
        '''Проверяем успешное добавление товара в корзину'''
        self.add_product_to_cart()
        self.assertEqual(
            f'Success: You have added {self.name} to your shopping cart!',
            self.product_page.get_alert_text().split('\n×')[0]
        )

    def test_shopping_cart(self):
        '''Проверяем наличие добавленных товаров в корзине и сумму'''
        self.add_product_to_cart()
        cart_page = CartPage(self.driver)
        cart_page.open()
        for self.name in self.product_name:
            self.assertEqual(
                self.name,
                cart_page.get_name(self.name)
            )
        self.assertEqual(
            self.sum,
            float(cart_page.total_sum()[1:])
        )

    def test_clear_cart(self):
        '''Еще не работает!'''
        self.add_product_to_cart()
        cart_page = CartPage(self.driver)
        cart_page.open()
        for _ in range(len(self.product_name)):
            cart_page.remove_cart()
            '''!!!'''

        self.assertIn(

            'Your shopping cart is empty!',
            cart_page.get_content_text()
        )
