# -*- encoding: utf-8 -*-
'''
@File    :   innerContactInfoShow.py
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/15 0015 19:33   dmk      1.0         None
'''

import allure
from pageObject.basePage import Action
from pageObject.innerContactInfoShowPage.innerContactInfoShowPage_loc import innerContactInfoShowPageLoc
from pageObject.innerContactInfoShowPage.innerContactInfoShowPageCommon import innerContactInfoShowPageCommon


class innerContactInfoShowPage(Action,innerContactInfoShowPageLoc):

    def __init__(self,driver):
        super(innerContactInfoShowPage,self).__init__(driver)
        self.innerContactInfoShowPageCommon = innerContactInfoShowPageCommon(driver)
        self.innerContactInfoShowPageCommon.click_unArchiverIcon()


    #内部联系人页面页面布局
    def run_unArchiverMainInfo_case(self):
        with allure.step("获取第一个内部联系人地址"):
            firstUnArchiveEmailAct = self.get_elementText(self.recipientBoxPage_innerContactEmailAct_loc)
        with allure.step("获取显示的内部联系人地址"):
            showUnArchiveEmailAct = self.get_elementText(self.innerContactInfoShowPage_contactEmailAct_loc)
        assert firstUnArchiveEmailAct in showUnArchiveEmailAct
        with allure.step("判断是否有智能推荐tab"):
            if self.find_element(self.innerContactInfoShowPage_smartRecommendBtn_loc):
                raise Exception("内部联系人页面，有智能推荐tab")
        with allure.step("判断是否有往来邮件tab"):
            if not self.is_element_exist(self.innerContactInfoShowPage_dealingEmailBtn_loc[1]):
                raise Exception("内部联系人页面，没有往来邮件tab")