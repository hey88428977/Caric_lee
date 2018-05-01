# coding:utf-8

from selenium import webdriver
import time
# 加载配置文件，免登录
profilepath = r"C:\Users\Gloria\AppData\Roaming\Mozilla\Firefox\Profiles\1x41j9of.default"
profile = webdriver.FirefoxProfile(profilepath)
driver = webdriver.Firefox(profile)

# 为了调试方便，直接进编辑界面
driver.get("https://i.cnblogs.com/EditPosts.aspx?opt=1")
time.sleep(2)
bodytext = "好123"
js_edit = "document.getElementById('Editor_Edit_EditorBody_ifr').contentWindow.document.body.innerHTML='%s'" % bodytext
js_edit1 = "document.getElementById('Editor_Edit_EditorBody_ifr').contentWindow.document.getElementById('tinymce').innerHTML='hao123'"
driver.execute_script(js_edit)
