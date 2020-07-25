# -*- encoding: utf-8 -*-
'''
@File    :   test_dealingEmail.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/13 0013 16:39   dmk      1.0         None
'''

import allure,pytest
from pageObject.customerInfoShowPage.dealingEmailPage import dealingEmailPage

receiveOrSendStatus_datas = [(1,"过滤全部的邮件",{"option":"全","except":{'rgba(23, 131, 251, 1)', 'rgba(255, 85, 0, 1)'}}),(2,"过滤全部发的邮件",{"option":"发","except":{'rgba(255, 85, 0, 1)'}}),(3,"过滤全部收的邮件",{"option":"收","except":{'rgba(23, 131, 251, 1)'}})]



@allure.feature("客户信息页面，往来邮件相关功能")
class TestDealingEmail:

    @allure.story("往来邮件，已读未读设置相关功能")
    def test_setEmailReadStatus(self,login):
        self.driver = dealingEmailPage(login)
        self.driver.run_setEmailReadStatus_case()

    @allure.story("往来邮件，星标邮件设置相关功能")
    def test_setEmailStarStatus(self,login):
        self.driver = dealingEmailPage(login)
        self.driver.run_setEmailStarStatus_case()


    @allure.story("往来邮件收发过滤")
    @pytest.mark.parametrize("caseid,casename,data",receiveOrSendStatus_datas)
    def test_receiveOrSendStatus(self,caseid,casename,data,login):
        self.driver = dealingEmailPage(login)
        self.driver.run_receiveOrSendStatus_case(data)


    @allure.story("往来邮件跳转")
    def test_clickDealingEmail(self,login):
        self.driver = dealingEmailPage(login)
        self.driver.run_clickDealingEmail_case()


    @allure.story("跟进邮件账号过滤往来邮件")
    def test_filterDealingEmailByEmailAct(self,login):
        self.driver = dealingEmailPage(login)
        self.driver.run_filterDealingEmailByEmailAct_case()


if __name__ == '__main__':
    pytest.main(["-s","test_dealingEmail.py"])