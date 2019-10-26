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
from selenium.webdriver.support.select import Select
from time import sleep

class Challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)

        self.driver.maximize_window()

        # find search field and enter Porsche, enter txt via send _key
        searchinput = self.driver.find_element_by_id("input-search")
        searchinput.send_keys("Porsche")
        sleep(5)
        searchinput.send_keys(Keys.RETURN)
        sleep(5)

        # clicking drpdwn
        drpdwn = self.driver.find_element(By.XPATH, "//select[@name='serverSideDataTable_length']")
        drpdwn.click()
        sleep(5)

        # select element 2 fromm list
        drpdwn.send_keys(Keys.ARROW_DOWN)
        drpdwn.send_keys(Keys.ARROW_DOWN)
        sleep(5)
        drpdwn.send_keys(Keys.ENTER)

        #options = self.driver.find_element(By.XPATH, "//select[@name='serverSideDataTable_length']/option")
        #options[2].click()
        #sleep(5)

        #opt = self.driver.find_element(By.XPATH, "//select[@name='serverSideDataTable_length']")
        #selector = Select(opt)
        #opt.click()
        sleep(10)

        # now get the models from the page
        nummod = self.driver.find_elements(By.XPATH, "//*[@id='serverSideDataTable']/tbody/tr/td[6]/span")
        num = len(nummod)

        # iterate
        for i in range(num):
            models = self.driver.find_element(By.XPATH, "//*[@id='serverSideDataTable']/tbody/tr[{}]/td[6]/span"
                                              .format(i + 1))
            print(models.text)

        # now get the damage from the page
        numdam = self.driver.find_elements(By.XPATH, "//*[@id='serverSideDataTable']/tbody/tr/td[12]/span")
        num2 = len(numdam)

        for x in range(num2):
            damage = self.driver.find_element(By.XPATH, "//*[@id='serverSideDataTable']/tbody/tr[{}]/td[12]/span"
                                               .format(x + 1))
            print(damage.text)

        """
        #object changed so send_keys was not working  trying this out
        #wait for dropdown to go away before selecting 100  *[@id
        #when Porsche is entered a list displays, this is intended to select porsche from the top of list
        poption = self.driver.find_elements_by_xpath("//a[starts-with(@href,'./popular/category')]")
        < a href = "./popular/category/exotics?intcmp=web_homepage_categories_exotics_public_en" > Exotics < / a >


        poption.__getattribute__("title")
        print(poption)
        
        <a href="" tabindex="-1" ng-bind-html="match.label | uibTypeaheadHighlight:query" ng-attr-title="{{match.label}}" \
        "" title="porsche cayenne"><strong>pors</strong>che cayenne</a>

        poption.click()
        sleep(30)

               
        # verify Porsche in title
        make = self.driver.find_elements(By.XPATH, "//span[contains(text(),'PORSCHE')]")
        assert "PORSCHE" in make[0].text, "Whoops, I can't find the text PORSCHE"

        # now get all models
        ##this gets me models where text = cayenne.  need to  identifiy the text attribure
        model = self.driver.find_elements(By.XPATH, "//span[contains(text(),'CAYENNE S')]")
        print(model.text)
        print(model.tag_name)
        print(model.location)
            
        assert "CAYENNE S" in model[0].text, "Whoops, I can't find the text model"

        # new stuff trying to get work
        for model in self.driver.find_elements(By.XPATH, "//span[contains(text(),'[CAYENNE S]')]"):
            

        for i in range(1,100):
            model in self.driver.find_elements(By.XPATH, "//span[contains(text(),'[CAYENNE S]')]")
            print(model.text)
            i += 1

            
            model in self.driver.find_elements(By.XPATH, "//span[contains(text(),'[CAYENNE S]')]")
            print(model.text)


        make = self.driver.find_elements(By.XPATH, "//*[@id='serverSideDataTable']/tbody/tr[14]/td[5]/span)")
            print(make)



        
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