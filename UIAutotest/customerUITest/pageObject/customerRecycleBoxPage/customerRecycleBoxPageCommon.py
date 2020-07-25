# -*- encoding: utf-8 -*-
'''
@File    :   customerRecycleBoxPageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/20 0020 10:14   dmk      1.0         None
'''
import allure,time
from random import randint
from selenium.webdriver.common.by import By
from pageObject.basePage import Action
from pageObject.customerRecycleBoxPage.customerRecycleBoxPage_loc import customerRecycleBoxPageLoc


class customerRecycleBoxPageCommon(Action,customerRecycleBoxPageLoc):
    
    #获取所有的客户
    def get_allCustomerName_recycleBox(self):
        allCustomerNameList = self.get_elementText(self.customerRecycleBoxPage_customerName_loc,index="all")
        return allCustomerNameList