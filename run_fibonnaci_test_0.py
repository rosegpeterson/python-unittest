# test unittest for fib function
import unittest
from fibonnaci_test import fib
import sys
	
if __name__ == '__main__':
    #assert fib(5) ==  [0]
    assert fib(5) ==  [0, 1, 1, 2, 3, 5]


"""
Testing first one ->
└─ $ ▶ python run_fibonnaci_test_0.py
fib =  [0, 1, 1, 2, 3, 5]
Traceback (most recent call last):
  File "run_fibonnaci_test_0.py", line 7, in <module>
    assert fib(5) ==  2
AssertionError

testing good ->
(base) salsa @ tango ~/myrepo/python
└─ $ ▶ python run_fibonnaci_test_0.py
fib =  [0, 1, 1, 2, 3, 5]
"""


