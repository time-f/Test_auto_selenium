# 实现加法操作
def add(x, y):
    return x + y


# 1. 导包
import unittest

# 2. 定义测试类
# 建议类名以Test开头
# 必须要继承unittest.TestCase
class TestAdd(unittest.TestCase):

    # 3. 定义测试方法
    # 测试的方法名必须以test开头
    def test_add01(self):
        result = add(1, 1)
        print("result111=", result)


    def test_add02(self):
        result = add(1, 2)
        print("result222=", result)



if __name__ == '__main__':
    unittest.main()

