
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

        fibval = (fibFuncs.fibLooping(25))  # seting fibval to the value in the nth position (zero based) in fibFuncs
        #fibval =17908
        print(fibval)

        # ones
        ones = {0: "", 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
                     9: 'Nine', 10: 'ten'}

        teens = {0: "", 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
                      17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}

        #tens
        tens = {0: "", 1: 'Ten', 2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty',
                     9: 'Ninety'}

        #hundreds
        hundreds = {0: "", 1: "One Hundred", 2: "Two Hundred", 3: "Three Hundred", 4: "Four Hundred",
                         5: "Five Hundred", 6: "Six Hundred", 7: "Seven Hundred", 8: "Eight Hundred",
                         9: "Nine Hundred"}

        #thousands
        thousands = {0: "", 1: 'One Thousand', 2: 'Two Thousand', 3: 'Three Thousand', 4: 'Four Thousand',
                          5: 'Five Thousand', 6: 'Six Thousand', 7: 'Seven Thousand', 8: 'Eight Thousand',
                          9: 'Nine Thousand'}

        #tenthousands
        tenthousands = {0: "", 1: 'Ten Thousand', 2: 'Twenty Thousand', 3: 'Thirty Thousand', 4: 'Forty Thousand',
                          5: 'Fifty Thousand', 6: 'Sixty Thousand', 7: 'Seventy Thousand', 8: 'Eighy Thousand',
                          9: 'Ninty Thousand'}

        #ones
        if fibval <=10:
            intval = ones.get(int(fibval))
            print(fibval, "-", str(intval))

        #teens
        elif fibval <20:
             intval = teens.get(int(fibval))
             print(fibval, " - ", str(intval))

        #tens
        elif fibval <100:
             intval = []
             intval += str(fibval)

             indexzero = tens.get(int(intval[0]))
             indexone = ones.get(int(intval[1]))

             print(fibval, "-", indexzero, indexone)

        #humdreds
        elif fibval <1000:
             intval = []
             intval += str(fibval)

             indexzero = hundreds.get(int(intval[0]))
             indexone = tens.get(int(intval[1]))
             indextwo = ones.get(int(intval[2]))

             print(fibval, "-", indexzero, indexone, indextwo)

        #thousands
        elif fibval <10000:
            intval = []
            intval += str(fibval)

            indexzero = thousands.get(int(intval[0]))
            indexone = hundreds.get(int(intval[1]))
            indextwo = tens.get(int(intval[2]))
            indexthree = ones.get(int(intval[3]))

            print(fibval, "-", indexzero, indexone, indextwo, indexthree)

        #tenthousands
        elif fibval < 100000:
            intval = []
            intval += str(fibval)

            indexzero = tenthousands.get(int(intval[0]))
            indexone = thousands.get(int(intval[1]))
            indextwo = hundreds.get(int(intval[2]))
            indexthree = tens.get(int(intval[3]))
            indexfour = ones.get(int(intval[4]))

            firstwo = int(str(fibval)[:2])
            lastwo = int(str(fibval)[-2:])

            subindex = ones.get(int(lastwo))
            subindex2 = teens.get(int(lastwo))

            if indexone =='' and lastwo <10:
                print(fibval, "-", indexzero, indexone, indextwo, subindex)
            elif indexone =='' and lastwo <20:
                print(fibval, "-", indexzero, indexone, indextwo, indexthree, indexfour, subindex2)
            else:
                index = teens.get(int(firstwo))
                indexzero = hundreds.get(int(intval[0]))
                indexone = tens.get(int(intval[1]))
                indextwo = hundreds.get(int(intval[2]))
                indexthree = tens.get(int(intval[3]))
                indexfour = ones.get(int(intval[4]))
                print(fibval, "-", index, "Thousand", indextwo, indexthree, indexfour, subindex, subindex2)

        """
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