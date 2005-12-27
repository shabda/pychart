import sys
import unittest

sys.path.append('..')
from pychart import *

class TestChartObject(unittest.TestCase):
    def test(self):
        b = bar_plot.T()
        b.label = "unknown"
        ok = False
        try:
            b.label = 10
        except TypeError:
            ok = True
        self.failUnless(ok)
        ok = False
        try:
            b.foobar = 999
        except Exception:
            ok = True
        self.failUnless(ok)
        
    def runTest(self):
        self.test()
if __name__ == '__main__':
    unittest.main()        
