# -*- encoding: utf-8 -*-
'''
@File    :   test_writeMailPageInsertFastText.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/15 0015 11:37   dmk      1.0         None
'''

import pytest,allure
from utils.generator import *
from pageObject.writeMailPage.writeMailPageInsertFastTextPage import writeMailPageInsertFastTextPage

writeMailPageAddFastText_datas = [("1","新增不重名快速文本"),("2","新增重名快速文本")]
writeMailPageEditFastText_datas = [("1","编辑不重名快速文本"),("2","编辑重名快速文本")]
writeMailPageInsertFastText_datas = [("1","插入一个纯文本，不换行","1","0","快速文本-纯文本测试，勿动快速文本-纯文本测试，勿动快速文本-纯文本测试，勿动",""),("2","插入一个纯文本，换行","1","1","快速文本-纯文本测试，勿动快速文本-纯文本测试，勿动快速文本-纯文本测试，勿动",""),("3","插入一个富文本，不换行","2","0","富文本测试1，勿动","ntYlhMNTCf..jpg"),("4","插入一富纯文本，换行","2","1","富文本测试1，勿动","ntYlhMNTCf..jpg"),("5","插入多个纯文本，不换行","3","0","快速文本-纯文本测试，勿动快速文本-纯文本测试，勿动快速文本-纯文本测试，勿动两个方法在线你的方式.日期注册回复免费国家这么开发.加入客户中文有关决定生产.以及首页所以状态商品本站.企业中国日本.开发积分如此什么的话.加入用户业务可能生活手机非常.因为产品处理这个日期显示.不同主题完全一直这里我们.国际在线使用回复可以选择.起来虽然积分发现那些同时.是否美国结果影响.怎么文件报告上海介绍选择.一些工作完成虽然其实.法律活动提高应该.地区作者搜索认为状态.",""),("6","插入多个纯文本，换行","3","1","快速文本-纯文本测试，勿动快速文本-纯文本测试，勿动快速文本-纯文本测试，勿动两个方法在线你的方式.日期注册回复免费国家这么开发.加入客户中文有关决定生产.以及首页所以状态商品本站.企业中国日本.开发积分如此什么的话.加入用户业务可能生活手机非常.因为产品处理这个日期显示.不同主题完全一直这里我们.国际在线使用回复可以选择.起来虽然积分发现那些同时.是否美国结果影响.怎么文件报告上海介绍选择.一些工作完成虽然其实.法律活动提高应该.地区作者搜索认为状态.",""),("7","插入多个富文本，不换行","4","0","富文本测试1，勿动富文本测试2，勿动","ntYlhMNTCf..jpg,lwWobkppMg..jpg"),("8","插入多个富文本，换行","4","1","富文本测试1，勿动富文本测试2，勿动","ntYlhMNTCf..jpg,lwWobkppMg..jpg"),("9","插入多个纯、富文本，不换行","5","0","富文本测试1，勿动快速文本-纯文本测试，勿动快速文本-纯文本测试，勿动快速文本-纯文本测试，勿动","ntYlhMNTCf..jpg"),("10","插入多个纯、富文本，换行","5","1","富文本测试1，勿动快速文本-纯文本测试，勿动快速文本-纯文本测试，勿动快速文本-纯文本测试，勿动","ntYlhMNTCf..jpg")]

@allure.feature("写信页面，插入快速文本相关功能")
class TestWriteMailPageInsertFastText:

    @allure.story("写信页面，新增快速文本")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("caseid,casename",writeMailPageAddFastText_datas)
    def test_writeMailPageAddFastText(self,caseid,casename,login,auto_refreshBro):
        self.driver = writeMailPageInsertFastTextPage(login)
        self.driver.run_writeMailPageAddFastText_case(casename)


    @allure.story("写信页面，编辑快速文本")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("caseid,casename",writeMailPageAddFastText_datas)
    def test_writeMailPageEditFastText(self,caseid,casename,login,auto_refreshBro):
        self.driver = writeMailPageInsertFastTextPage(login)
        self.driver.run_writeMailPageEditFastText_case(casename)


    @allure.story("写信页面，删除快速文本")
    @allure.severity(allure.severity_level.MINOR)
    def test_writeMailPageDelFastText(self,login,auto_refreshBro):
        self.driver = writeMailPageInsertFastTextPage(login)
        self.driver.run_writeMailPageDelFastText_case()


    @allure.story("写信页面，搜索快速文本")
    @allure.severity(allure.severity_level.MINOR)
    def test_writeMailPageSearchFastText(self,login,auto_refreshBro):
        self.driver = writeMailPageInsertFastTextPage(login)
        self.driver.run_writeMailPageSearchFastText_case()

    @allure.story("写信页面，插入快速文本")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.InsertFastText
    @pytest.mark.parametrize("caseid,casename,fastText_num,is_newLine,fastText,fastTextImgSrc",writeMailPageInsertFastText_datas)
    def test_writeMailPageInsertFastText(self,caseid,casename,fastText_num,is_newLine,fastText,fastTextImgSrc,login):
        self.driver = writeMailPageInsertFastTextPage(login)
        self.driver.run_writeMailPageInsertFastText_case(fastText_num,is_newLine)
        insertedFastText,insertedFastTextImgSrc = self.driver.get_fastTextInEmailBody()
        assert fastText in insertedFastText
        assert fastTextImgSrc in insertedFastTextImgSrc



if __name__ == '__main__':
    pytest.main(["-v","test_writeMailPageInsertFastText.py"])