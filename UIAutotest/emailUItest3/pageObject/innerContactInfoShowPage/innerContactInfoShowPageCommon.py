# -*- encoding: utf-8 -*-
'''
@File    :   innerContactInfoShowPageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/15 0015 19:33   dmk      1.0         None
'''

import allure,time
from pageObject.basePage import Action
from pageObject.innerContactInfoShowPage.innerContactInfoShowPage_loc import innerContactInfoShowPageLoc


class innerContactInfoShowPageCommon(Action,innerContactInfoShowPageLoc):

    #点击内部联系人图标
    def click_unArchiverIcon(self):
        with allure.step("获取所有的联系人icon"):
            allContactIconEles = self.find_element(self.recipientBoxPage_iconBtn_loc,index="all")
        with allure.step("点击内部联系人icon"):
            for contactIconEle in allContactIconEles:
                iconStyleColor = contactIconEle.value_of_css_property("color")
                if iconStyleColor == "rgba(23, 131, 251, 1)":
                    time.sleep(2)
                    contactIconEle.click()
                    break