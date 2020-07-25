# -*- encoding: utf-8 -*-
'''
@File    :   emailStarEmailPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/30 0030 15:40   dmk      1.0         None
'''

import time
from selenium.webdriver.common.by import By
from .basePage import Action

class emailStarEmailPage(Action):
    #星标邮件
    starEmail_loc = (By.XPATH,"//span[text()='星标邮件']")
    #星标邮件数量
    starEmailNum_loc = (By.XPATH,"//span[text()='星标邮件']/following-sibling::span")
    #星标按钮
    starBtn_loc = (By.XPATH,"//div[@class='star_g f0']//*[name()='svg']")


    def run_startEmailNum(self):
        #进入星标邮件页面
        time.sleep(3)
        self.find_element(self.starEmail_loc).click()
        self.starEmailNum = int(self.find_element(self.starEmailNum_loc).text)
        #点击取消星标
        time.sleep(1)
        self.find_element(self.starBtn_loc).click()
        #获取星标数量
        try:
            self.find_element(self.toast_loc)
            self.starEmailNum = self.starEmailNum - 1
        except Exception:
            raise Exception("取消星标后，星标数量没有变化")

        #点击标记星标
        self.find_element(self.starBtn_loc).click()
        #获取星标数量
        try:
            self.find_element(self.toast_loc)
            self.starEmailNum = self.starEmailNum + 1
        except Exception:
            raise Exception("标记星标后，星标数量没有变化")