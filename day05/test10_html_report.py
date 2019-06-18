import time
import unittest

from day05.test01_testcase import TestAdd
from day05.test09_login2 import TestLogin2
from day05.tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestAdd))
suite.addTest(unittest.makeSuite(TestLogin2))

# 定义测试报告文件
report_path = "./report/{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
with open(report_path, "wb") as f:
    # 创建HTMLTestRunner运行器
    runner = HTMLTestRunner(f, title="TPshopWeb自动化测试报告", description="Win10.Firefox")
    runner.run(suite)


