import unittest
from selenium import webdriver

class Restaurant(object):
    bankrupt = False
    def open_branch(self):
        if not self.bankrupt:
            print("branch opened")

    x = Restaurant()
    x.bankrupt

    Restaurant().bankrupt


if __name__ == '__main__':
    unittest.main()