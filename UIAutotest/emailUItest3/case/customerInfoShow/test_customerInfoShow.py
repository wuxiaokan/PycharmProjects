# -*- encoding: utf-8 -*-
'''
@File    :   test_customerInfoShow.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/13 0013 11:31   dmk      1.0         None
'''

import pytest,allure
from pageObject.customerInfoShowPage.customerInfoShowPage import customerInfoShowPage

customerBaseInfo_datas = [(1,"客户基础信息展示判断",{"客户编码":"C00000001","网址":"--","电 话":"1257423","传 真":"82069967","联系地址":"吉林省文市海港孙路x座 389615","主营产品":"电器,服装","客户等级":"重要","客户来源":"广交会","业务类型":"贸易公司"})]

@allure.feature("客户信息展示相关功能")
class TestCustomerInfoShow:

    @allure.story("客户主信息展示")
    def test_customerMainInfo(self,login):
        self.driver = customerInfoShowPage(login)
        self.driver.run_customerMainInfo_case()

    @allure.story("客户基础信息展示")
    @pytest.mark.parametrize("caseid,casename,data",customerBaseInfo_datas)
    def test_customerBaseInfo(self,caseid,casename,data,login):
        self.driver = customerInfoShowPage(login)
        self.driver.run_customerBaseInfo_case(data)

    @allure.story("联系人往来邮件数验证")
    def test_validateDealingEmailNum(self,login):
        self.driver = customerInfoShowPage(login)
        self.driver.run_validateDealingEmailNum_case()


    @allure.story("新建跟进相关功能")
    def test_addFollow(self,login):
        self.driver = customerInfoShowPage(login)
        self.driver.run_addFollow_case()


    @allure.story("邮件联系人带入写邮件页面")
    def test_sendEmail(self,login):
        self.driver = customerInfoShowPage(login)
        self.driver.run_sendEmail_case()


    @allure.story("编辑跟进阶段")
    def test_editFollowStage(self,login):
        self.driver = customerInfoShowPage(login)
        self.driver.run_editFollowStage_case()


    @allure.story("多个联系人切换相关功能")
    def test_someContactInfo(self,login):
        self.driver = customerInfoShowPage(login)
        self.driver.run_someContactInfo_case()



if __name__ == '__main__':
    pytest.main(["-s","test_customerInfoShow.py"])