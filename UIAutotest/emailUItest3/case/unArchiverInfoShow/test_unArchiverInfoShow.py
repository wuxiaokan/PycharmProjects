# -*- encoding: utf-8 -*-
'''
@File    :   test_unArchiverInfoShow.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/15 0015 17:34   dmk      1.0         None
'''

import allure,pytest
from pageObject.unArchiverInfoShowPage.unArchiverInfoShowPage import unArchiverInfoShowPage

archiveCustomer_datas = [(1,"添加为客户",{"is_addCustomer":1})]

@allure.feature("未建档联系人信息展示页面相关功能")
class TestUnArchiverInfoShow:


    @allure.story("未建档联系人页面布局")
    def test_unArchivePageLayout(self,login):
        self.driver = unArchiverInfoShowPage(login)
        self.driver.run_unArchiverMainInfo_case()

    @allure.story("添加未建档联系人为客户或供应商")
    @pytest.mark.parametrize("caseid,casename,data",archiveCustomer_datas)
    def test_archiveCustomer(self,caseid,casename,data,login):
        self.driver = unArchiverInfoShowPage(login)
        self.driver.run_archiveCustomer_case(data)


if __name__ == '__main__':
    pytest.main(["-s","test_unArchiverInfoShow.py"])