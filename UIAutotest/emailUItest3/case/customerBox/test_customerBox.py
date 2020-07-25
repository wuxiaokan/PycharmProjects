# -*- encoding: utf-8 -*-
'''
@File    :   test_mailSettingPageBaseSetting.py
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/20 0020 10:47   dmk      1.0         None
'''

import pytest,allure
from pageObject.customerBoxPage.customerBoxPage import customerBoxPage

# customerBoxPageAddCustomerBox_datas = [("1","新增不重名自定义箱客户箱"),("2","新增重名自定义箱客户箱")]

searchCustomerBox_datas = [(1,"按名称搜索客户箱-勿动",{"keyword":"勿动"}),(2,"按邮箱搜索客户箱-fttx",{"keyword":"fttx"}),(3,"按代码搜索客户箱-000",{"keyword":"000"})]

selectDisplayMode_datas = [(1,"全部选择",{"select_customerName":1,"select_customerShortName":1,"select_customerCode":1,"expect":"测试，勿动 : 客户简称test-勿动 : C00000001","toast":"设置成功"}),(2,"全部不选择",{"select_customerName":0,"select_customerShortName":0,"select_customerCode":0,"expect":"测试，勿动 : 客户简称test-勿动 : C00000001","toast":"显示方式至少选择一个"}),(3,"只选择客户代码",{"select_customerName":0,"select_customerShortName":0,"select_customerCode":1,"expect":"C00000001","toast":"设置成功"}),(4,"只选择客户简称",{"select_customerName":0,"select_customerShortName":1,"select_customerCode":0,"expect":"客户简称test-勿动","toast":"设置成功"}),(5,"只选择客户名称",{"select_customerName":1,"select_customerShortName":0,"select_customerCode":0,"expect":"测试，勿动","toast":"设置成功"})]

selectCategory_datas = [(1,"只选择一级分类-客户类型",{"firstCategory":"客户类型","secondCategory":"请选择","first_except":"合作客户"}),(2,"只选择一级分类-客户来源",{"firstCategory":"客户来源","secondCategory":"请选择","first_except":"广交会"}),(3,"只选择一级分类-客户等级",{"firstCategory":"客户等级","secondCategory":"请选择","first_except":"重要"}),(4,"只选择一级分类-国家地区",{"firstCategory":"国家地区","secondCategory":"请选择","first_except":"阿富汗"}),(5,"只选择一级分类-跟进阶段",{"firstCategory":"跟进阶段","secondCategory":"请选择","first_except":"商务洽谈"}),(6,"同时选择一级分类-客户类型，二级分类-客户类型",{"firstCategory":"客户类型","secondCategory":"客户类型","toast_except":"客户箱一级分类和二级分类请不要选择同一种分类方式"}),(7,"同时选择一级分类-客户类型，二级分类-客户来源",{"firstCategory":"客户类型","secondCategory":"客户来源","first_except":"合作客户","second_except":"广交会"}),(8,"同时选择一级分类-客户类型，二级分类-客户等级",{"firstCategory":"客户类型","secondCategory":"客户等级","first_except":"合作客户","second_except":"重要"}),(9,"同时选择一级分类-客户类型，二级分类-国家地区",{"firstCategory":"客户类型","secondCategory":"国家地区","first_except":"合作客户","second_except":"阿富汗"}),(10,"同时选择一级分类-客户类型，二级分类-跟进阶段",{"firstCategory":"客户类型","secondCategory":"跟进阶段","first_except":"合作客户","second_except":"商务洽谈"}),(11,"同时选择一级分类-客户来源，二级分类-客户类型",{"firstCategory":"客户来源","secondCategory":"客户类型","first_except":"广交会","second_except":"合作客户"}),(12,"同时选择一级分类-客户来源，二级分类-客户来源",{"firstCategory":"客户来源","secondCategory":"客户来源","toast_except":"客户箱一级分类和二级分类请不要选择同一种分类方式"}),(13,"同时选择一级分类-客户来源，二级分类-客户等级",{"firstCategory":"客户来源","secondCategory":"客户等级","first_except":"广交会","second_except":"重要"}),(14,"同时选择一级分类-客户来源，二级分类-国家地区",{"firstCategory":"客户来源","secondCategory":"国家地区","first_except":"广交会","second_except":"阿富汗"}),(15,"同时选择一级分类-客户来源，二级分类-跟进阶段",{"firstCategory":"客户来源","secondCategory":"跟进阶段","first_except":"广交会","second_except":"商务洽谈"})]


@allure.feature("客户箱相关功能")
class TestCustomerBox:

    # @allure.story("新增客户箱自定义箱")
    # def test_customerBoxPageAddCustomerBox(self,login,auto_refreshBro):
    #     self.driver = customerBoxPage(login)
    #     self.driver.run_customerBoxPageAddCustomerBox_case()

    @allure.story("搜索客户箱")
    @pytest.mark.parametrize("caseid,casename,data",searchCustomerBox_datas)
    def test_searchCustomerBox(self,caseid,casename,data,login):
        self.driver = customerBoxPage(login)
        self.driver.run_searchCustomerBox_case(data)


    @allure.story("显示方式选择")
    @pytest.mark.parametrize("caseid,casename,data",selectDisplayMode_datas)
    def test_selectDisplayMode(self,caseid,casename,data,login):
        self.driver = customerBoxPage(login)
        self.driver.run_selectDisplayMode_case(casename,data)


    @allure.story("一二级分类设置")
    @pytest.mark.parametrize("caseid,casename,data",selectCategory_datas)
    def test_selectCategory(self,caseid,casename,data,login,auto_refreshBro):
        self.driver = customerBoxPage(login)
        self.driver.run_selectCategory_case(data)


if __name__ == '__main__':
    pytest.main(["-v","test_customerBox.py"])