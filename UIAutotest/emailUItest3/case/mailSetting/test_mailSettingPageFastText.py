# -*- encoding: utf-8 -*-
'''
@File    :   test_mailSettingPageFastText.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/7 0007 10:34   dmk      1.0         None
'''

import pytest,allure
from pageObject.mailSettingPage.mailSettingPageFastTextPage import mailSettingPageFastTextPage

addFastText_datas = [(1,"新增不重名纯文本",{"is_pure":1,"is_repeat":0,"expect_toast":"新增成功"}),(2,"新增重名纯文本",{"is_pure":1,"is_repeat":1,"expect_toast":'文本名称 "xx"已存在'}),(3,"新增不重名富文本",{"is_pure":0,"is_repeat":0,"expect_toast":"新增成功"}),(4,"新增重名富文本",{"is_pure":0,"is_repeat":1,"expect_toast":'文本名称 "xx"已存在'})]

@allure.feature("邮箱设置，快速文本相关功能")
class TestMailSettingPageFastText:


    @allure.story("新增快速文本相关功能")
    @pytest.mark.parametrize("caseid,casename,data",addFastText_datas)
    def test_addFastText(self,caseid,casename,data,login):
        self.driver = mailSettingPageFastTextPage(login)
        self.driver.run_addFastText_case(data)


    @allure.story("删除快速文本相关功能")
    def test_delFastText(self,login):
        self.driver = mailSettingPageFastTextPage(login)
        self.driver.run_delFastText_case()


if __name__ == '__main__':
    pytest.main(["-s","test_mailSettingPageFastText.py"])