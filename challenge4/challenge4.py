
# For this challenge, we are going to:
# write a function that display the fibonacci sequence up to a certain number.
# If I want the fibonacci for the 9 order of the sequence, I should see 21.
# Keep your function to calculate the fibonacci sequence separate from the file that has the unittest.main().
# see fibFuncs

# However, to add additional challenge to this challenge, instead of displaying the number 21,
# I want the string # representation of twenty one.
# This will require you to use string concatenation to print out the string.


import unittest
from challenges.challenge4 import fibFuncs


class Challenge4(unittest.TestCase):

    def test_challange4(self):
        answer = fibFuncs.fiblooping(15)

        # adding this see if function is working how i expect.  I suppose I could run debug as well
        print(answer)

#now look at using an array or tuple or dictionary?

if __name__ == '__main__':
    unittest.main()