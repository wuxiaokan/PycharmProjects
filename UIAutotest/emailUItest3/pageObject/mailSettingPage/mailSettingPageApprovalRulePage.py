# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPageApprovalRulePage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/19 0019 11:15   dmk      1.0         None
'''

import time,allure
from selenium.webdriver.common.by import By
from utils.generator import *
from utils.log import logger
from .mailSettingPage import mailSettingPage
from .mailSettingPageApprovalRulePage_loc import mailSettingPageApprovalRulePageLoc
from pageObject.writeMailPage.writeMailPage_loc import writeMailPageLoc
from pageObject.recipientBoxPage.recipientBoxPage_loc import recipientBoxPageLoc
from pageObject.recipientBoxPage.recipientBoxPageCommon import recipientBoxPageCommon


class mailSettingPageApprovalRulePage(mailSettingPage,mailSettingPageApprovalRulePageLoc,writeMailPageLoc,recipientBoxPageLoc):

    def __init__(self,driver):
        super(mailSettingPageApprovalRulePage,self).__init__(driver)
        self.recipientBoxPageCommon = recipientBoxPageCommon(driver)

    def run_addApprovalRule_case(self,casename,condition,keyword,is_approval):
        with allure.step("回到邮件首页"):
            self.click_ele(self.emailHomePage_loc)
        with allure.step("审批掉所有的邮件"):
            self.recipientBoxPageCommon.run_approvalMail_case()
        with allure.step("切换到dmktest001"):
            self.switch_operator(operator="dmktest_001")
        with allure.step("点击邮箱设置按钮"):
            self.click_ele(self.mailSettingBtn_loc)
        with allure.step("点击审批规则按钮"):
            self.click_ele(self.mailSettingPageApprovalRulePage_approvalRuleBtn_loc)
            time.sleep(0.5)
        with allure.step("输入审批规则名字"):
            self.find_element(self.mailSettingPageApprovalRulePage_approvalRuleNameInput_loc).clear()
            self.find_element(self.mailSettingPageApprovalRulePage_approvalRuleNameInput_loc).send_keys("审批规则测试")
        # with allure.step("点击审批人选择框"):
        #     self.find_element(self.mailSettingPageApprovalRulePage_approvalPersonBtn_loc).click()
        # time.sleep(0.3)
        # with allure.step("选择审批人-管理员"):
        #     self.find_element(self.mailSettingPageApprovalRulePage_approvalPerson_loc).click()
        with allure.step("点击审批条件选择框"):
            self.find_element(self.mailSettingPageApprovalRulePage_approvalConditionBtn_loc).click()
        time.sleep(0.3)
        with allure.step("选中审批条件"):
            mailSettingPageApprovalRulePage_approvalCondition_loc = (By.XPATH,self.mailSettingPageApprovalRulePage_approvalCondition_loc[1].replace("全部审批（强制）",condition))
            self.screenshotImg(mailSettingPageApprovalRulePage_approvalCondition_loc)
            time.sleep(0.2)
            self.find_element(mailSettingPageApprovalRulePage_approvalCondition_loc).click()
        time.sleep(0.3)
        if "全部审批" not in condition:
            self.find_element(self.mailSettingPageApprovalRulePage_approvalConditionContainKeyInput_loc).clear()
            self.find_element(self.mailSettingPageApprovalRulePage_approvalConditionContainKeyInput_loc).send_keys(keyword)
        with allure.step("点击保存按钮"):
            self.find_element(self.mailSettingPageApprovalRulePage_saveApprovalRuleBtn).click()
        with allure.step("回到首页，点击写邮件"):
            self.find_element(self.emailHomePage_loc).click()
            self.find_element(self.writeEmailBtn_loc).click()
        time.sleep(2)
        with allure.step("输入收件人"):
            self.find_element(self.writeMailPage_recipientInput_loc).send_keys(random_email())
        with allure.step("输入邮件主题"):
            subject = random_name() + "-审批规则测试-" + time.strftime("%Y%m%d.%H.%M.%S")
            logger.info("用例：{}，测试审批规则的邮件主题：{}".format(casename,subject))
            logger.info("用例：{}，测试审批规则的邮件主题：{}".format(casename,subject))
            self.find_element(self.writeMailPage_emailSubjectInput_loc).send_keys(subject)
        with allure.step("输入邮件内容"):
            try:
                self.switch_frame(self.emailEditFrame_loc)
                self.find_element(self.emailBodyInEmailEdit_loc).send_keys(random_text())
            except Exception as e:
                print(e)
            finally:
                self.switch_parentFrame()
        with allure.step("点击发送按钮"):
            self.find_element(self.writeMailPage_sendEmailBtn_loc).click()
        if "可选" in condition:
            with allure.step("输入审批备注"):
                self.find_element(self.writeMailPage_submitApprovalInput_loc).send_keys("邮件审批测试{}".format(time.strftime("%Y%m%d.%H.%M.%S")))
            if is_approval == "1":
                self.find_element(self.writeMailPage_submitApprovalBtn_loc).click()
            elif is_approval == "0":
                self.find_element(self.writeMailPage_noApprovalBtn_loc).click()
        time.sleep(1)
        with allure.step("回到设置tab"):
            self.find_element(self.recipientBoxPage_settingTabBtn_loc).click()
        if "直接发送" not in casename:
            with allure.step("禁用审批规则，查看是否有正在审批的邮件的判断"):
                self.mouseHover(self.mailSettingPageApprovalRulePage_approvalRuleList_loc)
                time.sleep(0.3)
                self.find_element(self.mailSettingPageApprovalRulePage_disableApprovalRuleBtn_loc).click()
            with allure.step("获取toast提示"):
                toastText = self.find_element(self.toast_loc).text
                if toastText != "该审批规则有正在审批中的邮件，无法操作":
                    raise Exception("禁用有正在审批的邮件的审批规则，toast提示：{}，不对".format(toastText))
            time.sleep(1)
            with allure.step("删除审批规则，查看是否有正在审批的邮件的判断"):
                self.mouseHover(self.mailSettingPageApprovalRulePage_approvalRuleList_loc)
                time.sleep(0.3)
                self.find_element(self.mailSettingPageApprovalRulePage_approvalRuleDelBtn_loc).click()
                self.find_element(self.mailSettingPageApprovalRulePage_approvalRuleSureDelBtn_loc).click()
            with allure.step("获取toast提示"):
                toastText = self.find_element(self.toast_loc).text
                if toastText != "该审批规则有正在审批中的邮件，无法操作":
                    raise Exception("禁用有正在审批的邮件的审批规则，toast提示：{}，不对".format(toastText))
        time.sleep(3)
        with allure.step("回到邮件首页tab"):
            self.find_element(self.emailHomePage_loc).click()
        if is_approval == "0":
            with allure.step("点击已发箱，查看邮件"):
                self.find_element(self.recipientBoxPage_hasSendBoxBtn_loc).click()
        else:
            with allure.step("点击待发箱。查看邮件"):
                self.find_element(self.recipientBoxPage_waitSendBoxBtn_loc).click()
        with allure.step("查看是否有刚刚提交审批的邮件"):
            allEmailSubjectText = self.get_elementText(self.recipientBoxPage_emailSubject_loc,index="all")
            if subject not in allEmailSubjectText:
                raise Exception("待发箱或者已发箱没有主题是{}的邮件".format(subject))
        if "直接发送" not in casename:
            with allure.step("切换到dmktest账号"):
                self.switch_operator()
            with allure.step("审批所有的邮件"):
                self.recipientBoxPageCommon.run_approvalMail_case(subject=subject)
            with allure.step("切换到dmktest001"):
                self.switch_operator(operator="dmktest_001")
        with allure.step("判断已发箱是否有已经审批的邮件"):
            self.hasMailInBox(subject=subject)


    def hasMailInBox(self,subject):
        time.sleep(5)
        with allure.step("进入已发箱"):
            self.find_element(self.recipientBoxPage_hasSendBoxBtn_loc).click()
        time.sleep(1)
        with allure.step("判断已发箱是否有主题是：{}的邮件".format(subject)):
            allEmailSubjectText = self.get_elementText(self.recipientBoxPage_emailSubject_loc, index="all")
            logger.info(allEmailSubjectText)
            if subject not in allEmailSubjectText:
                raise Exception("已发箱没有主题是{}的邮件".format(subject))