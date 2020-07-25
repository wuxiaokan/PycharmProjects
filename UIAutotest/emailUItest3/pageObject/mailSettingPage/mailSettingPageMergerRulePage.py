# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPageMergerRulePage.py.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/26 0026 11:25   dmk      1.0         None
'''

import allure,time
from selenium.webdriver.common.by import By
from pageObject.mailSettingPage.mailSettingPage import mailSettingPage
from pageObject.mailSettingPage.mailSettingPageMergerRulePage_loc import mailSettingPageMergerRulePageLoc
from pageObject.recipientBoxPage.recipientBoxPage_loc import recipientBoxPageLoc
from pageObject.emailDetailPage.emailDetailPage_loc import emailDetailPageLoc
from pageObject.customerBoxPage.customerBoxPage_loc import customerBoxPageLoc
from pageObject.supplierBoxPage.supplierBoxPage_loc import supplierBoxPageLoc
from pageObject.innerBoxPage.innerBoxPage_loc import innerBoxPageLoc


class mailSettingPageMergerRulePage(mailSettingPage,mailSettingPageMergerRulePageLoc,recipientBoxPageLoc,emailDetailPageLoc,customerBoxPageLoc,supplierBoxPageLoc,innerBoxPageLoc):

    def __init__(self,driver):
        super(mailSettingPageMergerRulePage,self).__init__(driver)
        self.find_element(self.mailSettingPageMergerRulePage_mergerRuleBtn_loc).click()
        time.sleep(0.3)

    def run_addMergerRule_case(self,condition,is_contain,containOrEqualKey,boxCategory,boxName,queryBoxName):
        with allure.step("输入归并规则的名字"):
            self.find_element(self.mailSettingPageMergerRulePage_mergerRuleNameInput_loc).clear()
            self.find_element(self.mailSettingPageMergerRulePage_mergerRuleNameInput_loc).send_keys("归并规则测试")
        with allure.step("点击触发条件选择框"):
            self.find_element(self.mailSettingPageMergerRulePage_mergerConditionBtn_loc).click()
        time.sleep(0.2)
        with allure.step("选中归并条件：{}".format(condition)):
            mergerCondition_loc = (By.XPATH,self.mailSettingPageMergerRulePage_mergerCondition_loc[1].replace("邮件主题",condition))
            self.scroll_element(mergerCondition_loc)
            time.sleep(0.1)
            self.find_element(mergerCondition_loc).click()
        time.sleep(0.2)
        if is_contain:
            with allure.step("点击包含按钮"):
                self.find_element(self.mailSettingPageMergerRulePage_conditionContainBtn_loc).click()
            time.sleep(0.2)
            with allure.step("输入包含的关键词：{}".format(containOrEqualKey)):
                self.find_element(self.mailSettingPageMergerRulePage_conditionContainInput_loc).clear()
                self.find_element(self.mailSettingPageMergerRulePage_conditionContainInput_loc).send_keys(containOrEqualKey)
        else:
            with allure.step("点击等于按钮"):
                self.find_element(self.mailSettingPageMergerRulePage_conditionEqualBtn_loc).click()
            time.sleep(0.2)
            with allure.step("点击等于选择框"):
                self.find_element(self.mailSettingPageMergerRulePage_conditionEqualSecondBtn_loc).click()
            time.sleep(0.2)
            with allure.step("点击选中：{}".format(containOrEqualKey)):
                equalCondition_loc = (By.XPATH, self.mailSettingPageMergerRulePage_mergerCondition_loc[1].replace("邮件主题", containOrEqualKey))
                self.find_element(equalCondition_loc).click()
            with allure.step("点击等于按钮，使下拉框消失"):
                self.find_element(self.mailSettingPageMergerRulePage_conditionEqualBtn_loc).click()
        time.sleep(0.2)
        with allure.step("点击收取至一级选择框"):
            self.find_element(self.mailSettingPageMergerRulePage_firstChargeBtn).click()
        time.sleep(0.2)
        with allure.step("点击选中：{}".format(boxCategory)):
            boxCategoryBtn_loc = (By.XPATH, self.mailSettingPageMergerRulePage_mergerCondition_loc[1].replace("邮件主题", boxCategory))
            self.find_element(boxCategoryBtn_loc).click()
        with allure.step("点击收取至二级选择框"):
            self.find_element(self.mailSettingPageMergerRulePage_secondChargeBtn).click()
        time.sleep(0.2)
        with allure.step("点击选中：{}".format(boxName)):
            if boxCategory == "自定义箱":
                boxNameBtn_loc = self.mailSettingPageMergerRulePage_customBoxTest_loc
            else:
                boxNameBtn_loc = (By.XPATH, self.mailSettingPageMergerRulePage_mergerCondition_loc[1].replace("邮件主题", boxName))
                with allure.step("输入：{}，进行搜索".format(boxName)):
                    self.sendKeys(self.mailSettingPageMergerRulePage_secondChargeInput,key=boxName)
            self.scroll_element(boxNameBtn_loc)
            self.find_element(boxNameBtn_loc).click()
        time.sleep(0.2)
        with allure.step("点击保存按钮"):
            self.find_element(self.mailSettingPageMergerRulePage_firstChargeBtn).click()
            time.sleep(0.3)
            self.find_element(self.mailSettingPageMergerRulePage_saveMergerRuleBtn).click()
        with allure.step("回到邮件首页"):
            self.find_element(self.emailHomePage_loc).click()
        with allure.step("点击查询箱：{}，获取要归并的邮件".format(queryBoxName)):
            queryBoxBtn_loc = (By.XPATH,self.recipientBoxPage_queryBoxBtn_loc[1].replace("主题包含重构，勿动",queryBoxName))
            self.find_element(queryBoxBtn_loc).click()
        with allure.step("点击符合条件的邮件"):
            self.click_ele(self.recipientBoxPage_subject_loc)
            # self.find_element(self.recipientBoxPage_subject_loc).click()
            # allEmailSubjectEle = self.find_element(self.recipientBoxPage_subject_loc,index="all")
            # for emailSubjectEle in allEmailSubjectEle:
            #     if "收件箱" in emailSubjectEle.text:
            #         emailSubjectEle.click()
        time.sleep(1)
        with allure.step("获取要归并的邮件主题"):
            mergerMailSubject = self.find_element(self.emailDetailPage_subject_loc).text
        with allure.step("点击更多操作"):
            # self.find_element(self.emailDetailPage_moreOperateBtn_loc).click()
            self.click_ele(self.emailDetailPage_moreOperateBtn_loc)
        time.sleep(0.2)
        with allure.step("点击归并按钮"):
            self.find_element(self.emailDetailPage_mergerBtn_loc).click()
        time.sleep(0.5)
        with allure.step("点击确定按钮"):
            self.find_element(self.emailDetailPage_sureBtn_loc).click()
        with allure.step("断言归并操作之后的toast提示"):
            toastContent = self.find_element(self.toast_loc).text
            print(toastContent)
            if toastContent != "操作成功！":
                raise Exception("归并操作成功的提示不对：{}".format(toastContent))
        time.sleep(1)
        with allure.step("回到邮件首页"):
            self.find_element(self.emailHomePage_loc).click()
        with allure.step("点击{}下的{}箱子".format(boxCategory,boxName)):
            if boxCategory == "客户箱":
                self.find_element(self.customerBoxPage_customerBoxBtn_loc).click()
                time.sleep(0.2)
                self.find_element(self.customerBoxPage_firstCustomerBoxBtn_loc).click()
            elif boxCategory == "供应商箱":
                self.find_element(self.supplierBoxPage_supplierBoxBtn_loc).click()
                time.sleep(0.2)
                self.find_element(self.supplierBoxPage_firstsupplierBoxBtn_loc).click()
            elif boxCategory == "内部联系人箱":
                self.find_element(self.innerBoxPage_innerBoxBtn_loc).click()
                time.sleep(0.2)
                self.find_element(self.innerBoxPage_firstinnerBoxBtn_loc).click()
            elif boxCategory == "自定义箱":
                customxBoxBtn_loc = (By.XPATH,self.recipientBoxPage_customBoxListBtn_loc[1].replace("自定义箱测试，勿动",boxName))
                self.scroll_element(customxBoxBtn_loc)
                time.sleep(0.1)
                self.find_element(customxBoxBtn_loc).click()
        time.sleep(0.5)
        with allure.step("查看是否有主题是：{}的邮件".format(mergerMailSubject)):
            allMailSubjects = self.get_elementText(self.recipientBoxPage_emailSubject_loc,index="all")
            # allMergerMailSubjects = []
            # for mailSubject in allMailSubjects:
            #     allMergerMailSubjects.append(mailSubject.split("】")[1])
            if mergerMailSubject not in allMailSubjects:
                raise Exception("归并的邮件：{}，不在要归并的箱子里：{}".format(mergerMailSubject,boxName))
