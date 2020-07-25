# -*- encoding: utf-8 -*-
'''
@File    :   customerBoxPageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/28 0028 19:24   dmk      1.0         None
'''
from selenium.webdriver.common.by import By
from pageObject.basePage import Action
from pageObject.customerBoxPage.customerBoxPage_loc import customerBoxPageLoc

class customerBoxPageCommon(Action,customerBoxPageLoc):

    #获取所有的箱子名
    def get_allCustomerBoxName(self,level=1):
        customerBoxName_loc = (By.XPATH,self.customerBoxPage_customerBoxGroupNameList_loc[1].replace("1",str(level)))
        if self.is_element_exist(customerBoxName_loc[1]):
            return self.get_elementText(customerBoxName_loc,index="all")
        else:
            return None


    #选取显示方式
    def select_displayMode(self,is_select=0,type="客户名称"):
        type_loc = (By.XPATH,self.customerBoxPage_showCustomerName_loc[1].replace("客户名称",type))
        typeEle = self.find_element(type_loc)
        typeEleAttr = typeEle.get_attribute("class")
        if is_select:
            if "is-checked" not in typeEleAttr:
                typeEle.click()
        else:
            if "is-checked" in typeEleAttr:
                typeEle.click()