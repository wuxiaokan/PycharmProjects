# -*- encoding: utf-8 -*-
'''
@File    :   supplierBoxPageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/29 0029 17:11   dmk      1.0         None
'''
import allure,pytest
from selenium.webdriver.common.by import By
from pageObject.basePage import Action
from pageObject.supplierBoxPage.supplierBoxPage_loc import supplierBoxPageLoc

class supplierBoxPageCommon(Action,supplierBoxPageLoc):

    #选取显示方式
    def select_displayMode(self,is_select=0,type="供应商名称"):
        type_loc = (By.XPATH,self.supplierBoxPage_showSupplierName_loc[1].replace("供应商名称",type))
        typeEle = self.find_element(type_loc)
        typeEleAttr = typeEle.get_attribute("class")
        if is_select:
            if "is-checked" not in typeEleAttr:
                typeEle.click()
        else:
            if "is-checked" in typeEleAttr:
                typeEle.click()


    #获取所有的箱子名
    def get_allSupplierBoxName(self,level=1):
        supplierBoxName_loc = (By.XPATH,self.supplierBoxPage_supplierBoxGroupNameList_loc[1].replace("1",str(level)))
        if self.is_element_exist(supplierBoxName_loc[1]):
            return self.get_elementText(supplierBoxName_loc,index="all")
        else:
            return None