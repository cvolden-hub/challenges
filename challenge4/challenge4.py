
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

biggy = {0: "", 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
         9: 'Nine', 10: 'ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
         17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
         60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}

# ones
ones = {0: "", 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
        9: 'Nine', 10: 'ten'}

# teens
teens = {11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
         17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}

# tens
tens = {0: "", 1: 'Ten', 2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty',
        9: 'Ninety'}

# hundreds
hundreds = {0: "", 1: "One Hundred", 2: "Two Hundred", 3: "Three Hundred", 4: "Four Hundred",
            5: "Five Hundred", 6: "Six Hundred", 7: "Seven Hundred", 8: "Eight Hundred", 9: "Nine Hundred"}

# thousands
thousands = {0: "", 1: 'One Thousand', 2: 'Two Thousand', 3: 'Three Thousand', 4: 'Four Thousand',
             5: 'Five Thousand', 6: 'Six Thousand', 7: 'Seven Thousand', 8: 'Eight Thousand',
             9: 'Nine Thousand'}

# tenthousands
tenthousands = {0: "", 1: 'Ten Thousand', 2: 'Twenty Thousand', 3: 'Thirty Thousand', 4: 'Forty Thousand',
                5: 'Fifty Thousand', 6: 'Sixty Thousand', 7: 'Seventy Thousand', 8: 'Eighy Thousand',
                9: 'Ninty Thousand'}

# hundredthoussands
hundredthousands = {1: "One Hundred", 2: "Two Hundred", 3: "Three Hundred", 4: "Four Hundred",
                    5: "Five Hundred", 6: "Six Hundred", 7: "Seven Hundred", 8: "Eight Hundred",
                    9: "Nine Hundred"}

# millions
million = {1: "One Million", 2: "Two  Million", 3: "Three  Million", 4: "Four  Million",
                    5: "Five  Million", 6: "Six  Million", 7: "Seven  Million", 8: "Eight  Million",
                    9: "Nine  Million"}

# teenmillions
teenmillions = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
         17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}

# tensMillions
tenmillions = {1: 'Ten Million', 2: 'Twenty Million', 3: 'Thirty Million', 4: 'Forty Million',
                5: 'Fifty Million', 6: 'Sixty Million', 7: 'Seventy Million', 8: 'Eighy Million',
                9: 'Ninty Million'}

# hundredmillion
hundredmillion = {1: "One Hundred Million", 2: "Two Hundred Million", 3: "Three Hundred Million", 4: "Four Hundred Million",
                    5: "Five Hundred Million", 6: "Six Hundred Million", 7: "Seven Hundred Million", 8: "Eight Hundred Million",
                    9: "Nine Hundred Million"}

# trillions
trillion = {1: "One Trillion", 2: "Two  Trillion", 3: "Three  Trillion", 4: "Four  Trillion",
                    5: "Five  Trillion", 6: "Six  Trillion", 7: "Seven  Trillion", 8: "Eight  Trillion",
                    9: "Nine  Trillion"}

class Challenge4(unittest.TestCase):
    def test_fib_2(self):
        for i in range(0, 37):
            #iterate through the range and for each value print the value and verbal text equivalant
            fibval, results = self.engine(i)
            #fromengine = fibval
            print(i, "-", fibval, "-", results.capitalize())

    def engine(self, fibval):
        fibval = (fibFuncs.fibLooping(fibval))  # seting fibval to the value in the nth position (zero based) in fibFuncs
        results = self.getresults(fibval)
        return fibval, results

    def getresults(self, fibval):
        if fibval <=10:
            intval = self.theones(fibval)
        elif fibval < 20:
            intval = self.theteens(fibval)
        elif fibval < 100:
            intval = self.thetens(fibval)
        elif fibval < 1000:
            intval = self.thehundreds(fibval)
        elif fibval < 10000:
            intval = self.thethousands(fibval)
        elif fibval <100000:
            intval = self.thetenthousands(fibval)
        elif fibval <1000000:
            intval = self.thehundredthousands(fibval)
        elif fibval <10000000:
            intval = self.themillions(fibval)
        elif fibval <100000000:
            intval = self.theteenmillions(fibval)
        elif fibval <1000000000:
            intval = self.thetrillions(fibval)
        return intval

    # ones
    def theones(self, fibval) -> str:
        intval = ones.get(int(fibval))
        return intval

    # teens
    def theteens(self, fibval) -> str:
        intval = teens.get(int(fibval))
        return intval

    # tens
    def thetens(self, fibval) -> str:
        intval = []
        intval += str(fibval)

        indexzero = tens.get(int(intval[0]))
        indexone = ones.get(int(intval[1]))

        intval = f"{indexzero} {indexone}"
        return intval

    # humdreds
    def thehundreds(self, fibval) -> str:
        intval = []
        intval += str(fibval)

        indexzero = hundreds.get(int(intval[0]))
        indexone = tens.get(int(intval[1]))
        indextwo = ones.get(int(intval[2]))

        intval = f"{indexzero} {indexone} {indextwo}"
        return intval

    # thousands
    def thethousands(self, fibval) -> str:
        intval = []
        intval += str(fibval)

        indexzero = thousands.get(int(intval[0]))
        indexone = hundreds.get(int(intval[1]))
        indextwo = tens.get(int(intval[2]))
        indexthree = ones.get(int(intval[3]))

        intval = f"{indexzero} {indexone} {indextwo} {indexthree}"
        return intval

    # tenthousands
    def thetenthousands(self, fibval) -> str:
        intval = []
        intval += str(fibval)

        indexzero = tenthousands.get(int(intval[0]))    # 1
        indexone = thousands.get(int(intval[1]))        # 7
        indextwo = hundreds.get(int(intval[2]))         # 7
        indexthree = tens.get(int(intval[3]))           # 1
        indexfour = ones.get(int(intval[4]))            # 1

        firstwo = int(str(fibval)[:2])                  # Seventeen
        lastwo = int(str(fibval)[-2:])                  # Eleven
        indexteens = teens.get(int(firstwo))
        subindex2 = teens.get(int(lastwo))

        if firstwo <20 and lastwo <20:
            intval = f"{indexteens} Thousand {indextwo} {subindex2}"
            return intval
        elif indexone =='' and lastwo <20:
            intval = f"{indexzero} {indextwo} {indexthree} {indexfour}"
            return intval
        elif firstwo <100:
            indexzero = tens.get(int(intval[0]))
            indexone = ones.get(int(intval[1]))
            indextwo = hundreds.get(int(intval[2]))
            if lastwo <20:
                index = teens.get(int(lastwo))
                intval = f"{indexzero} {indexone} Thousand {indextwo} {index}"
            else:
                indexthree = tens.get(int(intval[3]))
                indexfour = ones.get(int(intval[4]))
                intval = f"{indexzero} {indexone} Thousand {indextwo} {indexthree} {indexfour}"
            return intval

    # hundredthousand
    def thehundredthousands(self, fibval) -> str:
        intval = []
        intval += str(fibval)

        indexzero = hundredthousands.get(int(intval[0]))    # 3
        indexone = tens.get(int(intval[1]))         # 1
        indextwo = ones.get(int(intval[2]))            # 7
        indexthree = hundreds.get(int(intval[3]))           # 8
        indexfour = tens.get(int(intval[4]))                # 1
        indexfive = ones.get(int(intval[5]))                # 1

        second = int(str(intval[1]))
        third = int(str(intval[2]))
        secondthird = (second*10+third)
        index23 = teens.get(int(secondthird))

        lastwo = int(str(fibval)[-2:])
        indexteens = teens.get(int(lastwo))

        if secondthird <20 and lastwo <20:
            intval = f"{indexzero} {index23} Thousand {indexthree} {indexteens}"
        elif secondthird <20:
            intval = f"{indexzero} {index23} Thousand {indexthree} {indexfour} {indexfive}"
        elif secondthird >19 and lastwo <20:
            intval = f"{indexzero} {indexone} {indextwo} Thousand {indexthree} {indexteens}"
        elif secondthird >19:
            intval = f"{indexzero} {indexone} {indextwo} Thousand {indexthree} {indexfour} {indexfive}"
        return intval

    # millions
    def themillions(self, fibval) -> str:
        intval = []
        intval += str(fibval)

        firstwo = int(str(fibval)[:2])
        indexteens = teens.get(int(firstwo))

        indexzero = biggy.get(int(intval[0]))  # 1
        indexone = hundreds.get(int(intval[1])) # 7
        indextwo = tens.get(int(intval[2]))   # 8
        indexthree = ones.get(int(intval[3]))   # 1
        indexfour = hundreds.get(int(intval[4]))   # 1
        indexfive = tens.get(int(intval[5]))
        indexsix = ones.get(int(intval[6]))

        digits = len(intval)

        if digits <8:
            intval = f"{indexzero} Million {indexone} {indextwo} {indexthree} Thousand {indexfour} {indexfive} {indexsix}"
        elif digits >7 and firstwo <10:
            intval = f"{indexteens} Million {indextwo} {indexthree} {indexfour} Thousand {indexfive} {indexsix} {indexseven}"
        return intval

    # teenmillions
    def theteenmillions(self, fibval) -> str:
        intval = []
        intval += str(fibval)

        indexzero = ones.get(int(intval[0]))  # 1
        indexone = ones.get(int(intval[1]))  # 7
        indextwo = hundreds.get(int(intval[2]))
        indexthree = tens.get(int(intval[3]))  # 8
        indexfour = ones.get(int(intval[4]))  # 1
        indexfive = hundreds.get(int(intval[5]))  # 1
        indexsix = tens.get(int(intval[6]))
        indexseven = ones.get(int(intval[7]))

        firstwo = int(str(fibval)[2:])
        indexteens = teens.get(int(firstwo))

        intval = f"{indexteens} Million {indextwo} {indexthree} {indexfour} Thousand {indexfive} {indexsix} {indexseven}"
        return intval


"""
    # trillions
    def thetrillions(self, fibval) -> str:
        intval = []
        intval += str(fibval)

        indexzero = million.get(int(intval[0]))
        indexone = hundredthousands.get(int(intval[1]))  # 3
        indextwo = tens.get(int(intval[2]))  # 1
        indexthree = ones.get(int(intval[3]))  # 7
        indexfour = hundreds.get(int(intval[4]))  # 8
        indexfive = tens.get(int(intval[5]))  # 1
        indexsix = ones.get(int(intval[6]))  # 1

        return intval



 #def setUp(self):
 #   self.driver = webdriver.Chrome("../chromedriver.exe")

#def tearDown(self):
#    self.driver.close()

def test_fib_2(self):
    # fibval = (fibFuncs.fibLooping(9))  # seting fibval to the value in the nth position (zero based) in fibFuncs
    # results = self.getresults(fibval)
    # print(fibval, "-", results)
    for i in range(0,32):
        #iterate through the range and for each value print the value and verbal text equivalant
        results = self.engine(i)
        print(i, "-", results)
        
        subindex = ones.get(int(lastwo))
        subindex2 = teens.get(int(lastwo))

        if lastwo <20:
            debug = (fibval, "-", indexzero, indexone, indextwo, "Thousand", indexthree, indexteens)
            print(debug)
        else:
            debug = (fibval, "-", indexzero, indexone, indextwo, "Thousand", indexthree, indexfour, indexfive)
            print(debug)

        if firstwo <20 and lastwo <20:
            debug = (fibval, "-", indexteens, "Thousand", indextwo, subindex2)
            print(debug)
        elif indexone =='' and lastwo <20:
            debug = (fibval, "-", indexzero, indextwo, indexthree, indexfour)
            print(debug)
        elif firsthree <1000:
            if secondthird <20:
                indexzero = tens.get(int(intval[0]))
                index23 = teens.get(int(secondthird))

            indexone = ones.get(int(intval[1]))
            indextwo = hundreds.get(int(intval[2]))

            if lastwo <20:
                index = teens.get(int(lastwo))
                debug = (fibval, "'-",indexzero, indexone, "Thousand", indextwo, teens)
            else:
                indexthree = tens.get(int(intval[3]))
                indexfour = ones.get(int(intval[4]))
                debug = (fibval, "-", indexzero, indexone, "Thousand",indextwo, indexthree, indexfour)
                print(debug)
    
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