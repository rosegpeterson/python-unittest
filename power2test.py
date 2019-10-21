#!/usr/bin/python
import unittest
import sys
sys.path.append('/home/salsa/myrepo/Scripts')
from power2 import power2


def is_power2():
    #expected result
    expRes = ['1 sum = 1', '2 sum = 3', '4 sum = 7', '8 sum = 15', '16 sum = 31', '32 sum = 63', '64 sum = 127', '128 sum = 255', '256 sum = 511']
    powerRes = power2()
    print "Comparing result: ", powerRes, " = ", expRes
    if expRes == powerRes:
        return True
    else:
        return False

class PowerCases(unittest.TestCase):

    def test_power(self):
        self.assertTrue(is_power2())


if __name__ == '__main__':
    # to run a simple run: unittest.main()
    # to run suite
    suite = unittest.TestLoader().loadTestsFromTestCase(PowerCases)
    unittest.TextTestRunner(verbosity=2).run(suite)



