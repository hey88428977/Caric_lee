from selenium import webdriver
import time
# 加载配置文件，免登录
driver = webdriver.Firefox()

# 为了调试方便，直接进编辑界面
driver.get("https://kyfw.12306.cn/otn/index/init")
# id是python里面的保留关键字
id_ = "train_date"
js = 'document.getElementById("train_date").removeAttribute("readonly");' \
     'document.getElementById("train_date").value="2016-12-15"'


driver.execute_script(js)

# js1 = 'document.getElementById("train_date").value="2016-12-15"'

# 清空文本输入内容
driver.find_element_by_id("train_date").clear()
driver.find_element_by_id("train_date").send_keys("2018-04-02")