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
from pageObject.emailInsertSitePage import emailInsertSitePage


class TestEmailInsertSite():


    def test_siteInfoByGroup(self,login):
        self.driver = emailInsertSitePage(login)
        self.driver.run_siteInfoByGroup_case()


if __name__ == '__main__':
    pytest.main(["-v","test_emailInsertSite.py"])
