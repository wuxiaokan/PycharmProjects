# -*- encoding: utf-8 -*-
'''
@File    :   test_emailAccountSetting.py
@Contact :   fttxtest<fttxtest@163.com>
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/26 0026 11:22   dmk      1.0         None
'''

import pytest
from pageObject.emailAccountSettingPage import emailAccountSettingPage


datas = [("1","没有默认账号",""),("2","有默认账号","fttxtest<fttxtest@126.com>"),("3","在取消默认账号","fttxtest<fttxtest@126.com>")]

class TestEmailDefaultAccount():

    @pytest.mark.parametrize("caseid,casename,testaccount",datas)
    def test_emailDefaultAccount(self,caseid,casename,testaccount,login):
        self.caseid = caseid
        self.casename = casename
        self.testaccount = testaccount
        self.driver = emailAccountSettingPage(login)

        self.account = self.driver.run_defaultAccount_case(self.caseid,self.testaccount)
        self.sender = self.driver.get_defaultSender()

        print(self.account)
        print(self.sender)
        assert self.account in self.sender

if __name__ == '__main__':
    pytest.main(["-v","test_emailDefaultAccount.py"])
