# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPageEmailTemplatePageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/29 0029 15:19   dmk      1.0         None
'''

import allure,time,os
from random import randint
from selenium.webdriver.common.by import By
from utils.config import ATTACH_PATH
from utils.generator import *
from pageObject.basePage import Action
from pageObject.mailSettingPage.mailSettingPageEmailTemplatePage_loc import mailSettingPageEmailTemplatePageLoc


class mailSettingPageEmailTemplatePageCommon(Action,mailSettingPageEmailTemplatePageLoc):

    #获取模板名
    def get_emailTemplateNames(self):
        with allure.step("点击邮箱设置按钮"):
            self.click_ele(self.mailSettingBtn_loc,key="点击邮箱设置按钮")
        with allure.step("点击邮件模板按钮"):
            self.click_ele(self.mailSettingPageEmailTemplatePage_emailTemplateBtn_loc,key="点击邮件模板按钮")
        with allure.step("获取所有的自定义模板名"):
            emailTemplateNames = self.get_elementText(self.mailSettingPageEmailTemplatePage_emailTemplateName_loc,index="all",key="获取所有的自定义模板名")
            return emailTemplateNames