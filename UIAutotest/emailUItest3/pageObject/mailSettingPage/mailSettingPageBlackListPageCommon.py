# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPageBlackListPageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/30 0030 10:46   dmk      1.0         None
'''


import allure,time,os
from random import randint
from selenium.webdriver.common.by import By
from utils.config import ATTACH_PATH
from utils.generator import *
from pageObject.basePage import Action
from pageObject.mailSettingPage.mailSettingPageBlackListPage_loc import mailSettingPageBlackListPageLoc

class mailSettingPageBlackListPageCommon(Action,mailSettingPageBlackListPageLoc):

    #获取黑名单列表
    def get_blackList(self):
        with allure.step("点击邮箱设置按钮"):
            self.click_ele(self.mailSettingBtn_loc,key="点击邮箱设置按钮")
        with allure.step("点击黑名单按钮"):
            self.click_ele(self.mailSettingPageBlackListPage_blackListBtn_loc,key="点击黑名单按钮")
        with allure.step("获取所有的黑名单列表"):
            blackLists = self.get_elementText(self.mailSettingPageBlackListPage_matchInfomationTd_loc,index="all",key="获取所有的黑名单列表")
            return blackLists

    #删除全部黑名单
    def del_allBlackList(self):
        with allure.step("切换到dmktest_001"):
            self.switch_operator(operator="dmktest_001")
        with allure.step("点击邮箱设置按钮"):
            self.click_ele(self.mailSettingBtn_loc,key="点击邮箱设置按钮")
        with allure.step("点击黑名单按钮"):
            self.click_ele(self.mailSettingPageBlackListPage_blackListBtn_loc,key="点击黑名单按钮")
        time.sleep(2)
        with allure.step("选择全选按钮"):
            allSelectCheckBoxEle = self.find_element(self.mailSettingPageBlackListPage_headCheckbox_loc,key="获取黑名单全选按钮")
            allSelectCheckBoxEleAttr = allSelectCheckBoxEle.get_attribute("class")
            if "is-disabled" not in allSelectCheckBoxEleAttr:
                self.click_ele(self.mailSettingPageBlackListPage_headCheckbox_loc,key="点击全选按钮")
                self.click_ele(self.mailSettingPageBlackListPage_delBlackListBtn_loc,key="点击全部删除按钮")