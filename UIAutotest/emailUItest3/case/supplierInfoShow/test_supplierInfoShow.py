# -*- encoding: utf-8 -*-
'''
@File    :   test_supplierInfoShow.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/15 0015 14:17   dmk      1.0         None
'''

import pytest,allure
from pageObject.supplierInfoShowPage.supplierInfoShowPage import supplierInfoShowPage

supplierBaseInfo_datas = [(1,"供应商基础信息展示判断",{"供应商编码":"S00000001","网址":"--","电 话":"13000000000","传 真":"--","联系地址":"--","主营产品":"鞋包,苹果"})]

@allure.feature("供应商信息展示页面相关功能")
class TestSupplierInfoShowPage:

    @allure.story("供应商主要信息")
    def test_supplierMainInfo(self,login):
        self.driver = supplierInfoShowPage(login)
        self.driver.run_supplierMainInfo_case()

    @allure.story("供应商基础信息展示")
    @pytest.mark.parametrize("caseid,casename,data",supplierBaseInfo_datas)
    def test_supplierBaseInfo(self,caseid,casename,data,login):
        self.driver = supplierInfoShowPage(login)
        self.driver.run_supplierBaseInfo_case(data)

    @allure.story("联系人往来邮件数验证")
    def test_validateDealingEmailNum(self,login):
        self.driver = supplierInfoShowPage(login)
        self.driver.run_validateDealingEmailNum_case()
        
        
    @allure.story("新建跟进相关功能")
    def test_addFollow(self,login):
        self.driver = supplierInfoShowPage(login)
        self.driver.run_addFollow_case()
        
    
    @allure.story("邮件联系人带入写邮件页面")
    def test_sendEmail(self,login):
        self.driver = supplierInfoShowPage(login)
        self.driver.run_sendEmail_case()
        

if __name__ == '__main__':
    pytest.main(["-s","test_supplierInfoShowPage.py"])