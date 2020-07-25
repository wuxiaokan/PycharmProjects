# -*- encoding: utf-8 -*-
'''
@File    :   test_mailSettingPageMailRule.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/16 0016 17:13   dmk      1.0         None
'''

import allure,pytest
from pageObject.mailSettingPage.mailSettingPageMailRulePage import mailSettingPageMailRulePage

addMailRule_datas = [("1","收件规则测试-全部邮件","全部邮件","直接归并","供应商箱","","",{'server':'smtp.sina.com','sender':'fttx111@sina.com','password':'5366be9f7b1c0b49'}),("2","收件规则测试-老客户邮件","老客户邮件","直接归并","客户箱","","",{'server':'smtp.aliyun.com','sender':'fttx111@aliyun.com','password':'fttxtest123'}),("3","收件规则测试-邮件主题包含","邮件主题","直接归并","内部联系人箱","","收件规则测试",{'server':'smtp.aliyun.com','sender':'fttx333@aliyun.com','password':'fttxtest123'}),("4","收件规则测试-发件地址包含","发件地址","直接归并","自定义箱","","aliyun",{'server':'smtp.aliyun.com','sender':'fttx888@aliyun.com','password':'fttxtest123'})]


@allure.feature("收件规则相关功能")
class TestMailSettingPageMailRule:

    @allure.story("新增收件规则并验证")
    @pytest.mark.parametrize("caseid,casename,condition,excuteOperate,deliverOrChargeFirst,deliverOrChargeSecond,containKey,send_info",addMailRule_datas)
    def test_addMailRule(self,caseid,casename,condition,excuteOperate,deliverOrChargeFirst,deliverOrChargeSecond,containKey,send_info,login):
        self.driver = mailSettingPageMailRulePage(login)
        self.driver.run_addMailRule_case(condition,excuteOperate,deliverOrChargeFirst,deliverOrChargeSecond,containKey,send_info)


if __name__ == '__main__':
    pytest.main(["-s","test_mailSettingPageMailRule.py"])