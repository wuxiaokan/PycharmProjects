# -*- encoding: utf-8 -*-
'''
@File    :   customerInfoShowPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/13 0013 10:45   dmk      1.0         None
'''

import allure,re,time
from random import randint
from selenium.webdriver.common.by import By
from utils.generator import *
from pageObject.basePage import Action
from pageObject.customerInfoShowPage.customerInfoShowPage_loc import customerInfoShowPageLoc
from pageObject.recipientBoxPage.recipientBoxPageCommon import recipientBoxPageCommon
from pageObject.customerInfoShowPage.addFollowPageCommon import addFollowPageCommon
from pageObject.customerInfoShowPage.relatedBusinessPageCommon import relatedBusinessPageCommon
from pageObject.writeMailPage.writeMailCommon import writeMailCommon

class customerInfoShowPage(Action,customerInfoShowPageLoc):

    def __init__(self,driver):
        super(customerInfoShowPage,self).__init__(driver)
        self.recipientBoxPageCommon = recipientBoxPageCommon(driver)
        self.addFollowPageCommon = addFollowPageCommon(driver)
        self.relatedBusinessPageCommon = relatedBusinessPageCommon(driver)
        self.writeMailCommon = writeMailCommon(driver)
        with allure.step("点击查询箱：合作客户，勿动"):
            queryBox_loc = (By.XPATH,self.receiptBox_loc[1].replace("收件箱","合作客户，勿动"))
            self.click_ele(queryBox_loc,key="点击查询箱：合作客户，勿动")
        with allure.step("点击客户icon图标"):
            self.click_ele(self.recipientBoxPage_iconBtn_loc,key="点击客户icon图标")


    #客户主信息展示
    def run_customerMainInfo_case(self):
        with allure.step("获取并判断联系人是否正确"):
            customerContact = self.get_elementText(self.customerInfoShowPage_showContact_loc,key="获取客户联系人")
            assert customerContact == "fttx444<fttx444@aliyun.com>"
        with allure.step("获取客户名称信息"):
            customerName = self.get_elementText(self.customerInfoShowPage_showCustomerName_loc,key="获取客户名称简称")
            assert customerName == "客户简称test-勿动--测试，勿动"
        with allure.step("获取客户类型"):
            customerType = self.get_elementText(self.customerInfoShowPage_customerType_loc,key="获取客户类型")
            assert customerType == "合作客户"
        with allure.step("获取客户标签"):
            customerMark = self.get_elementText(self.customerInfoShowPage_customerMark_loc,key="获取客户标签")
            assert customerMark == "勿动"
        with allure.step("获取跟进阶段"):
            followStage = self.get_elementText(self.customerInfoShowPage_followStage_loc,key="获取跟进阶段")
            assert followStage in ["商务洽谈","资料获得","产品推广"]


    #基础信息展示
    def run_customerBaseInfo_case(self,data):
        for k,v in data.items():
            with allure.step("获取{}，并断言".format(k)):
                info_loc = (By.XPATH,self.customerInfoShowPage_adrress_loc[1].replace("联系地址",k))
                info_text = self.get_elementText(info_loc,key="获取{}信息".format(k))
                assert info_text == v
        with allure.step("获取所有的联系人姓名，并断言"):
            contactName = self.get_elementText(self.customerInfoShowPage_contactName_loc,index="all",key="获取联系人姓名")
            assert contactName == ["fttx444","联系人测试"]
        with allure.step("获取所有的联系人邮箱地址，并断言"):
            contactEmailAct = self.get_elementText(self.customerInfoShowPage_contactEmailAct_loc,index="all",key="获取联系人地址")
            assert contactEmailAct == ["fttx444@aliyun.com","789@qq.com"]
        with allure.step("获取所有的联系人手机号"):
            contactTel = self.get_elementText(self.customerInfoShowPage_contactTel_loc,index="all",key="获取联系人手机号")
            assert contactTel == ["13836167619","--"]

    #判断往来邮件数
    def run_validateDealingEmailNum_case(self):
        with allure.step("获取往来邮件数，并点击"):
            contactInfo_dealingEmailNum = self.get_elementText(self.customerInfoShowPage_contactEmailNum_loc,key="获取客户信息展示页面的邮件数")
            contactInfo_dealingEmailNum = re.findall("\d+",contactInfo_dealingEmailNum)
            self.click_ele(self.customerInfoShowPage_contactEmailNum_loc,key="点击客户信息展示页面的邮件数")
        time.sleep(2)
        with allure.step("获取列表中，实际的往来邮件数"):
            dealingEmailNum = self.get_elementText(self.emailNumTotal_loc,index=-1,key="获取实际的往来邮件数")
            dealingEmailNum = re.findall("\d+",dealingEmailNum)
            assert dealingEmailNum == contactInfo_dealingEmailNum


    #新建跟进
    def run_addFollow_case(self):
        with allure.step("点击新建跟进按钮"):
            self.click_ele(self.customerInfoShowPage_addFollowBtn_loc,key="点击新建跟进按钮")
            followContent = random_text().replace("\n","")
        self.addFollowPageCommon.addFollow(followContent)
        time.sleep(1)
        with allure.step("获取第一个跟进"):
            firstFollowContent = self.relatedBusinessPageCommon.get_followContent()
            assert firstFollowContent == followContent


    #写邮件
    def run_sendEmail_case(self):
        with allure.step("获取当前的邮件地址"):
            current_emailAct = self.get_elementText(self.customerInfoShowPage_showContact_loc,key="获取当前的邮件地址")
        with allure.step("点击写邮件按钮"):
            self.click_ele(self.customerInfoShowPage_sendEmailBtn_loc,key="点击写邮件按钮")
        time.sleep(2)
        with allure.step("获取写信页面带入的收件人"):
            recipient = self.writeMailCommon.get_recipientsOfWriteEmailPage()
            print(recipient)
        assert current_emailAct == recipient[0]
        assert len(recipient) == 1


    #修改跟进阶段
    def run_editFollowStage_case(self):
        with allure.step("点击修改跟进阶段按钮"):
            self.click_ele(self.customerInfoShowPage_editFollowStageBtn_loc,key="点击修改跟进阶段按钮")
        time.sleep(0.5)
        with allure.step("点击跟进阶段下拉框"):
            self.click_ele(self.customerInfoShowPage_followStageCheckBox_loc,key="点击跟进阶段下拉框")
        time.sleep(1)
        with allure.step("随机选中一个跟进阶段"):
            random_followStageEle = self.find_element(self.customerInfoShowPage_followStageList_loc,index=randint(0,2))
            random_followStage_text = random_followStageEle.text
            random_followStageEle.click()
        with allure.step("点击确认按钮"):
            self.click_ele(self.customerInfoShowPage_sureEditFollowStageBtn_loc,key="点击确认按钮")
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc,key="获取toast提示")
            assert toast_text == "修改成功"
        with allure.step("获取修改后的跟进阶段"):
            followStage_edited = self.get_elementText(self.customerInfoShowPage_followStage_loc,key="获取修改后的跟进阶段")
        assert random_followStage_text == followStage_edited



    #多个收件联系人信息展示
    def run_someContactInfo_case(self):
        with allure.step("发送一封普通邮件，收件人包含客户，供应商，内部联系人，未建档"):
            self.click_ele(self.writeEmailBtn_loc)
            recipients = ["fttx444<fttx444@aliyun.com>","fttxtest<fttxtest@sina.cn>","fttx666<fttx666@aliyun.com>","云基础<fttx333@aliyun.com>"]
            emailSubect = random_name() + "--多个收件人测试--" + time.strftime("%Y%m%d.%H.%M.%S")
            self.writeMailCommon.send_generalEmail(recipient=recipients,subject=emailSubect)
        with allure.step("回到已发箱，点击邮件icon"):
            if self.recipientBoxPageCommon.is_existEmailOfBox(email_subject=emailSubect,boxName="已发箱",time_num=3):
                with allure.step("判断是否有右上角提示框，如果有，则关闭"):
                    self.recipientBoxPageCommon.is_closeRightTopNotify()
                icon_loc = (By.XPATH,self.recipientBoxPage_iconBtnBySubject_loc[1].replace("333",emailSubect))
                self.click_ele(icon_loc)
            else:
                raise Exception("已发箱没有主题是：{}的邮件".format(emailSubect))
        for recipient in recipients:
            with allure.step("点击联系人地址，出现下拉框"):
                self.click_ele(self.customerInfoShowPage_showContact_loc)
            time.sleep(1)
            with allure.step("选中联系人：{}".format(recipient)):
                contact_loc = (By.XPATH,self.customerInfoShowPage_showContactList_loc[1].replace("xxx",recipient))
                self.click_ele(contact_loc)
            time.sleep(1)
            if recipient == "fttx444<fttx444@aliyun.com>":
                with allure.step("获取客户名，并断言"):
                    customerName = self.get_elementText(self.customerInfoShowPage_showCustomerName_loc)
                    assert customerName == "客户简称test-勿动--测试，勿动"
            elif recipient == "fttxtest<fttxtest@sina.cn>":
                with allure.step("获取供应商名，并断言"):
                    supplierName = self.get_elementText(self.customerInfoShowPage_showCustomerName_loc)
                    assert supplierName == "供应商测试，勿动，谢谢，fttxtest@sina.cn--fttxtest@sina.cn"
            elif recipient == "fttx666<fttx666@aliyun.com>":
                with allure.step("判断是否有添加客户按钮"):
                    if not self.is_element_exist(self.unArchiverInfoShowPage_addCustomerBtn_loc[1]):
                        raise Exception("未建档联系人信息展示页面，没有添加客户按钮")
            elif recipient == "云基础<fttx333@aliyun.com>":
                with allure.step("判断是否有基础信息，只能推荐tab按钮"):
                    if self.is_element_click(self.customerInfoShowPage_baseInfoTabBtn_loc):
                        raise Exception("内部联系人信息页面有基础信息tab按钮")
                    recommendBtn_loc = (By.XPATH,self.customerInfoShowPage_baseInfoTabBtn_loc[1].replace("基础信息","智能推荐"))
                    if self.is_element_click(recommendBtn_loc):
                        raise Exception("内部联系人信息页面有智能推荐tab按钮")