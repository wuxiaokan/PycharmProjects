# -*- encoding: utf-8 -*-
'''
@File    :   test_recipientBoxPageAttachShow.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/21 0021 14:38   dmk      1.0         None
'''
import pytest,allure
from pageObject.recipientBoxPage.recipientBoxPageAttachShowPage import recipientBoxPageAttachShowPage
from pageObject.seniorSearchMailPage.seniorSearchMailPage import seniorSearchMailPage

recipientBoxPageAttachInfoShow_datas = [("1","有附件的邮件",1),("2","没有附件的邮件",0)]

@allure.feature("收件箱页面，附件相关功能")
class TestRecipientBoxPageAttachShow:

    @allure.story("收件箱页面，附件信息展示")
    @pytest.mark.parametrize("caseid,casename,is_attach",recipientBoxPageAttachInfoShow_datas)
    def test_recipientBoxPageAttachInfoShow(self,caseid,casename,is_attach,login):
        self.driver = seniorSearchMailPage(login)
        self.driver.searchMailByAttach(is_attach)
        self.driver.click_searchBtn()
        self.driver = recipientBoxPageAttachShowPage(login)
        self.driver.run_recipientBoxPageAttachInfoShow_case(is_attach)


if __name__ == '__main__':
    pytest.main(["-v","test_recipientBoxPageAttachShow.py"])