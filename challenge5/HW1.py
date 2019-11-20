import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from collections import Counter


from time import sleep
class HW1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_HW1(self):
        self.driver.get("https://www.doterra.com/US/en/using-essential-oils")
        self.assertIn("Oils", self.driver.title)

        top = []

        top = self.driver.find_elements_by_xpath("//a[starts-with(@href,'./li')]")
        print(top)
        for x in top:
            print(x.text + " - " + x.get_attribute("href"))
            x += 1


if __name__ == '__main__':
    unittest.main()