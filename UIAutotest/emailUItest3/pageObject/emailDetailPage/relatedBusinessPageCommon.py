# -*- encoding: utf-8 -*-
'''
@File    :   relatedBusinessPageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/9 0009 11:39   dmk      1.0         None
'''

import time,allure
from selenium.webdriver.common.by import By
from pageObject.basePage import Action
from pageObject.emailDetailPage.relatedBusinessPage_loc import relatedBusinessPageLoc


class relatedBusinessPageCommon(Action,relatedBusinessPageLoc):

    #获取已经关联的合同号
    def get_relatedCode(self,type):
        with allure.step("点击{}tab按钮".format(type)):
            typeTabBtn_loc = (By.XPATH,self.relatedBusinessPage_quoteTabBtn_loc[1].replace("报价",type))
            self.click_ele(typeTabBtn_loc,key="点击{}tab按钮".format(type))
            time.sleep(1)
        if type == "商机":
            return self.get_elementText(self.relatedBusinessPage_relatedBusinessCode_loc,key="获取商机编码")
        else:
            return self.get_elementText(self.relatedBusinessPage_relatedQuoteCode_loc,index="all",key="获取已经关联的合同号")