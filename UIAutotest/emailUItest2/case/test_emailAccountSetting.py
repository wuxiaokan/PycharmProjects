# -*- encoding: utf-8 -*-
'''
@File    :   test_emailAccountSetting.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/26 0026 11:22   dmk      1.0         None
'''

import pytest,time
from utils.generator import *
from selenium.webdriver.common.by import By
from pageObject.emailAccountSettingPage import emailAccountSettingPage

emailAccountNickName_datas = [("1","没有昵称",0,""),("2","有昵称",1,"富通test123")]

datas = [("1","没有昵称"),("2","有昵称")]

accountSSLPort_datas = [("1","aliyun邮箱账号SSL端口号测试","aliyun","995","110","465","25"),("2","126邮箱账号SSL端口号测试","126","993","143","465","25"),("3","21cn邮箱账号SSL端口号测试","21cn","995","110","465","25"),("4","hotmail邮箱账号SSL端口号测试","hotmail","995","110","465","587")]

@pytest.fixture(scope="function")
def addAccount(login):
    driver = login

    yield
    driver.find_element(By.XPATH,"//div[@class='setIcon icon']").click()
    driver.find_element(By.XPATH,"//button[@class='el-button add_account el-button--primary']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH,"//input[@placeholder='请输入E-mail地址']").send_keys("fangwang@hotmail.com")
    driver.find_element(By.XPATH,"//input[@placeholder='请输入邮箱密码或授权码']").send_keys("aceholde")
    driver.find_element(By.XPATH,"//div[@class='el-form-item__content']//button[3]").click()

class TestEmailAccountSetting():


    def test_saveEmailAccount(self,login):
        self.random_account = random_email()
        self.random_password = random_phone_number()

        self.driver = emailAccountSettingPage(login)
        # self.driver.refresh_bro()
        self.driver.runcase(self.random_account,self.random_password)
        self.accountListText = self.driver.get_accountList()
        assert self.accountListText.count(self.random_account) == 1
        #删掉新增的账号
        self.driver.del_account(self.random_account)
        self.accountListText = self.driver.get_accountList()
        assert self.accountListText.count(self.random_account) == 0

    @pytest.mark.parametrize("caseid,casename,has_nick,nick_name",emailAccountNickName_datas)
    def test_emailAccountNickName(self,caseid,casename,has_nick,nick_name,login):
        self.caseid = caseid
        self.has_nick = has_nick
        self.nick_name = nick_name
        self.random_account = random_email()
        self.random_password = random_phone_number()
        self.driver = emailAccountSettingPage(login)
        self.driver.refresh_bro()
        self.driver.run_emailAccountNickName_case(self.random_account,self.random_password,self.has_nick,self.nick_name)
        #写信页面获取新增的发件人
        self.sender = self.driver.get_sender(self.random_account,self.has_nick,self.nick_name)
        print(self.sender)
        #切换到设置页面
        self.driver.click_settingBtn()
        #删掉新增的账号
        if self.has_nick:
            self.random_account = self.nick_name + "<"+ self.random_account + ">"
        self.driver.del_account(self.random_account)

    def test_operatorShow(self,login):
        self.driver = emailAccountSettingPage(login)
        self.driver.refresh_bro()
        #获取显示的人员信息
        self.showOperator = self.driver.run_operatorShow_case()
        assert self.showOperator == "管理员(dmktest)"

    @pytest.mark.parametrize("caseid,casename",datas)
    def test_delAccount(self,caseid,casename,login,addAccount):
        self.driver = emailAccountSettingPage(login)
        # self.driver.refresh_bro()
        #启用，禁用账号
        delAccountToast,accountList_settingPage = self.driver.run_delAccount_case()
        assert delAccountToast == "该账号在草稿箱、待发箱、群发箱仍有未发送成功的邮件，是否确认禁用或删除？" or delAccountToast == "是否删除账号?"
        assert "fangwang@hotmail.com" not in accountList_settingPage
        #获取写信页面的邮件账号
        accountList_writePage = self.driver.get_sender("fangwang@hotmail.com",0,0)
        assert accountList_writePage == False


    @pytest.mark.parametrize("caseid,casename,emailHost,receiptPort_ssl,receiptPort,sendPort_ssl,sendPort",accountSSLPort_datas)
    def test_accountSSLPort(self,caseid,casename,emailHost,receiptPort_ssl,receiptPort,sendPort_ssl,sendPort,login):
        self.driver = emailAccountSettingPage(login)
        self.driver.run_accountSSLPort_case(emailHost,receiptPort_ssl,receiptPort,sendPort_ssl,sendPort)


if __name__ == '__main__':
    pytest.main(["-s","test_emailAccountSetting.py"])