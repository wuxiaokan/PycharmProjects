# -*- encoding: utf-8 -*-
'''
@File    :   test_unArchivesContact.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/19 0019 9:53   dmk      1.0         None
'''
import pytest,allure
from pageObject.unArchiverInfoShowPage.unArchiverInfoShowPage import unArchiverInfoShowPage
from pageObject.recipientBoxPage.unArchivesContactPage import unArchivesContactPage

unArchivesContactPageAddContact_datas = [("1","添加客户-子账号-云基础-联系人","1","1"),("2","添加客户-子账号-管理员-联系人","1","2"),("3","添加供应商-联系人","2","")]

@allure.feature("未建档联系人相关功能")
class TestUnArchivesContactPage():

    @allure.story("未建档联系人信息")
    def test_unArchiverMainInfo(self,login):
        self.driver = unArchiverInfoShowPage(login)
        self.driver.run_unArchiverMainInfo_case()

    @allure.story("添加未建档联系人")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("caseid,casename,type,operator",unArchivesContactPageAddContact_datas)
    def test_unArchivesContactPageAddContact(self,caseid,casename,type,operator,login,auto_refreshBro):
        self.driver = unArchivesContactPage(login)
        exceped_emailAccount = self.driver.run_unArchivesContactPageAddContact_case(type=type,operator=operator)
        taked_emailAccount = self.driver.get_takedEmailAccount(type)
        assert exceped_emailAccount == taked_emailAccount


if __name__ == '__main__':
    pytest.main(["-v","test_unArchivesContact.py"])