# -*- encoding: utf-8 -*-
'''
@File    :   test_queryBox.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/21 0021 15:07   dmk      1.0         None
'''

import allure,pytest
from pageObject.queryBoxPage.queryBoxPage import queryBoxPage
from pageObject.queryBoxPage.queryBoxPageCommon import queryBoxPageCommon

@pytest.fixture(scope="function")
def del_queryBox(login):
    queryBoxPageCom = queryBoxPageCommon(driver=login)
    yield
    queryBoxPageCom.del_queryBox()

addQueryBox_datas = [(1,"新建不重名查询箱",{"is_repeat":0,"except_text":"新建成功！"}),(2,"新建重名查询箱",{"is_repeat":1,"except_text":"箱子名称已存在"})]

setSubjectCondition_datas = [(1,"主题包含",{"is_equal":0,"subject":"黑名单"}),(1,"主题等于",{"is_equal":1,"subject":"系统退信"})]

setSenderCondition_datas = [(1,"发件人包含",{"is_equal":0,"sender":"sina"}),(2,"发件人包含",{"is_equal":0,"sender":"163"}),(3,"发件人包含",{"is_equal":0,"sender":"test"}),(4,"发件人等于",{"is_equal":1,"sender":"fttx666@aliyun.com"})]

setRecipientCondition_datas = [(1,"收件人包含",{"is_equal":0,"recipient":"fttxtest"}),(2,"收件人等于",{"is_equal":1,"recipient":"fttx222@aliyun.com"})]

setCcCondition_datas = [(1,"抄送人包含",{"is_equal":0,"cc":"c"}),(2,"抄送人等于",{"is_equal":1,"cc":"fttxtest<fttxtest@21cn.com>"})]

setServalDaysCondition_datas = [(1,"几天内-收件",{"is_send":0,"day_num":7}),(2,"几天内-收件",{"is_send":0,"day_num":30}),(3,"几天内-发件",{"is_send":1,"day_num":7}),(4,"几天内-发件",{"is_send":1,"day_num":20})]

setemailBoxCondition_datas = [(1,"设置邮件箱-收件箱",{"index":0,"emailBox":"收件箱"}),(2,"设置邮件箱-草稿箱",{"index":1,"emailBox":"草稿箱"}),(2,"设置邮件箱-草稿箱",{"index":1,"emailBox":"草稿箱"}),(3,"设置邮件箱-待发箱",{"index":2,"emailBox":"待发箱"}),(4,"设置邮件箱-群发箱",{"index":3,"emailBox":"群发箱"}),(5,"设置邮件箱-已发箱",{"index":4,"emailBox":"已发箱"}),(6,"设置邮件箱-自定义箱",{"index":5,"emailBox":"自定义箱"}),(7,"设置邮件箱-客户箱",{"index":6,"emailBox":"客户箱"}),(8,"设置邮件箱-供应商箱",{"index":7,"emailBox":"供应商箱"}),(9,"设置邮件箱-内部联系人箱",{"index":8,"emailBox":"内部联系人箱"})]

setAttachCondition_datas = [(1,"设置附件-不限",{"index":0,"btn_text":"不限"}),(2,"设置附件-含附件",{"index":2,"btn_text":"含附件"}),(3,"设置附件-不含附件",{"index":1,"btn_text":"不含附件"})]

setReplyStatusCondition_datas = [(1,"设置我的回复-已回复",{"index":1,"btn_text":"已回复"}),(2,"设置我的回复-未回复",{"index":2,"btn_text":"未回复"})]

setForwardStatusCondition_datas = [(1,"设置转发状态-已转发",{"index":1,"btn_text":"已转发"}),(2,"设置转发状态-未转发",{"index":2,"btn_text":"未转发"})]

setReadStatusCondition_datas = [(1,"设置阅读状态-已阅读",{"index":1,"btn_text":"已阅读"}),(2,"设置阅读状态-未阅读",{"index":2,"btn_text":"未阅读"})]

setInnerForwardStatusCondition_datas = [(1,"设置内部转发-已转发",{"index":1,"btn_text":"已转发"}),(2,"设置内部转发-未转发",{"index":2,"btn_text":"未转发"})]

setTraceStatusCondition_datas = [(1,"设置追踪状态-追踪",{"index":1,"btn_text":"追踪"}),(2,"设置追踪状态-未追踪",{"index":2,"btn_text":"未追踪"})]

setCustomerCondition_datas = [(1,"设置主营产品-电器",{"condition":"主营产品","secondCondition":"电器"}),(2,"设置跟进阶段-商务洽谈",{"condition":"跟进阶段","secondCondition":"商务洽谈"}),(3,"设置客户类型-合作客户",{"condition":"客户类型","secondCondition":"合作客户"}),(4,"设置客户等级-重要",{"condition":"客户等级","secondCondition":"重要"}),(5,"设置客户来源-广交会",{"condition":"客户来源","secondCondition":"广交会"}),(6,"设置客户标签-勿动",{"condition":"客户标签","secondCondition":"勿动"}),(7,"设置洲-北美洲",{"condition":"洲","secondCondition":"北美洲"}),(8,"设置国家地区-阿富汗",{"condition":"国家地区","secondCondition":"阿富汗"}),(9,"设置业务类型-贸易公司",{"condition":"业务类型","secondCondition":"贸易公司"})]


@allure.feature("查询箱相关功能")
class TestQueryBox:

    @allure.story("新增查询箱相关功能")
    @pytest.mark.parametrize("caseid,casename,data",addQueryBox_datas)
    def test_addQueryBox(self,caseid,casename,data,login):
        self.driver = queryBoxPage(login)
        self.driver.run_addQueryBox_case(data)


    @allure.story("删除查询箱相关功能")
    def test_delQueryBox(self,login):
        self.driver = queryBoxPage(login)
        self.driver.run_delQueryBox_case()


    @allure.story("修改查询箱")
    def test_modifyQueryBox(self,login,del_queryBox):
        self.driver = queryBoxPage(login)
        self.driver.run_modifyQueryBox_case()



    @allure.story("设置查询箱条件-主题")
    @pytest.mark.parametrize("caseid,casename,data",setSubjectCondition_datas)
    def test_setSubjectCondition(self,caseid,casename,data,login,del_queryBox):
        self.driver = queryBoxPage(login)
        self.driver.run_setSubjectCondition_case(data)


    @allure.story("查询箱设置条件-标签")
    def test_setMarkCondition(self,login,del_queryBox):
        self.driver = queryBoxPage(login)
        self.driver.run_setMarkCondition_case()


    @allure.story("设置查询箱条件-发件人")
    @pytest.mark.parametrize("caseid,casename,data",setSenderCondition_datas)
    def test_setSenderCondition(self,caseid,casename,data,login,del_queryBox):
        self.driver = queryBoxPage(login)
        self.driver.run_setSenderCondition_case(data)


    @allure.story("设置查询箱条件-收件人")
    @pytest.mark.parametrize("caseid,casename,data",setRecipientCondition_datas)
    def test_setRecipientCondition(self,caseid,casename,data,login,del_queryBox):
        self.driver = queryBoxPage(login)
        self.driver.run_setRecipientCondition_case(data)


    @allure.story("设置查询箱条件-抄送人")
    @pytest.mark.parametrize("caseid,casename,data",setCcCondition_datas)
    def test_setCcCondition(self,caseid,casename,data,login,del_queryBox):
        self.driver = queryBoxPage(login)
        self.driver.run_setCcCondition_case(data)


    @allure.story("设置查询箱条件-几天内")
    @pytest.mark.parametrize("caseid,casename,data",setServalDaysCondition_datas)
    def test_setServalDaysCondition(self,caseid,casename,data,login,del_queryBox):
        self.driver = queryBoxPage(login)
        self.driver.run_setServalDaysCondition_case(data)


    @allure.story("设置查询箱条件-邮件箱")
    @pytest.mark.parametrize("caseid,casename,data",setemailBoxCondition_datas)
    def test_setemailBoxCondition(self,caseid,casename,data,login,del_queryBox):
        self.driver = queryBoxPage(login)
        self.driver.run_setemailBoxCondition_case(data)


    @allure.story("设置查询箱条件-时间范围")
    def test_setdateScopeCondition(self,login,del_queryBox):
        self.driver = queryBoxPage(login)
        self.driver.run_setdateScopeCondition_case()


    @allure.story("设置查询箱条件-附件")
    @pytest.mark.parametrize("caseid,casename,data",setAttachCondition_datas)
    def test_setAttachCondition(self,caseid,casename,data,login,del_queryBox):
        self.driver = queryBoxPage(login)
        self.driver.run_setAttachCondition_case(data)


    @allure.story("设置查询箱条件-我的回复")
    @pytest.mark.parametrize("caseid,casename,data",setReplyStatusCondition_datas)
    def test_setReplyStatusCondition(self,caseid,casename,data,login,del_queryBox):
        self.driver = queryBoxPage(login)
        self.driver.run_setReplyStatusCondition_case(data)


    @allure.story("设置查询箱条件-转发状态")
    @pytest.mark.parametrize("caseid,casename,data",setForwardStatusCondition_datas)
    def test_setForwardStatusCondition(self,caseid,casename,data,login,del_queryBox):
        self.driver = queryBoxPage(login)
        self.driver.run_setForwardStatusCondition_case(data)


    @allure.story("设置查询箱条件-阅读状态")
    @pytest.mark.parametrize("caseid,casename,data",setReadStatusCondition_datas)
    def test_setReadStatusCondition(self,caseid,casename,data,login,del_queryBox):
        self.driver = queryBoxPage(login)
        self.driver.run_setReadStatusCondition_case(data)

    @allure.story("设置查询箱条件-内部转发")
    @pytest.mark.parametrize("caseid,casename,data",setInnerForwardStatusCondition_datas)
    def test_setInnerForwardStatusCondition(self,caseid,casename,data,login,del_queryBox):
        self.driver = queryBoxPage(login)
        self.driver.run_setInnerForwardStatusCondition_case(data)


    @allure.story("设置查询箱条件-追踪状态")
    @pytest.mark.parametrize("caseid,casename,data",setTraceStatusCondition_datas)
    def test_setTraceStatusCondition(self,caseid,casename,data,login,del_queryBox):
        self.driver = queryBoxPage(login)
        self.driver.run_setTraceStatusCondition_case(data)


    @allure.story("设置查询箱条件-客户的各个信息")
    @pytest.mark.parametrize("caseid,casename,data",setCustomerCondition_datas)
    def test_setCustomerCondition(self,caseid,casename,data,login,del_queryBox):
        self.driver = queryBoxPage(login)
        self.driver.run_setCustomerCondition_case(data)


if __name__ == '__main__':
    pytest.main(["-s","test_queryBox.py"])