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
from pageObject.emailApprovalRuleSettingPage import emailApprovalRuleSettingPage


datas = [("1","编辑审批规则",0),("2","新建审批规则",1)]

class TestCurrentApprovalClick():

    @pytest.mark.parametrize("caseid,casename,is_new",datas)
    def test_currentApprovalClick(self,caseid,casename,is_new,login):
        self.caseid = caseid
        self.casename = casename
        self.is_new = is_new
        self.driver = emailApprovalRuleSettingPage(login)
        self.currentApproval_property = self.driver.run_currentApprovalClick_case(self.is_new)
        assert "is-disabled" in self.currentApproval_property

if __name__ == '__main__':
    pytest.main(["-v","test_currentApprovalClick.py"])
