# -*- encoding: utf-8 -*-
'''
@File    :   test_customer.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/20 0020 9:25   dmk      1.0         None
'''

import pytest,allure
from utils.generator import *
from pageObject.customerPage.customerPage import customerPage

delCustomer_datas = [(1,"客户，单个删除",0,1),(2,"客户，多个删除",0,0),(3,"回收箱客户，单个删除",1,1),(4,"回收箱客户，多个删除",1,0)]


@allure.feature("客户主页相关功能")
class TestCustomer:

    @allure.story("客户主页面的删除功能")
    @pytest.mark.parametrize("caseid,casename,is_recycleBox,is_single",delCustomer_datas)
    def test_delCustomer(self,caseid,casename,is_recycleBox,is_single,login):
        self.driver = customerPage(login)
        self.driver.run_delCustomer_case(is_recycleBox,is_single)


if __name__ == '__main__':
    pytest.main(["-s","test_customer.py"])