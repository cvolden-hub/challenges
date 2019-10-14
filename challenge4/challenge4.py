
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
        timestoloop = 9

        for i in range(timestoloop):
            #print(fibFuncs.fibLooping(i))
            answer = (fibFuncs.fibLooping(i))
            print(answer)

    i = 0
    intval = " "
    nword = str(result)

    onesplace = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
                 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
                 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}

    tensplace = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

    def number(Number):
        if 1 <= Number < 19:
            return onesplace[Number]
        elif 20 <= Number <= 99:
            tens, below_ten = divmod(Number, 10)
            return tensplace[tens - 2] + ' ' + onesplace[below_ten]
        else:
            print("Number out of range")
        print()

if __name__ == '__main__':
    unittest.main()