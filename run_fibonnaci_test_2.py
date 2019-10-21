# test unittest for fib function
import unittest
from fibonnaci_test import fib
import sys
	
class FibonacciTest(unittest.TestCase):
	
    # hook method for setting up the test fixture
    def setUp(self):
        self.fib_elems = ( (5,'[0, 1, 1, 2, 3, 5]'), (10,55) )
        print ("setup executed")
    	
    def testFib(self):
        for (i,val) in self.fib_elems:
            print("aca",i,val)
            self.assertEqual(fib(i), val)
    	
    def testFib2(self):
        for (i,val) in self.fib_elems:
            self.assertEqual(fib(i), val)
    	
    # hook method for descontructing the class fixture after run test
    def tearDown(self):
        self.fib_elems = None
        print ("tearDown executed")
	
if __name__ == '__main__':
    unittest.main()

"""
└─ $ ▶ python run_fibonnaci_test_2.py
setup executed
aca 5 [0, 1, 1, 2, 3, 5]
fib =  [0, 1, 1, 2, 3, 5]
tearDown executed
Fsetup executed
fib =  [0, 1, 1, 2, 3, 5]
tearDown executed
F
======================================================================
FAIL: testFib (__main__.FibonacciTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "run_fibonnaci_test_2.py", line 16, in testFib
    self.assertEqual(fib(i), val)
AssertionError: [0, 1, 1, 2, 3, 5] != '[0, 1, 1, 2, 3, 5]'

======================================================================
FAIL: testFib2 (__main__.FibonacciTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "run_fibonnaci_test_2.py", line 20, in testFib2
    self.assertEqual(fib(i), val)
AssertionError: [0, 1, 1, 2, 3, 5] != '[0, 1, 1, 2, 3, 5]'

----------------------------------------------------------------------
Ran 2 tests in 0.004s

FAILED (failures=2)
"""
