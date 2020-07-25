# -*- encoding: utf-8 -*-
'''
@File    :   supplierInfoShowPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/15 0015 14:05   dmk      1.0         None
'''

import allure,re,time
from utils.generator import *
from selenium.webdriver.common.by import By
from pageObject.basePage import Action
from pageObject.supplierInfoShowPage.supplierInfoShowPage_loc import supplierInfoShowPageLoc
from pageObject.customerInfoShowPage.addFollowPageCommon import addFollowPageCommon
from pageObject.supplierInfoShowPage.relatedBusinessPageCommon import relatedBusinessPageCommon
from pageObject.writeMailPage.writeMailCommon import writeMailCommon


class supplierInfoShowPage(Action,supplierInfoShowPageLoc):

    def __init__(self,driver):
        super(supplierInfoShowPage,self).__init__(driver)
        self.addFollowPageCommon = addFollowPageCommon(driver)
        self.relatedBusinessPageCommon = relatedBusinessPageCommon(driver)
        self.writeMailCommon = writeMailCommon(driver)
        with allure.step("点击查询箱：供应商邮件，勿动"):
            queryBox_loc = (By.XPATH,self.receiptBox_loc[1].replace("收件箱","供应商邮件，勿动"))
            self.click_ele(queryBox_loc,key="点击查询箱:供应商邮件，勿动")
        with allure.step("点击供应商icon图标"):
            self.click_ele(self.recipientBoxPage_iconBtn_loc,key="点击供应商icon图标")
            
            
    #供应商主信息展示
    def run_supplierMainInfo_case(self):
        with allure.step("获取并判断联系人是否正确"):
            supplierContact = self.get_elementText(self.supplierInfoShowPage_showContact_loc,key="获取供应商联系人")
            assert supplierContact == "fttxtest<fttxtest@sina.cn>"
        with allure.step("获取供应商名称信息"):
            supplierName = self.get_elementText(self.supplierInfoShowPage_showSupplierName_loc,key="获取供应商名称简称")
            assert supplierName == "供应商测试，勿动，谢谢，fttxtest@sina.cn--fttxtest@sina.cn"
        with allure.step("获取供应商类型"):
            supplierType = self.get_elementText(self.supplierInfoShowPage_supplierType_loc,key="获取供应商类型")
            assert supplierType == "加工商"
        with allure.step("获取供应商标签"):
            supplierMark = self.get_elementText(self.supplierInfoShowPage_supplierMark_loc,key="获取供应商标签")
            assert supplierMark == "蓝色"



    #基础信息展示
    def run_supplierBaseInfo_case(self,data):
        for k,v in data.items():
            with allure.step("获取{}，并断言".format(k)):
                info_loc = (By.XPATH,self.supplierInfoShowPage_adrress_loc[1].replace("联系地址",k))
                info_text = self.get_elementText(info_loc,key="获取{}信息".format(k))
                assert info_text == v
        with allure.step("获取所有的联系人姓名，并断言"):
            contactName = self.get_elementText(self.supplierInfoShowPage_contactName_loc,index="all",key="获取联系人姓名")
            assert contactName == ['fttxtest', 'test']
        with allure.step("获取所有的联系人邮箱地址，并断言"):
            contactEmailAct = self.get_elementText(self.supplierInfoShowPage_contactEmailAct_loc,index="all",key="获取联系人地址")
            assert contactEmailAct == ['fttxtest@sina.cn', 'test@aliyun.com']
        with allure.step("获取所有的联系人手机号"):
            contactTel = self.get_elementText(self.supplierInfoShowPage_contactTel_loc,index="all",key="获取联系人手机号")
            assert contactTel == ['--', '19999999999']


    #判断往来邮件数
    def run_validateDealingEmailNum_case(self):
        with allure.step("获取往来邮件数，并点击"):
            contactInfo_dealingEmailNum = self.get_elementText(self.supplierInfoShowPage_contactEmailNum_loc,key="获取客户信息展示页面的邮件数")
            contactInfo_dealingEmailNum = re.findall("\d+",contactInfo_dealingEmailNum)
            self.click_ele(self.supplierInfoShowPage_contactEmailNum_loc,key="点击客户信息展示页面的邮件数")
        time.sleep(2)
        with allure.step("获取列表中，实际的往来邮件数"):
            dealingEmailNum = self.get_elementText(self.emailNumTotal_loc,index=-1,key="获取实际的往来邮件数")
            dealingEmailNum = re.findall("\d+",dealingEmailNum)
            assert dealingEmailNum == contactInfo_dealingEmailNum


    #新建跟进
    def run_addFollow_case(self):
        with allure.step("点击新建跟进按钮"):
            self.click_ele(self.supplierInfoShowPage_addFollowBtn_loc,key="点击新建跟进按钮")
            followContent = random_text().replace("\n","")
        self.addFollowPageCommon.addFollow(followContent=followContent,is_customer=0)
        time.sleep(1)
        with allure.step("获取第一个跟进"):
            firstFollowContent = self.relatedBusinessPageCommon.get_followContent()
            assert firstFollowContent == followContent
            
    #写邮件
    def run_sendEmail_case(self):
        with allure.step("获取当前的邮件地址"):
            current_emailAct = self.get_elementText(self.supplierInfoShowPage_showContact_loc,key="获取当前的邮件地址")
        with allure.step("点击写邮件按钮"):
            self.click_ele(self.supplierInfoShowPage_sendEmailBtn_loc,key="点击写邮件按钮")
        time.sleep(2)
        with allure.step("获取写信页面带入的收件人"):
            recipient = self.writeMailCommon.get_recipientsOfWriteEmailPage()
            print(recipient)
        assert current_emailAct == recipient[0]
        assert len(recipient) == 1