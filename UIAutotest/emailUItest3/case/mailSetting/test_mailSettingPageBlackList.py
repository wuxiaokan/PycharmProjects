# -*- encoding: utf-8 -*-
'''
@File    :   test_mailSettingPageBlackList.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/5 0005 13:26   dmk      1.0         None
'''

import pytest,allure
from pageObject.mailSettingPage.mailSettingPageBlackListPage import mailSettingPageBlackListPage


addBlackList_datas = [("1","存放到垃圾箱",0),("2","直接删除",1)]


@allure.feature("黑名单相关功能")
class TestMailSettingPageBlackList:

    @allure.story("新增黑名单，并验证")
    @pytest.mark.Elapsed
    @pytest.mark.parametrize("caseid,casename,is_del",addBlackList_datas)
    def test_addBlackList(self,caseid,casename,is_del,login,auto_refreshBro):
        self.driver = mailSettingPageBlackListPage(login)
        self.driver.run_addBlackList_case(is_del)


if __name__ == '__main__':
    pytest.main("-s","test_mailSettingPageBlackList.py")