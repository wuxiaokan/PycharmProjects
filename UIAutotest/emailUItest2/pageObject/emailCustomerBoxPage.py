# -*- encoding: utf-8 -*-
'''
@File    :   emailCustomerBoxPage.py
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/30 0030 11:05   dmk      1.0         None
'''
import time
from selenium.webdriver.common.by import By
from .basePage import Action

class emailCustomerBoxPage(Action):
    #客户箱按钮
    customerBox_loc = (By.XPATH,"//div[@id='tab-customer']")
    #客户箱设置按钮
    customerBoxSetting_loc = (By.XPATH,"//div[@class='customer-menu-page']//span[@class='el-tooltip icon-border']")
    #显示设置页面
    showSetting_loc = (By.XPATH,"//div[@aria-label='显示设置']")
    #显示方式的勾选框
    showCheckbox_loc = (By.XPATH,"//div[@aria-label='显示设置']//label[starts-with(@class,'el-checkbox')]")
    #确定按钮
    sureBtn_loc = (By.XPATH,"//div[@aria-label='显示设置']//button[@class='el-button el-button--primary']")


    def run_customerBoxSetting_case(self):
        #进入设置页面
        self.find_element(self.customerBox_loc).click()
        #点击客户箱设置
        self.find_element(self.customerBoxSetting_loc).click()
        #判断是否有选中
        if self.is_element_exist(self.showSetting_loc[1]):
            #获取所有的选择框
            self.checkBoxs = self.find_element(self.showCheckbox_loc,index="all")
            #遍历，如果选中，点击
            for self.checkBox in self.checkBoxs:
                if "is-checked" in self.checkBox.get_attribute("class"):
                    self.checkBox.click()
        #点击确定按钮
        self.find_element(self.sureBtn_loc).click()
        time.sleep(1)
        self.toastText1 = self.find_element(self.toast_loc).text
        print(self.toastText1)
        #选中第一个显示方式
        self.find_element(self.showCheckbox_loc).click()
        self.find_element(self.sureBtn_loc).click()
        time.sleep(1)
        self.toastText2 = self.find_element(self.toast_loc).text
        print(self.toastText2)
        return self.toastText1,self.toastText2

    #获取toas提示
    def get_toastText(self):
        #获取toas提示
        time.sleep(1)
        return self.find_element(self.toast_loc).text