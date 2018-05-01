# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.cnblogs.com/yoyoketang/p/")
time.sleep(3)

ele = driver.find_element_by_xpath("//h3[text()='最新评论']")
driver.execute_script("arguments[0].scrollIntoView();", ele)




