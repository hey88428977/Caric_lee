# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://mail.qq.com/cgi-bin/frame_html?sid=hDvKiuRm-R7CFARe&r=959450726b2fd63b1906c38254e95fc0")
# 为了调试方便，等待十秒，手动点登录
time.sleep(10)
driver.find_element_by_id("composebtn").click()
time.sleep(2)

driver.switch_to_frame("mainFrame")
# driver.find_element_by_css_selector("#scAreaCtrl>.addr_text>.js_input").send_keys("122@qq.com")
time.sleep(2)
driver.find_element_by_id("subject").send_keys("主题")
time.sleep(2)

# 第二次切换iframe
elem = driver.find_element_by_xpath("//iframe")
driver.switch_to_frame(elem)
driver.find_element_by_css_selector("[accesskey='q']").send_keys("正文")




