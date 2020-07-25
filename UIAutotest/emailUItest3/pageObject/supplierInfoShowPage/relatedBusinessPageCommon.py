# -*- encoding: utf-8 -*-
'''
@File    :   relatedBusinessPageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/14 0014 13:53   dmk      1.0         None
'''

import allure
from pageObject.basePage import Action
from pageObject.customerInfoShowPage.relatedBusinessPage_loc import relatedBusinessPageLoc


class relatedBusinessPageCommon(Action,relatedBusinessPageLoc):

    #获取跟进内容
    def get_followContent(self,index=0):
        with allure.step("点击相关业务按钮"):
            self.click_ele(self.relatedBusinessPage_relatedBusinessBtn_loc,key="点击相关业务按钮")
        if isinstance(index,int):
            with allure.step("获取第{}个跟进内容".format(int(index)+1)):
                return self.get_elementText(self.relatedBusinessPage_followContentList_loc,index=index,key="获取第{}个跟进内容".format(int(index)+1))
        else:
            with allure.step("获取所有的跟进内容"):
                return self.get_elementText(self.relatedBusinessPage_followContentList_loc,index="all",key="获取所有的跟进内容")