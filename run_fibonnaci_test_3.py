# test unittest for fib function
import unittest
from fibonnaci_test import fib
import sys
	
def is_fibonaci():
    #expected result
    expRes = [0, 1, 1, 2, 3, 5]
    fibRes=list(fib(5))
    print("Comparing result: ", expRes, " = ", fibRes)
    if expRes == fibRes:
        return True
    else:
        return False

class FibonacciTest(unittest.TestCase):
	
    def testFIb(self):
        #self.assertEqual(fib(0), 0)
        self.assertTrue(is_fibonaci())
	
# to run suite
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FibonacciTest)
    unittest.TextTestRunner(verbosity=2).run(suite)


"""
└─ $ ▶ python run_fibonnaci_test_3.py
testFIb (__main__.FibonacciTest) ... fib =  [0, 1, 1, 2, 3, 5]
Comparing result:  [0, 1, 1, 2, 3, 5]  =  [0, 1, 1, 2, 3, 5]
ok

----------------------------------------------------------------------
Ran 1 test in 0.002s

OK

"""
