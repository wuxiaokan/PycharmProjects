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
from pageObject.emailWriteMailPageInsertOrderPage import emailWriteMailPageInsertOrderPage

insertOrder_datas = [("1","插入第一页第一个订单","0","PDF"),("2","插入第一页第一个订单","0","EXCEL"),("3","插入第一页全部订单","1","PDF"),("4","插入第一页全部订单","1","EXCEL")]

class TestEmailWriteMailPageInsertOrder():

    @pytest.mark.parametrize("caseid,casename,is_all,file_type",insertOrder_datas)
    def test_insertOrder_(self,caseid,casename,is_all,file_type,login):
        self.driver = emailWriteMailPageInsertOrderPage(login)
        self.driver.run_insertOrder_case(is_all,file_type)


if __name__ == '__main__':
    pytest.main(["-v","test_emailWriteMailPageInsertOrder.py"])
