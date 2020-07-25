# -*- encoding: utf-8 -*-
'''
@File    :   supplierBoxPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/26 0026 17:40   dmk      1.0         None
'''
import allure,pytest,time
from selenium.webdriver.common.by import By
from pageObject.basePage import Action
from pageObject.supplierBoxPage.supplierBoxPage_loc import supplierBoxPageLoc
from pageObject.supplierBoxPage.supplierBoxPageCommon import supplierBoxPageCommon


class supplierBoxPage(Action,supplierBoxPageLoc):

    def __init__(self,driver):
        super().__init__(driver)
        self.supplierBoxPageCommon = supplierBoxPageCommon(driver)
        self.click_ele(self.supplierBoxPage_supplierBoxBtn_loc)


    #显示方式选择
    """display_type:0,名称，1，简称，2，代码，3，全选,4,全不选"""
    def run_selectDisplayMode_case(self,casename,data):
        with allure.step("点击设置按钮"):
            self.click_ele(self.supplierBoxPage_supplierBoxSettingBtn_loc)
        with allure.step("{}".format(casename)):
            if data["select_supplierName"]:
                self.supplierBoxPageCommon.select_displayMode(is_select=1)
            else:
                self.supplierBoxPageCommon.select_displayMode(is_select=0)
            if data["select_supplierShortName"]:
                self.supplierBoxPageCommon.select_displayMode(is_select=1,type="供应商简称")
            else:
                self.supplierBoxPageCommon.select_displayMode(is_select=0,type="供应商简称")
            if data["select_supplierCode"]:
                self.supplierBoxPageCommon.select_displayMode(is_select=1,type="供应商代码")
            else:
                self.supplierBoxPageCommon.select_displayMode(is_select=0,type="供应商代码")
        with allure.step("点击确定按钮"):
            self.click_ele(self.supplierBoxPage_sureBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            pytest.assume(data["toast"] == toast_text,'data["toast"]:{},toast_text:{}'.format(data["toast"],toast_text))
        with allure.step("获取最近联系的供应商箱名"):
            supplierBoxNames = self.supplierBoxPageCommon.get_allSupplierBoxName(level=2)
            pytest.assume(data["expect"] in supplierBoxNames,'data["expect"]:{},supplierBoxNames:{}'.format(data["expect"],supplierBoxNames))
            
            
    #搜索供应商箱
    def run_searchSupplierBox_case(self,data):
        with allure.step("搜索框输入{}".format(data["keyword"])):
            self.sendKeys(self.supplierBoxPage_supplierBoxSearchInput_loc,key=data["keyword"])
        time.sleep(1)
        with allure.step("点击搜索按钮"):
            self.click_ele(self.supplierBoxPage_supplierBoxSearchBtn_loc)
        with allure.step("获取搜索结果，并断言"):
            """UI上不能准备断言结果，所以暂时使用数量"""
            supplierBoxNames = self.supplierBoxPageCommon.get_allSupplierBoxName()
            pytest.assume(len(supplierBoxNames) == 1,"所有的供应商箱名：{}".format(supplierBoxNames))
            
            
    
    #分类设置
    def run_selectCategory_case(self,data):
        with allure.step("点击设置按钮"):
            self.click_ele(self.supplierBoxPage_supplierBoxSettingBtn_loc)
        with allure.step("点击一级分类下拉框"):
            self.click_ele(self.supplierBoxPage_firstCategoryInput_loc)
        time.sleep(0.5)
        with allure.step("选中一级分类：{}".format(data["firstCategory"])):
            firstCategory_loc = (By.XPATH,self.supplierBoxPage_supplierCategoryList_loc[1].replace("供应商类型",data["firstCategory"]))
            self.click_ele(firstCategory_loc)
        time.sleep(1)
        with allure.step("点击二级分类下拉框"):
            self.click_ele(self.supplierBoxPage_secondCategoryInput_loc)
        time.sleep(0.5)
        with allure.step("选中二级分类：{}".format(data["secondCategory"])):
            secondCategory_loc = (By.XPATH,self.supplierBoxPage_supplierCategoryList_loc[1].replace("供应商类型",data["secondCategory"]))
            self.click_ele(secondCategory_loc)
        with allure.step("点击确定按钮"):
            self.click_ele(self.supplierBoxPage_sureBtn_loc)
        if data["firstCategory"] == data["secondCategory"]:
            with allure.step("获取toast提示"):
                toast_text = self.get_elementText(self.toast_loc)
                pytest.assume(toast_text == data["toast_except"])
        else:
            time.sleep(2)
            with allure.step("获取所有的一级供应商箱子"):
                firstsupplierBoxNames = self.get_elementText(self.supplierBoxPage_supplierBoxGroupNameList_loc,index="all")
                print(firstsupplierBoxNames)
                pytest.assume(data["first_except"] in firstsupplierBoxNames,'data["first_except"]:{},firstsupplierBoxNames:{}'.format(data["first_except"],firstsupplierBoxNames))
            if data["secondCategory"] != "请选择":
                with allure.step("获取所有的二级供应商箱子"):
                    secondsupplierBoxEles = self.find_element(self.supplierBoxPage_supplierBoxGroupNameList_loc, index="all")
                    for secondsupplierBoxEle in secondsupplierBoxEles:
                        secondsupplierBoxEle.click()
                        time.sleep(0.5)
                    secondsupplierBoxNames = self.get_elementText(self.supplierBoxPage_supplierBoxSecondGroupNameList_loc,index="all")
                    print(secondsupplierBoxNames)
                    pytest.assume(data["second_except"] in secondsupplierBoxNames,'data["second_except"]:{},secondsupplierBoxNames:{}'.format(data["second_except"],secondsupplierBoxNames))