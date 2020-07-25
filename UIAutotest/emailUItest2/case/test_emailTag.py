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
from pageObject.emailTagPage import emailTagPage



class TestEmailTag():


    def test_addTag(self,login):
        self.driver = emailTagPage(login)
        self.driver.run_addTag_case()

    def test_editTag(self,login):
        self.driver = emailTagPage(login)
        self.driver.run_editTag_case()

    def test_delTag(self,login):
        self.driver = emailTagPage(login)
        self.driver.run_delTag_case()

    def test_markTag(self,login):
        self.driver = emailTagPage(login)
        self.driver.run_markTag_case()

if __name__ == '__main__':
    pytest.main(["-v","test_emailTag.py"])
