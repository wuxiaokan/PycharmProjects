# -*- encoding: utf-8 -*-
'''
@File    :   queryBoxPageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/21 0021 14:42   dmk      1.0         None
'''

import allure,time,pytest
from selenium.webdriver.common.by import By
from pageObject.basePage import Action
from pageObject.queryBoxPage.queryBoxPage_loc import queryBoxPageLoc



class queryBoxPageCommon(Action,queryBoxPageLoc):



    #获取查询箱名
    def get_queryBoxNames(self,is_del=0,index="all"):
        if is_del:
            return self.get_elementText(self.queryBoxPage_canDelQueryBoxList_loc,index=index)
        else:
            return self.get_elementText(self.queryBoxPage_queryBoxList_loc,index=index)


    #删除查询箱
    def del_queryBox(self):
        if self.is_element_exist(self.queryBoxPage_canDelQueryBoxList_loc[1]):
            with allure.step("悬浮第1个可删除的查询箱"):
                self.mouseHover_visibleEle(self.queryBoxPage_canDelQueryBoxList_loc)
            time.sleep(0.5)
            with allure.step("悬浮更多操作按钮"):
                self.mouseHover_visibleEle(self.queryBoxPage_queryBoxMoreOperateBtn_loc)
            time.sleep(1)
            with allure.step("点击删除该查询箱按钮"):
                self.click_ele(self.queryBoxPage_delQueryBoxBtn_loc)
            with allure.step("点击确定按钮"):
                self.click_ele(self.queryBoxPage_sureDelQueryBoxBtn_loc)
            with allure.step("获取toast提示"):
                toast_text = self.get_elementText(self.toast_loc)
                pytest.assume(toast_text == "删除成功","toast_text:{}".format(toast_text))


    #根据主题生成输入框xpath
    def generateXpathBySubject(self,text):
        loc = (By.XPATH,self.queryBoxPage_subjectInput_loc[1].replace("主题",text))
        return loc


    #根据主题生成输入框xpath
    def generateEqualXpathBySubject(self,text):
        loc = (By.XPATH,self.queryBoxPage_equalBtn_loc[1].replace("主题",text))
        return loc


    #根据附件按钮生成xpath
    def generateRadioBtnXpathBySubject(self,text):
        loc = (By.XPATH,self.queryBoxPage_attachRadioBtn_loc[1].replace("附件",text))
        return loc


    #根据主营产品列表生成xpath
    def generateXpathByMainProductList(self,text):
        loc = (By.XPATH,self.queryBoxPage_mainProductelEctrical_loc[1].replace("电器",text))
        return loc