# coding:utf-8
from page.loginpage import LoginPage
from selenium import webdriver
import unittest
import ddt

# 参数和代码分离
testdata = [
        {"username": "admin", "psw": "123456", "result": "admin"},
        {"username": "admin1", "psw": "123456", "result": ""},
        {"username": "admin2", "psw": "111111",  "result": "admin2"},
        {"username": "admin3", "psw": "111111",  "result": "admin3"},
        {"username": "admin", "psw": "123456", "result": "admin"},
        {"username": "admin1", "psw": "123456", "result": ""},
        {"username": "admin2", "psw": "111111",  "result": "admin2"},
        {"username": "admin3", "psw": "111111",  "result": "admin3"},
]

@ddt.ddt
class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("开始测试")

    @ddt.data(*testdata)
    def test_login_01(self, canshu):
        print(canshu)
        print("账号：%s" % canshu["username"])
        print("密码：%s" % canshu["psw"])
        print("结果：%s" % canshu["result"])

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        print("结束")

if __name__ == "__main__":
    unittest.main()









