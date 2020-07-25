# -*- encoding: utf-8 -*-
'''
@File    :   test_mailSettingPageShowSetting.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/27 0027 11:07   dmk      1.0         None
'''

import allure,pytest
from pageObject.mailSettingPage.mailSettingPageShowSettingPage import mailSettingPageShowSettingPage

setTrace_datas = [(2,"关闭邮件追踪",{"is_open":0}),(1,"开启邮件追踪",{"is_open":1})]

emailReceipt_datas = [(1,"开启回执",1),(2,"关闭回执",0)]

@allure.feature("邮箱显示设置相关功能")
class TestMailSettingPageShowSetting:

    @allure.story("邮件追踪相关功能")
    @pytest.mark.parametrize("caseid,casename,data",setTrace_datas)
    def test_setTrace(self,caseid,casename,data,login):
        self.driver = mailSettingPageShowSettingPage(login)
        self.driver.run_setTrace_case(data)


    @allure.story("邮件字体大小，颜色设置相关功能")
    def test_etFont(self,login,auto_refreshBro):
        self.driver = mailSettingPageShowSettingPage(login)
        self.driver.run_setFont_case()


    @allure.story("需要回执相关功能")
    @pytest.mark.Elapsed
    @pytest.mark.parametrize("caseid,casename,is_openReceipt",emailReceipt_datas)
    def test_emailReceipt(self,caseid,casename,is_openReceipt,login):
        self.driver = mailSettingPageShowSettingPage(login)
        self.driver.run_emailReceipt_case(is_openReceipt)

if __name__ == '__main__':
    pytest.main(["-s","test_mailSettingPageShowSetting.py"])