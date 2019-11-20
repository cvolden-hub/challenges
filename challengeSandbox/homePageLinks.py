import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_homePageLinks(self):
        qa3us = "https://qa3.doterra.com/US/en"

        self.driver.get(qa3us)
        self.assertIn("Essential Oils Pure and Natural", self.driver.title)

        sleep(5)

        """
        self.assertIn("Exotics", self.driver.title)
        elements = self.driver.find_elements(By.XPATH, "//span[contains(text(),'PORSCHE')]")

        assert "PORSCHE" in elements[0].text, "Whoops, I can't find the text PORSCHE"
        """

if __name__ == '__main__':
    unittest.main()