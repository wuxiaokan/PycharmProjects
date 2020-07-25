# -*- encoding: utf-8 -*-
'''
@File    :   emailWriteMailPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/30 0030 13:41   dmk      1.0         None
'''

import time
from utils.generator import *
from utils.log import logger
from selenium.webdriver.common.by import By
from .basePage import Action

class emailWriteMailPage(Action):

    #邮件主题输入框
    emailTitle_loc = (By.XPATH,"//div[@class='no_border input JOINF el-input el-input--suffix']//input")
    #收件人输入框
    emailReceipt_loc = (By.XPATH,"//div[@class='addressee_input_item b_line i_item addressee']//input")
    #保存草稿按钮
    saveEmail_loc = (By.XPATH,"//div[@class='o_bar']//span[text()='存草稿']")
    #首页收件人
    homePageReceipt_loc = (By.XPATH,"//span[@class='contact_names']")
    #写信页面发件人按钮
    sender_loc = (By.XPATH,"//div[@class='sender-select']")
    #群发单显按钮
    massMailBtn_loc = (By.XPATH,"//div[@class='o_bar']//li[text()='群发单显']")
    #邮件发送按钮
    emailSendBtn_loc = (By.XPATH,'//button[@class="el-button item send f12 el-button--primary"]')
    #邮件主题
    emailSubject_loc = (By.XPATH,'//div[@class="sub_item"]')
    #不审批，直接发送按钮
    not_approvalBtn_loc = (By.XPATH,"//span[text()='不审，发送']")
    #详细信息按钮
    detailInformationBtn_loc = (By.XPATH,'//div[@class="detailed_btn fc01 pointer no-sel m-l-10"]')
    #详情页面查看详情按钮-群发邮件
    detailPage_massMail_checkBtn_loc = (By.XPATH,'//span[@class="detailed_btn fc01 no-sel pointer"]')
    #详情页面发件人-群发邮件
    detailPage_massMail_sender_loc = (By.XPATH,'//div[@class="el-table__body-wrapper is-scrolling-none"]//td[1]')
    #详情页面收件人-群发邮件
    detailPage_massMail_receipt_loc = (By.XPATH,'//div[@class="el-table__body-wrapper is-scrolling-none"]//td[2]')
    #详情页面发件人
    detailPage_sender_loc = (By.XPATH,"//span[@class='contact_names fc01']")
    #详情页面收件人
    detailPage_receipt_loc = (By.XPATH,"//span[text()='收件人']/preceding-sibling::div//span[@class='contact_names']")
    worldTime_loc = (By.XPATH,'//div[@class="international_time f12 fc02 f-w-400"]')
    #写信页面收件人
    emailWriteReceipt_loc = (By.XPATH,"//p[@class='show_txt f12 fc02 no-sel']")
    #写信页面收件人联想
    emailWriteReceiptContectList_loc = (By.XPATH,'//li[@class="no-sel pointer"]')
    #收件箱页面，查看邮件按钮
    recipientPage_lookEmailBtn_loc = (By.XPATH,'//a[text()="查看邮件"]')


    def __init__(self,driver):
        super(emailWriteMailPage,self).__init__(driver)
        self.enter_writeMail()

    #判断是否有审批按钮
    def has_approval(self):
        try:
            self.find_element(self.not_approvalBtn_loc).click()
            time.sleep(2)
        except Exception as e:
            print("没有找到审批按钮，可直接发送，或者是强制审批")

    #进入写信页面
    def enter_writeMail(self):
        self.find_element(self.writeEmail_loc).click()
        time.sleep(2)

    def run_saveMail_case(self,receipt):
        #输入主题
        time.sleep(2)
        title = random_name()+"草稿邮件测试"
        self.find_element(self.emailTitle_loc).send_keys(title)
        #判断是否输入收件人
        if receipt:
            self.find_element(self.emailReceipt_loc).send_keys(receipt)
        #保存草稿
        self.find_element(self.saveEmail_loc).click()

    #获取刚刚保存的草稿箱的邮件收件人
    def get_draftEmail_receipt(self):
        #回到邮件首页
        time.sleep(1)
        if not self.is_element_exist(self.toast_loc[1]):
            time.sleep(2)
        self.find_element(self.emailHomePage_loc).click()
        # 切到草稿箱
        self.find_element(self.draftBox_loc).click()
        receipt = self.find_element(self.homePageReceipt_loc).text
        print(receipt)
        return receipt


    def run_massEmail_case(self):
        #点击群发单显按钮
        self.find_element(self.massMailBtn_loc).click()
        receiptList = ["fttxtest@126.com","fttx222@aliyun.com","fttx666@aliyun.com","fttxtest@21cn.com"]
        #逐个输入收件人
        for i in range(len(receiptList)):
            self.find_element(self.emailReceipt_loc).send_keys(receiptList[i])
            self.find_element(self.emailTitle_loc).click()
        #输入邮件主题
        subject = random_name()+"-群发单显测试-"+time.strftime("%Y%m%d.%H.%M.%S")
        logger.info("群发单显的邮件主题是：{}".format(subject))
        self.find_element(self.emailTitle_loc).send_keys(subject)
        #输入邮件内容
        try:
            self.switch_frame(self.emailEditFrame_loc)
            content = random_text()
            self.find_element((By.XPATH,"/html/body")).send_keys(content)
        except Exception as e:
            print("输入邮件内容报错，请排查")
        finally:
            self.switch_parentFrame()
        #点击发送按钮，开始发送邮件
        self.find_element(self.emailSendBtn_loc).click()
        self.has_approval()
        #切换到群发箱
        self.find_element(self.massBox_loc).click()
        time.sleep(2)
        #获取群发箱所有主题，遍历
        allSubjectElements = self.find_element(self.emailSubject_loc,index="all")
        for allSubjectElement in allSubjectElements:
            if subject == allSubjectElement.text:
                allSubjectElement.click()
                break
        # time.sleep(0.3)
        # self.find_element(self.recipientPage_lookEmailBtn_loc).click()
        #判断详细信息是否展示
        time.sleep(1)
        detailInformationBtnEle = self.find_element(self.detailInformationBtn_loc)
        if "详细" in detailInformationBtnEle.text:
            detailInformationBtnEle.click()
        #判断详情是否展示
        time.sleep(0.2)
        self.find_element(self.detailPage_massMail_checkBtn_loc).click()

        #获取所有的发件人
        is_success = 1
        allMassSenders = self.get_elementText(self.detailPage_massMail_sender_loc,index="all")
        logger.info("主题是：{}的群发单显邮件，所有的发件人是：{}".format(subject,allMassSenders))
        try:
            for allMassSender in allMassSenders:
                if allMassSender == "":
                    is_success = 0
                    print("群发单显，发件人存在空账号，请排查")
        except Exception as e:
            print(e)
        allMassReceipts = self.get_elementText(self.detailPage_massMail_receipt_loc,index="all")
        logger.info("主题是：{}的群发单显邮件，所有的收件人是：{}".format(subject,allMassReceipts))
        try:
            for allMassReceipt in allMassReceipts:
                if allMassReceipt == "":
                    is_success = 0
                    print("群发单显，收件人存在空账号，请排查")
        except Exception as e:
            print(e)
        self.screenshotImg(key="群发单显邮件，发件详情")
        #回到首页，收件箱，查看是否收到群发单显邮件
        t1 = int(time.time()*1000)
        time.sleep(60)
        self.find_element(self.emailHomePage_loc).click()
        self.find_element(self.receiptBox_loc).click()
        time.sleep(2)
        purpose_subject_loc = (By.XPATH,"//div[@class='sub_item']//span[text()='{}']".format(subject))
        logger.info("群发单显的邮件在收件箱的xpath：{}".format(purpose_subject_loc))
        while True:
            t2 = int(time.time()*1000)
            if self.is_element_exist(purpose_subject_loc[1]):
                self.screenshotImg(key="群发单显邮件")
                self.find_element(purpose_subject_loc).click()
                break
            elif t2-t1>300000:
                raise Exception("已经超过了5分钟，仍然没有收到主题是：{}的邮件".format(subject))
            else:
                self.refresh_bro()
                time.sleep(30)
        #判断发件人，收件人是不是只有一个
        try:
            if len(self.find_element(self.detailPage_sender_loc,index="all")) != 1:
                is_success = 2
                print("群发单显邮件，发件人数量不是一个")
        except Exception as e:
            print(e)
        try:
            if len(self.find_element(self.detailPage_receipt_loc,index="all")) != 1:
                is_success = 2
                print("群发单显邮件，收件件人数量不是一个")
        except Exception as e:
            print(e)

        self.screenshotImg(key="收件箱内，群发单显邮件详情")

        if is_success == 2:
            raise Exception("群发单显邮件详情里面，收件人，发件人数量不是一个")

        if is_success == 0:
            raise Exception("群发单显测试，收件人，发件人存在空账号")


    def run_worldTimeShowNickName_case(self):
        #输入收件人
        self.find_element(self.emailReceipt_loc).send_keys("fttx444@aliyun.com")
        self.find_element(self.emailTitle_loc).click()
        #获取世界时间文本
        wordlTimeText = self.find_element(self.worldTime_loc).text
        if "管理员" in wordlTimeText or "fttx444" not in wordlTimeText or "fttx444@aliyun.com" not in wordlTimeText:
            self.screenshotImg(key="写信页面世界时间")
            raise Exception("世界时间处显示错误,{}".format(wordlTimeText))


    def run_receiptConnect_case(self,key):
        #输入联想关键词
        self.find_element(self.emailReceipt_loc).send_keys(key)
        allContectReceipt = self.get_elementText(self.emailWriteReceiptContectList_loc,index="all")
        logger.info("根据关键词：{}，联想的收件人：{}".format(key,allContectReceipt))
        #判断结果是否正确
        for contectReceipt in allContectReceipt:
            if key not in contectReceipt and key.upper() not in contectReceipt:
                self.screenshotImg(key="收件人联想，关键词:{}".format(key))
                raise Exception("收件人联想结果报错，结果：{}，里面有不包含联想词：{}的账号".format(contectReceipt,key))

            if "null" in contectReceipt:
                self.screenshotImg(key="收件人联想，关键词:{}".format(key))
                raise Exception("收件人联想结果报错，结果：{}，里面包含了null字符".format(contectReceipt))