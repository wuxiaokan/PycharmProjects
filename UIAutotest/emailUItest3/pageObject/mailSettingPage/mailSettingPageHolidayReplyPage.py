# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPageHolidayReplyPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/27 0027 20:52   dmk      1.0         None
'''

import time,allure,re
from utils.generator import *
from utils.mail import Email
from pageObject.mailSettingPage.mailSettingPage import mailSettingPage
from pageObject.mailSettingPage.mailSettingPageHolidayReplyPage_loc import mailSettingPageHolidayReplyPageLoc
from pageObject.recipientBoxPage.recipientBoxPage_loc import recipientBoxPageLoc


class mailSettingPageHolidayReplyPage(mailSettingPage,mailSettingPageHolidayReplyPageLoc,recipientBoxPageLoc):

    def __init__(self,driver):
        super(mailSettingPageHolidayReplyPage,self).__init__(driver)
        self.find_element(self.mailSettingPageHolidayReplyPage_holidayReplyBtn_loc).click()

    def run_holidayReply_case(self,is_reply,is_available):
        time.sleep(1)
        replySettingCheckboxEle = self.find_element(self.mailSettingPageHolidayReplyPage_replySettingCheckbox_loc)
        if is_reply:
            with allure.step("勾选回复设置选择框"):
                if "is-checked" not in replySettingCheckboxEle.get_attribute("class"):
                    replySettingCheckboxEle.click()
            if is_available:
                with allure.step("点击结束日期选择框"):
                    self.find_element(self.mailSettingPageHolidayReplyPage_endDateInput_loc).click()
                time.sleep(0.2)
                with allure.step("点击当前日期的后一天"):
                    self.find_element(self.mailSettingPageHolidayReplyPage_currentTodayAfterDay_loc).click()
            else:
                with allure.step("点击开始日期选择框"):
                    self.find_element(self.mailSettingPageHolidayReplyPage_startDateInput_loc).click()
                time.sleep(0.2)
                with allure.step("点击当前日期的前一天"):
                    self.find_element(self.mailSettingPageHolidayReplyPage_currentTodayBeforeDay_loc).click()
                with allure.step("点击结束日期选择框"):
                    self.find_element(self.mailSettingPageHolidayReplyPage_endDateInput_loc).click()
                time.sleep(0.2)
                with allure.step("点击当前日期的前一天"):
                    self.find_element(self.mailSettingPageHolidayReplyPage_currentTodayBeforeDay_loc).click()
            # with allure.step("获取当前日期"):
            #     currentDate_text = self.find_element(self.mailSettingPageHolidayReplyPage_currentDate_loc).text
            #     currentDate = int(re.findall('\d+',currentDate_text)[0])

        else:
            with allure.step("不勾选回复设置选择框"):
                if "is-checked" in replySettingCheckboxEle.get_attribute("class"):
                    replySettingCheckboxEle.click()

        with allure.step("点击保存按钮"):
            self.find_element(self.mailSettingPageHolidayReplyPage_saveBtn_loc).click()

        with allure.step("发送一封邮件至该SaaS账号"):
            emailTitle = random_name() + "--节假回复测试--" + time.strftime("%Y%m%d.%H.%M.%S")
            e = Email(
                title=emailTitle,
                message=random_text(),
                receiver="fttx222@aliyun.com",
                server='smtp.aliyun.com',
                sender='fttx666@aliyun.com',
                password='fttxtest123'
            )
            e.send()
        time.sleep(60)
        with allure.step("回到邮件首页"):
            self.find_element(self.emailHomePage_loc).click()
        time.sleep(3)
        with allure.step("查询收件箱是否收到发送的邮件"):
            num = 0
            while True:
                allMailSubjects = self.get_elementText(self.recipientBoxPage_emailSubject_loc,index="all")
                if emailTitle in allMailSubjects:
                    break
                else:
                    num = num + 1
                    time.sleep(20)
                if num == 35:
                    raise Exception("收件箱没有主题是：{}的邮件，请排查".format(emailTitle))
        with allure.step("切换到已发箱"):
            self.find_element(self.recipientBoxPage_hasSendBoxBtn_loc).click()
        with allure.step("查看是否有回复邮件"):
            allMailSubjects_hasSendBox = self.get_elementText(self.recipientBoxPage_emailSubject_loc,index="all")
            replyMailSubject_hasSendBox = "Re:"+emailTitle
            if is_available:
                if replyMailSubject_hasSendBox not in allMailSubjects_hasSendBox:
                    raise Exception("已发箱中没有主题是:{}的邮件，请排查".format(replyMailSubject_hasSendBox))
                # with allure.step("点击主题是：{}的邮件".format(replyMailSubject_hasSendBox)):
                #     self.find_element()
            else:
                if replyMailSubject_hasSendBox in allMailSubjects_hasSendBox:
                    raise Exception("已发箱中有主题是:{}的邮件，请排查".format(replyMailSubject_hasSendBox))