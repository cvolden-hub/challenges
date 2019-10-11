import unittest
from selenium import webdriver

class HW1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_HW1(self):
        self.driver.get("https://www.doterra.com/US/en/using-essential-oils")
        self.assertIn("Oils", self.driver.title)

        top = self.driver.find_elements_by_xpath("//a[starts-with(@href,'./li')]")

        for x in top:
            print(x.text + " - " + x.get_attribute("href"))

if __name__ == '__main__':
    unittest.main()