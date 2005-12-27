import sys
import unittest
import random
import tempfile
import os

sys.path.append('..')
from pychart import *

class TestChartData(unittest.TestCase):
    def test(self):
        try:
            data = [[5,10], [6,13], [8,165]]

            # pass a file object.
            n, path = tempfile.mkstemp()
            fd = os.fdopen(n, "w")
            chart_data.write_csv(fd, data)
            fd.close()
            
            # pass a pathname.
            n, path2 = tempfile.mkstemp()
            os.fdopen(n, "w").close()
            chart_data.write_csv(path2, data)

            if os.WEXITSTATUS(os.system("cmp %s %s" % (path, path2))) != 0:
                self.fail("write_csv failed. Results are in %s and %s"
                          % (path, path2))
            print "Wrote on ", path, path2
            
            data2 = chart_data.read_csv(path, "%d,%d")
            self.failUnless(data == data2)

            fd = open(path2)
            data2 = chart_data.read_csv(fd, "%d,%d")
            self.failUnless(data == data2)
            
        finally:
            os.unlink(path)
            os.unlink(path2)
    def runTest(self):
        self.test()
if __name__ == '__main__':
    unittest.main()        
