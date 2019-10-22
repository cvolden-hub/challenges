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

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        searchinput = self.driver.find_element_by_id("input-search")
        searchinput.send_keys("Exotics")
        searchinput.send_keys(Keys.RETURN)
        sleep(5)

        self.assertIn("Exotics", self.driver.title)
        elements = self.driver.find_elements(By.XPATH, "//span[contains(text(),'PORSCHE')]")

        assert "PORSCHE" in elements[0].text, "Whoops, I can't find the text PORSCHE"


if __name__ == '__main__':
    unittest.main()