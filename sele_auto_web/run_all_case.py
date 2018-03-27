#coding=utf-8
'''
'''
import unittest
def all_case():
    '''加载所有的测试用例'''
    # 待执行用例的目录
    case_dir = "D:/s15/case"

    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,
                                               pattern="test*.py",
                                               top_level_dir=None)
    # 直接加载discover    这个方法兼容py2 和py3
    testcase.addTests(discover)
    print(testcase)
    return testcase
if __name__ == '__main__':
    # 返回实例
    # runner = unittest.TextTestRunner()

    # 生成报告
    import HTMLTestRunner_jpg
    report_path = "D:/s15/report/result.html"

    fp =open(report_path, "wb")
    runner = HTMLTestRunner_jpg.HTMLTestRunner(
                    stream=fp,  # 测试报告写入文件的存储区域
                    title='这是我的自动化测试报告',  # 测试报告的主题
                    description='用例执行情况：'   # 测试报告的描述
    )
    # run所有用例
    runner.run(all_case())
    fp.close()