# -*- encoding: utf-8 -*-
'''
@File    :   emailReceiptBoxPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/26 0026 17:54   dmk      1.0         None
'''
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .basePage import Action

class emailReceiptBoxPage(Action):
    #第三封邮件
    email_loc = (By.XPATH,'//tr[@class="el-table__row"]')
    #发件人按钮
    sender_loc = (By.XPATH,"//div[contains(@class,'sender-select')]")
    #默认发件人
    defaultSender_loc = (By.XPATH,"//div[@x-placement='top-start' or @x-placement='bottom-start']//li[@class='el-select-dropdown__item selected']")
    #签名内容
    signatureContent_loc = (By.XPATH,"//section[@class='signature']/p")
    #回复按钮
    reply_loc = (By.XPATH,"//div[@class='mail_read window']//div[@class='operate_button_vue el-tooltip'][1]")
    #转发按钮
    forword_loc = (By.XPATH,"//div[@class='mail_read window']//div[@class='operate_button_vue el-tooltip'][3]")
    #绑定邮箱账号
    bindMailAccount_loc = (By.XPATH,"//div[text()='绑定邮箱账号']")
    #关闭绑定邮箱弹窗按钮
    bindMailAccount_close_loc = (By.XPATH,"//div[@class='el-dialog el-dialog--center']//*[name()='svg']")
    #设置页面
    setting_loc = (By.XPATH,"//div[text()='设置']")

    #进入写信页面
    def enterWriteEmail(self):
        self.find_element(self.writeEmail_loc).click()
    #获取默认发件人
    def get_defaultSender(self):
        time.sleep(2)
        # self.mouseClick(self.sender_loc)
        self.click_ele(self.sender_loc)
        time.sleep(1)
        self.screenshotImg(key="点击发件人列表")
        return self.find_element(self.defaultSender_loc).text

    #判断默认发件人，并切换
    def switch_sender(self,default_account,purpose_account):
        time.sleep(3)
        self.screenshotImg(key="签名切换页面")
        if self.get_defaultSender() == default_account:
            sender_loc = (By.XPATH, "//div[@x-placement='top-start' or @x-placement='bottom-start']//span[text()='{}']".format(purpose_account))
            self.find_element(sender_loc).click()
            return purpose_account
        else:
            sender_loc = (By.XPATH, "//div[@x-placement='top-start' or @x-placement='bottom-start']//span[text()='{}']".format(default_account))
            self.find_element(sender_loc).click()
            return default_account

    #获取签名内容
    def get_signatureContent(self):
        #切换frame，获取签名内容
        if self.switch_frame(self.emailEditFrame_loc):
            self.signatureContent = self.get_elementText(self.signatureContent_loc,index="all")
            return self.signatureContent
        else:
            print("切入邮件内容frame失败")

    #随机进入一封邮件
    def enter_email(self):
        time.sleep(2)
        self.find_element(self.email_loc,index=2).click()

    #点击回复按钮
    def reply_email(self):
        self.find_element(self.reply_loc).click()

    #点击转发按钮
    def forword_email(self):
        self.find_element(self.forword_loc).click()


    #进入写信页面，点击发件人，判断是否可以点击
    def run_lackSenderWriteMail_case(self):
        #首先判断是否会有绑定账号弹窗
        # if self.is_element_exist(self.bindMailAccount_loc[1]):
        #     self.find_element(self.bindMailAccount_close_loc).click()
        # else:
        #     raise Exception("缺少绑定邮箱账号弹窗")
        try:
            self.find_element(self.bindMailAccount_loc)
            self.find_element(self.bindMailAccount_close_loc).click()
        except Exception:
            raise Exception("缺少绑定邮箱账号弹窗")
        time.sleep(0.5)
        self.find_element(self.writeEmail_loc).click()
        #点击发件人
        time.sleep(2)
        self.find_element(self.sender_loc).click()
        #判断是否会跳转到设置页面
        time.sleep(0.5)
        if not self.is_element_exist(self.setting_loc[1]):
            self.screenshotImg(key="无账号情况，点击写信页面的发件账号")
            raise Exception("点击设置邮箱账号，未跳转到设置页面")
