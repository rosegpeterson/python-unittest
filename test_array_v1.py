#!/usr/bin/python3
#unit test

import unittest

def is_fiveMulp(number):
    """Return True if *number* is fiveMulp."""
    for element in range(number):
       if number % 5 == 0:
          return True
       return False

def is_fiveCount(number):
    """Return True if *number* is 5"""
    if number == 5:
       return True
    return False


class FiveTestCase(unittest.TestCase):
    def test_is_fiveMulp(self):
        """Is 10 successfully determined to be 5number?"""
        self.assertTrue(is_fiveMulp(10))

class CountFiveTestCase(unittest.TestCase):
    def test_is_countFives(self):
        """Is 5 successfully determined to be number of multiple of fives ?"""
        self.assertTrue(is_fiveCount(5))

if __name__ == '__main__':
    unittest.main()

