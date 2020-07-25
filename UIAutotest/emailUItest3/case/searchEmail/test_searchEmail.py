# -*- encoding: utf-8 -*-
'''
@File    :   test_searchEmail.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/1 0001 16:17   dmk      1.0         None
'''

import allure,pytest
from pageObject.basePage import Action
from pageObject.searchEmailPage.searchEmailPage import searchEmailPage


searchEmail_datas = [(1,"普通搜索全部",{"keyword":"test","select_index":4}),(2,"普通搜索-主题",{"keyword":"重构","select_index":0}),(3,"普通搜索-正文",{"keyword":"测试","select_index":1}),(4,"普通搜索-附件主题",{"keyword":"测试","select_index":2}),(5,"普通搜索-联系人",{"keyword":"163","select_index":3})]

@allure.feature("邮件搜索相关功能")
class TestSearchEmail:

    @allure.story("邮件普通搜索功能")
    @pytest.mark.parametrize("caseid,casename,data",searchEmail_datas)
    def test_searchEmail(self,caseid,casename,data,login):
        self.driver = searchEmailPage(login)
        self.driver.run_searchEmail_case(data)

if __name__ == '__main__':
    pytest.main(["-s","test_searchEmail.py"])