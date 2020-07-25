# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/19 0019 16:12   dmk      1.0         None
'''
import allure,time,traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.log import logger
from utils.config import IMAGE_PATH
from utils.generator import *
from pageObject.basePage import Action


class mailSettingPage(Action):
    #邮箱设置按钮
    mailSettingBtn_loc = (By.XPATH,'//div[@class="setIcon icon"]')


    def __init__(self,driver):
        super(mailSettingPage,self).__init__(driver)
        self.find_element(self.mailSettingBtn_loc).click()


