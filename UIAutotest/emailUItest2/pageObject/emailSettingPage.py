# -*- encoding: utf-8 -*-
'''
@File    :   emailSettingPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/26 0026 10:50   dmk      1.0         None
'''

import time
from selenium.webdriver.common.by import By
from .basePage import Action

class emailSettingPage(Action):
    #设置按钮xpath
    emailSetting_loc = (By.XPATH,"//div[@class='setIcon icon']")


    def __init__(self,driver):
        super(emailSettingPage,self).__init__(driver=driver)
        self.find_element(self.emailSetting_loc).click()


    #点击设置按钮，进入设置页面
    def click_settingBtn(self):
        self.find_element(self.emailSetting_loc).click()