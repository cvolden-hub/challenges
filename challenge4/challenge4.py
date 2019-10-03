import unittest

from selenium import webdriver

from time import sleep

class Challenge4FibSequence(unittest.TestCase):


    def fibSeq(n):
        n = 5

        if n == 0:
            return n
        if n == 1
            return 1
        else:
            return fibSeq(n-1) + fibSeq(n-2)

            #if n <= 1:
                #return n
            #else:
                #return(recur_fibo(n-1) + recur_fibo(n-2))


if __name__ == '__main__':
    unittest.main()