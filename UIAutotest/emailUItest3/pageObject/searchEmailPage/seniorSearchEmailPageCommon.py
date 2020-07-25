# -*- encoding: utf-8 -*-
'''
@File    :   seniorSearchEmailPageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/2 0002 10:13   dmk      1.0         None
'''

import allure,pytest
from pageObject.basePage import Action
from pageObject.searchEmailPage.seniorSearchEmailPage_loc import seniorSearchEmailPageLoc


class seniorSearchEmailPageCommon(Action,seniorSearchEmailPageLoc):

    #获取搜索结果邮件数
    """type:邮件数的类型，0，相关客户/供应商，1，全部位置，2，回复状态，3，阅读状态
        is_all:是否累加后返回
    """
    def get_searchEmailNum(self,type=0,is_all=1):
        if type == 0:
            with allure.step("获取每组客户的邮件总数，并返回"):
                emailNums = self.get_elementText(self.seniorSearchEmailPage_customerEmailNumList_loc,index="all")
        elif type == 1:
            with allure.step("获取全部的邮件总数，并返回"):
                emailNums = self.get_elementText(self.seniorSearchEmailPage_allPositionEmailNumList_loc,index="all")
        elif type == 2:
            with allure.step("获取回复状态的邮件总数，并返回"):
                emailNums = self.get_elementText(self.seniorSearchEmailPage_replyStatusEmailNumList_loc,index="all")
        elif type == 3:
            with allure.step("获取阅读状态的邮件总数，并返回"):
                emailNums = self.get_elementText(self.seniorSearchEmailPage_readStatusEmailNumList_loc,index="all")
        emailNums = [int(num[1:-1]) for num in emailNums]
        if is_all:
            return sum(emailNums)
        return emailNums


    #检查左边分组的邮件数
    def check_emailNumOfLeftSide(self,homepage_totalEmailNum=0):
        with allure.step("获取搜索之后的邮件总数"):
            totalEmailNum_v2 = self.get_elementText(self.emailNumTotal_loc)
            totalEmailNum_v2 = int(totalEmailNum_v2[2:-2])
            if homepage_totalEmailNum:
                pytest.assume(homepage_totalEmailNum != totalEmailNum_v2,"homepage_totalEmailNum:{},totalEmailNum_v2:{}".format(homepage_totalEmailNum,totalEmailNum_v2))
        with allure.step("获取客户/供应商的邮件总数"):
            totalEmailNum_customer = self.get_searchEmailNum()
            pytest.assume(totalEmailNum_customer > 0,"totalEmailNum_customer:{}".format(totalEmailNum_customer))
        with allure.step("获取全部位置的邮件总数"):
            totalEmailNum_allPosition = self.get_searchEmailNum(type=1)
            pytest.assume(totalEmailNum_allPosition == totalEmailNum_v2,"totalEmailNum_allPosition:{},totalEmailNum_v2:{}".format(totalEmailNum_allPosition,totalEmailNum_v2))
        with allure.step("获取回复状态的邮件总数"):
            totalEmailNum_reply = self.get_searchEmailNum(type=2)
            pytest.assume(totalEmailNum_reply == totalEmailNum_v2,"totalEmailNum_reply:{},totalEmailNum_v2:{}".format(totalEmailNum_reply,totalEmailNum_v2))
        with allure.step("获取阅读状态的邮件总数"):
            totalEmailNum_read = self.get_searchEmailNum(type=3)
            pytest.assume(totalEmailNum_read == totalEmailNum_v2,"totalEmailNum_read:{},totalEmailNum_v2:{}".format(totalEmailNum_read,totalEmailNum_v2))