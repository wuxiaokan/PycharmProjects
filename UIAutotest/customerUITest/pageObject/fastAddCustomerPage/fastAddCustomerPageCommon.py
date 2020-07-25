# -*- encoding: utf-8 -*-
'''
@File    :   fastAddCustomerPageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/23 0023 9:26   dmk      1.0         None
'''


import allure,time,os
from utils.config import ATTACH_PATH
from selenium.webdriver.common.by import By
from pageObject.basePage import Action
from pageObject.fastAddCustomerPage.fastAddCustomerPage_loc import fastAddCustomerPageLoc

class fastAddCustomerCommon(Action,fastAddCustomerPageLoc):

    #根据客户名称重新生成xpath
    def generateXpathByCustomerName(self,xpath):
        if xpath == "联系地址":
            loc = (By.XPATH,self.fastAddCustomerPage_customerNameInput_loc[1].replace("客户名称",xpath).replace("input","textarea"))
        else:
            loc = (By.XPATH,self.fastAddCustomerPage_customerNameInput_loc[1].replace("客户名称",xpath))
        return loc

    #根据国家地区列表重新生成xpath
    def generateXpathByCountryList(self,xpath):
        loc = (By.XPATH,self.fastAddCustomerPage_customerTypeList_loc[1].replace("新客户",xpath))
        return loc



    #输入客户的相关字段
    def sendKeys_customer(self,xpath,key):
        loc = self.generateXpathByCustomerName(xpath)
        self.scroll_element(loc)
        self.find_element(loc).clear()
        self.find_element(loc).send_keys(str(key))

    #选择客户的相关字段
    def selectKeys_customer(self,xpath,key):
        loc1 = self.generateXpathByCustomerName(xpath)
        self.scroll_element(loc1)
        self.find_element(loc1).click()
        time.sleep(0.3)
        loc2 = self.generateXpathByCountryList(key)
        self.find_element(loc2).click()


    #获取input框里面的value
    def get_valueOfInput(self,xpath,index=0):
        loc = self.generateXpathByCustomerName(xpath)
        return self.find_element_byPresence(loc,index=index).get_attribute("value")

    #快速新建客户，输入，各个字段
    def addCustomer(self,customer_sendKeys,customer_selectKeys,customer_comment,attach):
        for data in customer_sendKeys:
            key = list(data.keys())[0]
            value = list(data.values())[0]
            with allure.step("输入：{}".format(key)):
                self.sendKeys_customer(xpath=key, key=value)
        for data in customer_selectKeys:
            key = list(data.keys())[0]
            value = list(data.values())[0]
            with allure.step("选择：{}".format(key)):
                self.selectKeys_customer(xpath=key, key=value)
        with allure.step("输入备注"):
            self.find_element(self.fastAddCustomerPage_contactComment_loc).send_keys(customer_comment)
        with allure.step("上传一个附件"):
            attach_path = os.path.join(ATTACH_PATH, attach)
            self.find_element_byPresence(self.fastAddCustomerPage_attachInput_loc).send_keys(attach_path)
            time.sleep(1)