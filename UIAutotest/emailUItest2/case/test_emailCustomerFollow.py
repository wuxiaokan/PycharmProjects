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
from pageObject.emailCustomerFollowPage import emailCustomerFollowPage

followStepPageLayout_datas = [("1","新客户跟进页面布局",1),("2","老客户跟进页面布局",0)]

class TestEmailCustomerFollow():


    def test_editFollowStep(self,login):
        self.driver = emailCustomerFollowPage(login)
        self.driver.run_editFollowStep_case()

    def test_sendMailFollowStepPage(self,login):
        self.driver = emailCustomerFollowPage(login)
        self.driver.run_sendMailFollowStepPage_case()

    @pytest.mark.parametrize("caseid,casename,is_newCustomer",followStepPageLayout_datas)
    def test_followStepPageLayout(self,caseid,casename,is_newCustomer,login):
        self.driver = emailCustomerFollowPage(login)
        self.driver.run_followStepPageLayout_case(is_newCustomer)


if __name__ == '__main__':
    pytest.main(["-v","test_emailCustomerFollow.py"])
