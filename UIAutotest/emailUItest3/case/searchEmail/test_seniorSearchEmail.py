# -*- encoding: utf-8 -*-
'''
@File    :   test_seniorSearchEmail.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/2 0002 11:38   dmk      1.0         None
'''

import allure,pytest
from pageObject.searchEmailPage.seniorSearchEmailPage import seniorSearchEmailPage

seniorSearchInput_datas = [(1,"高级搜索主题-重构",{"option":"主题","keyword":"重构"}),(2,"高级搜索正文-合作",{"option":"正文","keyword":"合作"}),(3,"高级搜索附件标题-测试",{"option":"附件标题","keyword":"测试"}),(4,"高级搜索收件人-fttx111",{"option":"收件人","keyword":"fttx111"}),(5,"高级搜索发件人-fttx222",{"option":"发件人","keyword":"fttx222"}),(6,"高级搜索抄送人-21cn",{"option":"抄送人","keyword":"21cn"}),(7,"高级搜索报价单号-004",{"option":"报价单号","keyword":"004"}),(8,"高级搜索销售合同号-003",{"option":"销售合同号","keyword":"003"})]


seniorSearchDrop_datas = [(1,"高级搜索邮件箱-收件箱",{"option":"邮件箱","dropList":"收件箱"}),(2,"高级搜索邮件箱-群发箱",{"option":"邮件箱","dropList":"群发箱"}),(3,"高级搜索时间范围-30天内",{"option":"时间范围","dropList":"30天内"}),(4,"高级搜索时间范围-1天内",{"option":"时间范围","dropList":"1天内"}),(5,"高级搜索账号-fttx111@21cn.com",{"option":"账号","dropList":"fttx111@21cn.com"}),(6,"高级搜索标签-标签测试勿动",{"option":"标签","dropList":"标签测试勿动"})]

seniorSearchRadio_data = [(1,"高级搜索-附件-含附件",{"option":"附件","radio":"含附件"}),(2,"高级搜索-附件-不含附件",{"option":"附件","radio":"不含附件"}),(3,"高级搜索-收发类型-收到的",{"option":"收发类型","radio":"收到的"}),(4,"高级搜索-收发类型-发送的",{"option":"收发类型","radio":"发送的"}),(5,"高级搜索-转发状态-已转发",{"option":"转发状态","radio":"已转发"}),(6,"高级搜索-转发状态-未转发",{"option":"转发状态","radio":"未转发"}),(7,"高级搜索-内部转发-未转发",{"option":"内部转发","radio":"未转发"}),(8,"高级搜索-内部转发-已转发",{"option":"内部转发","radio":"已转发"}),(9,"高级搜索-阅读状态-已读",{"option":"阅读状态","radio":"已读"}),(10,"高级搜索-阅读状态-未读",{"option":"阅读状态","radio":"未读"}),(11,"高级搜索-追踪状态-追踪",{"option":"追踪状态","radio":"追踪"}),(12,"高级搜索-追踪状态-未追踪",{"option":"追踪状态","radio":"未追踪"}),(13,"高级搜索-星标状态-已标记",{"option":"星标状态","radio":"已标记"}),(14,"高级搜索-星标状态-未标记",{"option":"星标状态","radio":"未标记"}),(15,"高级搜索-对方回复-未回复",{"option":"对方回复","radio":"未回复"}),(16,"高级搜索-对方回复-已回复",{"option":"对方回复","radio":"已回复"}),(17,"高级搜索-我的回复-未回复",{"option":"我的回复","radio":"未回复"}),(18,"高级搜索-我的回复-已回复",{"option":"我的回复","radio":"已回复"}),(19,"高级搜索-我的回复-已回复-包含免回复",{"option":"我的回复","radio":"已回复"}),(20,"高级搜索-我的回复-未回复-包含免回复",{"option":"我的回复","radio":"未回复"})]

seniorSearchRadio_datas = [(19,"高级搜索-我的回复-未回复-包含免回复",{"option":"我的回复","radio":"未回复"})]


@allure.feature("高级搜索相关按钮")
class TestSeniorSearchEmail:

    @allure.story("输入条件的高级搜索")
    @pytest.mark.parametrize("caseid,casename,data",seniorSearchInput_datas)
    def test_seniorSearchInput(self,caseid,casename,data,login):
        self.driver = seniorSearchEmailPage(login)
        self.driver.run_seniorSearchInput_case(data)


    @allure.story("下拉框条件的高级搜索")
    @pytest.mark.parametrize("caseid,casename,data",seniorSearchDrop_datas)
    def test_seniorSearchDrop(self,caseid,casename,data,login):
        self.driver = seniorSearchEmailPage(login)
        self.driver.run_seniorSearchDrop_case(data)


    @allure.story("单选按钮条件的高级搜索")
    @pytest.mark.parametrize("caseid,casename,data",seniorSearchRadio_datas)
    def test_seniorSearchRadio(self,caseid,casename,data,login):
        self.driver = seniorSearchEmailPage(login)
        self.driver.run_seniorSearchRadio_case(casename,data)


if __name__ == '__main__':
    pytest.main(["-s","test_seniorSearchEmail.py"])