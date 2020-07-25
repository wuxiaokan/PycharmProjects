# -*- encoding: utf-8 -*-
'''
@File    :   dealingEmailPageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/13 0013 15:50   dmk      1.0         None
'''

import allure,time
from pageObject.basePage import Action
from pageObject.customerInfoShowPage.dealingEmailPage_loc import dealingEmailPageLoc

class dealingEmailPageCommon(Action,dealingEmailPageLoc):


    #选择邮件地址账号
    def selectEmailAct(self,emailAct):
        with allure.step("点击所有联系人按钮"):
            self.click_ele(self.dealingEmailPage_allContactBtn_loc, key="点击所有联系人按钮")
        time.sleep(1)
        with allure.step("选择地址包含：{}的账号".format(emailAct)):
            allContactEles = self.find_element(self.dealingEmailPage_emailActList_loc, index="all")
            i = 0
            for contactEle in allContactEles:
                if emailAct in contactEle.text:
                    contactEle.click()
                    break
                else:
                    i = i + 1
                if i == len(allContactEles):
                    raise Exception("地址列表中，没有包含：{}的账号".format(emailAct))