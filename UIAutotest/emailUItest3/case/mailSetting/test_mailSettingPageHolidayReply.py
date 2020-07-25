# -*- encoding: utf-8 -*-
'''
@File    :   test_mailSettingPageHolidayReply.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/2 0002 11:35   dmk      1.0         None
'''

import pytest,allure
from pageObject.mailSettingPage.mailSettingPageHolidayReplyPage import mailSettingPageHolidayReplyPage

holidayReply_datas = [("1","无效的回复时间",1,0),("2","有效的回复时间",1,1),("3","不开启回复",0,0)]


@allure.feature("节假回复相关功能")
class TestmailSettingPageHolidayReply:

    @allure.story("节假回复功能测试")
    @pytest.mark.Elapsed
    @pytest.mark.parametrize("caseid,casename,is_reply,is_available",holidayReply_datas)
    def test_holidayReply(self,caseid,casename,is_reply,is_available,login,auto_refreshBro):
        self.driver = mailSettingPageHolidayReplyPage(login)
        self.driver.run_holidayReply_case(is_reply,is_available)



if __name__ == '__main__':
    pytest.main(["-s","test_mailSettingPageHolidayReply.py"])