#coding:utf-8
from selenium import webdriver # 导入webdriver包
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://ceshilogin.joinf.com/login/")
time.sleep(5)
driver.find_element_by_id("loginID").send_keys("7777")
driver.find_element_by_id("loginPassword").send_keys("123456")
driver.find_element_by_id("loginBtn").click()

time.sleep(5)
driver.get("https://customcn.joinf.com/customs")
h1=driver.current_window_handle
print(h1)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/div[1]/div[3]/div/div[1]/div/div/input').send_keys('led')
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/div[1]/div[3]/div/div[1]/button').click()
time.sleep(5)
target = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/div[6]/div/div[2]/div/div[1]/div[3]/table/tbody/tr[3]/td[13]/div/a')
driver.execute_script("arguments[0].scrollIntoView();", target)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/div[6]/div/div[2]/div/div[1]/div[3]/table/tbody/tr[20]/td[8]/div/a').click()
time.sleep(2)
h2=driver.current_window_handle
print(h2)
driver.switch_to.window(h2)

#driver.get_screenshot_as_file("C:\\Users\\WIN7\\Desktop\\1.jpg")