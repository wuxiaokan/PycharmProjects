# -*- encoding: utf-8 -*-
'''
@File    :   test_relatedBusiness.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/9 0009 14:45   dmk      1.0         None
'''

import pytest,allure,time
from pageObject.emailDetailPage.relatedBusinessPage import relatedBusinessPage



relatedQuoteAndOrder_datas = [(1,"相关业务-报价",{"type":"报价"}),(2,"相关业务-订单",{"type":"订单"})]

buildRelateBusiness_datas = [(1,"建立关联相关业务-报价",{"type":"报价"}),(2,"建立关联相关业务-订单",{"type":"订单"}),(3,"建立关联相关业务-商机",{"type":"商机"})]


@allure.feature("邮件详情内，相关业务相关功能")
class TestRelatedBusiness:

    @allure.story("邮件详情内，已关联的订单，报价相关业务")
    @pytest.mark.parametrize("caseid,casename,data",relatedQuoteAndOrder_datas)
    def test_relatedQuoteAndOrder(self,caseid,casename,data,login):
        self.driver = relatedBusinessPage(login)
        self.driver.run_relatedQuoteAndOrder_case(caseid,casename,data)


    @allure.story("邮件详情内，已关联的商机相关业务")
    def test_relatedBusiness(self,login):
        self.driver = relatedBusinessPage(login)
        self.driver.run_relatedBusiness_case()


    @allure.story("邮件详情内，建立关联相关业务")
    @pytest.mark.parametrize("caseid,casename,data",buildRelateBusiness_datas)
    def test_buildRelateBusiness(self,caseid,casename,data,login):
        self.driver = relatedBusinessPage(login)
        self.driver.run_buildRelateBusiness_case(caseid,casename,data)


if __name__ == '__main__':
    pytest.main(["-s","test_relatedBusiness.py"])