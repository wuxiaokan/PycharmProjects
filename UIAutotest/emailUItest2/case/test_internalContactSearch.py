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
from pageObject.emailSelectContactsPage import emailSelectContactsPage

internalContactSearch_datas = [(1,"联系人汉字搜索",0,"管理"),(2,"联系人数字搜索",0,"1"),(3,"联系人字母搜索",0,"k"),(4,"用户组汉字搜索",1,"云"),(5,"用户组数字搜索",1,"0"),(6,"用户组字母搜索",1,"m")]


class TestInternalContactSearch():

    @pytest.mark.parametrize("caseid,casename,is_userGroup,key",internalContactSearch_datas)
    def test_internalContactSearch(self,caseid,casename,is_userGroup,key,login):
        self.driver = emailSelectContactsPage(login)

        self.driver.run_internalContactSearch_case(is_userGroup,key)

if __name__ == '__main__':
    pytest.main(["-v","test_internalContactSearch.py"])
