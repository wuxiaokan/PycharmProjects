# -*- encoding: utf-8 -*-
'''
@File    :   test_writeMail.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/14 0014 14:32   dmk      1.0         None
'''

import pytest,allure
from utils.generator import *
from pageObject.writeMailPage.writeMailPage import writeMailPage
from pageObject.recipientBoxPage.recipientBoxPage import recipientBoxPage

editRecipientAgain_datas = [("1","重新编辑有效格式的收件账号",1),("2","重新编辑无效格式的收件账号",0)]

saveEmailDraft_datas = [(1,"普通邮件存草稿",{"is_timeSend":0}),(2,"定时发送邮件-存草稿",{"is_timeSend":1})]


@allure.feature("写信页面相关功能")
class TestWriteMail:

    @pytest.mark.AddSignature
    @allure.story("写信页面新增签名按钮测试")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_writeMailPageAddSignature(self,login,auto_refreshBro):
        """写信页面新增签名"""
        self.driver = writeMailPage(login)
        self.driver.run_writeMailPageAddSignature_case()


    @allure.story("写信页面最近联系人显示测试")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_writeMailPageShowRecentContacts(self,login,auto_refreshBro):
        """写信页面最近联系人显示"""
        self.driver = writeMailPage(login)
        subject = "邮件普通发送测试"
        recipient = random_email()
        self.driver.run_writeMailPageShowRecentContacts_case(recipient,subject)


    @allure.story("写信页面，收件人重新编辑测试")
    @pytest.mark.parametrize("caseid,casename,is_valid",editRecipientAgain_datas)
    def test_editRecipientAgain(self,caseid,casename,is_valid,login,auto_refreshBro):
        self.driver = writeMailPage(login)
        self.driver.run_editRecipientAgain_case(is_valid)


    @allure.story("写信页面，保存纯文本草稿")
    def test_savePureEmailDraft(self,login,auto_refreshBro):
        self.driver = writeMailPage(login)
        self.driver.run_savePureEmailDraft_case(is_pure=1)


    @allure.story("保存富文本草稿")
    @pytest.mark.parametrize("caseid,casename,data",saveEmailDraft_datas)
    def test_saveEmailDraft(self,caseid,casename,data,login):
        self.driver = writeMailPage(login)
        self.driver.run_saveEmailDraft_case(data)


    @allure.story("主链路发送邮件")
    @pytest.mark.mainProcess
    def test_sendEmailMainProcess(self,login):
        self.driver = writeMailPage(login)
        self.driver.run_sendEmailMainProcess_case()



    @allure.story("群发单显相关功能测试")
    def test_massEmail(self,login):
        self.driver = writeMailPage(login)
        self.driver.run_massEmail_case()

        # self.driver1 = recipientBoxPage(login001)
        # with allure.step("查看dmktest_001是否收到邮件"):
        #     self.driver1.get_emailAndClick(subject=email_subject,time_min=4)
        # with allure.step("查看并验证转发意见是否正确"):
        #     emailDetail_forwardIdeaText = self.driver1.get_forwardText_emailDetail()
        #     assert forwardIdeaText == emailDetail_forwardIdeaText


    @allure.story("插入宏相关功能测试")
    def test_sendMacro(self,login):
        self.driver = writeMailPage(login)
        self.driver.run_sendMacro_case()


if __name__ == '__main__':
    pytest.main(["-v","test_writeMail.py"])