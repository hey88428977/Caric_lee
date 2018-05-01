# coding:utf-8
import unittest
# help(unittest)
class IntegerArithmeticTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def testAdd(self):  # test method names begin with 'test'
        '''aa'''
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 3)   # 一个测试用例里面可以有多个断言

    def testMultiply(self):
        '''aa'''
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

if __name__ == '__main__':
    unittest.main()