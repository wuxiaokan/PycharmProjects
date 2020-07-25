# -*- encoding: utf-8 -*-
'''
@File    :   generalAddCustomerCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/16 0016 11:00   dmk      1.0         None
'''

import allure,time
from random import randint
from selenium.webdriver.common.by import By
from utils.generator import *
from pageObject.basePage import Action
from pageObject.customerPage.customerPage_loc import customerPageLoc
from pageObject.generalAddCustomerPage.generalAddCustomerPage_loc import generalAddCustomerPageLoc
from pageObject.customerDetailPage.customerDetailPage_loc import customerDetailPageLoc

class generalAddCustomerCommon(Action,generalAddCustomerPageLoc,customerDetailPageLoc,customerPageLoc):

    #根据客户名称重新生成xpath
    def generateXpathByCustomerName(self,xpath):
        if xpath[:-2] == "Linked":
            loc = (By.XPATH,self.generalAddCustomerPage_countryDropDownBtn_loc[1].replace("国家/地区","Linked"))
        elif xpath == "联系地址":
            loc = (By.XPATH,self.generalAddCustomerPage_customerNameInput_loc[1].replace("客户名称",xpath).replace("input","textarea"))
        else:
            loc = (By.XPATH,self.generalAddCustomerPage_customerNameInput_loc[1].replace("客户名称",xpath))
        return loc

    #根据国家地区列表重新生成xpath
    def generateXpathByCountryList(self,xpath):
        loc = (By.XPATH,self.generalAddCustomerPage_customerCode_countryList_loc[1].replace("阿富汗",xpath))
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


    #判断新增客户还是编辑客户
    def is_addCustomer(self,is_add):
        if is_add:
            with allure.step("悬浮新建客户下拉按钮"):
                self.mouseHover(self.generalAddCustomerPage_addCustomerDropDownBtn_loc)
            time.sleep(1)
            with allure.step("点击普通新建客户按钮"):
                print(self.find_element(self.generalAddCustomerPage_generalAddCustomerBtn_loc).text)
                self.mouseClick(self.generalAddCustomerPage_generalAddCustomerBtn_loc)
        else:
            with allure.step("点击可删除的客户"):
                allCustomerNameEles = self.find_element(self.customerPage_customerName_loc,index="all")
                for customerNameEle in allCustomerNameEles:
                    if "可删除" in customerNameEle.text:
                        customerNameEle.click()
                        break
            time.sleep(1)
            with allure.step("点击编辑按钮"):
                self.find_element(self.customerDetailPage_customerEditBtn_loc).click()



    #生成一个客户编码
    def generate_customerCode(self):
        with allure.step("生成客户代码"):
            with allure.step("点击客户二维码按钮"):
                self.find_element(self.generalAddCustomerPage_customerQRcodeBtn_loc).click()
            with allure.step("点击国家一级选择框"):
                self.find_element(self.generalAddCustomerPage_customerCode_firstDropBoxOfCountry_loc).click()
            time.sleep(0.3)
            with allure.step("随机选择一个国家"):
                randomCountryEle = self.find_element(self.generalAddCustomerPage_customerCodeList_loc,index=randint(0,9))
                randomCountryEle.click()
            time.sleep(0.2)
            with allure.step("点击sku一级选择框"):
                self.find_element(self.generalAddCustomerPage_customerCode_firstDropBoxOfSku_loc).click()
            time.sleep(0.2)
            with allure.step("选择一个sku编码"):
                randomSKUcodeEle = self.find_element(self.generalAddCustomerPage_customerCodeList_loc,index=randint(0,1))
                skuText = randomSKUcodeEle.text.split("|")[0].strip()
                randomSKUcodeEle.click()
            with allure.step("点击申请编码按钮"):
                self.find_element(self.generalAddCustomerPage_appplyCustomerCodeBtn_loc).click()
            time.sleep(0.5)
            with allure.step("获取生成的客户编码"):
                customerCode = self.find_element(self.generateXpathByCustomerName("客户代码")).get_attribute("value")
            with allure.step("判断生成的代码是否正确"):
                currentTime = time.strftime("%Y%m%d")
                if "C" not in customerCode or skuText not in customerCode or currentTime not in customerCode:
                    raise Exception("生成的客户代码：{}，不正确".format(customerCode))
                return customerCode


    #输入几个必要信息
    def write_needfulCustomerInfo(self):
        with allure.step("输入客户编码"):
            customerInput_loc = self.generateXpathByCustomerName("客户代码")
            self.find_element(customerInput_loc).send_keys(random_number(20))
        with allure.step("输入客户名称"):
            customerName = random_name() +str(random_number(3))+ "测试，可删除"
            self.find_element(self.generalAddCustomerPage_customerNameInput_loc).send_keys(customerName)
        with allure.step("点击客户类型一级选择框"):
            customerType_loc = self.generateXpathByCustomerName("客户类型")
            self.find_element(customerType_loc).click()
            time.sleep(0.3)
        with allure.step("选择第一个客户类型"):
            customerType_loc = self.generateXpathByCountryList("合作客户")
            self.find_element(customerType_loc).click()
            with allure.step("输入联系人姓名"):
                contactNameInput_loc = self.generateXpathByCustomerName("姓名")
                self.find_element(contactNameInput_loc).send_keys("联系人测试")