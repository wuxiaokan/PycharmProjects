# -*- encoding: utf-8 -*-
'''
@File    :   dealingEmailPage.py
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/13 0013 15:49   dmk      1.0         None
'''

import allure,re,time
from selenium.webdriver.common.by import By
from pageObject.supplierInfoShowPage.supplierInfoShowPage import supplierInfoShowPage
from pageObject.customerInfoShowPage.dealingEmailPage_loc import dealingEmailPageLoc
from pageObject.emailDetailPage.emailDetailPageCommon import emailDetailPageCommon
from pageObject.customerInfoShowPage.dealingEmailPageCommon import dealingEmailPageCommon
from pageObject.recipientBoxPage.recipientBoxPageCommon import recipientBoxPageCommon


class dealingEmailPage(supplierInfoShowPage,dealingEmailPageLoc):

    def __init__(self,driver):
        super(dealingEmailPage,self).__init__(driver)
        self.click_ele(self.dealingEmailPage_dealingEmailBtn_loc,key="点击往来邮件按钮")
        self.emailDetailPageCommon = emailDetailPageCommon(driver)
        self.dealingEmailPageCommon = dealingEmailPageCommon(driver)
        self.recipientBoxPageCommon = recipientBoxPageCommon(driver)


    #设置邮件未读，已读
    def run_setEmailReadStatus_case(self):
        with allure.step("获取未读邮件数"):
            unreadEmailNum_v1 = self.recipientBoxPageCommon.get_unReadEmailNum()
        with allure.step("获取读按钮title,并点击"):
            readEmailBtn_title = self.find_element(self.dealingEmailPage_markReadBtn_loc,key="获取邮件读按钮").get_attribute("title")
            self.click_ele(self.dealingEmailPage_markReadBtn_loc,key="点击读状态按钮")
        with allure.step("获取未读邮件数"):
            unreadEmailNum_v2 = self.recipientBoxPageCommon.get_unReadEmailNum()
        with allure.step("判断未读邮件数是否正确"):
            if readEmailBtn_title == "点击标记已读":
                assert int(unreadEmailNum_v1) == int(unreadEmailNum_v2) + 1
            else:
                assert int(unreadEmailNum_v1) == int(unreadEmailNum_v2) - 1
        with allure.step("再次点击读按钮"):
            self.click_ele(self.dealingEmailPage_markReadBtn_loc,key="点击读按钮")
        with allure.step("获取未读邮件数"):
            unreadEmailNum_v3 = self.recipientBoxPageCommon.get_unReadEmailNum()
        with allure.step("判断未读邮件数是否正确"):
            assert int(unreadEmailNum_v1) == int(unreadEmailNum_v3)


    # 设置邮件星标
    def run_setEmailStarStatus_case(self):
        with allure.step("获取星标邮件数"):
            starEmailNum_v1 = self.recipientBoxPageCommon.get_starEmailNum()
        with allure.step("获取星标按钮title,并点击"):
            starEmailBtn_title = self.find_element(self.dealingEmailPage_markStarBtn_loc, key="获取邮件星标按钮").get_attribute("title")
            self.click_ele(self.dealingEmailPage_markStarBtn_loc, key="点击星标状态按钮")
        with allure.step("获取星标邮件数"):
            starEmailNum_v2 = self.recipientBoxPageCommon.get_starEmailNum()
        with allure.step("判断星标邮件数是否正确"):
            if starEmailBtn_title == "点击设置星标":
                assert int(starEmailNum_v1) == int(starEmailNum_v2) - 1
            else:
                assert int(starEmailNum_v1) == int(starEmailNum_v2) + 1
        with allure.step("再次点击星标按钮"):
            self.click_ele(self.dealingEmailPage_markStarBtn_loc, key="点击星标按钮")
        with allure.step("获取未星标邮件数"):
            starEmailNum_v3 = self.recipientBoxPageCommon.get_starEmailNum()
        with allure.step("判断未星标邮件数是否正确"):
            assert int(starEmailNum_v1) == int(starEmailNum_v3)

    #收发状态判断
    def run_receiveOrSendStatus_case(self,data):
        with allure.step("点击{}按钮".format(data["option"])):
            statusBtn_loc = (By.XPATH,self.dealingEmailPage_allEmailBtn_loc[1].replace("全",data["option"]))
            self.click_ele(statusBtn_loc,key="点击{}按钮".format(data["option"]))
        with allure.step("获取所有的收发状态"):
            allStatusEles = self.find_element(self.dealingEmailPage_emailReceiveSendIcon_loc,index="all",key="获取所有的收发状态")
            allStatusColors = []
            for statusEle in allStatusEles:
                allStatusColors.append(statusEle.value_of_css_property("color"))
            assert set(allStatusColors) == data["except"]


    #往来邮件跳转
    def run_clickDealingEmail_case(self):
        with allure.step("获取第一封邮件主题,并点击"):
            firstEmailSubject = self.get_elementText(self.dealingEmailPage_emailSubjectList_loc,key="获取第一封往来邮件主题")
            self.click_ele(self.dealingEmailPage_emailSubjectList_loc,key="点击第一封往来邮件")
        time.sleep(2)
        with allure.step("获取邮件详情中的邮件主题"):
            emailSubject_detail = self.emailDetailPageCommon.get_subjectOfEmailDetail()
            assert firstEmailSubject == emailSubject_detail


    #根据邮件账号往来邮件过滤
    def run_filterDealingEmailByEmailAct_case(self):
        self.dealingEmailPageCommon.selectEmailAct("test@ali")
        with allure.step("判断是否有邮件"):
            if self.is_element_exist(self.dealingEmailPage_emailList_loc[1]):
                raise Exception("选择了包含789的地址，不应该有邮件列表，实际上却有邮件列表")
        self.dealingEmailPageCommon.selectEmailAct("test@sina")
        with allure.step("判断是否有邮件"):
            if not self.is_element_exist(self.dealingEmailPage_emailList_loc[1]):
                raise Exception("选择了包含fttx444的地址，应该有邮件列表，实际上却没有邮件列表")