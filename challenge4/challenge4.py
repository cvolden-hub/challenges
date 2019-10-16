
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

    def test_challange4(self):
        #timestoloop = 9     # change this value

        #for i in range(timestoloop):
            #print(fibFuncs.fibLooping(i))   # using print function to display fib sequnece
            #print(fibFuncs.fibLooping(8))   # using the print function to display specific value, zero based
            #answer = (fibFuncs.fibLooping(i))  # setting answer = to the value of i
        answer2 = (fibFuncs.fibLooping(8))  # seting answer2 to the value in the nth position (zero based) in fibFuncs
            #print(answer)   # using print function to display name
        #print(answer2)

       #o
        # nesplace values
        onesplace = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
                    10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
                    17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twendy', 21: 'Twenty One'}

        #tenslace vaues
        tensplace = {20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
                     90: 'Ninety'}

        #hundredsplace values
        hundredsplace = ["One Hundred", "Two Hundred", "Three Hundred", "Foru Hundred", "Five Hundred", "Six Hundred",
                         "Seven Hundred", "Eight Hundred", "Nine Hundred"]
        i = 0

        if answer2 < 22:
            intval = onesplace.get(int(answer2))
            print(answer2, "-", str(intval))
        else:
            intval = tensplace.get[int(answer2[int(i)])]
            #print(intval)
            print(answer2, "-", str(intval))

"""
    def number(Number):
        if 1 <= answer2 < 19:  #change Number to answer
            return onesplace[Number]
        elif 20 <= answer2 <= 99:  #change Number to answer
            tens, below_ten = divmod(Number, 10)
            print(return tensplace[tens - 2] + ' ' + onesplace[below_ten])  #SO HOW DO I GET THIS VALUE INTO FUNCTIO
        else:
            print("Number out of range")
        print(Number) 


    number(Number)
"""

if __name__ == '__main__':
    unittest.main()