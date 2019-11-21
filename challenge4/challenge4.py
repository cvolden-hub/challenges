
# For this challenge, we are going to:
# write a function that display the fibonacci sequence up to a certain number.
# If I want the fibonacci for the 9 order of the sequence, I should see 21.
# Keep your function to calculate the fibonacci sequence separate from the file that has the unittest.main().
# see fibFuncs

# However, to add additional challenge to this challenge, instead of displaying the number 21,
# I want the string # representation of twenty one.
# This will require you to use string concatenation to print out the string.

import unittest

from selenium import webdriver

from challenges.challenge4 import fibFuncs


class Challenge4(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challange4(self):

        fibval = (fibFuncs.fibLooping(8))  # seting fibval to the value in the nth position (zero based) in fibFuncs

        #nested_dict goes here
        # oneplace values
        onesplace = {0: "", 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
                     9: 'Nine', 10: 'ten'}

        teens = {11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
                      17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}

        #tenslace vaues
        tensplace = {0: "", 1: 'Ten', 2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty',
                     9: 'Ninety'}

        #hundredsplace values
        hundredsplace = {0: "", 1: "One Hundred", 2: "Two Hundred", 3: "Three Hundred", 4: "Four Hundred",
                         5: "Five Hundred", 6: "Six Hundred", 7: "Seven Hundred", 8: "Eight Hundred",
                         9: "Nine Hundred"}

        #thousandplace values
        thousandplace = {0: "", 1: 'One Thousand', 2000: 'Two Thousand', 3000: 'Three Thousand', 4000: 'Four Thousand',
                         5000: 'Five Thousand', 6000: 'Six Thousand', 7000: 'Seven Thousand', 8000: 'Eight Thousadn',
                         9000: 'Nine Thousand'}

        #tenthousannsplace values
        tenthousandsplace = {0: "", 10: 'Ten Thousand'}

        if fibval < 10:
            intval = onesplace.get(int(fibval))
            print(fibval, "-", str(intval))

        elif fibval <20:
             intval = teens.get(int(fibval))
             print(fibval, " - ", str(intval))

        elif fibval > 19 < 100:
             intval = []
             intval += str(fibval)

             what = intval.index(tensplace[2])

             for i in range(len(intval -1)):
                 print(tensplace,str(intval))
                 
                 intval = tensplace.get(int(fibval))
                 numdigits = len(intval)
                 print(fibval, "-", str(intval))

        elif fibval > 19:
            intval = []
            intval += str(fibval)
            numdigits = len(intval)

            i = 0

            if numdigits == 2:
                tens = intval.get(int[0])


                ones = intval.get(int[1])

                print(fibval, "-", str(tens," ", ones))

        i = 0

        # using string cat functionality
        if fibval < 22:
            intval = onesplace.get(int(fibval))
            print(fibval, "-", str(intval))
        else:
            intval = tensplace.get[int(fibval[int(i)])]
            print(fibval, "-", str(intval))

        """
        so if the value is > 19 < 100
        split number into parts in a list
        get the len of list
        if len = 2
        the number is greater than 19
        get the first digit and map to tensplace then get second num and map to ones
        
        if len = 3
        etc    
    
        """



if __name__ == '__main__':
    unittest.main()