from selenium import webdriver
import unittest
from splinter import Browser


class NewGametest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('ML-TTT', self.browser.title)
        header = self.browser.find_element_by_tag_name('li').text
        self.assertEqual("Welcome to TicTacToe Man vs. Machine!", header)


    def test_links(self):
        self.browser.get('http://localhost:8000')
        image = self.browser.find_element_by_xpath("//img[@title='github']")
        image.click()
        self.assertEqual(self.browser.current_url, 'https://github.com/simontanner/machine-learning')
        #button = self.browser.find_element_by_name("Play ML TTT")

    def test_play_button(self):
        self.browser.get('http://localhost:8000')
        button = self.browser.find_element_by_name("playGame")
        button.click()
        header = self.browser.find_element_by_tag_name('li').text
        self.assertEqual('Play the Machine', header)

    def test_can_enter_their_name(self):
        self.browser.get('http://localhost:8000/newgame')
        submit_name = self.browser.find_element_by_tag_name("submitName")
        submit_name.send_keys('Simon')
        submit_name.send_keys(Keys.ENTER)
        time.sleep(10)
        header = self.browser.find_element_by_tag_name('li').text
        self.assertEqual('Simon vs. Machine', header)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
