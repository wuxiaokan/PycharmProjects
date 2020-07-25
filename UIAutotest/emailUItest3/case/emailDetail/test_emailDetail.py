# -*- encoding: utf-8 -*-
'''
@File    :   test_emailDetail.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/16 0016 10:12   dmk      1.0         None
'''


import pytest,allure,time
from pageObject.emailDetailPage.emailDetailPage import emailDetailPage
from pageObject.recipientBoxPage.recipientBoxPage import recipientBoxPage
from pageObject.mailSettingPage.mailSettingPageBlackListPageCommon import mailSettingPageBlackListPageCommon


@pytest.fixture(scope="class")
def restoreRecipientBoxData(login):
    driver = recipientBoxPage(login)
    driver.moveEmailToRecipientBox()


@pytest.fixture(scope="class")
def clearBlackList(login):
    yield
    driver = mailSettingPageBlackListPageCommon(login)
    driver.del_allBlackList()

moveEmail_datas = [(1,"移动到已发箱",{"boxCategory":"已发箱"}),(2,"移动到群发箱",{"boxCategory":"群发箱"}),(3,"移动到客户箱",{"boxCategory":"客户箱"}),(4,"移动到供应商箱",{"boxCategory":"供应商箱"}),(5,"移动到内部联系人箱",{"boxCategory":"内部联系人箱"}),(6,"移动到自定义箱",{"boxCategory":"自定义箱"})]

forwardEmail_datas = [(1,"邮件详情页面-普通转发",{"forward":1}),(2,"邮件详情页面-内部转发",{"forward":2}),(3,"邮件详情页面-作为附件转发",{"forward":3})]

delEmail_datas = [(1,"删除收件箱内的邮件",{"boxName":"收件箱"}),(2,"删除垃圾箱内的邮件",{"boxName":"垃圾箱"}),(3,"删除回收箱内的邮件",{"boxName":"回收箱"})]

mergerEmailWithoutMergerRule_datas = [(1,"归并未建档联系人",{"queryBoxName":"未建档联系人邮件，勿动","boxCategory":"","purposeBoxName":""}),(2,"归并供应商联系人",{"queryBoxName":"供应商邮件，勿动","boxCategory":"供应商箱","purposeBoxName":"fttx111@sina.com"}),(3,"归并客户联系人",{"queryBoxName":"客户邮件，勿动","boxCategory":"客户箱","purposeBoxName":"fttx111@aliyun.com"}),(4,"归并内部联系人",{"queryBoxName":"内部联系人邮件，勿动","boxCategory":"内部联系人箱","purposeBoxName":"云基础"})]


markRubbishEmail_datas = [(1,"标记未建档联系人为垃圾邮件",{"boxName":"未建档联系人邮件，勿动"}),(2,"标记内部联系人为垃圾邮件",{"boxName":"内部联系人邮件，勿动"}),(3,"标记客户联系人为垃圾邮件",{"boxName":"客户邮件，勿动"}),(4,"标记供应商联系人为垃圾邮件",{"boxName":"供应商邮件，勿动"})]


showFollowBtn_datas = [(1,"跟进未建档联系人为垃圾邮件",{"boxName":"未建档联系人邮件，勿动"}),(2,"跟进内部联系人为垃圾邮件",{"boxName":"内部联系人邮件，勿动"}),(3,"跟进客户联系人为垃圾邮件",{"boxName":"客户邮件，勿动"}),(4,"跟进供应商联系人为垃圾邮件",{"boxName":"供应商邮件，勿动"})]

markEmail_datas = [(1,"标记邮件为未读-已读"),(2,"标记邮件为星标-取消星标"),(3,"标记邮件为免回复-取消免回复")]

previewFile_datas = [(1,"预览PDF文件",{"fileType":"pdf"}),(2,"预览xlsx文件",{"fileType":"xlsx"}),(3,"预览jpg文件",{"fileType":"jpg"})]

downloadAttach_datas = [(1,"下载单个小附件"),(2,"批量下载小附件"),(3,"下载大附件")]


@allure.feature("邮件详情相关功能")
class TestEmailDetail:

    @allure.story("邮件详情-移动邮件相关功能")
    @pytest.mark.parametrize("caseid,casename,data",moveEmail_datas)
    def test_moveEmail(self,caseid,casename,data,login,restoreRecipientBoxData):
        self.driver = emailDetailPage(login)
        self.driver.run_moveEmail_case(data)


    @allure.story("邮件详情-转发相关功能")
    @pytest.mark.parametrize("caseid,casename,data",forwardEmail_datas)
    def test_forwardEmail(self,caseid,casename,data,login):
        self.driver = emailDetailPage(login)
        self.driver.run_forwardEmail_case(caseid,casename,data)

        # if caseid == 2:
        #         #     self.driver = recipientBoxPage(login)
        #         #     with allure.step("判断云基础账号是否收到内部转发的邮件"):
        #         #         self.driver.assert_emailSubjectAndForwardIdea(emailSubject,forwardIdea)



    @allure.story("邮件详情翻页相关功能")
    def test_pageUpAndPageDown(self,login):
        self.driver = emailDetailPage(login)
        self.driver.run_pageUpAndPageDown_case()


    @allure.story("邮件日志相关功能")
    def test_checkLog(self,login):
        self.driver = emailDetailPage(login)
        self.driver.run_checkLog_case()


    @allure.story("邮件删除相关功能")
    @pytest.mark.parametrize("caseid,casename,data",delEmail_datas)
    def test_delEmail(self,caseid,casename,data,login):
        self.driver = emailDetailPage(login)
        self.driver.run_delEmail_case(data)

    @allure.story("邮件翻译相关功能")
    def test_transEmail(self,login):
        self.driver = emailDetailPage(login)
        self.driver.run_transEmail_case()


    @allure.story("邮件详情内，归并相关功能")
    @pytest.mark.parametrize("caseid,casename,data",mergerEmailWithoutMergerRule_datas)
    def test_mergerEmailWithoutMergerRule(self,caseid,casename,data,login):
        # self.driver = emailDetailPage(login)
        # self.driver.run_mergerEmailWithoutMergerRule_case(data)
        self.driver = emailDetailPage(login)
        self.driver.run_mergerEmailWithoutMergerRule_case(data)


    @allure.story("邮件详情内，分发相关功能")
    def test_deliveryEmail(self,login):
        self.driver = emailDetailPage(login)
        self.driver.run_deliveryEmail_case()


    @allure.story("邮件详情内，重发相关功能")
    def test_resendEmail(self,login):
        self.driver = emailDetailPage(login)
        self.driver.run_resendEmail_case()


    @allure.story("邮件详情内，重新生成相功能")
    def test_reGenerateEmail(self,login):
        self.driver = emailDetailPage(login)
        self.driver.run_reGenerateEmail_case()

    @allure.story("邮件详情内，导出相关功能")
    def test_exportEmail(self,login):
        self.driver = emailDetailPage(login)
        self.driver.run_exportEmail_case()

    @allure.story("邮件详情内，存为模板功能")
    def test_saveTemplate(self,login):
        self.driver = emailDetailPage(login)
        self.driver.run_saveTemplate_case()

    @allure.story("邮件详情内，标记为垃圾邮件")
    @pytest.mark.parametrize("caseid,casename,data",markRubbishEmail_datas)
    def test_markRubbishEmail(self,caseid,casename,data,login,clearBlackList):
        self.driver = emailDetailPage(login)
        self.driver.run_markRubbishEmail_case(caseid,casename,data)


    @allure.story("邮件详情内，跟进按钮展示")
    @pytest.mark.parametrize("caseid,casename,data",showFollowBtn_datas)
    def test_showFollowBtn(self,caseid,casename,data,login):
        self.driver = emailDetailPage(login)
        self.driver.run_showFollowBtn_case(caseid,casename,data)


    @allure.story("标记邮件未读，星标相关功能")
    @pytest.mark.parametrize("caseid,casename",markEmail_datas)
    def test_markEmail(self,caseid,casename,login):
        self.driver = emailDetailPage(login)
        self.driver.run_markEmail_case(caseid,casename)



    @allure.story("邮件详情内，文件预览相关功能")
    @pytest.mark.parametrize("caseid,casename,data",previewFile_datas)
    def test_previewFile(self,caseid,casename,data,login):
        self.driver = emailDetailPage(login)
        self.driver.run_previewFile_case(caseid,casename,data)


    @allure.story("邮件详情内，相关邮件相关功能")
    def test_relatedEmail(self,login):
        self.driver = emailDetailPage(login)
        self.driver.run_relatedEmail_case()


    @allure.story("邮件详情内，下载附件相关功能")
    @pytest.mark.parametrize("caseid,casename",downloadAttach_datas)
    def test_downloadAttach(self,caseid,casename,login):
        self.driver = emailDetailPage(login)
        self.driver.run_downloadAttach_case(caseid,casename)




if __name__ == '__main__':
    pytest.main(["-s","test_emailDetail.py"])