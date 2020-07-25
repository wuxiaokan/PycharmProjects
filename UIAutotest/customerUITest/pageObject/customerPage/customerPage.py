#-*- encoding: utf-8 -*-
'''
@File    :   customerPage.py
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/17 0017 16:57   dmk      1.0         None
'''

import allure,time,os
from random import randint
from selenium.webdriver.common.by import By
from utils.generator import *
from utils.config import ATTACH_PATH
from pageObject.basePage import Action
from pageObject.customerPage.customerPage_loc import customerPageLoc
from pageObject.customerPage.customerPageCommon import customerPageCommon
from pageObject.customerRecycleBoxPage.customerRecycleBoxPageCommon import customerRecycleBoxPageCommon


class customerPage(Action,customerPageLoc):

    def __init__(self,driver):
        super(customerPage,self).__init__(driver)
        self.customerPageCommon = customerPageCommon(driver)
        self.customerRecycleBoxPageCommon = customerRecycleBoxPageCommon(driver)

    def run_delCustomer_case(self,is_recycleBox,is_single):
        if is_recycleBox:
            self.find_element(self.customerRecycleBoxPage_RecycleBoxBtn_loc).click()
            time.sleep(1)
        with allure.step("勾选可删除的客户选择框"):
            customerNameList_deleted = self.customerPageCommon.select_ableDelCustomer(is_single)
        with allure.step("点击删除按钮"):
            self.find_element(self.customerPage_customerDelBtn_loc).click()
        with allure.step("点击确定删除按钮"):
            self.find_element(self.customerPage_customerSureDelBtn_loc).click()
        time.sleep(0.5)
        # with allure.step("如果有再次确认，在次点击确认"):
        #     if len(self.is_element_exist(self.customerPage_customerSureDelBtn_loc[1])) > 1:
        #         self.find_element(self.customerPage_customerSureDelBtn_loc,index=1).click()
        with allure.step("判断toast提示是否正确"):
            toast_text = self.find_element(self.toast_loc).text
            if toast_text != "删除成功":
                raise Exception("客户删除成功后的提示：{}，不正确".format(toast_text))
        time.sleep(1)
        with allure.step("获取所有的客户列表"):
            customerNameList = self.customerPageCommon.get_allCustomerName()
        with allure.step("判断客户列表中是否还存在刚刚删除的客户"):
            for customerName_deleted in customerNameList_deleted:
                if customerName_deleted in customerNameList:
                    raise Exception("刚刚删除的客户：{}，依然在客户列表中：{}".format(customerName_deleted,customerNameList))
        with allure.step("判断回收箱是否有该客户"):
            with allure.step("点击回收箱按钮"):
                self.find_element(self.customerRecycleBoxPage_RecycleBoxBtn_loc).click()
            time.sleep(1)
            with allure.step("获取所有的回收箱客户"):
                customerNameList_recycleBox = self.customerRecycleBoxPageCommon.get_allCustomerName_recycleBox()
            with allure.step("判断回收箱是否有删除的箱子"):
                for customerName in customerNameList_deleted:
                    if is_recycleBox:
                        if customerName in customerNameList_recycleBox:
                            raise Exception("删除的客户：{}，没有在回收箱里面：{}".format(customerName,customerNameList_deleted))
                    else:
                        if customerName not in customerNameList_recycleBox:
                            raise Exception("删除的客户：{}，没有在回收箱里面：{}".format(customerName,customerNameList_deleted))