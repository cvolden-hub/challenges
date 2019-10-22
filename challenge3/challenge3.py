import unittest

from selenium import webdriver


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    # gets make
    def test_challenge3ForLoop(self):
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)

        makemodel = self.driver.find_elements_by_xpath("//a[starts-with(@href,'./popular/m')]")
        for x in makemodel:
            print(x.text + " - " + x.get_attribute("href"))

    # gets model
    def test_challenge3WhileLoop(self):
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)

        categories = self.driver.find_elements_by_xpath("//a[starts-with(@href,'./popular/category')]")

        i = 0
        while i <len(categories):
            print(categories[i].text + " - " + categories[1].get_attribute("href"))
            i += 1


if __name__ == '__main__':
    unittest.main()

