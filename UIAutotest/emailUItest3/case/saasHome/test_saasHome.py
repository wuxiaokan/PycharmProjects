# -*- encoding: utf-8 -*-
'''
@File    :   test_saasHome.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/25 0025 21:06   dmk      1.0         None
'''

import pytest,allure
from pageObject.saasHomePage.saasHomePage import saasHomePage


@allure.feature("SaaS系统首页相关功能")
class TestSaasHome:

    @allure.story("SaaS首页导航栏tab定位相关功能")
    def test_sysNavLocal(self,login,auto_refreshBro):
        self.driver = saasHomePage(login)
        self.driver.run_sysNavLocal_case()


if __name__ == '__main__':
    pytest.main(["-s","test_saasHome.py"])