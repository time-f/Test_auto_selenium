# 导包
import unittest
from day05.test01_testcase import TestAdd
from day05.test02_testcase2 import TestSub

# 创建测试套件对象
suite = unittest.TestSuite()

# 添加测试用例
# 添加指定的类中的指定的测试方法
suite.addTest(TestAdd("test_add01"))
suite.addTest(TestAdd("test_add02"))

# 添加指定测试类中的所有的测试方法
suite.addTest(unittest.makeSuite(TestSub))


# 创建运行器对象
runner = unittest.TextTestRunner()
runner.run(suite)


