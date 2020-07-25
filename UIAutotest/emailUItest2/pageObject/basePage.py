# -*- encoding: utf-8 -*-
'''
@File    :   basePage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/26 0026 10:24   dmk      1.0         None
'''

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utils.log import logger
from utils.config import IMAGE_PATH

class Action(object):

    def __init__(self,driver):
        self.driver = driver
        self.refresh_bro()
        self.timeout = 10
        self.t = 0.5
        # 主frame
        self.mainFrame_loc = (By.XPATH, "//iframe[@id='businessList']")
        #邮件主体frame
        self.emailBodyFrame_loc = (By.XPATH,"//iframe[@class='mail_iframe_vue']")
        #邮件编辑器
        self.emailEditFrame_loc = (By.XPATH,"//iframe[@class='cke_wysiwyg_frame cke_reset']")
        # 邮件首页
        self.emailHomePage_loc = (By.XPATH, "//div[text()='邮件首页']")
        # 写邮件按钮
        self.writeEmail_loc = (By.XPATH, "//button[@class='el-button el-tooltip item email_write_btn f12 el-button--primary']")
        #收件箱
        self.receiptBox_loc = (By.XPATH,"//span[text()='收件箱']")
        #草稿箱
        self.draftBox_loc = (By.XPATH,"//span[text()='草稿箱']")
        # 群发箱
        self.massBox_loc = (By.XPATH, "//span[text()='群发箱']")
        # toast提示
        self.toast_loc = (By.XPATH, "//p[@class='el-message__content']")

    #定义获取元素
    def find_element(self,*loc,index=0):
        wait = WebDriverWait(self.driver, self.timeout, self.t)
        if isinstance(index,int):
            return wait.until(EC.visibility_of_any_elements_located(*loc))[index]
        else:
            return wait.until(EC.visibility_of_any_elements_located(*loc))


    def find_element_byPresence(self,*loc,index=0):
        wait = WebDriverWait(self.driver, self.timeout, self.t)
        if isinstance(index,int):
            return wait.until(EC.presence_of_all_elements_located(*loc))[index]
        else:
            return wait.until(EC.presence_of_all_elements_located(*loc))


    #判断元素是否可见
    def is_visible(self,*loc,visibility=True):
        if visibility:
            return WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located(*loc))
        else:
            return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(*loc))

    #重写发送文本的方法
    def send(self,*loc,key,clear=1):
        if clear:
            self.find(*loc).clear().send_keys(key)
        else:
            self.find(*loc).send_keys(key)

    #切换frame



    #获取元素文本
    def get_elementText(self,*loc,index=0):
        elements = self.find_element(*loc,index="all")
        if isinstance(index,int):
            return elements[index].text
        else:
            text = []
            for element in elements:
                text.append(element.text)
            return text

    # 点击元素
    def click_ele(self, *loc):
        # 先滚动元素
        self.scroll_element(*loc)
        time.sleep(0.5)
        self.find_element(*loc).click()

    # 输入内容
    def sendKeys(self, *loc, key, clear=1):
        # 先滚动元素
        self.scroll_element(*loc)
        time.sleep(0.5)
        # 默认清空输入框
        ele = self.find_element(*loc)
        if clear:
            ele.clear()
        time.sleep(0.3)
        ele.send_keys(key)


    #鼠标悬浮操作
    def mouseHover(self,*loc):
        ele = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(*loc))
        ActionChains(self.driver).move_to_element(ele).perform()

    #鼠标点击操作
    def mouseClick(self,*loc):
        self.scroll_element(*loc)
        ele = self.find_element(*loc)
        ActionChains(self.driver).click(ele).perform()

    # 鼠标双击操作
    def mouseDoubleClick(self, *loc):
        self.scroll_element(*loc)
        ele = self.find_element(*loc)
        ActionChains(self.driver).double_click(ele).perform()

    # # 鼠标悬停操作
    # def mouseHover(driver, element):
    #     ActionChains(driver).move_to_element(element).perform()
    #
    # # 鼠标点击操作
    # def mouseClick(driver, element):
    #     ActionChains(driver).click(element).perform()
    #
    # # 鼠标双击操作
    # def mouseDoubleClick(driver, element):
    #     ActionChains(driver).double_click(element).perform()
    #切换frame
    def switch_frame(self,*loc):
        return EC.frame_to_be_available_and_switch_to_it(*loc)(self.driver)

    #切回父frame
    def switch_parentFrame(self):
        print("切回父frame")
        self.driver.switch_to.parent_frame()

    #切回主文档
    def switch_mainPage(self):
        print("切回主文档")
        self.driver.switch_to.default_content()

    #刷新浏览器
    def refresh_bro(self,frame=1):
        mainFrame_loc = (By.XPATH, "//iframe[@id='businessList']")
        self.driver.refresh()
        # try:
        #     time.sleep(2)
        #     ele = self.driver.switch_to_alert()
        #     ele.accept()
        #     time.sleep(1)
        # except Exception as e:
        #     print("没有捕获到弹窗")
        #判断是否有弹窗
        time.sleep(2)
        alert = EC.alert_is_present()(self.driver)
        if alert:
            alert.accept()
        if frame == 1:
            EC.frame_to_be_available_and_switch_to_it(mainFrame_loc)(self.driver)

    #判断元素是否存在
    def is_element_exist(self,xpath):
        s = self.driver.find_elements_by_xpath(xpath)
        if len(s) == 0:
            print("元素未找到:%s" % xpath)
            return False
        else:
            print("一共找到{}个元素".format(len(s)))
            return s


    #滚动元素到指定位置，以点击
    def scroll_element(self,*loc):
        ele = self.find_element(*loc)
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, ele)

    #保存截图
    def screenshotImg(self,key=None):
        nowTime = time.strftime("%Y%m%d.%H.%M.%S")
        logger.info("保存的图片：{}/{}-{}.png".format(IMAGE_PATH, nowTime, key))
        self.driver.get_screenshot_as_file("{}/{}-{}.png".format(IMAGE_PATH, nowTime, key))