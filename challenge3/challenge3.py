import unittest

from selenium import webdriver

class Challenge3ForWhile(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge3ForLoop(self):
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)

        makeModel = self.driver.find_elements_by_xpath("//a[starts-with(@href,'./popular/m')]")
        #print(len(makeModel))
        for x in makeModel:
            print(x.text + " - " + x.get_attribute("href"))

    def test_challenge3WhileLoop(self):
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)

        categories = self.driver.find_elements_by_xpath("//a[starts-with(@href,'./popular/category')]")
        #print(len(categories))
        i = 0
        while i <len(categories):
            print(categories[i].text + " - " + categories[1].get_attribute("href"))
            i += 1


if __name__ == '__main__':
    unittest.main()

