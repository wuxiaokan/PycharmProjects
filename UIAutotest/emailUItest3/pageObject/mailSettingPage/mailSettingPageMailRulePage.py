# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPageMailRulePage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/15 0015 16:39   dmk      1.0         None
'''

import allure,time,json
from selenium.webdriver.common.by import By
from utils.mail import Email
from utils.generator import *
from .mailSettingPage import mailSettingPage
from .mailSettingPageMailRulePage_loc import mailSettingPageMailRulePageLoc

class mailSettingPageMailRulePage(mailSettingPage,mailSettingPageMailRulePageLoc):

    def __init__(self,driver):
        super(mailSettingPageMailRulePage,self).__init__(driver)
        self.switch_operator(operator="dmktest_001")
        time.sleep(2)
        self.click_ele(self.mailSettingBtn_loc)


    def run_addMailRule_case(self,condition,excuteOperate,deliverOrChargeFirst,deliverOrChargeSecond,containKey,send_info):

        self.find_element(self.mailSettingPageMailRulePage_mailRuleBtn).click()
        with allure.step("输入收件规则的名字"):
            time.sleep(0.2)
            self.find_element(self.mailSettingPageMailRulePage_mailRuleNameInput).clear()
            self.find_element(self.mailSettingPageMailRulePage_mailRuleNameInput).send_keys("邮件规则测试")
        time.sleep(0.2)
        with allure.step("点击触发条件"):
            self.find_element(self.mailSettingPageMailRulePage_conditionBtn).click()
        time.sleep(0.2)
        with allure.step("选中{}".format(condition)):
            mailSettingPageMailRulePage_condition_loc = (By.XPATH,self.mailSettingPageMailRulePage_condition_allMails[1].replace("全部邮件",condition))
            self.scroll_element(mailSettingPageMailRulePage_condition_loc)
            time.sleep(0.3)
            self.find_element(mailSettingPageMailRulePage_condition_loc).click()
        if "邮件主题" in condition or "发件地址" in condition:
            with allure.step("输入包含的关键词"):
                self.find_element(self.mailSettingPageMailRulePage_containKeyInput).clear()
                self.find_element(self.mailSettingPageMailRulePage_containKeyInput).send_keys(containKey)
        time.sleep(0.2)
        with allure.step("点击执行操作"):
            self.find_element(self.mailSettingPageMailRulePage_excuteOperateBtn).click()
        time.sleep(0.2)
        with allure.step("选中{}".format(excuteOperate)):
            mailSettingPageMailRulePage_excuteOperate_loc = (By.XPATH,self.mailSettingPageMailRulePage_excuteOperate_merger[1].replace("直接归并",excuteOperate))
            self.find_element(mailSettingPageMailRulePage_excuteOperate_loc).click()
        time.sleep(0.2)
        with allure.step("点击收取至或者分发给一级选择框"):
            self.find_element(self.mailSettingPageMailRulePage_firstChargeBtn).click()
        time.sleep(0.2)
        with allure.step("选中{}".format(deliverOrChargeFirst)):
            mailSettingPageMailRulePage_deliverOrChargeFirstBox_loc = (By.XPATH,self.mailSettingPageMailRulePage_firstCharge_customizeBox[1].replace("自定义箱",deliverOrChargeFirst))
            self.find_element(mailSettingPageMailRulePage_deliverOrChargeFirstBox_loc).click()
        # with allure.step("选中二级箱子选择框"):
        #     self.find_element(self.mailSettingPageMailRulePage_secondChargeBtn).click()
        # time.sleep(0.2)
        # with allure.step("选中{}".format(deliverOrChargeSecond)):
        #     mailSettingPageMailRulePage_deliverOrChargeSecondBox_loc = (By.XPATH,self.mailSettingPageMailRulePage_secondCharge_boxList[1].replace(""))
        #     self.find_element(self.mailSettingPageMailRulePage_secondCharge_boxList).click()
        with allure.step("点击保存按钮"):
            self.find_element(self.mailSettingPageMailRulePage_saveMailRuleBtn).click()
        with allure.step("开始发送邮件"):
            emailTitle = random_name() + "收件规则测试-{}".format(condition) + time.strftime("%Y%m%d.%H.%M.%S")
            e = Email(
                title=emailTitle,
                message=random_text(),
                receiver="fttx111@sina.cn",
                server=send_info['server'],
                sender=send_info['sender'],
                password=send_info['password']
            )
            e.send()
        time.sleep(150)
        with allure.step("点击邮件首页"):
            self.find_element(self.emailHomePage_loc).click()
        with allure.step("遍历箱子，查看是否收到主题是：{}的邮件".format(emailTitle)):
            num = 0
            while True:
                if deliverOrChargeFirst == "客户箱":
                    with allure.step("点击客户箱tab"):
                        self.find_element(self.recipientBoxPage_customerBoxBtn_loc).click()
                    time.sleep(0.5)
                    with allure.step("点击最近联系的第一个客户箱"):
                        self.find_element(self.customerBoxPage_firstRecentBox_loc).click()
                elif deliverOrChargeFirst == "供应商箱":
                    with allure.step("点击供应商tab"):
                        self.find_element(self.recipientBoxPage_supplierBoxBtn_loc).click()
                    time.sleep(0.5)
                    with allure.step("点击最近联系的第一个供应商箱子"):
                        self.find_element(self.supplierBoxPage_firstRecentBox_loc).click()
                elif deliverOrChargeFirst == "内部联系人箱":
                    with allure.step("点击内部联系人tab"):
                        self.find_element(self.recipientBoxPage_innerBoxBtn_loc).click()
                    time.sleep(0.5)
                    with allure.step("点击最近联系的第一个内部联系人箱子"):
                        self.find_element(self.innerBoxPage_firstRecentBox_loc).click()
                else:
                    with allure.step("点击自定义测试箱,查看是否收到邮件"):
                        self.find_element(self.customizeBoxPage_firstBox_loc).click()
                time.sleep(3)
                subjects = self.get_elementText(self.recipientBoxPage_emailSubject_loc,index="all")
                # allMailSubjects = []
                # for subject in subjects:
                #     allMailSubjects.append(subject.split("】")[1])
                if emailTitle in subjects:
                    break
                else:
                    with allure.step("点击邮箱tab"):
                        self.find_element(self.recipientBoxPage_emailBoxBtn_loc).click()
                    with allure.step("点击收件箱"):
                        self.find_element(self.receiptBox_loc).click()
                    time.sleep(2)
                    num = num + 1
                    time.sleep(20)
                if num == 15:
                    print(subjects)
                    raise Exception("收件箱没有主题是：{}的邮件，请排查".format(emailTitle))
        # time.sleep(1)
        # with allure.step("判断该箱子里面是否有标题是{}的邮件".format(emailTitle)):
        #     allEmailSubjectText = self.get_elementText(self.recipientBoxPage_emailSubject_loc,index="all")
        #     print(allEmailSubjectText)
        #     for emailSubject in allEmailSubjectText:
        #         if emailTitle not in emailSubject:
        #             raise Exception("{}里面没有收取到主题是{}的邮件".format(deliverOrChargeFirst,emailTitle))