
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
            #print (answer)
            something = self.intWrd((answer)

    def intWrd (self, result):
        i = 0
        intval = " "
        nword = str(result)

        ones = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9: "nine",}
        tens = {0:"", 1:"ten", 2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty"}
        dterms = {0:"",1:""}

    def len (self, nword):
        if int(nword) <20:
            intval = ones.get(int(nword))
        else int(nword):
            intval = tens.get[int(nword[int(i)])]
            i += 1
            intval += less

    intWard

if __name__ == '__main__':
    unittest.main()