# -*- encoding: utf-8 -*-
'''
@File    :   seniorSearchEmailPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/2 0002 10:13   dmk      1.0         None
'''

import allure,pytest,traceback,time,re
from selenium.webdriver.common.by import By
from pageObject.basePage import Action
from pageObject.searchEmailPage.seniorSearchEmailPage_loc import seniorSearchEmailPageLoc
from pageObject.searchEmailPage.seniorSearchEmailPageCommon import seniorSearchEmailPageCommon
from pageObject.recipientBoxPage.recipientBoxPageCommon import recipientBoxPageCommon
from pageObject.emailDetailPage.emailDetailPageCommon import emailDetailPageCommon


class seniorSearchEmailPage(Action,seniorSearchEmailPageLoc):

    def __init__(self,driver):
        super().__init__(driver)
        self.seniorSearchEmailPageCommon = seniorSearchEmailPageCommon(driver)
        self.recipientBoxPageCommon = recipientBoxPageCommon(driver)
        self.emailDetailPageCommon = emailDetailPageCommon(driver)
        self.totalEmailNum_v1 = self.get_elementText(self.emailNumTotal_loc)
        try:
            self.switch_mainPage()
            self.click_ele(self.seniorSearchEmailPage_seniorSearchBtn_loc)
        except Exception:
            traceback.print_exc()
        finally:
            self.switch_frame(self.mainFrame_loc)


    #搜索输入框条件
    def run_seniorSearchInput_case(self,data):
        with allure.step("输入{}".format(data["keyword"])):
            optionInput_loc = (By.XPATH, self.seniorSearchEmailPage_subjectInput_loc[1].replace("主题", data["option"]))
            self.sendKeys(optionInput_loc, key=data["keyword"])
        with allure.step("点击确定按钮"):
            self.click_ele(self.seniorSearchEmailPage_sureBtn_loc)
        # with allure.step("获取搜索之后的邮件总数"):
        #     totalEmailNum_v2 = self.get_elementText(self.emailNumTotal_loc)
        #     totalEmailNum_v2 = int(totalEmailNum_v2[2:-2])
        #     pytest.assume(self.totalEmailNum_v1 != totalEmailNum_v2,"self.totalEmailNum_v1:{},totalEmailNum_v2:{}".format(self.totalEmailNum_v1,totalEmailNum_v2))
        # with allure.step("获取客户/供应商的邮件总数"):
        #     totalEmailNum_customer = self.seniorSearchEmailPageCommon.get_searchEmailNum()
        #     pytest.assume(totalEmailNum_customer > 0,"totalEmailNum_customer:{}".format(totalEmailNum_customer))
        # with allure.step("获取全部位置的邮件总数"):
        #     totalEmailNum_allPosition = self.seniorSearchEmailPageCommon.get_searchEmailNum(type=1)
        #     pytest.assume(totalEmailNum_allPosition == totalEmailNum_v2,"totalEmailNum_allPosition:{},totalEmailNum_v2:{}".format(totalEmailNum_allPosition,totalEmailNum_v2))
        # with allure.step("获取回复状态的邮件总数"):
        #     totalEmailNum_reply = self.seniorSearchEmailPageCommon.get_searchEmailNum(type=2)
        #     pytest.assume(totalEmailNum_reply == totalEmailNum_v2,"totalEmailNum_reply:{},totalEmailNum_v2:{}".format(totalEmailNum_reply,totalEmailNum_v2))
        # with allure.step("获取阅读状态的邮件总数"):
        #     totalEmailNum_read = self.seniorSearchEmailPageCommon.get_searchEmailNum(type=3)
        #     pytest.assume(totalEmailNum_read == totalEmailNum_v2,"totalEmailNum_read:{},totalEmailNum_v2:{}".format(totalEmailNum_read,totalEmailNum_v2))
        self.seniorSearchEmailPageCommon.check_emailNumOfLeftSide(homepage_totalEmailNum=self.totalEmailNum_v1)
        if data["option"] == "主题":
            with allure.step("获取所有的邮件主题"):
                emailSubjects = self.recipientBoxPageCommon.get_allEmailSubject()
                for subject in emailSubjects:
                    pytest.assume(data["keyword"] in subject,'data["keyword"]:{},subject:{}'.format(data["keyword"],subject))
        elif data["option"] == "正文":
            with allure.step("点击第一封邮件"):
                self.recipientBoxPageCommon.click_emailSubject()
            with allure.step("获取邮件正文"):
                emailContent = self.emailDetailPageCommon.get_emailTextOfEmailDetail(index="all")
                emailContent_contain = [content for content in emailContent if data["keyword"] in content]
                if not emailContent_contain:
                    raise Exception("邮件正文：{}，不包含搜索的关键词：{}".format(emailContent,data["keyword"]))
        elif data["option"] == "附件标题":
            with allure.step("获取第一封邮件的所有的附件"):
                attachNames = self.recipientBoxPageCommon.get_attachName()
                attachNames_contain = [attachName for attachName in attachNames if data["keyword"] in attachName]
                if not attachNames_contain:
                    raise Exception("附件标题:{}，不包含关键词：{}".format(attachNames,data["keyword"]))
        elif data["option"] == "收件人":
            with allure.step("获取所有的收件人"):
                recipients = self.recipientBoxPageCommon.get_allEmailRecipient()
                for recipient in recipients:
                    pytest.assume(data["keyword"] in recipient or recipient == "管理员",'data["keyword"]:{},recipient:{}'.format(data["keyword"],recipient))
        elif data["option"] == "抄送人":
            with allure.step("点击第一封邮件"):
                self.recipientBoxPageCommon.click_emailSubject()
            with allure.step("获取抄送人"):
                ccs = self.emailDetailPageCommon.get_ccOfEmailDetail(index="all")
                ccs_contains = [cc for cc in ccs if data["keyword"] in cc]
                if not ccs_contains:
                    raise Exception("抄送人：{}，不包含关键词：{}".format(ccs,data["keyword"]))
        elif data["option"] == "报价单号":
            with allure.step("点击第一封邮件"):
                self.recipientBoxPageCommon.click_emailSubject()
            with allure.step("获取所有的报价单号"):
                quoteCodes = self.emailDetailPageCommon.get_allSmallAttachNamesOfEmailDetail()
                quoteCodes_contain = [quoteCode for quoteCode in quoteCodes if data["keyword"] in quoteCode]
                pytest.assume(quoteCodes_contain != [],"quoteCodes:{},data['keyword']:{}".format(quoteCodes,data["keyword"]))
        elif data["option"] == "销售合同号":
            with allure.step("点击第一封邮件"):
                self.recipientBoxPageCommon.click_emailSubject()
            with allure.step("获取所有的销售合同号"):
                orderCodes = self.emailDetailPageCommon.get_allSmallAttachNamesOfEmailDetail()
                orderCodes_contain = [orderCode for orderCode in orderCodes if data["keyword"] in orderCode]
                pytest.assume(orderCodes_contain != [],"orderCodes:{},data['keyword']:{}".format(orderCodes, data["keyword"]))


    #搜索下拉框条件
    def run_seniorSearchDrop_case(self,data):
        with allure.step("点击{}".format(data["option"])):
            optionInput_loc = (By.XPATH, self.seniorSearchEmailPage_subjectInput_loc[1].replace("主题", data["option"]))
            self.click_ele(optionInput_loc)
        time.sleep(1)
        with allure.step("选中{}".format(data["dropList"])):
            dropList_loc = (By.XPATH,self.seniorSearchEmailPage_emailBoxList_loc[1].replace("收件箱",data["dropList"]))
            self.click_ele(dropList_loc)
        with allure.step("点击确定按钮"):
            self.click_ele(self.seniorSearchEmailPage_sureBtn_loc)
        self.seniorSearchEmailPageCommon.check_emailNumOfLeftSide(homepage_totalEmailNum=self.totalEmailNum_v1)
        if data["option"] == "邮件箱":
            with allure.step("获取邮件的箱子名"):
                emailBoxNames = self.recipientBoxPageCommon.get_allEmailBoxName()
                for box in emailBoxNames:
                    pytest.assume(box[1:-1] == data["dropList"],"box:{}".format(box))
        elif data["option"] == "时间范围":
            with allure.step("点击最后一页"):
                self.recipientBoxPageCommon.turnEmailPage()
            with allure.step("获取所有的邮件时间"):
                emailDates = self.recipientBoxPageCommon.get_allEmailDate()
                print(emailDates)
            if data["dropList"] == "1天内":
                for date in emailDates:
                    pytest.assume("前" in date,"date:{}".format(date))
            else:
                actual_time = emailDates[-1].replace("/", "")
                with allure.step("判断时间是否正确"):
                    current_time = time.time()
                    print(current_time)
                    date_pattern = "\d+"
                    day_num = re.findall(date_pattern,data["dropList"])[0]
                    purpose_time = time.strftime("%m%d",time.localtime(current_time - 24 * 60 * 60 * int(day_num)))
                    print(purpose_time)
                    pytest.assume(int(purpose_time) <= int(actual_time),"设置的条件，天数：{}，最后一个结果实际时间：{}，当前的时间：{}".format(data["dropList"], actual_time,current_time))
        elif data["option"] == "账号":
            with allure.step("点击第一封邮件"):
                self.recipientBoxPageCommon.click_emailSubject()
            with allure.step("获取收件人"):
                recipients = self.emailDetailPageCommon.get_recipientOfEmailDetail()
                pytest.assume(data["dropList"] in recipients,"recipients:{}".format(recipients))
        elif data["option"] == "标签":
            with allure.step("获取所有的标签"):
                emailMarks = self.recipientBoxPageCommon.get_everyEmailMark()
                for mark in emailMarks:
                    pytest.assume(data["dropList"] in mark,"mark:{}".format(mark))


    #单选按钮条件
    def run_seniorSearchRadio_case(self,casename,data):
        with allure.step("点击{}选项里面的{}".format(data["option"],data["radio"])):
            radio_loc = (By.XPATH,self.seniorSearchEmailPage_sendedBtn_loc[1].replace("收发类型",data["option"]).replace("发送的",data["radio"]))
            self.click_ele(radio_loc)
        if "包含免回复" in casename:
            with allure.step("点击包含免回复按钮"):
                containFreeReplyBtn_loc = (By.XPATH,self.seniorSearchEmailPage_sendedBtn_loc[1].replace("收发类型", data["option"]).replace("发送的","包含免回复"))
                self.click_ele(containFreeReplyBtn_loc)
        with allure.step("点击确定按钮"):
            self.click_ele(self.seniorSearchEmailPage_sureBtn_loc)
        self.seniorSearchEmailPageCommon.check_emailNumOfLeftSide(homepage_totalEmailNum=self.totalEmailNum_v1)
        if data["option"] == "附件":
            if data["radio"] == "含附件":
                with allure.step("获取的邮件数量，并判断是否与收件箱数量一致"):
                    emailNum_v2 = self.recipientBoxPageCommon.get_emailNums()
                with allure.step("获取所有的包含附件的邮件数"):
                    emailNum_v3 = self.recipientBoxPageCommon.get_containAttachEmailNum()
                with allure.step("获取每页的邮件数"):
                    emailNum_pageSize = self.recipientBoxPageCommon.get_pageSizeEmailNum()
                if emailNum_v2 > emailNum_pageSize:
                    pytest.assume(emailNum_pageSize == emailNum_v3)
                else:
                    pytest.assume(emailNum_v2 == emailNum_v3)
            else:
                with allure.step("判断是否有附件icon"):
                    if self.recipientBoxPageCommon.get_containAttachEmailNum():
                        raise Exception("设置了不含附件，但是查询结果却有包含附件的邮件")
        elif data["option"] == "转发状态":
            if data["radio"] == "未转发":
                with allure.step("判断是否有已转发icon"):
                    if self.recipientBoxPageCommon.get_forwardEmailNum():
                        raise Exception("设置了未转发，但是查询结果却有包含已转发的邮件")
            else:
                with allure.step("获取的邮件数量，并判断是否与收件箱数量一致"):
                    emailNum_v2 = self.recipientBoxPageCommon.get_emailNums()
                with allure.step("获取所有的包含已转发的邮件数"):
                    emailNum_v3 = self.recipientBoxPageCommon.get_forwardEmailNum()
                with allure.step("获取每页的邮件数"):
                    emailNum_pageSize = self.recipientBoxPageCommon.get_pageSizeEmailNum()
                if emailNum_v2 > emailNum_pageSize:
                    pytest.assume(emailNum_pageSize == emailNum_v3)
                else:
                    pytest.assume(emailNum_v2 == emailNum_v3)
        elif data["option"] == "内部转发":
            if data["radio"] == "未转发":
                with allure.step("判断是否有已转发icon"):
                    if self.recipientBoxPageCommon.get_innerForwardEmailNum():
                        raise Exception("设置了未转发，但是查询结果却有包含已转发的邮件")
            else:
                with allure.step("获取的邮件数量，并判断是否与收件箱数量一致"):
                    emailNum_v2 = self.recipientBoxPageCommon.get_emailNums()
                with allure.step("获取所有的包含已回复的邮件数"):
                    emailNum_v3 = self.recipientBoxPageCommon.get_innerForwardEmailNum()
                with allure.step("获取每页的邮件数"):
                    emailNum_pageSize = self.recipientBoxPageCommon.get_pageSizeEmailNum()
                if emailNum_v2 > emailNum_pageSize:
                    pytest.assume(emailNum_pageSize == emailNum_v3)
                else:
                    pytest.assume(emailNum_v2 == emailNum_v3,"emailNum_v2:{},emailNum_v3:{}".format(emailNum_v2,emailNum_v3))
        elif data["option"] == "阅读状态":
            if data["radio"] == "未阅读":
                with allure.step("判断是否有已读icon"):
                    if self.recipientBoxPageCommon.get_readEmailNum(is_read=1):
                        raise Exception("设置了未读，但是查询结果却有包含已读的邮件")
            else:
                with allure.step("判断是否有未读icon"):
                    if self.recipientBoxPageCommon.get_readEmailNum(is_read=0):
                        raise Exception("设置了已读，但是查询结果却有包含未读的邮件")
        elif data["option"] == "追踪状态":
            if data["radio"] == "未追踪":
                with allure.step("判断是否有追踪icon"):
                    if self.recipientBoxPageCommon.get_traceEmailNum():
                        raise Exception("设置了未追踪，但是查询结果却有包含追踪的邮件")
            else:
                with allure.step("获取的邮件数量，并判断是否与收件箱数量一致"):
                    emailNum_v2 = self.recipientBoxPageCommon.get_emailNums()
                with allure.step("获取所有的包含追踪的邮件数"):
                    emailNum_v3 = self.recipientBoxPageCommon.get_traceEmailNum()
                with allure.step("获取每页的邮件数"):
                    emailNum_pageSize = self.recipientBoxPageCommon.get_pageSizeEmailNum()
                if emailNum_v2 > emailNum_pageSize:
                    pytest.assume(emailNum_pageSize == emailNum_v3)
                else:
                    pytest.assume(emailNum_v2 == emailNum_v3,"emailNum_v2:{},emailNum_v3:{}".format(emailNum_v2,emailNum_v3))
        elif data["option"] == "星标状态":
            if data["radio"] == "未标记":
                with allure.step("判断是否有标记按钮"):
                    if self.recipientBoxPageCommon.get_starNumOfEmailList(is_star=1):
                        raise Exception("设置了未标记，但是查询结果却有包含星标的邮件")
            else:
                with allure.step("判断是否有标记按钮"):
                    if self.recipientBoxPageCommon.get_starNumOfEmailList(is_star=0):
                        raise Exception("设置了已标记，但是查询结果却有包含未标记星标的邮件")
        elif data["option"] == "我的回复":
            freeReplyEmailNum = 0
            if "包含免回复" in casename:
                with allure.step("判断是否有免回复邮件"):
                    freeReplyEmailNum = self.recipientBoxPageCommon.get_freeReplyEmailNum()
                    if not freeReplyEmailNum:
                        raise Exception("设置了包含免回复，但是并没有搜索到免回复邮件")
            if data["radio"] == "未回复":
                with allure.step("判断是否有已回复icon"):
                    if self.recipientBoxPageCommon.get_replyedEmailNum():
                        raise Exception("设置了未回复，但是查询结果却有包含已回复的邮件")
            else:
                with allure.step("获取的邮件数量，并判断是否与收件箱数量一致"):
                    emailNum_v2 = self.recipientBoxPageCommon.get_emailNums()
                with allure.step("获取所有的包含已回复的邮件数"):
                    emailNum_v3 = self.recipientBoxPageCommon.get_replyedEmailNum()
                with allure.step("获取每页的邮件数"):
                    emailNum_pageSize = self.recipientBoxPageCommon.get_pageSizeEmailNum()
                if emailNum_v2 > emailNum_pageSize:
                    pytest.assume(emailNum_pageSize == emailNum_v3 + freeReplyEmailNum)
                else:
                    pytest.assume(emailNum_v2 == emailNum_v3 + freeReplyEmailNum)