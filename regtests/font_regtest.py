import sys
import unittest

sys.path.append('..')
from pychart import *

class TestFonts(unittest.TestCase):
    def __draw_invalid_string(self, s):
        got_exception = False
        try:
            self.__canvas.show(0, 0, s)
        except font.FontException, e:
            print "Got font exception [%s] for [%s] (this is expected)" % (e, s)
            got_exception = True
        self.failUnless(got_exception)
    def setUp(self):
        self.__canvas = canvas.init("/dev/null", "pdf")
    def test(self):
        
        self.__canvas.show(0, 0, 'blahblah')
        self.__draw_invalid_string('/<<')
        self.__draw_invalid_string('/hccc')
        self.__canvas.show(0, 0, '/hCfoo')
        self.__draw_invalid_string('/hCfoo/hLbar')
        self.__canvas.show(0, 0, '/vTfoo')
        self.__draw_invalid_string('/vMfoo/vTbar')
    def runTest(self):
        self.test()
        
if __name__ == '__main__':
    unittest.main()        
