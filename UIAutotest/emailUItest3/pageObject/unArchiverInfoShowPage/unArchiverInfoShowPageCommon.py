# -*- encoding: utf-8 -*-
'''
@File    :   unArchiverInfoShowPageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/15 0015 16:14   dmk      1.0         None
'''

import allure,time
from pageObject.basePage import Action
from pageObject.unArchiverInfoShowPage.unArchiverInfoShowPage_loc import unArchiverInfoShowPageLoc


class unArchiverInfoShowPageCommmon(Action,unArchiverInfoShowPageLoc):

    #点击未建档联系人图标
    def click_unArchiverIcon(self):
        with allure.step("获取所有的联系人icon"):
            allContactIconEles = self.find_element(self.recipientBoxPage_iconBtn_loc,index="all")
        with allure.step("点击未建档联系人icon"):
            for contactIconEle in allContactIconEles:
                iconStyleColor = contactIconEle.value_of_css_property("color")
                if iconStyleColor == "rgba(92, 107, 119, 1)":
                    time.sleep(2)
                    contactIconEle.click()
                    break