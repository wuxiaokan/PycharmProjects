# -*- encoding: utf-8 -*-
'''
@File    :   test_showSetting.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/11 0011 19:12   dmk      1.0         None
'''

import allure,pytest
from pageObject.mailMoreSettingPage.showSettingPage import showSettingPage

showSetting_datas = [(1,"不勾选显示邮件地址",{"option":"显示邮件地址","is_select":0,"key":"fttx444@aliyun.com"}),(2,"勾选显示邮件地址",{"option":"显示邮件地址","is_select":1,"key":"fttx444@aliyun.com"}),(3,"不勾选显示客户简称",{"option":"显示客户简称","is_select":0,"key":"客户简称test-勿动"}),(4,"勾选显示客户简称",{"option":"显示客户简称","is_select":1,"key":"客户简称test-勿动"}),(5,"不勾选显示客户全称",{"option":"显示客户全称","is_select":0,"key":"测试，勿动"}),(6,"勾选显示客户全称",{"option":"显示客户全称","is_select":1,"key":"测试，勿动"}),(7,"不勾选显示正文摘要",{"option":"显示正文摘要","is_select":0}),(8,"勾选显示正文摘要",{"option":"显示正文摘要","is_select":1})]


groupEmail_datas = [(2,"按邮件地址分组邮件",{"option":"按邮件地址分组"}),(3,"按客户/供应商分组邮件",{"option":"按客户/供应商分组","except_groupNames":["没有客户信息","fttxtest@sina.cn","内部联系人"]}),(1,"按日期分组邮件",{"option":"按日期分组","except_groupNames":["今天","昨天","上周","更早"]})]

quickRead_datas = [(1,"勾选快捷阅读",{"is_select":1}),(2,"取消勾选快捷阅读",{"is_select":0})]



@allure.feature("邮箱更多设置相关功能")
class TestShowSetting:

    @allure.story("邮箱显示设置相关功能")
    @pytest.mark.parametrize("caseid,casename,data",showSetting_datas)
    def test_showSetting(self,caseid,casename,data,login):
        self.driver = showSettingPage(login)
        self.driver.run_showSetting_case(casename,data)


    @allure.story("邮件显示分组")
    @pytest.mark.parametrize("caseid,casename,data",groupEmail_datas)
    def test_groupEmail(self,caseid,casename,data,login):
        self.driver = showSettingPage(login)
        self.driver.run_groupEmail_case(data)


    @allure.story("快捷阅读邮件相关功能")
    @pytest.mark.parametrize("caseid,casename,data",quickRead_datas)
    def test_quickRead(self,caseid,casename,data,login):
        self.driver = showSettingPage(login)
        self.driver.run_quickRead_case(data)



if __name__ == '__main__':
    pytest.main(["-s","test_showSetting.py"])