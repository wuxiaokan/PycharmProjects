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
from pageObject.emailWriteMailPage import emailWriteMailPage

receiptConnect_dats = [("1","根据纯数字来联想","66"),("2","根据纯字母来联想","aliyun"),("3","根据数字+字母来联想","g7"),("4","根据汉字来联想","测试")]

class TestEmailWriteMail():


    def test_massEmail(self,login):
        self.driver = emailWriteMailPage(login)
        self.driver.run_massEmail_case()

    def test_worldTimeShowNickName(self,login):
        self.driver = emailWriteMailPage(login)
        self.driver.run_worldTimeShowNickName_case()

    @pytest.mark.parametrize("caseid,casename,key",receiptConnect_dats)
    def test_receiptConnect(self,caseid,casename,key,login):
        self.driver = emailWriteMailPage(login)
        self.driver.run_receiptConnect_case(key)

if __name__ == '__main__':
    pytest.main(["-v","test_emailWriteMail.py"])
