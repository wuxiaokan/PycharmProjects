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

saveMail_datas = [("1","没有收件账号","","<无收件人>"),("2","有收件账号","fttxtest<fttxtest@163.com>","fttxtest<fttxtest@163.com>")]

class TestSaveMail():

    @pytest.mark.parametrize("caseid,casename,payload,message",saveMail_datas)
    def test_saveMail(self,caseid,casename,payload,message,login):
        self.payload = payload
        self.message = message
        self.driver = emailWriteMailPage(login)
        self.driver.run_saveMail_case(self.payload)
        self.receipt = self.driver.get_draftEmail_receipt()
        assert self.receipt in self.message

if __name__ == '__main__':
    pytest.main(["-v","test_saveMail.py"])
