# -*- encoding: utf-8 -*-
'''
@File    :   customerBoxPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/21 0021 10:13   dmk      1.0         None
'''

import allure,time,pytest
from selenium.webdriver.common.by import By
from pageObject.basePage import Action
from pageObject.customerBoxPage.customerBoxPage_loc import customerBoxPageLoc
from pageObject.customerBoxPage.customerBoxPageCommon import customerBoxPageCommon

class customerBoxPage(Action,customerBoxPageLoc):

    def __init__(self,driver):
        super(customerBoxPage,self).__init__(driver)
        self.customerBoxPageCommon = customerBoxPageCommon(driver)
        self.find_element(self.customerBoxPage_customerBoxBtn_loc).click()


    # #客户箱新增自定义箱
    # def run_customerBoxPageAddCustomerBox_case(self):
    #     with allure.step("悬浮最近联系分组下的一个分组"):
    #         self.mouseHover(self.customerBoxPage_recentContactGroupCustomer_loc)
    #     time.sleep(0.2)
    #     with allure.step("悬浮更多操作按钮"):
    #         self.mouseHover(self.customerBoxPage_customerGroupMoreOperate_loc)
    #     time.sleep(0.3)
    #     with allure.step("点击新增自定义箱按钮"):
    #         # self.mouseClick(self.customerBoxPage_addCustomerBoxBtn_loc)
    #         self.click_ele(self.customerBoxPage_addCustomerBoxBtn_loc,key="点击新增自定义箱")
    #     with allure.step("输入自定义箱名字"):
    #         self.find_element(self.customerBoxPage_addCustomerBoxInput_loc).send_keys("箱子测试")
    #     with allure.step("点击√号，新增箱子"):
    #         self.find_element(self.customerBoxPage_sureAddCustomerBoxBtn_loc).click()
    #     with allure.step("获取所有的箱子列表"):
    #         time.sleep(0.5)
    #         allCustomBoxList = self.get_elementText(self.customerBoxPage_customBox_loc,index="all")
    #         print(allCustomBoxList)
    #     with allure.step("断言刚刚创建的箱子是否在列表中"):
    #         if "箱子测试" not in allCustomBoxList:
    #             self.screenshotImg(key="客户箱新增自定义箱")
    #             raise Exception("创建的自定义箱不在自定义箱子列表中")

    #搜索客户箱
    def run_searchCustomerBox_case(self,data):
        with allure.step("搜索框输入{}".format(data["keyword"])):
            self.sendKeys(self.customerBoxPage_customerBoxSearchInput_loc,key=data["keyword"])
        time.sleep(1)
        with allure.step("点击搜索按钮"):
            self.click_ele(self.customerBoxPage_customerBoxSearchBtn_loc)
        with allure.step("获取搜索结果，并断言"):
            """UI上不能准备断言结果，所以暂时使用数量"""
            customerBoxNames = self.customerBoxPageCommon.get_allCustomerBoxName()
            pytest.assume(len(customerBoxNames) == 1,"所有的客户箱名：{}".format(customerBoxNames))


    #显示方式选择
    """display_type:0,名称，1，简称，2，代码，3，全选,4,全不选"""
    def run_selectDisplayMode_case(self,casename,data):
        with allure.step("点击设置按钮"):
            self.click_ele(self.customerBoxPage_customerBoxSettingBtn_loc)
        with allure.step("{}".format(casename)):
            if data["select_customerName"]:
                self.customerBoxPageCommon.select_displayMode(is_select=1)
            else:
                self.customerBoxPageCommon.select_displayMode(is_select=0)
            if data["select_customerShortName"]:
                self.customerBoxPageCommon.select_displayMode(is_select=1,type="客户简称")
            else:
                self.customerBoxPageCommon.select_displayMode(is_select=0,type="客户简称")
            if data["select_customerCode"]:
                self.customerBoxPageCommon.select_displayMode(is_select=1,type="客户代码")
            else:
                self.customerBoxPageCommon.select_displayMode(is_select=0,type="客户代码")
        with allure.step("点击确定按钮"):
            self.click_ele(self.customerBoxPage_sureBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            pytest.assume(data["toast"] == toast_text,'data["toast"]:{},toast_text:{}'.format(data["toast"],toast_text))
        with allure.step("获取最近联系的客户箱名"):
            customerBoxNames = self.customerBoxPageCommon.get_allCustomerBoxName(level=2)
            pytest.assume(data["expect"] in customerBoxNames,'data["expect"]:{},customerBoxNames:{}'.format(data["expect"],customerBoxNames))


    #分类设置
    def run_selectCategory_case(self,data):
        with allure.step("点击设置按钮"):
            self.click_ele(self.customerBoxPage_customerBoxSettingBtn_loc)
        with allure.step("点击一级分类下拉框"):
            self.click_ele(self.customerBoxPage_firstCategoryInput_loc)
        time.sleep(0.5)
        with allure.step("选中一级分类：{}".format(data["firstCategory"])):
            firstCategory_loc = (By.XPATH,self.customerBoxPage_customerCategoryList_loc[1].replace("客户类型",data["firstCategory"]))
            self.click_ele(firstCategory_loc)
        time.sleep(1)
        with allure.step("点击二级分类下拉框"):
            self.click_ele(self.customerBoxPage_secondCategoryInput_loc)
        time.sleep(0.5)
        with allure.step("选中二级分类：{}".format(data["secondCategory"])):
            secondCategory_loc = (By.XPATH,self.customerBoxPage_customerCategoryList_loc[1].replace("客户类型",data["secondCategory"]))
            self.click_ele(secondCategory_loc)
        with allure.step("点击确定按钮"):
            self.click_ele(self.customerBoxPage_sureBtn_loc)
        if data["firstCategory"] == data["secondCategory"]:
            with allure.step("获取toast提示"):
                toast_text = self.get_elementText(self.toast_loc)
                pytest.assume(toast_text == data["toast_except"])
        else:
            time.sleep(2)
            with allure.step("获取所有的一级客户箱子"):
                # firstCustomerBoxNames = []
                # firstCustomerBoxEles = self.find_element(self.customerBoxPage_customerBoxGroupNameList_loc,index="all")
                # for firstCustomerBoxEle in firstCustomerBoxEles:
                #     firstCustomerBoxEle.click()
                #     time.sleep(0.5)
                #     firstCustomerBoxNames.append(firstCustomerBoxEle.text)
                firstCustomerBoxNames = self.get_elementText(self.customerBoxPage_customerBoxGroupNameList_loc,index="all")
                print(firstCustomerBoxNames)
                pytest.assume(data["first_except"] in firstCustomerBoxNames,'data["first_except"]:{},firstCustomerBoxNames:{}'.format(data["first_except"],firstCustomerBoxNames))
            if data["secondCategory"] != "请选择":
                with allure.step("获取所有的二级客户箱子"):
                    secondCustomerBoxEles = self.find_element(self.customerBoxPage_customerBoxGroupNameList_loc, index="all")
                    for secondCustomerBoxEle in secondCustomerBoxEles:
                        secondCustomerBoxEle.click()
                        time.sleep(0.5)
                    secondCustomerBoxNames = self.get_elementText(self.customerBoxPage_customerBoxSecondGroupNameList_loc,index="all")
                    print(secondCustomerBoxNames)
                    pytest.assume(data["second_except"] in secondCustomerBoxNames,'data["second_except"]:{},secondCustomerBoxNames:{}'.format(data["second_except"],secondCustomerBoxNames))