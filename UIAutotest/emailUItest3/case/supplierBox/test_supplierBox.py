# -*- encoding: utf-8 -*-
'''
@File    :   test_supplierBox.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/29 0029 19:05   dmk      1.0         None
'''
import allure,pytest
from pageObject.supplierBoxPage.supplierBoxPage import supplierBoxPage

searchSupplierBox_datas = [(1,"按名称搜索供应商箱-勿动",{"keyword":"勿动"}),(2,"按邮箱搜索供应商箱-fttx",{"keyword":"fttx"}),(3,"按代码搜索供应商箱-000",{"keyword":"0001"})]

selectDisplayMode_datas = [(1,"全部选择",{"select_supplierName":1,"select_supplierShortName":1,"select_supplierCode":1,"expect":"fttxtest@sina.cn : 供应商测试，勿动，谢谢，fttxtest@sina.cn : S00000001","toast":"设置成功"}),(2,"全部不选择",{"select_supplierName":0,"select_supplierShortName":0,"select_supplierCode":0,"expect":"fttxtest@sina.cn : 供应商测试，勿动，谢谢，fttxtest@sina.cn : S00000001","toast":"显示方式至少选择一个"}),(3,"只选择供应商代码",{"select_supplierName":0,"select_supplierShortName":0,"select_supplierCode":1,"expect":"S00000001","toast":"设置成功"}),(4,"只选择供应商简称",{"select_supplierName":0,"select_supplierShortName":1,"select_supplierCode":0,"expect":"供应商测试，勿动，谢谢，fttxtest@sina.cn","toast":"设置成功"}),(5,"只选择供应商名称",{"select_supplierName":1,"select_supplierShortName":0,"select_supplierCode":0,"expect":"fttxtest@sina.cn","toast":"设置成功"})]

selectCategory_datas = [(1,"只选择一级分类-供应商类型",{"firstCategory":"供应商类型","secondCategory":"请选择","first_except":"加工商"}),(2,"只选择一级分类-国家地区",{"firstCategory":"国家地区","secondCategory":"请选择","first_except":"中国大陆"}),(3,"只选择一级分类-省份",{"firstCategory":"省份","secondCategory":"请选择","first_except":"安徽"}),(4,"只选择一级分类-主营产品",{"firstCategory":"主营产品","secondCategory":"请选择","first_except":"鞋包"}),(5,"只选择一级分类-供应商类型,二级分类-供应商类型",{"firstCategory":"供应商类型","secondCategory":"供应商类型","toast_except":"供应商箱分类规则一级分类和二级分类请不要选择同一种分类方式"}),(6,"只选择一级分类-供应商类型,二级分类-国家地区",{"firstCategory":"供应商类型","secondCategory":"国家地区","first_except":"加工商","second_except":"中国大陆"}),(7,"只选择一级分类-供应商类型,二级分类-省份",{"firstCategory":"供应商类型","secondCategory":"省份","first_except":"加工商","second_except":"安徽"}),(8,"只选择一级分类-供应商类型,二级分类-主营产品",{"firstCategory":"供应商类型","secondCategory":"主营产品","first_except":"加工商","second_except":"鞋包"})]


@allure.feature("供应商箱相关功能")
class TestSupplierBox:


    @allure.story("供应商箱显示方式设置相关功能")
    @pytest.mark.parametrize("caseid,casename,data",selectDisplayMode_datas)
    def test_selectDisplayMode(self,caseid,casename,data,login,auto_refreshBro):
        self.driver = supplierBoxPage(login)
        self.driver.run_selectDisplayMode_case(casename,data)
        
        
    @allure.story("搜索供应商箱")
    @pytest.mark.parametrize("caseid,casename,data",searchSupplierBox_datas)
    def test_searchSupplierBox(self,caseid,casename,data,login,auto_refreshBro):
        self.driver = supplierBoxPage(login)
        self.driver.run_searchSupplierBox_case(data)


    @allure.story("一二级分类设置")
    @pytest.mark.parametrize("caseid,casename,data",selectCategory_datas)
    def test_selectCategory(self,caseid,casename,data,login,auto_refreshBro):
        self.driver = supplierBoxPage(login)
        self.driver.run_selectCategory_case(data)


if __name__ == '__main__':
    pytest.main(["-s","test_supplierBox.py"])