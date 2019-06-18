# 1. 导包
import unittest


# 2. 定义测试类
# 建议类名以Test开头
# 必须要继承unittest.TestCase
class TestSub(unittest.TestCase):

    # 3. 定义测试方法
    # 测试的方法名必须以test开头
    def test_sub01(self):
        print("test_sub01")


    def test_sub02(self):
        print("test_sub02")
