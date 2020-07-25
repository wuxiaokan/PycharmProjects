# -*- encoding: utf-8 -*-
'''
@File    :   customBoxPageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/18 0018 10:02   dmk      1.0         None
'''
import allure
from pageObject.basePage import Action
from pageObject.customBoxPage.customBoxPage_loc import customBoxPageLoc
from pageObject.moveToBoxPage.moveToBoxPageCommon import moveToBoxPageCommon
from pageObject.recipientBoxPage.recipientBoxPageCommon import recipientBoxPageCommon


class customBoxPageCommon(Action,customBoxPageLoc):

    def __init__(self,driver):
        super(customBoxPageCommon,self).__init__(driver)
        self.recipientBoxPageCommon = recipientBoxPageCommon(driver)
        self.moveToBoxPageCommon = moveToBoxPageCommon(driver)




    #获取所有的自定义箱子
    def get_allCustomBoxName(self,index="all",is_del=1):
        if is_del:
            return self.get_elementText(self.customBoxPage_canCancelParentCustomBoxList_loc,index=index)+self.get_elementText(self.customBoxPage_canCancelChildCustomBoxList_loc,index=index)
        return self.get_elementText(self.customBoxPage_customBoxList_loc,index=index)