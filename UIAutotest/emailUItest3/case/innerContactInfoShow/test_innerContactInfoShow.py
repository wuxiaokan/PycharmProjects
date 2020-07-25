# -*- encoding: utf-8 -*-
'''
@File    :   test_innerContactInfoShow.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/15 0015 19:41   dmk      1.0         None
'''
import allure,pytest
from pageObject.innerContactInfoShowPage.innerContactInfoShowPage import innerContactInfoShowPage

@allure.feature("内部联系人页面信息")
class TestInnerContactInfoShow:

    @allure.story("内部联系人信息")
    def test_unArchiverMainInfo(self,login):
        self.driver = innerContactInfoShowPage(login)
        self.driver.run_unArchiverMainInfo_case()


if __name__ == '__main__':
    pytest.main(["-s","test_innerContactInfoShow.py"])