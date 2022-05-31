import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageobject.search_page import SearchPage


class SearchPageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.name_apple = 'Apple Cinema 30"'
        self.price_apple_class = 'price-new'
        self.name_sony = 'Sony VAIO'



    def tearDown(self) -> None:
        self.driver.close()

    def test_search_apple(self):
        search_page = SearchPage(self.driver)
        search_page.open()
        search_page.get_search_field()
        search_page.enter_word('apple')
        search_page.get_search_button().click()
        search_page.clear_search()

        self.assertEqual(
            self.name_apple,
            search_page.get_name_product(self.name_apple)
        )

        self.assertEqual(
            '$110.00',
            search_page.get_price_product(self.price_apple_class)
        )

    def test_search_sony(self):
        search_page = SearchPage(self.driver)
        search_page.open()
        search_page.get_search_field()
        search_page.enter_word('sony')
        search_page.get_search_button().click()
        search_page.clear_search()

        self.assertEqual(
            self.name_sony,
            search_page.get_name_product(self.name_sony)
        )

        self.assertEqual(
            '$1,202.00',
            search_page.get_price_sony()
        )

    def test_search_nokia(self):
        search_page = SearchPage(self.driver)
        search_page.open()
        search_page.get_search_field()
        search_page.enter_word('nokia')
        search_page.get_search_button().click()
        search_page.clear_search()

        self.assertIn(
            'There is no product that matches the search criteria.',
            search_page.get_expected_text()
        )





