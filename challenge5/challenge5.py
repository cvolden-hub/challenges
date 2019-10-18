"""
For this challenge, go to https://www.copart.com and do a search for “porsche”
and change the  drop down for “Show Entries” to 100 from 20.
Count how many different models of porsche is in the results on the first page
and return in the terminal how many of each type exists.
"""

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

        #Find search field and enter Exotics and search
        searchInput = self.driver.find_element_by_id("input-search")
        searchInput.send_keys("Exotics")
        searchInput.send_keys(Keys.RETURN)
        sleep(5)

        #verify Exotics in title
        self.assertIn("Exotics", self.driver.title)

        #change show entries from 20 to 100
        drpEntys = self.driver.find_element(By.XPATH, "//select[@name='serverSideDataTable_length']")
        drpEntys.click()
        options = self.driver.find_elements_by_xpath("//select[@name='serverSideDataTable_length']/option")
        options[2].click()

        #wait for page to update then find porsche
        sleep(5)

        self.assertIn("Exotics", self.driver.title)

        make = self.driver.find_elements(By.XPATH, "//span[contains(text(),'PORSCHE')]")
        assert "PORSCHE" in make[0].text, "Whoops, I can't find the text PORSCHE"

        model = self.driver.find_elements(By.XPATH, "//span[contains(text(),'CAYENNE S')]")
        assert "CAYENNE S" in model[0].text, "Whoops, I can't find the text model"

        # new stuff trying to get work
        for model in self.driver.find_elements(By.XPATH, "//span[contains(text(),'[CAYENNE S]')]"):
            print(model.text)

        for (row = 1:row <= 100):
            model in self.driver.find_elements(By.XPATH, "//span[contains(text(),'[CAYENNE S]')]")
            print(model.text)
            row +1

        make = self.driver.find_elements(By.XPATH, "//*[@id='serverSideDataTable']/tbody/tr[14]/td[5]/span)")
            print(make)



        """
        i = 0
        while i < len(make):
            i += 1

        assert "PORSCHE" in make[0].text, "Whoops, I can't find the text PORSCHE"
            print(make[i].text + " - " +make[1].get_attribute("lotsearchlotmodel"))

        model = self.driver.find_elements(By.XPATH, "//*[@id='serverSideDataTable']/tbody/tr[1]/td[6]/span)

        #now look for models of porsche on first page

                                          < span
        

        make = self.driver.find_elements(By.XPATH, "//select[@uname='lotsearchLotmake' > PORSCHE < / span >
        // *[ @ id = "serverSideDataTable"] / tbody / tr[1] / td[5] / span
"""



if __name__ == '__main__':
    unittest.main()