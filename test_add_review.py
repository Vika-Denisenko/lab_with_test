import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageobject.product_apple_page import ProductPage


class AddReviewTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.name = 'John'
        self.review24 = 'asdfghjklqwertyuiopzxcvb'
        self.review25 = 'asdfghjklqwertyuiopzxcvbf'
        self.product_id = '42'
        self.product_page = ProductPage(self.driver, self.product_id)
        self.product_page.open()
        self.product_page.open_review()

    def tearDown(self) -> None:
        self.driver.close()

    def test_reviews_without_rating(self):

        self.product_page.review()
        self.assertEqual(
            'Warning: Please select a review rating!',
            self.product_page.get_alert_text()

        )

    def test_with_24(self):
        self.product_page.rating()
        self.product_page.enter_name(self.name)
        self.product_page.enter_review(self.review24)
        self.product_page.review()
        self.assertEqual(
            'Warning: Review Text must be between 25 and 1000 characters!',
            self.product_page.get_alert_text()

        )

    def test_with_25(self):
        self.product_page.rating()
        self.product_page.enter_name(self.name)
        self.product_page.enter_review(self.review25)
        self.product_page.review()
        self.assertEqual(
            'Thank you for your review. It has been submitted to the webmaster for approval.',
            self.product_page.get_alert_text()
        )




