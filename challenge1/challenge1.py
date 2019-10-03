import unittest
from selenium import webdriver

class Challenge1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        #code to startup webdriver

    def tearDown(self):
        self.driver.close()
        #code to close webdriver

    def test_challenge1(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)
        #code for our test steps


if __name__ == '__main__':
    unittest.main()