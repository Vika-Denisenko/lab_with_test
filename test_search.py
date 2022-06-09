import unittest
from decimal import Decimal

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageobject.search_page import SearchPage
from webdriver_factory import WebDriverFactory


class SearchPageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = WebDriverFactory.get_driver()
        self.search_page = SearchPage(self.driver)
        self.search_page.open()
        self.name_apple = 'Apple Cinema 30"'
        self.price_apple = '$110.00'
        self.name_sony = 'Sony VAIO'
        self.price_sony = '$1,202.00'
        self.search_list = ['HP LP3065', 'iMac']

    def tearDown(self) -> None:
        self.driver.close()

    def test_search_apple(self):
        self.search_page.enter_word('apple')
        self.search_page.search_basic()
        self.search_page.clear_search()

        self.assertEqual(
            self.name_apple,
            self.search_page.get_search_results()[0].name

        )

        self.assertEqual(
            Decimal(self.price_apple[1:]),
            self.search_page.get_search_results()[0].price
        )

    def test_search_sony(self):
        self.search_page.enter_word('sony')
        self.search_page.search_basic()
        self.search_page.clear_search()

        self.assertEqual(
            self.name_sony,
            self.search_page.get_search_results()[0].name
        )

        self.assertEqual(
            Decimal(self.price_sony[1:].replace(",", "")),
            self.search_page.get_search_results()[0].price
        )

    def test_search_nokia(self):
        self.search_page.enter_word('nokia')
        self.search_page.search_basic()
        self.search_page.clear_search()

        self.assertIn(
            'There is no product that matches the search criteria.',
            self.search_page.get_expected_text()
        )

    def test_with_search_criteria(self):
        self.search_page.enter_word_in_field_criteria('stunning')
        self.search_page.click_checkbox()
        self.search_page.search_advanced()

        self.assertEqual(
            self.search_list,
            [product.name for product in self.search_page.get_search_results()]

        )

