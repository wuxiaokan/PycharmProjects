# -*- encoding: utf-8 -*-
'''
@File    :   test_ApprovalSettingPageApprovalRule.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/16 0016 17:13   dmk      1.0         None
'''

import allure,pytest
from pageObject.mailSettingPage.mailSettingPageApprovalRulePage import mailSettingPageApprovalRulePage
from pageObject.recipientBoxPage.recipientBoxPage import recipientBoxPage


addApprovalRule_datas = [("1","审批规则测试-全部审批（可选）-提交审批","全部审批（可选）","","1"),("2","审批规则测试-全部审批（可选）-直接发送","全部审批（可选）","","0"),("3","审批规则测试-全部审批（强制）","全部审批（强制）","","1"),("4","审批规则测试-邮件主题","邮件主题","审批规则","1"),("5","审批规则测试-发件地址","发件地址","sina","1"),("6","审批规则测试-收件地址","收件地址","@","1")]


@allure.feature("审批规则相关功能")
class TestApprovalSettingPageApprovalRule:

    @allure.story("新增审批规则并验证")
    @pytest.mark.parametrize("caseid,casename,condition,containKey,is_approval",addApprovalRule_datas)
    def test_addApprovalRule(self,caseid,casename,condition,containKey,is_approval,login):

        # self.driver = recipientBoxPage(login)
        # self.driver.run_approvalMail_case(subject=None)
        #
        # self.driver1 = mailSettingPageApprovalRulePage(login001)
        # subject = self.driver1.run_addApprovalRule_case(casename,condition,containKey,is_approval)
        #
        # if caseid != "2":
        #     self.driver = recipientBoxPage(login)
        #     self.driver.run_approvalMail_case(subject)
        #
        # self.driver1.hasMailInBox(subject)

        self.driver = mailSettingPageApprovalRulePage(login)
        self.driver.run_addApprovalRule_case(casename,condition,containKey,is_approval)


if __name__ == '__main__':
    pytest.main(["-s","test_mailSettingPageApprovalRule.py"])