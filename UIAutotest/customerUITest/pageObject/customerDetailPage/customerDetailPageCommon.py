# -*- encoding: utf-8 -*-
'''
@File    :   customerDetailPageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/17 0017 15:27   dmk      1.0         None
'''

import allure,time
from random import randint
from selenium.webdriver.common.by import By
from pageObject.basePage import Action
from pageObject.customerDetailPage.customerDetailPage_loc import customerDetailPageLoc

class customerDetailPageCommon(Action,customerDetailPageLoc):


    #根据客户详情客户代码重新生成xpath
    def generateXpathByCustomerCodeDetail(self,xpath):
        if xpath[:-2] == "Linked":
            xpath = "Linked"
        loc = (By.XPATH,self.customerDetailPage_customerCodeDetail_loc[1].replace("客户代码",xpath))
        return loc

    #获取客户详情信息
    def get_customerInfo(self,xpath):
        loc = self.generateXpathByCustomerCodeDetail(xpath)
        info = self.find_element(loc)
        return info.text


    #快速新建客户后的校验
    def checkFastAddCustomer(self,customer_sendKeys,customer_selectKeys,attach):
        with allure.step("判断客户详情信息"):
            with allure.step("校验附件"):
                with allure.step("点击文件按钮"):
                    self.scroll_element(self.customerDetailPage_fileBtn_loc)
                    time.sleep(0.5)
                    # self.find_element(self.customerDetailPage_fileBtn_loc).click()
                    self.mouseClick(self.customerDetailPage_fileBtn_loc)
                time.sleep(0.5)
                with allure.step("获取所有的附件名"):
                    allAttachNames = self.get_elementText(self.customerDetailPage_attachName_loc, index="all")
                with allure.step("判断附件是否在详情中"):
                    if attach not in allAttachNames:
                        raise Exception("客户详情中的附件：{}，不包含上传的附件：{}".format(allAttachNames, attach))
            with allure.step("全部展开客户信息"):
                customerInfoShowBtnEles = self.find_element(self.customerDetailPage_customerInfoShowBtn_loc,index="all")
                for customerInfoShowBtnEle in customerInfoShowBtnEles:
                    customerInfoShowBtnEle.click()
                    time.sleep(0.5)
            with allure.step("展开联系人信息"):
                self.find_element(self.customerDetailPage_contactInfoShowBtn_loc).click()
            for data in customer_sendKeys:
                key = list(data.keys())[0]
                value = list(data.values())[0]
                if key != "姓名" and key != "职务":
                    with allure.step("获取：{}的信息，并判断".format(key)):
                        info = self.get_customerInfo(xpath=key)
                        if key == "邮箱":
                            if value not in info:
                                raise Exception("该字段：{}，输入的客户信息：{}，与客户详情里面的信息：{}，不一致".format(key,value,info))
                        else:
                            if str(value) != info:
                                raise Exception("该字段：{}，输入的客户信息：{}，与客户详情里面的信息：{}，不一致".format(key,value,info))
                elif key == "姓名":
                    with allure.step("获取联系人的姓名，并判断是否正确"):
                        contactName = self.find_element(self.customerDetailPage_contactName_loc).text
                        if value != contactName:
                            raise Exception("输入的客户联系人姓名：{}，与客户详情里面的联系人姓名：{}，不一致".format(value,contactName))
                elif key == "职务":
                    with allure.step("获取联系人的职务，并判断是否正确"):
                        contactJob = self.find_element(self.customerDetailPage_contactJob_loc).text
                        if value != contactJob:
                            raise Exception("输入的客户联系人的职务：{}，与客户详情里面的联系人职务：{}，不一致".format(value,contactJob))
            for data in customer_selectKeys:
                key = list(data.keys())[0]
                value = list(data.values())[0]
                with allure.step("获取：{}的信息，并判断".format(key)):
                    info = self.get_customerInfo(xpath=key)
                    if key == "国家/地区":
                        if value not in info:
                            raise Exception("该字段：{}，输入的客户信息：{}，与客户详情里面的信息：{}，不一致".format(key, value, info))
                    else:
                        if value != info:
                            raise Exception("该字段：{}，输入的客户信息：{}，与客户详情里面的信息：{}，不一致".format(key, value, info))