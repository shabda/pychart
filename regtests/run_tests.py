import unittest
import font_regtest
import chart_object_regtest
import chart_data_regtest

suite = unittest.TestSuite()
suite.addTest(font_regtest.TestFonts())
suite.addTest(chart_object_regtest.TestChartObject())
suite.addTest(chart_data_regtest.TestChartData())
unittest.TextTestRunner().run(suite)
