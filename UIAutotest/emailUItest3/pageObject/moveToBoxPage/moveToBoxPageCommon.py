# -*- encoding: utf-8 -*-
'''
@File    :   moveToBoxPageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/18 0018 19:11   dmk      1.0         None
'''

import allure,time
from pageObject.basePage import Action
from pageObject.moveToBoxPage.moveToBoxPage_loc import moveToBoxPageLoc
from pageObject.recipientBoxPage.recipientBoxPageCommon import recipientBoxPageCommon

class moveToBoxPageCommon(Action,moveToBoxPageLoc):

    def __init__(self,driver):
        super(moveToBoxPageCommon,self).__init__(driver)
        self.recipientBoxPageCommon = recipientBoxPageCommon(driver)

    #选择一个自定义箱子
    def selectCustomBox(self,is_del=1,index=0):
        if is_del:
            with allure.step("点击第一个可删除的自定义箱子"):
                firstBoxEle = self.find_element(self.moveToBoxPage_canDelCustomBoxList_loc,index=index)
                firstBoxEle.click()
                return firstBoxEle.text
        else:
            with allure.step("点击第一个自定义箱子"):
                firstBoxEle = self.find_element(self.moveToBoxPage_customBoxList_loc,index=index)
                firstBoxEle.click()
                return firstBoxEle.text

    #选择一个客户箱或者供应商箱子
    def selectCustomerOrSupplierBox(self):
        firstBoxEle = self.find_element(self.moveToBoxPage_customerBoxList_loc)
        firstBoxEle.click()
        return firstBoxEle.text

    #选择第一个内部联系人箱子
    def selectInnerBox(self):
        firstBoxEle = self.find_element(self.moveToBoxPage_innerBoxList_loc)
        firstBoxEle.click()
        return firstBoxEle.text.split("<")[0]



    #点击确认移动按钮
    def click_sureMove(self):
        self.click_ele(self.moveToBoxPage_sureMoveBtn_loc)


    #移动邮件到自定义箱子
    def moveEmailToCustomBox(self):
        with allure.step("选择2封邮件"):
            self.recipientBoxPageCommon.selectEmail(email_num=2)
        with allure.step("点击移动到自定义箱子"):
            self.recipientBoxPageCommon.moveToBox(boxCategory="自定义箱")
        time.sleep(1)
        with allure.step("选择第一个可删除的自定义箱子"):
            self.selectCustomBox(is_del=1)
        with allure.step("点击确认按钮"):
            self.click_sureMove()