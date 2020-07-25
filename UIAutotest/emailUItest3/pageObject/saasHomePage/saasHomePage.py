# -*- encoding: utf-8 -*-
'''
@File    :   saasHomePage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/25 0025 19:52   dmk      1.0         None
'''


import allure,time,traceback
from selenium.webdriver.common.by import By
from utils.log import logger
from utils.config import IMAGE_PATH
from pageObject.basePage import Action
from pageObject.saasHomePage.saasHomePage_loc import saasHomePageLoc
from pageObject.saasHomePage.seniorSearchEmailPage_loc import seniorSearchEmailPageLoc

class saasHomePage(Action,saasHomePageLoc):

    def run_sysNavLocal_case(self):
        with allure.step("悬浮外贸管理tab"):
            self.switch_mainPage()
            self.mouseHover(self.saasHomePage_sysNav_tradeTabBtn_loc)
        with allure.step("判断每个tab的href值"):
            conditions = ["邮件查询","写邮件","未读箱","审批箱"]
            keywords = ["search","write","unread","approve"]

            for i in range(len(conditions)):
                condition_loc = (By.XPATH,self.saasHomePage_sysNav_tradeTabBtn_loc[1].replace("外贸管理",conditions[i]))
                href = self.find_element(condition_loc).get_attribute("href")
                href_key = href.split("=")[-1]
                if href_key != keywords[i]:
                    raise Exception("该tab：{}的href：{}不对".format(conditions[i],keywords[i]))