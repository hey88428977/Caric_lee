# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.cnblogs.com/yoyoketang/p/")
time.sleep(3)

# # 只在火狐生效，chrome不生效的
# js1 = "document.documentElement.scrollTop=10000" # python里面是str
# driver.execute_script(js1)
# # chrome上生效的
# js_chrome = "document.body.scrollTop=10000"
# driver.execute_script(js1)

# 两个浏览器都生效
# js_all = "window.scrollTo(0,10000);"
# driver.execute_script(js_all)

# 自动获取高度
js_heig = "window.scrollTo(0, document.body.scrollHeight)"
driver.execute_script(js_heig)





