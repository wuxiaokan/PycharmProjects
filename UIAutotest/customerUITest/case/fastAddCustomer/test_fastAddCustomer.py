# -*- encoding: utf-8 -*-
'''
@File    :   test_fastAddCustomer.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/23 0023 10:12   dmk      1.0         None
'''

import allure,pytest
from utils.generator import *
from pageObject.fastAddCustomerPage.fastAddCustomerPage import fastAddCustomer

fastAddCustomer_datas = [(1,"快速新建客户",[{"客户代码":random_phone_number()+random_str(3,6)},{"客户名称":random_name()+str(random_number(3))+"测试，可删除"},{"客户简称":random_name()+"测试"},{"联系地址":random_address()},{"姓名":random_name()+"测试"},{"邮箱":str(random_number(3))+random_email()},{"手机":random_phone_number()}],[{"国家/地区":"安哥拉"},{"客户类型":"大客户"}],random_text().replace("\n",""),"product_1560415976360_1.xlsx")]

closeFastAddCustomer_datas = [(1,"关闭快速新建客户-保存",{"is_save":1,"customer_sendKeys":[{"客户代码":random_phone_number()+random_str(3,6)},{"客户名称":random_name()+str(random_number(3))+"测试，可删除"},{"客户简称":random_name()+"测试"},{"联系地址":random_address()},{"姓名":random_name()+"测试"},{"邮箱":str(random_number(3))+random_email()},{"手机":random_phone_number()}],"customer_selectKeys":[{"国家/地区":"安哥拉"},{"客户类型":"大客户"}],"customer_comment":random_text().replace("\n",""),"attach":"product_1560415976360_1.xlsx"}),(2,"关闭快速新建客户-不保存",{"is_save":0}),(3,"关闭快速新建客户-取消保存",{"is_save":2})]


@allure.feature("快速新建客户相关功能")
class TestFastAddCustomer:

    @allure.story("快速新建客户")
    @pytest.mark.parametrize("caseid,casename,customer_sendKeys,customer_selectKeys,customer_comment,attach",fastAddCustomer_datas)
    def test_fastAddCustomer(self,caseid,casename,customer_sendKeys,customer_selectKeys,customer_comment,attach,login):
        self.driver = fastAddCustomer(login)
        self.driver.run_fastAddCustomer_case(customer_sendKeys,customer_selectKeys,customer_comment,attach)


    @allure.story("快速新建客户-全屏操作")
    @pytest.mark.parametrize("caseid,casename,customer_sendKeys,customer_selectKeys,customer_comment,attach",fastAddCustomer_datas)
    def test_fastAddCustomerFullScreen(self,caseid,casename,customer_sendKeys,customer_selectKeys,customer_comment,attach,login):
        self.driver = fastAddCustomer(login)
        self.driver.run_fastAddCustomerFullScreen_case(customer_sendKeys,customer_selectKeys,customer_comment,attach)


    @allure.story("关闭快速新建客户页面")
    @pytest.mark.parametrize("caseid,casename,data",closeFastAddCustomer_datas)
    def test_closeFastAddCustomer(self,caseid,casename,data,login):
        self.driver = fastAddCustomer(login)
        self.driver.run_closeFastAddCustomer_case(data)


if __name__ == '__main__':
    pytest.main(["-s","test_fastAddCustomer.py"])