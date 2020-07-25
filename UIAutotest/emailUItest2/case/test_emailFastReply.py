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
from pageObject.emailFastReplyPage import emailFastReplyPage



class TestEmailFastReply():


    def test_fastReplySend(self,login):
        self.driver = emailFastReplyPage(login)
        self.driver.run_fastReplySend_case()

    def test_fastReplyFullScreen(self,login):
        self.driver = emailFastReplyPage(login)
        self.driver.run_fastReplyFullScreen_case()


if __name__ == '__main__':
    pytest.main(["-v","test_emailFastReply.py"])
