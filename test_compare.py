import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageobject.compare import ComparePage
from pageobject.product_page import ProductPage


class CompareTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.url_list = ['42', '33']
        self.product_name = []
        self.product_page = ProductPage(self.driver, self.url_list[0])
        self.product_page.open()
        self.product_name.append(self.product_page.get_name())
        self.product_page.compare()

    def tearDown(self) -> None:
        self.driver.close()

    def test_compare(self):
        '''Проверяем успешно ли добавлен продукт к сравнению'''
        self.assertEqual(
            f'Success: You have added {self.product_page.get_name()} to your product comparison!',
            self.product_page.get_alert_text().split('\n')[0]
        )

    def add_product(self):
        '''Добавление продуктов в сравнение и их название добавляем в список'''
        for i in range(1, len(self.url_list)):
            product_page = ProductPage(self.driver, self.url_list[i])
            product_page.open()
            self.product_name.append(product_page.get_name())
            product_page.compare()

    def test_product_in_comparison(self):
        '''Проверяем каждое имя на странице сравнения'''
        self.add_product()
        compare_page = ComparePage(self.driver)
        compare_page.open()

        for name in self.product_name:
            self.assertEqual(
                name,
                compare_page.get_name_in_comparison(name)
            )

    def test_del_product(self):
        '''Проверяем успешно ли удалены продукты из сравнения'''
        self.add_product()
        compare_page = ComparePage(self.driver)
        compare_page.open()
        for i in range(len(self.product_name)):
            compare_page.remove()

        self.assertEqual(
            'Success: You have modified your product comparison!',
            compare_page.get_alert_text().split('\n×')[0]
        )



