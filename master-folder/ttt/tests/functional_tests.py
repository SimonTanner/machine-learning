from selenium import webdriver
import unittest
from splinter import Browser


class NewGametest(unittest.TestCase):

    browser = Browser()

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_game(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('TTT', self.browser.title)

    def test_links(self):
        self.browser.get('http://localhost:8000')
        image = self.browser.find_element_by_xpath("//img[@title='logo']")
        image.click()
        self.assertEqual(self.browser.url, 'https://github.com/pmuldoon86/machine-learning')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
