import unittest

from day05.case.test_01 import Test01
from day05.case.test_02 import Test02
from day05.case.test_03 import Test03
from day05.case.test_04 import Test04
from day05.case.test_05 import Test05
from day05.case.test_06 import Test06
from day05.case.test_07 import Test07
from day05.case.test_08 import Test08
from day05.case.test_09 import Test09
from day05.case.test_10 import Test10

# suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite(Test01))
# suite.addTest(unittest.makeSuite(Test02))
# suite.addTest(unittest.makeSuite(Test03))
# suite.addTest(unittest.makeSuite(Test04))
# suite.addTest(unittest.makeSuite(Test05))
# suite.addTest(unittest.makeSuite(Test06))
# suite.addTest(unittest.makeSuite(Test07))
# suite.addTest(unittest.makeSuite(Test08))
# suite.addTest(unittest.makeSuite(Test09))
# suite.addTest(unittest.makeSuite(Test10))
# unittest.TextTestRunner().run(suite)


# 通过TestLoader自动扫描测试用例
# suite = unittest.TestLoader().discover("./case/", pattern="test*.py")
suite = unittest.defaultTestLoader.discover("./case/", pattern="test*.py")
unittest.TextTestRunner().run(suite)

