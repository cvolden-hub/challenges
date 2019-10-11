#For this challenge, go to https://www.copart.com and do a search for “porsche”
# and change the  drop down for “Show Entries” to 100 from 20.
# Count how many different models of porsche is in the results on the first page
# and return in the terminal how many of each type exists.

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from time import sleep

class Challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):

        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)

        searchInput = self.driver.find_element_by_id("input-search")
        searchInput.send_keys("Exotics")
        searchInput.send_keys(Keys.RETURN)
        sleep(5)

        self.assertIn("Exotics", self.driver.title)
        #pageview = self.driver.find_element_by_xpath("//serverSideDataTable_length"]/label/select/option[3]")
        select = Select(self.driver.find_element_by_class_name("form-control"))
        select.select_by_value("100")
        #select = Select(driver.find_element_by_xpath("//serverSideDataTable_length"]/label/select/option[3]")
        #categories = self.driver.find_elements_by_xpath("//a[starts-with(@href,'./popular/category')]")
        sleep(2)

        makemodel = self.driver.find_elements(By.XPATH, "//span[contains(text(),'PORSCHE')]")
        sleep (20)

        assert "PORSCHE" in makemodel[0].text, "Whoops, I can't find the text PORSCHE"

        #select = Select(driver.find_elements(By.XPATH,"//select[@id='serverSideDataTable_length']/option[@value='100']"))




if __name__ == '__main__':
    unittest.main()