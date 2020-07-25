# -*- encoding: utf-8 -*-
'''
@File    :   test_mailSettingPageBaseSetting.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/20 0020 10:47   dmk      1.0         None
'''

import pytest,allure,time
from utils.generator import *
from pageObject.mailSettingPage.mailSettingPageBaseSettingPage import mailSettingPageBaseSettingPage
from pageObject.recipientBoxPage.recipientBoxPage import recipientBoxPage


mailSettingPageReadedSetting_datas = [("1","开始已读设置","1"),("2","关闭已读设置","0")]

autoReceipt_datas = [(1,"关闭自动回执-不勾选自动回执",0,0),(2,"关闭自动回执-勾选自动回执",0,1),(3,"开启自动回执-勾选自动回执",1,0)]

delaySend_datas = [(1,"开启延迟发送",{"is_open":1}),(2,"关闭延迟发送",{"is_open":0})]

setCcAndBc_datas = [(1,"设置抄送密送人",{"is_open":1}),(2,"不设置抄送密送人",{"is_open":0})]


@allure.feature("邮箱基础设置相关功能")
class TestMailSettingPageBaseSetting:

    @allure.story("邮箱账号已读设置功能")
    @pytest.mark.parametrize("caseid,casename,is_openRead",mailSettingPageReadedSetting_datas)
    def test_mailSettingPageReadedSetting(self,caseid,casename,is_openRead,login):
        # # self.driver = mailSettingPageBaseSettingPage(login)
        # # self.driver.run_mailSettingPageReadedSetting_case(is_openRead)
        # # self.driver1 = recipientBoxPage(login001)
        # markAttribute = self.driver1.get_emailAttributeOfRead()
        # # assert excepted_text in markAttribute
        self.driver = mailSettingPageBaseSettingPage(login)
        self.driver.run_mailSettingPageReadedSetting_case(is_openRead)


    @allure.story("自动回执功能")
    @pytest.mark.Elapsed
    @pytest.mark.parametrize("caseid,casename,is_autoReceipt,is_selectAutoReceipt",autoReceipt_datas)
    def test_autoReceipt(self,caseid,casename,is_autoReceipt,is_selectAutoReceipt,login):
        self.driver = mailSettingPageBaseSettingPage(login)
        self.driver.run_autoReceipt_case(is_autoReceipt,is_selectAutoReceipt)



    @allure.story("延迟发送相关功能")
    @pytest.mark.parametrize("caseid,casename,data",delaySend_datas)
    def test_delaySend(self,caseid,casename,data,login):
        self.driver = mailSettingPageBaseSettingPage(login)
        self.driver.run_delaySend_case(data)



    @allure.story("抄送密送人相关功能")
    @pytest.mark.parametrize("caseid,casename,data",setCcAndBc_datas)
    def test_setCcAndBc(self,caseid,casename,data,login):
        self.driver = mailSettingPageBaseSettingPage(login)
        self.driver.run_setCcAndBc_case(data)



if __name__ == '__main__':
    pytest.main(["-v","test_mailSettingPageBaseSetting.py"])