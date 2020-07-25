# -*- encoding: utf-8 -*-
'''
@File    :   unArchiverInfoShowPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/15 0015 16:13   dmk      1.0         None
'''

import allure
from pageObject.basePage import Action
from pageObject.unArchiverInfoShowPage.unArchiverInfoShowPage_loc import unArchiverInfoShowPageLoc
from pageObject.unArchiverInfoShowPage.unArchiverInfoShowPageCommon import unArchiverInfoShowPageCommmon


class unArchiverInfoShowPage(Action,unArchiverInfoShowPageLoc):

    def __init__(self,driver):
        super(unArchiverInfoShowPage,self).__init__(driver)
        self.unArchiverInfoShowPageCommmon = unArchiverInfoShowPageCommmon(driver)
        self.unArchiverInfoShowPageCommmon.click_unArchiverIcon()


    #未建档联系人页面页面布局
    def run_unArchiverMainInfo_case(self):
        with allure.step("获取第一个未建档联系人地址"):
            firstUnArchiveEmailAct = self.get_elementText(self.recipientBoxPage_unArchiverEmailAct_loc)
        with allure.step("获取显示的未建档联系人地址"):
            showUnArchiveEmailAct = self.get_elementText(self.unArchiverInfoShowPage_contactEmailAct_loc)
        assert firstUnArchiveEmailAct == showUnArchiveEmailAct
        with allure.step("判断是否有智能推荐tab"):
            if not self.is_element_exist(self.unArchiverInfoShowPage_smartRecommendBtn_loc[1]):
                raise Exception("未建档联系人页面，没有智能推荐tab")
        with allure.step("判断是否有往来邮件tab"):
            if not self.is_element_exist(self.unArchiverInfoShowPage_dealingEmailBtn_loc[1]):
                raise Exception("未建档联系人页面，没有往来邮件tab")


    #添加为客户或者供应商
    def run_archiveCustomer_case(self,data):
        with allure.step("获取联系人邮件地址"):
            contactEmailAct = self.get_elementText(self.unArchiverInfoShowPage_contactEmailAct_loc)
            contactEmailAct_name = contactEmailAct.split("<")[0]
            contactEmailAct_act = contactEmailAct.split("<")[-1].split(">")[0]
        if data["is_addCustomer"]:
            with allure.step("点击添加客户按钮"):
                self.click_ele(self.unArchiverInfoShowPage_addCustomerBtn_loc)
            with allure.step("获取客户姓名"):
                customerName = self.find_element(self.customerPage_customerName_loc).get_attribute("value")
                assert customerName == contactEmailAct_act
            with allure.step("获取客户联系人姓名"):
                customerContactName = self.get_elementText(self.customerPage_contactName_loc)
                assert customerContactName == contactEmailAct_name
            with allure.step("获取客户联系人邮箱"):
                customerContactEmailAct = self.get_elementText(self.customerPage_contactEmailAct_loc)
                assert customerContactEmailAct == contactEmailAct_act