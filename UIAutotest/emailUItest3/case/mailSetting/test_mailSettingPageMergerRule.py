# -*- encoding: utf-8 -*-
'''
@File    :   test_mailSettingPageMergerRule.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/26 0026 16:46   dmk      1.0         None
'''

import allure,pytest
from pageObject.mailSettingPage.mailSettingPageMergerRulePage import mailSettingPageMergerRulePage

addMergerRule_datas = [("1","归并规则测试-邮件主题-包含-重构","邮件主题",1,"重构","客户箱","测试，勿动","主题包含重构，勿动"),("2","归并规则测试-收件地址-包含-126","收件地址",1,"126","供应商箱","fttxtest@sina.cn","收件地址包含126，勿动"),("3","归并规则测试-发件地址-包含-aliyun","发件地址",1,"aliyun","内部联系人箱","管理员","发件地址包含aliyun，勿动"),("4","归并规则测试-客户类型-等于-合作客户","客户类型",0,"合作客户","自定义箱","自定义箱测试，勿动","合作客户，勿动"),("5","归并规则测试-客户等级-等于-重要","客户等级",0,"重要","客户箱","按客户自动匹配","客户等级，重要，勿动"),("6","归并规则测试-客户来源-等于-广交会","客户来源",0,"广交会","客户箱","按客户自动匹配","客户来源，广交会，勿动")]


@allure.feature("归并规则相关功能")
class TestMailSettingPageMergerRulePage:


    @allure.story("新增归并规则并验证")
    @pytest.mark.parametrize("caseid,casename,condition,is_contain,containOrEqualKey,boxCategory,boxName,queryBoxName",addMergerRule_datas)
    def test_addMergerRule(self,caseid,casename,condition,is_contain,containOrEqualKey,boxCategory,boxName,queryBoxName,login):

        self.driver = mailSettingPageMergerRulePage(login)
        self.driver.run_addMergerRule_case(condition,is_contain,containOrEqualKey,boxCategory,boxName,queryBoxName)


if __name__ == '__main__':
    pytest.main(["-s","test_mailSettingPageMergerRule.py"])