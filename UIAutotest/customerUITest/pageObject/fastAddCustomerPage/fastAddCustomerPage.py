# -*- encoding: utf-8 -*-
'''
@File    :   fastAddCustomerPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/23 0023 9:26   dmk      1.0         None
'''

import allure,time,os
from random import randint
from selenium.webdriver.common.by import By
from utils.generator import *
from utils.config import ATTACH_PATH
from pageObject.basePage import Action
from pageObject.fastAddCustomerPage.fastAddCustomerPage_loc import fastAddCustomerPageLoc
from pageObject.fastAddCustomerPage.fastAddCustomerPageCommon import fastAddCustomerCommon
from pageObject.customerPage.customerPageCommon import customerPageCommon
from pageObject.customerPage.customerPage_loc import customerPageLoc
from pageObject.customerDetailPage.customerDetailPage_loc import customerDetailPageLoc
from pageObject.customerDetailPage.customerDetailPageCommon import customerDetailPageCommon
from pageObject.generalAddCustomerPage.generalAddCustomerPage_loc import generalAddCustomerPageLoc


class fastAddCustomer(Action,fastAddCustomerPageLoc,customerPageLoc,customerDetailPageLoc,generalAddCustomerPageLoc):

    def __init__(self,driver):
        super(fastAddCustomer,self).__init__(driver)
        self.fastAddCustomerCommon = fastAddCustomerCommon(driver)
        self.customerPageCommon = customerPageCommon(driver)
        self.customerDetailPageCommon = customerDetailPageCommon(driver)
        print(self.get_elementText(self.fastAddCustomerPage_fastAddCustomerBtn_loc))
        self.scroll_element(self.fastAddCustomerPage_fastAddCustomerBtn_loc)
        time.sleep(0.2)
        self.find_element(self.fastAddCustomerPage_fastAddCustomerBtn_loc).click()

    #快速新建客户
    def run_fastAddCustomer_case(self,customer_sendKeys,customer_selectKeys,customer_comment,attach):
        # for data in customer_sendKeys:
        #     key = list(data.keys())[0]
        #     value = list(data.values())[0]
        #     with allure.step("输入：{}".format(key)):
        #         self.fastAddCustomerCommon.sendKeys_customer(xpath=key,key=value)
        # for data in customer_selectKeys:
        #     key = list(data.keys())[0]
        #     value = list(data.values())[0]
        #     with allure.step("选择：{}".format(key)):
        #         self.fastAddCustomerCommon.selectKeys_customer(xpath=key, key=value)
        # with allure.step("输入备注"):
        #     self.find_element(self.fastAddCustomerPage_contactComment_loc).send_keys(customer_comment)
        # with allure.step("上传一个附件"):
        #     attach_path = os.path.join(ATTACH_PATH,attach)
        #     self.find_element_byPresence(self.fastAddCustomerPage_attachInput_loc).send_keys(attach_path)
        self.fastAddCustomerCommon.addCustomer(customer_sendKeys, customer_selectKeys,customer_comment, attach)
        with allure.step("点击保存按钮"):
            self.find_element(self.fastAddCustomerPage_saveBtn_loc).click()
        time.sleep(2)
        with allure.step("判断客户列表中是否有该客户"):
            with allure.step("获取所有的客户"):
                allCustomerList = self.customerPageCommon.get_allCustomerName()
            with allure.step("判断是否有新建的客户"):
                if customer_sendKeys[1]["客户名称"] in allCustomerList:
                    i = allCustomerList.index(customer_sendKeys[1]["客户名称"])
                    self.find_element(self.customerPage_customerName_loc,index=i).click()
                else:
                    raise Exception("快速新建的客户：{}，不在客户列表中：{}".format(customer_sendKeys[1]["客户名称"],allCustomerList))
        with allure.step("判断客户详情信息"):
            # with allure.step("全部展开客户信息"):
            #     customerInfoShowBtnEles = self.find_element(self.customerDetailPage_customerInfoShowBtn_loc,index="all")
            #     for customerInfoShowBtnEle in customerInfoShowBtnEles:
            #         customerInfoShowBtnEle.click()
            #         time.sleep(0.5)
            # with allure.step("展开联系人信息"):
            #     self.find_element(self.customerDetailPage_contactInfoShowBtn_loc).click()
            # for data in customer_sendKeys:
            #     key = list(data.keys())[0]
            #     value = list(data.values())[0]
            #     if key != "姓名" and key != "职务":
            #         with allure.step("获取：{}的信息，并判断".format(key)):
            #             info = self.customerDetailPageCommon.get_customerInfo(xpath=key)
            #             if key == "邮箱":
            #                 if value not in info:
            #                     raise Exception("该字段：{}，输入的客户信息：{}，与客户详情里面的信息：{}，不一致".format(key,value,info))
            #             else:
            #                 if str(value) != info:
            #                     raise Exception("该字段：{}，输入的客户信息：{}，与客户详情里面的信息：{}，不一致".format(key,value,info))
            #     elif key == "姓名":
            #         with allure.step("获取联系人的姓名，并判断是否正确"):
            #             contactName = self.find_element(self.customerDetailPage_contactName_loc).text
            #             if value != contactName:
            #                 raise Exception("输入的客户联系人姓名：{}，与客户详情里面的联系人姓名：{}，不一致".format(value,contactName))
            #     elif key == "职务":
            #         with allure.step("获取联系人的职务，并判断是否正确"):
            #             contactJob = self.find_element(self.customerDetailPage_contactJob_loc).text
            #             if value != contactJob:
            #                 raise Exception("输入的客户联系人的职务：{}，与客户详情里面的联系人职务：{}，不一致".format(value,contactJob))
            # for data in customer_selectKeys:
            #     key = list(data.keys())[0]
            #     value = list(data.values())[0]
            #     with allure.step("获取：{}的信息，并判断".format(key)):
            #         info = self.customerDetailPageCommon.get_customerInfo(xpath=key)
            #         if key == "国家/地区":
            #             if value not in info:
            #                 raise Exception("该字段：{}，输入的客户信息：{}，与客户详情里面的信息：{}，不一致".format(key, value, info))
            #         else:
            #             if value != info:
            #                 raise Exception("该字段：{}，输入的客户信息：{}，与客户详情里面的信息：{}，不一致".format(key, value, info))

    #快速新建，全屏操作
            self.customerDetailPageCommon.checkFastAddCustomer(customer_sendKeys, customer_selectKeys,attach)


    def run_fastAddCustomerFullScreen_case(self,customer_sendKeys,customer_selectKeys,customer_comment,attach):
        # for data in customer_sendKeys:
        #     key = list(data.keys())[0]
        #     value = list(data.values())[0]
        #     with allure.step("输入：{}".format(key)):
        #         self.fastAddCustomerCommon.sendKeys_customer(xpath=key, key=value)
        # for data in customer_selectKeys:
        #     key = list(data.keys())[0]
        #     value = list(data.values())[0]
        #     with allure.step("选择：{}".format(key)):
        #         self.fastAddCustomerCommon.selectKeys_customer(xpath=key, key=value)
        # with allure.step("输入备注"):
        #     self.find_element(self.fastAddCustomerPage_contactComment_loc).send_keys(customer_comment)
        # with allure.step("上传一个附件"):
        #     attach_path = os.path.join(ATTACH_PATH, attach)
        #     self.find_element_byPresence(self.fastAddCustomerPage_attachInput_loc).send_keys(attach_path)
        self.fastAddCustomerCommon.addCustomer(customer_sendKeys, customer_selectKeys,customer_comment, attach)
        with allure.step("点击全屏按钮"):
            self.find_element(self.fastAddCustomerPage_fullScreenBtn_loc).click()
        time.sleep(1)
        with allure.step("判断全屏之后，信息是否丢失"):
            for data in customer_sendKeys:
                key = list(data.keys())[0]
                value = list(data.values())[0]
                with allure.step("判断全屏前后的值是否一样"):
                    fullScreen_value = self.fastAddCustomerCommon.get_valueOfInput(key)
                    print(fullScreen_value)
                    if fullScreen_value != value:
                        raise Exception("全屏之后的值：{}，与全屏之前的值：{}，不一样".format(fullScreen_value,value))
            for data in customer_selectKeys:
                key = list(data.keys())[0]
                value = list(data.values())[0]
                with allure.step("判断全屏前后的值是否一样"):
                    fullScreen_value = self.fastAddCustomerCommon.get_valueOfInput(key)
                    print(fullScreen_value)
                    if fullScreen_value != value:
                        raise Exception("全屏之后的值：{}，与全屏之前的值：{}，不一样".format(fullScreen_value,value))
            with allure.step("判断联系人备注是否被带过来"):
                # with allure.step("点击联系人信息展开按钮"):
                #     self.find_element(self.generalAddCustomerPage_showOrHideContactBtn_loc).click()
                # time.sleep(0.3)
                with allure.step("获取联系人备注，并判断"):
                    fullScreen_comment_value = self.find_element_byPresence(self.fastAddCustomerPage_contactComment_loc,index=1).get_attribute("value")
                    print(fullScreen_comment_value)
                    if fullScreen_comment_value != customer_comment:
                        raise Exception("全屏之后的联系人备注：{}，与全屏前的联系人备注：{}，不一样".format(fullScreen_comment_value,customer_comment))
            with allure.step("判断附件是否被带过来"):
                pass

    #is_save,1，保存，0，不保存，2取消
    #关闭快速新建页面
    def run_closeFastAddCustomer_case(self,data):
        if data["is_save"] == 1:
            self.fastAddCustomerCommon.addCustomer(data["customer_sendKeys"], data["customer_selectKeys"],data["customer_comment"], data["attach"])
        else:
            self.find_element(self.fastAddCustomerPage_customerNameInput_loc).send_keys(random_name()+"测试")
        time.sleep(1)
        with allure.step("点击关闭按钮"):
            self.find_element(self.fastAddCustomerPage_cloaseBtn_loc).click()
        if data["is_save"] == 1:
            with allure.step("点击是按钮"):
                self.find_element(self.fastAddCustomerPage_isSaveBtn_loc).click()
            time.sleep(2)
            with allure.step("判断快速新建页面是否会消失"):
                if self.is_element_exist(self.fastAddCustomerPage_fastAddHeader_loc[1]):
                    raise Exception("点击是之后，快速新建页面，不消失")
            with allure.step("判断客户列表中是否有该客户"):
                with allure.step("获取所有的客户"):
                    allCustomerList = self.customerPageCommon.get_allCustomerName()
                with allure.step("判断是否有新建的客户"):
                    if data["customer_sendKeys"][1]["客户名称"] in allCustomerList:
                        i = allCustomerList.index(data["customer_sendKeys"][1]["客户名称"])
                        self.find_element(self.customerPage_customerName_loc, index=i).click()
                        time.sleep(1)
                    else:
                        raise Exception("快速新建的客户：{}，不在客户列表中：{}".format(data["customer_sendKeys"][1]["客户名称"], allCustomerList))
            with allure.step("判断客户详情信息"):
                self.customerDetailPageCommon.checkFastAddCustomer(data["customer_sendKeys"],data["customer_selectKeys"],data["attach"])
        elif data["is_save"] == 0:
            with allure.step("点击否按钮"):
                self.find_element(self.fastAddCustomerPage_notSaveBtn_loc).click()
            time.sleep(2)
            with allure.step("判断快速新建页面是否会消失"):
                if self.is_element_exist(self.fastAddCustomerPage_fastAddHeader_loc[1]):
                    raise Exception("点击否之后，快速新建页面，不消失")
        elif data["is_save"] == 2:
            with allure.step("点击取消按钮"):
                self.find_element(self.fastAddCustomerPage_cancelSaveBtn_loc).click()
            time.sleep(2)
            with allure.step("判断快速新建页面是否还在"):
                if not self.is_element_exist(self.fastAddCustomerPage_fastAddHeader_loc[1]):
                    raise Exception("点击取消之后，快速新建页面消失")