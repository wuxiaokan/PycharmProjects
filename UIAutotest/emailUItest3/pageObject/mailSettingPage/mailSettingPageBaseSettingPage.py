# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPageBaseSettingPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/19 0019 16:16   dmk      1.0         None
'''

import allure,time,traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.log import logger
from utils.config import IMAGE_PATH
from utils.generator import *
from utils.mail import Email
from .mailSettingPage import mailSettingPage
from pageObject.mailSettingPage.mailSettingPageBaseSettingPage_loc import mailSettingPageBaseSettingPageLoc
from pageObject.writeMailPage.writeMailPage_loc import writeMailPageLoc
from pageObject.emailDetailPage.emailDetailPage_loc import emailDetailPageLoc
from pageObject.recipientBoxPage.recipientBoxPage_loc import recipientBoxPageLoc
from pageObject.writeMailPage.writeMailCommon import writeMailCommon
from pageObject.recipientBoxPage.recipientBoxPageCommon import recipientBoxPageCommon
from pageObject.mailSettingPage.mailSettingPageShowSettingPage_loc import mailSettingPageShowSettingPageLoc


class mailSettingPageBaseSettingPage(mailSettingPage,mailSettingPageBaseSettingPageLoc,writeMailPageLoc,emailDetailPageLoc,recipientBoxPageLoc,mailSettingPageShowSettingPageLoc):


    def __init__(self,driver):
        super(mailSettingPageBaseSettingPage,self).__init__(driver)
        # self.find_element(self.mailSettingPageBaseSettingPage_baseSettingBtn_loc).click()
        self.click_ele(self.mailSettingPageBaseSettingPage_baseSettingBtn_loc,index=0)
        self.writeMailCommon = writeMailCommon(driver)
        self.recipientBoxPageCommon = recipientBoxPageCommon(driver)


    def run_mailSettingPageReadedSetting_case(self,is_openRead):
        time.sleep(1)
        readedSettingElement = self.find_element(self.mailSettingPageBaseSettingPage_readedSettingBtn_loc)
        if is_openRead == "1":
            with allure.step("开启已读设置"):
                if "is-checked" not in readedSettingElement.get_attribute("class"):
                    readedSettingElement.click()
        else:
            with allure.step("关闭已读设置"):
                if "is-checked" in readedSettingElement.get_attribute("class"):
                    readedSettingElement.click()
        with allure.step("切到dmktest001"):
            self.switch_operator(operator="dmktest_001")
        with allure.step("获取未读邮件数"):
            unReadEamilNum_v1 = self.recipientBoxPageCommon.get_unReadEmailNum()
        with allure.step("点击一封未读邮件"):
            self.recipientBoxPageCommon.clickUnReadEmail()
        with allure.step("回到邮件首页"):
            self.click_ele(self.emailHomePage_loc)
        with allure.step("获取未读邮件数"):
            unReadEamilNum_v2 = self.recipientBoxPageCommon.get_unReadEmailNum()
        if is_openRead == "1":
            assert unReadEamilNum_v1 == unReadEamilNum_v2
        else:
            assert int(unReadEamilNum_v1) == int(unReadEamilNum_v2) + 1




    #自动回执用例
    def run_autoReceipt_case(self,is_autoReceipt,is_selectAutoReceipt):
        time.sleep(2)
        with allure.step("点击显示设置按钮"):
            self.click_ele(self.mailSettingPageShowSettingPage_showSettingBtn_loc,key="点击显示设置")
            time.sleep(2)
            needReceiptBtnEle = self.find_element(self.mailSettingPageShowSettingPage_needReceiptBtn_loc)
            with allure.step("开启需要回执"):
                if "is-checked" not in needReceiptBtnEle.get_attribute("class"):
                    self.mouseClick(self.mailSettingPageShowSettingPage_needReceiptBtn_loc)
                with allure.step("点击保存按钮"):
                    self.find_element_byPresence(self.mailSettingPageShowSettingPage_saveBtn_loc).click()
        with allure.step("点击基础设置按钮"):
            self.click_ele(self.mailSettingPageBaseSettingPage_baseSettingBtn_loc,key="点击基础设置按钮")
        time.sleep(2)
        autoReceiptBtnEle = self.find_element(self.mailSettingPageBaseSettingPage_autoReceiptBtn_loc)
        print(autoReceiptBtnEle.get_attribute("class"))
        if is_autoReceipt:
            with allure.step("开启自动回执"):
                if "is-checked" not in autoReceiptBtnEle.get_attribute("class"):
                    self.mouseClick(self.mailSettingPageBaseSettingPage_autoReceiptBtn_loc)
                time.sleep(1)
        else:
            with allure.step("关闭自动回执"):
                if "is-checked" in autoReceiptBtnEle.get_attribute("class"):
                    self.mouseClick(self.mailSettingPageBaseSettingPage_autoReceiptBtn_loc)
                time.sleep(1)
        with allure.step("回到邮件首页"):
            self.find_element(self.emailHomePage_loc).click()
        with allure.step("点击写邮件"):
            self.find_element(self.writeEmailBtn_loc).click()
        time.sleep(2)
        with allure.step("输入主题"):
            emailTitle = random_name() + "--自动回执测试--" + time.strftime("%Y%m%d.%H.%M.%S")
            self.find_element(self.writeMailPage_emailSubjectInput_loc).send_keys(emailTitle)
        with allure.step("输入收件人"):
            self.find_element(self.writeMailPage_recipientInput_loc).send_keys("fttxtest@126.com")
        with allure.step("切换到邮件编辑器,输入随机文本"):
            self.switch_frame(self.emailEditFrame_loc)
            self.find_element(self.emailBodyInEmailEdit_loc).send_keys(random_text())
            self.switch_parentFrame()
        with allure.step("选择发件账号：fttx222<fttx222@aliyun.com>"):
            # self.find_element(self.writeMailPage_senderInput_loc).click()
            # time.sleep(0.3)
            # self.find_element(self.writeMailPage_sender_loc).click()
            self.writeMailCommon.select_sender(sender="fttx222@aliyun.com")
        with allure.step("点击发送按钮"):
            self.find_element(self.writeMailPage_sendEmailBtn_loc).click()
        time.sleep(150)
        with allure.step("遍历收件箱，查看是否收到主题是：{}的邮件".format(emailTitle)):
            num = 0
            while True:
                self.find_element(self.recipientBoxPage_recipientBoxBtn_loc).click()
                time.sleep(3)
                allMailSubjects = self.get_elementText(self.recipientBoxPage_emailSubject_loc,index="all",key="获取自动回执邮件")
                if emailTitle in allMailSubjects:
                    mailSubject_loc = (By.XPATH,'//span[contains(text(),"{}")]'.format(emailTitle))
                    self.find_element(mailSubject_loc).click()
                    time.sleep(3)
                    break
                else:
                    num = num + 1
                    time.sleep(20)
                if num == 18:
                    raise Exception("收件箱没有主题是：{}的邮件，请排查".format(emailTitle))
        if not is_autoReceipt:
            if is_selectAutoReceipt:
                with allure.step("勾选自动回执选择框"):
                    self.mouseClick(self.emailDetailPage_autoReceiptBtn_loc)
            with allure.step("点击发送回执按钮"):
                self.find_element(self.emailDetailPage_sendReceiptBtn_loc).click()
            time.sleep(1)
            with allure.step("回到设置tab"):
                self.find_element(self.mailSettingBtn_loc).click()
            with allure.step("点击账号设置"):
                accountSettingBtn_loc = (By.XPATH,self.mailSettingPageBaseSettingPage_baseSettingBtn_loc[1].replace("基础","账号"))
                self.find_element(accountSettingBtn_loc).click()
            time.sleep(0.2)
            with allure.step("点击基础设置按钮"):
                self.find_element(self.mailSettingPageBaseSettingPage_baseSettingBtn_loc).click()
            time.sleep(1)
            autoReceiptBtnEle = self.find_element(self.mailSettingPageBaseSettingPage_autoReceiptBtn_loc)
            with allure.step("判断基础设置里面，自动设置是否被勾选"):
                if is_selectAutoReceipt:
                    if "is-checked" not in autoReceiptBtnEle.get_attribute("class"):
                        raise Exception("用例是勾选了自动回执，但是基础设置里面还是没有勾选")
                else:
                    if "is-checked" in autoReceiptBtnEle.get_attribute("class"):
                        raise Exception("用例是不勾选了自动回执，但是基础设置里面却勾选了")
        with allure.step("回到邮件首页tab"):
            self.find_element(self.emailHomePage_loc).click()
        time.sleep(150)
        receiptMailSubject = "Read："+emailTitle
        with allure.step("遍历收件箱，查看是否收到主题是：{}的邮件".format(receiptMailSubject)):
            num = 0
            while True:
                self.find_element(self.recipientBoxPage_recipientBoxBtn_loc).click()
                time.sleep(3)
                allMailSubjects = self.get_elementText(self.recipientBoxPage_emailSubject_loc, index="all")
                if receiptMailSubject in allMailSubjects:
                    mailSubject_loc = (By.XPATH, '//span[contains(text(),"{}")]'.format(receiptMailSubject))
                    self.find_element(mailSubject_loc).click()
                    time.sleep(2)
                    break
                else:
                    num = num + 1
                    time.sleep(20)
                if num == 18:
                    raise Exception("收件箱没有主题是：{}的邮件，请排查".format(emailTitle))


    #延迟发送用例
    def run_delaySend_case(self,data):
        with allure.step("获取延迟发送的class属性"):
            delaySendBtnEle = self.find_element(self.mailSettingPageBaseSettingPage_delaySendBtn_loc)
            delaySendBtnEle_attr = delaySendBtnEle.get_attribute("class")
        if data["is_open"]:
            if "is-checked" not in delaySendBtnEle_attr:
                self.click_ele(self.mailSettingPageBaseSettingPage_delaySendBtn_loc,key="点击开启延迟发送")
        else:
            if "is-checked" in delaySendBtnEle_attr:
                self.click_ele(self.mailSettingPageBaseSettingPage_delaySendBtn_loc,key="点击关闭延迟发送")
        with allure.step("回到邮件首页"):
            self.click_ele(self.emailHomePage_loc)
        with allure.step("点击写邮件按钮"):
            self.click_ele(self.writeEmailBtn_loc)
        with allure.step("发送一封普通邮件"):
            subject = random_name() + "--延迟发送测试--" + time.strftime("%Y%m%d.%H.%M.%S")
            recipient = ["fttxtest@sohu.com"]
            self.writeMailCommon.send_generalEmail(subject=subject,recipient=recipient)
        current_time = time.strftime("%Y-%m-%d %H:%M")
        current_time_second = int(current_time.split(":")[-1])
        if data["is_open"]:
            with allure.step("回到草稿箱，查看是否有该邮件：{}".format(subject)):
                self.recipientBoxPageCommon.get_emailBySubject(email_subject=subject,box="草稿箱")
            with allure.step("获取定时时间文本"):
                setted_time = self.writeMailCommon.get_settedTime_writeMailPage()
                setted_time_second = int(setted_time.split(":")[-1])
                if setted_time_second - current_time_second != 3:
                    raise Exception("设置延迟发送的时间不对，发送时候的时间：{}，邮件实际的定时时间：{}".format(current_time,setted_time))
            with allure.step("点击取消定时按钮"):
                self.click_ele(self.writeMailPage_cancelTimedSendBtn_loc)
            with allure.step("点击存草稿按钮"):
                self.click_ele(self.writeMailPage_saveDraftBtn_loc)
        else:
            time.sleep(20)
            with allure.step("回到已发箱，查看是否有邮件"):
                self.recipientBoxPageCommon.get_emailBySubject(email_subject=subject,box="已发箱",is_click=0)


    #设置抄送密送人
    def run_setCcAndBc_case(self,data):
        with allure.step("点击抄送密送设置"):
            self.click_ele(self.mailSettingPageCcAndBcSettingPage_ccAndBcSettingBtn_loc)
        with allure.step("判断是否有抄送密送人，如果有，全部删掉"):
            if self.is_element_exist(self.mailSettingPageCcAndBcSettingPage_delCcAndBcSettingBtn_loc[1]):
                delCcAndBcSettingBtnEles = self.find_element(self.mailSettingPageCcAndBcSettingPage_delCcAndBcSettingBtn_loc,index="all")
                for delCcAndBcSettingBtnEle in delCcAndBcSettingBtnEles:
                    delCcAndBcSettingBtnEle.click()
                    time.sleep(0.3)
        if data["is_open"]:
            with allure.step("输入默认抄送人"):
                defaultCcAccount = str(random_email())
                defaultCcAccount = defaultCcAccount.split("@")[0] + "<" + defaultCcAccount + ">"
                self.sendKeys(self.mailSettingPageCcAndBcSettingPage_defaultCcInput_loc,key=defaultCcAccount)
            with allure.step("输入默认密送人"):
                defaultBcAccount = random_email()
                defaultBcAccount = defaultBcAccount.split("@")[0] + "<" + defaultBcAccount + ">"
                self.sendKeys(self.mailSettingPageCcAndBcSettingPage_defaultBcInput_loc,key=defaultBcAccount)
            with allure.step("输入强制抄送人"):
                forceCcAccount = str(random_email())
                forceCcAccount = forceCcAccount.split("@")[0] + "<" + forceCcAccount + ">"
                self.sendKeys(self.mailSettingPageCcAndBcSettingPage_forceCcInput_loc,key=forceCcAccount)
        with allure.step("点击保存按钮"):
            self.click_ele(self.mailSettingPageCcAndBcSettingPage_saveBtn_loc)
        with allure.step("点击邮件首页"):
            self.click_ele(self.emailHomePage_loc)
        with allure.step("点击写邮件按钮"):
            self.click_ele(self.writeEmailBtn_loc)
        with allure.step("获取写邮件页面的抄送密送人"):
            cc_writeMail,bc_writeMail = self.writeMailCommon.get_writeMail_ccAndBc()
        with allure.step("判断设置前后的抄送密送人是否正确"):
            if data["is_open"]:
                cc_settingPage = [forceCcAccount,defaultCcAccount]
                if cc_writeMail != cc_settingPage:
                    raise Exception("写信页面的抄送人：{}，与设置的抄送人：{}，不一致，默认抄送人：{}，强制抄送人：{}".format(cc_writeMail,cc_settingPage,defaultCcAccount,forceCcAccount))
                bc_settingPage = [defaultBcAccount]
                if bc_writeMail != bc_settingPage:
                    raise Exception("写信页面的抄密送人：{}，与设置的密送人：{}，不一致，默认密送人：{}".format(bc_writeMail,bc_settingPage,defaultBcAccount))
            else:
                if cc_writeMail:
                    raise Exception("没有设置抄送人，但是写信页面却有抄送人：{}".format(cc_writeMail))
                if bc_writeMail:
                    raise Exception("没有设置面试人，但是写信页面却有密送人：{}".format(bc_writeMail))