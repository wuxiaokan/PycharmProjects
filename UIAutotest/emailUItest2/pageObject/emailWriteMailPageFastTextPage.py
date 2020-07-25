# -*- encoding: utf-8 -*-
'''
@File    :   emailWriteMailPageFastTextPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/6 0006 14:31   dmk      1.0         None
'''

import time
from utils.log import logger
from selenium.webdriver.common.by import By
from .emailWriteMailPage import emailWriteMailPage

class emailWriteMailPageFastTextPage(emailWriteMailPage):
    #写信页面插入快速文本按钮
    writeMailPage_insertFastText_loc = (By.XPATH,"//a[@class='cke_button cke_button__shortcut cke_button_off']")
    #插入快速文本按钮
    insertFastText_loc = (By.XPATH,'//button[@id="insertText"]')
    #快速文本页面关闭按钮
    fastTextPage_close_loc = (By.XPATH,'//div[@id="Modal-Select-Shortcut"]//button[@class="el-dialog__headerbtn"]')
    #快速文本列表
    fastTextList_loc = (By.XPATH,'//div[@id="Modal-Select-Shortcut"]//tbody//tr')
    #快速文本标题列表
    fastTextTitleList_loc = (By.XPATH,'//div[@id="Modal-Select-Shortcut"]//span[@class="w130"]')
    #快速文本删除按钮
    fastTextDelBtn_loc = (By.XPATH,'//div[@id="Modal-Select-Shortcut"]//i[@class="icons_del icon fr el-icon-delete"]')
    #确定删除快速文本按钮
    fastTextSureDelBtn_loc = (By.XPATH,'//div[@id="Modal-Shortcut-Del"]//button[@class="el-button small el-button--primary el-button--mini"]')
    #快速文本编辑按钮
    fastTextEditBtn_loc = (By.XPATH,'//div[@id="Modal-Select-Shortcut"]//i[@class="icons_edit icon fr el-icon-edit"]')
    #快速文本输入框
    fastTextTextarea_loc = (By.XPATH,'//div[@id="Modal-Shortcut-Edit"]//textarea[@placeholder="请输入文本内容"]')
    #快速文本保存按钮
    fastTextSaveBtn_loc = (By.XPATH,'//div[@id="Modal-Shortcut-Edit"]//button[@class="el-button small el-button--primary el-button--mini"]')

    def __init__(self,driver):
        super(emailWriteMailPageFastTextPage,self).__init__(driver)
        self.find_element(self.writeMailPage_insertFastText_loc).click()

    def run_editFastText_case(self):
        #悬浮第一个快速文本
        self.mouseHover(self.fastTextList_loc)
        #点击编辑按钮
        self.find_element(self.fastTextEditBtn_loc).click()
        #输入快速文本
        time.sleep(0.2)
        self.find_element(self.fastTextTextarea_loc).clear()
        self.find_element(self.fastTextTextarea_loc).send_keys("快速文本修改测试")
        self.screenshotImg(key="修改后的快速文本")
        #点击保存
        self.find_element(self.fastTextSaveBtn_loc).click()
        #插入第一个快速文本
        time.sleep(0.5)
        # self.find_element(self.fastTextList_loc).click()
        self.find_element(self.insertFastText_loc).click()
        self.find_element(self.fastTextPage_close_loc).click()
        #切换到邮件编辑器frame，获取邮件内容
        try:
            self.switch_frame(self.emailEditFrame_loc)
            emailBody = self.find_element((By.XPATH,"/html/body")).text
        except Exception as e:
            print("获取邮件内容失败，请排查")
        finally:
            self.switch_parentFrame()

        if "快速文本修改测试" not in emailBody:
            raise Exception("修改后的快速文本内容没有插入到写信编辑器，请排查")

    def run_delFastText_case(self):
        #获取第一个快速文本，并悬浮
        firstFastText_title = self.find_element(self.fastTextTitleList_loc).text
        logger.info("要删除的快速文本标题是：{}".format(firstFastText_title))
        self.mouseHover(self.fastTextTitleList_loc)
        #点击删除按钮
        self.find_element(self.fastTextDelBtn_loc).click()
        self.find_element(self.fastTextSureDelBtn_loc).click()
        time.sleep(0.5)
        self.screenshotImg(key="删除快速文本")
        allFastText_titles = self.get_elementText(self.fastTextTitleList_loc,index="all")
        if firstFastText_title in allFastText_titles:
            raise Exception("刚刚删除的快速文本:{},依然在列表中，请排查".format(firstFastText_title))