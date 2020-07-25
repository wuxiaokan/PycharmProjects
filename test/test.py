#coding:utf-8
from selenium import webdriver # 导入webdriver包
import time
import allure
import pytest
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
time.sleep(2)
driver.find_element_by_id('kw').send_keys('python')
time.sleep(2)
driver.find_element_by_id('su').click()
time.sleep(2)
#聚焦元素 下拉滚动条
target = driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]')
driver.execute_script("arguments[0].scrollIntoView();", target)
time.sleep(2)
#记录第一个窗口
window_1 = driver.current_window_handle
#点击python百度百科
driver.find_element_by_xpath('//*[@id="2"]/h3/a').click()
print(driver.title)
time.sleep(3)

#tab标签切换
# window_2 = driver.current_window_handle
#
# windows = driver.window_handles
# for current_window in windows:
#     if current_window != windows[0]:
#         driver.switch_to.window(current_window)
#         #获取百度百科页面的title
#         print(driver.title)
# time.sleep(3)
#
# #返回首页句柄
# driver.switch_to.window(windows[0])
# time.sleep(3)
# print(driver.title)
#
#
# #关闭浏览器
# driver.quit()


# print("hello,python")
# print(1+2)
# name=input()
# print name
# a=1
# print(a)


