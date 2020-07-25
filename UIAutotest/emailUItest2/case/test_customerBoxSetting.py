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
from pageObject.emailCustomerBoxPage import emailCustomerBoxPage


class TestCustomerBoxSetting():

    def test_customerBoxSetting(self,login):
        self.driver = emailCustomerBoxPage(login)
        self.driver.refresh_bro()
        self.toastWarn,self.toastSuccess = self.driver.run_customerBoxSetting_case()
        assert self.toastWarn == "显示方式至少选择一个"
        assert self.toastSuccess == "设置成功"

if __name__ == '__main__':
    pytest.main(["-v","test_customerBoxSetting.py"])
