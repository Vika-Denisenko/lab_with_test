import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageobject.product_apple_page import ProductApplePage


class AddReviewTest(unittest.TestCase):
    '''Не работает пока!'''

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.name = 'John'
        self.review24 = 'asdfghjklqwertyuiopzxcvb'
        self.review25 = 'asdfghjklqwertyuiopzxcvbf'

    def tearDown(self) -> None:
        self.driver.close()

    def test_reviews_without_rating(self):
        product_page = ProductApplePage(self.driver)
        product_page.open()
        product_page.open_review()
        product_page.review()
        self.assertEqual(
            'Warning: Please select a review rating!',
            product_page.get_warning_text()
        )

    def test_with_24(self):
        product_page = ProductApplePage(self.driver)
        product_page.open()
        product_page.open_review()
        product_page.click_raning()
        product_page.enter_name(self.name)
        product_page.enter_review(self.review24)
        product_page.review()
        self.assertEqual(
            'Warning: Review Text must be between 25 and 1000 characters!',
            product_page.get_warning_text()

        )

    def test_with_25(self):
        product_page = ProductApplePage(self.driver)
        product_page.open()
        product_page.open_review()
        product_page.click_raning()
        product_page.enter_name(self.name)
        product_page.enter_review(self.review25)
        product_page.review()
        self.assertEqual(
            'Thank you for your review. It has been submitted to the webmaster for approval.',
            product_page.get_success_text()

        )




