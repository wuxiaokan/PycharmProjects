# -*- encoding: utf-8 -*-
'''
@File    :   customerPageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/19 0019 20:27   dmk      1.0         None
'''

import allure,time
from random import randint
from selenium.webdriver.common.by import By
from pageObject.basePage import Action
from pageObject.customerPage.customerPage_loc import customerPageLoc

class customerPageCommon(Action,customerPageLoc):

    #获取所有的客户
    def get_allCustomerName(self):
        allCustomerNameList = self.get_elementText(self.customerPage_customerName_loc,index="all")
        return allCustomerNameList

    #获取所有的可删除的客户名称
    def get_allAbleDelCustomerName(self):
        allAbleDelCustomerNameList = self.get_elementText(self.customerPage_canDelCustomerName_loc,index="all")
        return allAbleDelCustomerNameList

    #勾选可删除的客户
    def select_ableDelCustomer(self,is_single):
        with allure.step("获取所有的客户列表"):
            self.allCustomerNameList = self.get_allCustomerName()
        with allure.step("获取所有的可删除的客户列表"):
            self.allAbleDelCustomerNameList = self.get_allAbleDelCustomerName()
        with allure.step("获取所有的可删除的客户列表在所有的客户列表中的index"):
            allAbleDelCustomerNameIndex = []
            for self.customerName in self.allCustomerNameList:
                if self.customerName in self.allAbleDelCustomerNameList:
                    allAbleDelCustomerNameIndex.append(self.allCustomerNameList.index(self.customerName))
        self.customerNameList_selected = []
        if is_single:
            num = 1
        else:
            num = randint(2,5)
        with allure.step("勾选{}个客户".format(num)):
            for i in range(num):
                self.find_element(self.customerPage_customerCheckBox_loc,index=allAbleDelCustomerNameIndex[i]).click()
                self.customerNameList_selected.append(self.get_elementText(self.customerPage_customerName_loc,index=allAbleDelCustomerNameIndex[i]))
        return self.customerNameList_selected