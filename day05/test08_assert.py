import unittest


# 实现加法操作
def add(x, y):
    return x + y


class TestAssert(unittest.TestCase):

    def test_add01(self):
        result = add(1, 1)
        self.assertEqual(result, 2)

    def test_add02(self):
        result = add(1, 2)
        is_ok = result == 3
        self.assertTrue(is_ok)



"""

class TestAssert(unittest.TestCase):

    def add01(self):

        try:
            self.add02()
        except :
            pass
            raise



    def add02(self):

        try:
            pass
            # .....
        except Exception as e:
            pass
            raise

"""