# test unittest for fib function
import unittest
from fibonnaci_test import fib
import sys
	
class FibonacciTest(unittest.TestCase):
	
    def testFIb(self):
        #self.assertEqual(fib(0), 0)
        self.assertEqual(fib(5), [0, 1, 1, 2, 3, 5])
	
if __name__ == '__main__':
    unittest.main()

"""
b =  [0, 1, 1, 2, 3, 5]
F
======================================================================
FAIL: testFIb (__main__.FibonacciTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "run_fibonnaci_test.py", line 10, in testFIb
    self.assertEqual(fib(5), '[0, 1, 1, 2, 3, 5]')
AssertionError: [0, 1, 1, 2, 3, 5] != '[0, 1, 1, 2, 3, 5]'

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
(base) user1 @ tango ~/myrepo/python
└─ $ ▶ python run_fibonnaci_test.py
fib =  [0, 1, 1, 2, 3, 5]
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
"""
