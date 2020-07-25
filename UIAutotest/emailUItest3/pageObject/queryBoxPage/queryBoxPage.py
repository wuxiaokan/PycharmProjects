# -*- encoding: utf-8 -*-
'''
@File    :   queryBoxPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/21 0021 14:41   dmk      1.0         None
'''

import allure,time,pytest
from utils.generator import *
from pageObject.basePage import Action
from pageObject.queryBoxPage.queryBoxPage_loc import queryBoxPageLoc
from pageObject.queryBoxPage.queryBoxPageCommon import queryBoxPageCommon
from pageObject.recipientBoxPage.recipientBoxPageCommon import recipientBoxPageCommon
from pageObject.emailDetailPage.emailDetailPageCommon import emailDetailPageCommon


class queryBoxPage(Action,queryBoxPageLoc):

    def __init__(self,driver):
        super(queryBoxPage,self).__init__(driver)
        self.queryBoxPageCommon = queryBoxPageCommon(driver)
        self.recipientBoxPageCommon = recipientBoxPageCommon(driver)
        self.emailDetailPageCommon = emailDetailPageCommon(driver)


    #点击查询箱
    def click_addQueryBoxBtn(func):
        def inner(self,data=None):
            with allure.step("点击新建查询箱按钮"):
                self.click_ele(self.queryBoxPage_addQueryBoxBtn_loc)
            func(self,data=data)
        return inner

    #输入查询箱名字
    def send_queryBoxName(func):
        def inner(self,data=None):
            with allure.step("输入查询箱名字"):
                queryBoxName = random_name()+"test@$，可删除"+str(random_number(1))
                self.sendKeys(self.queryBoxPage_queryBoxNameInput_loc,key=queryBoxName)
            func(self,data=data)
        return inner


    #点击确定按钮
    def click_sureAddQueryBoxBtn(func):
        def inner(self,data=None):
            with allure.step("点击确定按钮"):
                self.click_ele(self.queryBoxPage_sureBtn_loc)
            func(self,data=data)
        return inner


    #编辑查询箱
    def edit_queryBox(func):
        def inner(self,data=None):
            time.sleep(3)
            with allure.step("悬浮一个可删除的查询箱"):
                self.mouseHover_visibleEle(self.queryBoxPage_canDelQueryBoxList_loc)
            time.sleep(0.5)
            with allure.step("悬浮更多操作按钮"):
                self.mouseHover_visibleEle(self.queryBoxPage_queryBoxMoreOperateBtn_loc)
            time.sleep(1)
            with allure.step("点击修改按钮"):
                self.click_ele(self.queryBoxPage_editQueryBoxBtn_loc)
            func(self, data=data)
        return inner

    #新建查询箱
    @click_addQueryBoxBtn
    def run_addQueryBox_case(self,data):
        if data["is_repeat"]:
            with allure.step("获取所有的查询箱名字"):
                queryBoxNames = self.queryBoxPageCommon.get_queryBoxNames()
                queryBoxName = queryBoxNames[0]
        else:
            queryBoxName = random_name()+"test@$，可删除"+str(random_number(1))
        with allure.step("输入查询名字"):
            self.sendKeys(self.queryBoxPage_queryBoxNameInput_loc,key=queryBoxName)
        with allure.step("点击确定按钮"):
            self.click_ele(self.queryBoxPage_sureBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            pytest.assume(toast_text == data["except_text"],"toast_text:{}".format(toast_text))
        if not data["is_repeat"]:
            with allure.step("获取所有的查询箱名字"):
                queryBoxNames = self.queryBoxPageCommon.get_queryBoxNames()
            pytest.assume(queryBoxName in queryBoxNames)


    #删除查询箱
    def run_delQueryBox_case(self):
        with allure.step("悬浮一个可删除的查询箱"):
            firstCanDelQueryBoxName = self.get_elementText(self.queryBoxPage_canDelQueryBoxList_loc)
            self.mouseHover_visibleEle(self.queryBoxPage_canDelQueryBoxList_loc)
        time.sleep(0.5)
        with allure.step("悬浮更多操作按钮"):
            self.mouseHover_visibleEle(self.queryBoxPage_queryBoxMoreOperateBtn_loc)
        time.sleep(1)
        with allure.step("点击删除按钮"):
            self.click_ele(self.queryBoxPage_delQueryBoxBtn_loc)
        with allure.step("点击确认删除按钮"):
            self.click_ele(self.queryBoxPage_sureDelQueryBoxBtn_loc)
        with allure.step("获取toast提示，并判断"):
            toast_text = self.get_elementText(self.toast_loc)
            pytest.assume(toast_text == "删除成功","toast_text:{}".format(toast_text))
        with allure.step("获取所有的查询箱名"):
            queryBoxNames = self.queryBoxPageCommon.get_queryBoxNames()
            pytest.assume(firstCanDelQueryBoxName not in queryBoxNames,"删除的查询箱：{}，删除后的查询箱列表：{}".format(firstCanDelQueryBoxName,queryBoxNames))


    #修改查询箱
    @click_addQueryBoxBtn
    @send_queryBoxName
    @click_sureAddQueryBoxBtn
    @edit_queryBox
    def run_modifyQueryBox_case(self,data=None):
        with allure.step("输入包含主题-重构"):
            self.sendKeys(self.queryBoxPage_subjectInput_loc,key="重构")
        with allure.step("点击不含附件按钮"):
            self.click_ele(self.queryBoxPage_unContainAttachBtn_loc)
        with allure.step("点击确定按钮"):
            self.click_ele(self.queryBoxPage_sureBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            pytest.assume(toast_text == "修改成功","toast_text:{}".format(toast_text))
        with allure.step("点击第一个查询箱"):
            self.click_ele(self.queryBoxPage_queryBoxList_loc)
        with allure.step("判断主题是否包含重构"):
            subjects = self.recipientBoxPageCommon.get_allEmailSubject()
            for subject in subjects:
                pytest.assume("重构" in subject,"subject:{}".format(subject))
        with allure.step("判断邮件中是否包含附件"):
            if self.recipientBoxPageCommon.get_containAttachEmailNum():
                raise Exception("查询箱选择了不含附件，但是搜索结果却有含附件的邮件")


    #设置查询箱条件-主题
    @click_addQueryBoxBtn
    @send_queryBoxName
    def run_setSubjectCondition_case(self,data):
        if data["is_equal"]:
            with allure.step("点击等于按钮"):
                self.click_ele(self.queryBoxPage_equalBtn_loc)
        with allure.step("输入主题"):
            self.sendKeys(self.queryBoxPage_subjectInput_loc,key=data["subject"])
        with allure.step("点击确定按钮"):
            self.click_ele(self.queryBoxPage_sureBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            pytest.assume(toast_text == "新建成功！","toast_text:{}".format(toast_text))
        with allure.step("点击第一个查询箱"):
            self.click_ele(self.queryBoxPage_queryBoxList_loc)
        with allure.step("获取所有的邮件主题"):
            emailSubjects = self.recipientBoxPageCommon.get_allEmailSubject()
        for subject in emailSubjects:
            if data["is_equal"]:
                pytest.assume(data["subject"] == subject,"包含的主题：{}，查询箱的主题：{}".format(data["subject"],subject))
            else:
                pytest.assume(data["subject"] in subject,"等于的主题：{}，查询箱的主题：{}".format(data["subject"],subject))


    #设置查询箱条件-标签
    @click_addQueryBoxBtn
    @send_queryBoxName
    def run_setMarkCondition_case(self,data=None):
        with allure.step("点击标签下拉框按钮"):
            markInput_loc = self.queryBoxPageCommon.generateXpathBySubject("标签")
            self.click_ele(markInput_loc)
        time.sleep(1)
        with allure.step("选择第一个标签"):
            firstMarkEle = self.find_element(self.queryBoxPage_markList_loc)
            firstMark_text = firstMarkEle.text
            firstMarkEle.click()
        with allure.step("点击确定按钮"):
            self.click_ele(self.queryBoxPage_sureBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            pytest.assume(toast_text == "新建成功！","toast_text:{}".format(toast_text))
        with allure.step("点击第一个查询箱"):
            self.click_ele(self.queryBoxPage_queryBoxList_loc)
        with allure.step("获取所有的每封邮件的标签,并判断是否包含条件里面的标签"):
            everyEmailMarks = self.recipientBoxPageCommon.get_everyEmailMark()
            for mark in everyEmailMarks:
                pytest.assume(firstMark_text in mark,"条件里面的标签：{}，每封邮件的标签:{}".format(firstMark_text,mark))



    #设置查询箱条件-发件人
    @click_addQueryBoxBtn
    @send_queryBoxName
    def run_setSenderCondition_case(self,data):
        if data["is_equal"]:
            with allure.step("点击等于按钮"):
                equalSenderBtn_loc = self.queryBoxPageCommon.generateEqualXpathBySubject("发件人")
                self.click_ele(equalSenderBtn_loc)
        with allure.step("输入发件人"):
            senderInput_loc = self.queryBoxPageCommon.generateXpathBySubject("发件人")
            self.sendKeys(senderInput_loc,key=data["sender"])
        with allure.step("点击确定按钮"):
            self.click_ele(self.queryBoxPage_sureBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            pytest.assume(toast_text == "新建成功！","toast_text:{}".format(toast_text))
        with allure.step("点击第一个查询箱"):
            self.click_ele(self.queryBoxPage_queryBoxList_loc)
        with allure.step("获取所有的发件人"):
            emailSenders = self.recipientBoxPageCommon.get_allEmailSender()
        for sender in emailSenders:
            pytest.assume(data["sender"] in sender or sender == "管理员","设置的条件，发件人-data['sender']：{}，查询箱的查询结果，发件人-sender：{}".format(data["sender"],sender))


    # 设置查询箱条件-收件人
    @click_addQueryBoxBtn
    @send_queryBoxName
    def run_setRecipientCondition_case(self, data):
        if data["is_equal"]:
            with allure.step("点击等于按钮"):
                equalRecipientBtn_loc = self.queryBoxPageCommon.generateEqualXpathBySubject("收件人")
                self.click_ele(equalRecipientBtn_loc)
        with allure.step("输入收件人"):
            recipientInput_loc = self.queryBoxPageCommon.generateXpathBySubject("收件人")
            self.sendKeys(recipientInput_loc, key=data["recipient"])
        with allure.step("点击确定按钮"):
            self.click_ele(self.queryBoxPage_sureBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            pytest.assume(toast_text == "新建成功！", "toast_text:{}".format(toast_text))
        with allure.step("点击第一个查询箱"):
            self.click_ele(self.queryBoxPage_queryBoxList_loc)
        with allure.step("获取所有的收件人"):
            emailRecipients = self.recipientBoxPageCommon.get_allEmailRecipient()
        if data["is_equal"]:
            for recipient in emailRecipients:
                pytest.assume(data["recipient"].split("@")[0] == recipient,"设置的条件，收件人-data['recipient']：{}，查询箱的查询结果，收件人-recipient：{}".format(data["recipient"],recipient))
        else:
            num = emailRecipients.count(data["recipient"]) + emailRecipients.count("管理员")
            pytest.assume(num/len(emailRecipients) > 0.8,"设置的条件，收件人-data['recipient']：{}，查询箱的查询结果，收件人-recipient：{}".format(data["recipient"],emailRecipients))

    # 设置查询箱条件-抄送人
    @click_addQueryBoxBtn
    @send_queryBoxName
    def run_setCcCondition_case(self, data):
        if data["is_equal"]:
            with allure.step("点击等于按钮"):
                equalCcBtn_loc = self.queryBoxPageCommon.generateEqualXpathBySubject("抄送人")
                self.click_ele(equalCcBtn_loc)
        with allure.step("输入抄送人"):
            CcInput_loc = self.queryBoxPageCommon.generateXpathBySubject("抄送人")
            self.sendKeys(CcInput_loc, key=data["cc"])
        with allure.step("点击确定按钮"):
            self.click_ele(self.queryBoxPage_sureBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            pytest.assume(toast_text == "新建成功！", "toast_text:{}".format(toast_text))
        with allure.step("点击第一个查询箱"):
            self.click_ele(self.queryBoxPage_queryBoxList_loc)
        with allure.step("点击第一封邮件"):
            self.recipientBoxPageCommon.click_emailSubject()
        with allure.step("获取邮件详情里面的抄送人"):
            cc = self.emailDetailPageCommon.get_ccOfEmailDetail()
        if data["is_equal"]:
            pytest.assume(data["cc"].split("<")[-1].split(">")[0] == cc, "设置的条件，抄送人-data['cc']:{},查询结果里面的抄送人-cc:{}".format(data["cc"], cc))
        else:
            pytest.assume(data["cc"] in cc,"设置的条件，抄送人-data['cc']:{},查询结果里面的抄送人-cc:{}".format(data["cc"],cc))
        with allure.step("回到邮件首页"):
            self.click_ele(self.emailHomePage_loc)

    # 设置查询箱条件-几天内
    @click_addQueryBoxBtn
    @send_queryBoxName
    def run_setServalDaysCondition_case(self, data):
        if data["is_send"]:
            with allure.step("点击发件按钮"):
                self.click_ele(self.queryBoxPage_servalDaysSendBtn_loc)
        with allure.step("输入日期"):
            servalDaysInput_loc = self.queryBoxPageCommon.generateXpathBySubject("几天内")
            self.sendKeys(servalDaysInput_loc, key=data["day_num"])
        with allure.step("点击确定按钮"):
            self.click_ele(self.queryBoxPage_sureBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            pytest.assume(toast_text == "新建成功！", "toast_text:{}".format(toast_text))
        with allure.step("点击第一个查询箱"):
            self.click_ele(self.queryBoxPage_queryBoxList_loc)
        with allure.step("点击最后一页"):
            self.recipientBoxPageCommon.turnEmailPage()
        with allure.step("获取邮件详情里面的日期"):
            dates = self.recipientBoxPageCommon.get_allEmailDate()
        if "前" not in dates[-1]:
            print(dates[-1].replace("/",""))
            actual_time = dates[-1].replace("/","")
            with allure.step("判断时间是否正确"):
                current_time = time.time()
                print(current_time)
                purpose_time = time.strftime("%m%d",time.localtime(current_time-24*60*60*data["day_num"]))
                print(purpose_time)
                pytest.assume(int(purpose_time) <= int(actual_time),"设置的条件，天数：{}，查询箱的最后一个结果实际时间：{}，当前的时间：{}".format(data["day_num"],actual_time,current_time))


    # 设置查询箱条件-邮件箱
    @click_addQueryBoxBtn
    @send_queryBoxName
    def run_setemailBoxCondition_case(self, data):
        with allure.step("点击邮件箱下拉框按钮"):
            emailBoxInput_loc = self.queryBoxPageCommon.generateXpathBySubject("邮件箱")
            self.click_ele(emailBoxInput_loc)
        time.sleep(1)
        with allure.step("选择第一个邮件箱"):
            firstemailBoxEle = self.find_element(self.queryBoxPage_markList_loc,index=data["index"])
            firstemailBox_text = firstemailBoxEle.text
            pytest.assume(firstemailBox_text == data["emailBox"])
            firstemailBoxEle.click()
        with allure.step("点击确定按钮"):
            self.click_ele(self.queryBoxPage_sureBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            pytest.assume(toast_text == "新建成功！", "toast_text:{}".format(toast_text))
        with allure.step("点击第一个查询箱"):
            self.click_ele(self.queryBoxPage_queryBoxList_loc)
        with allure.step("获取所有的每封邮件的邮件箱,并判断是否包含条件里面的邮件箱"):
            everyEmailemailBoxs = self.recipientBoxPageCommon.get_allEmailBoxName()
            if data["index"] < 5:
                for emailBox in everyEmailemailBoxs:
                    pytest.assume(firstemailBox_text in emailBox,"条件里面的邮件箱：{}，每封邮件的邮件箱:{}".format(firstemailBox_text, emailBox))
            else:
                allEmailBoxs = [box.split("【")[1].split(">")[0].strip() for box in everyEmailemailBoxs]
                pytest.assume(firstemailBox_text in allEmailBoxs,"条件里面的邮件箱：{}，每封邮件的邮件箱:{}".format(firstemailBox_text, allEmailBoxs))

    # 设置查询箱条件-时间范围
    @click_addQueryBoxBtn
    @send_queryBoxName
    def run_setdateScopeCondition_case(self, data=None):
        with allure.step("点击时间范围下拉框按钮"):
            dateScopeInput_loc = self.queryBoxPageCommon.generateXpathBySubject("时间范围")
            self.click_ele(dateScopeInput_loc)
        time.sleep(1)
        with allure.step("选择第一个时间范围"):
            self.click_ele(self.queryBoxPage_markList_loc)
        with allure.step("点击确定按钮"):
            self.click_ele(self.queryBoxPage_sureBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            pytest.assume(toast_text == "新建成功！", "toast_text:{}".format(toast_text))
        with allure.step("点击第一个查询箱"):
            self.click_ele(self.queryBoxPage_queryBoxList_loc)
        with allure.step("获取所有的每封邮件的时间范围,并判断是否包含条件里面的时间范围"):
            everyEmaildateScopes = self.recipientBoxPageCommon.get_allEmailDate()
            for date in everyEmaildateScopes:
                pytest.assume("小时前" in date or "分钟前" in date,"date:{}".format(date))

    # 设置查询箱条件-附件
    @click_addQueryBoxBtn
    @send_queryBoxName
    def run_setAttachCondition_case(self, data):
        with allure.step("获取收件箱的邮件数量"):
            emailNum_v1 = self.recipientBoxPageCommon.get_emailNums()
        with allure.step("点击{}按钮".format(data["btn_text"])):
            attachRadioBtn_loc = self.queryBoxPageCommon.generateRadioBtnXpathBySubject("附件")
            self.click_ele(attachRadioBtn_loc,index=data["index"])
        with allure.step("点击确定按钮"):
            self.click_ele(self.queryBoxPage_sureBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            pytest.assume(toast_text == "新建成功！", "toast_text:{}".format(toast_text))
        with allure.step("点击第一个查询箱"):
            self.click_ele(self.queryBoxPage_queryBoxList_loc)
        if data["btn_text"] == "不含附件":
            with allure.step("判断是否有附件icon"):
                if self.recipientBoxPageCommon.get_containAttachEmailNum():
                    raise Exception("查询箱设置了不含附件，但是查询结果却有包含附件的邮件")
        else:
            with allure.step("获取查询箱的邮件数量，并判断是否与收件箱数量一致"):
                emailNum_v2 = self.recipientBoxPageCommon.get_emailNums()
            if data["btn_text"] == "不限":
                pytest.assume(emailNum_v1 == emailNum_v2)
            else:
                with allure.step("获取所有的包含附件的邮件数"):
                    emailNum_v3 = self.recipientBoxPageCommon.get_containAttachEmailNum()
                with allure.step("获取每页的邮件数"):
                    emailNum_pageSize = self.recipientBoxPageCommon.get_pageSizeEmailNum()
                if emailNum_v2 > emailNum_pageSize:
                    pytest.assume(emailNum_pageSize == emailNum_v3)
                else:
                    pytest.assume(emailNum_v2 == emailNum_v3)

    # 设置查询箱条件-我的回复
    @click_addQueryBoxBtn
    @send_queryBoxName
    def run_setReplyStatusCondition_case(self, data):
        with allure.step("点击{}按钮".format(data["btn_text"])):
            ReplyStatusRadioBtn_loc = self.queryBoxPageCommon.generateRadioBtnXpathBySubject("我的回复")
            self.click_ele(ReplyStatusRadioBtn_loc, index=data["index"])
        with allure.step("点击确定按钮"):
            self.click_ele(self.queryBoxPage_sureBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            pytest.assume(toast_text == "新建成功！", "toast_text:{}".format(toast_text))
        with allure.step("点击第一个查询箱"):
            self.click_ele(self.queryBoxPage_queryBoxList_loc)
        if data["btn_text"] == "未回复":
            with allure.step("判断是否有已回复icon"):
                if self.recipientBoxPageCommon.get_replyedEmailNum():
                    raise Exception("查询箱设置了未回复，但是查询结果却有包含已回复的邮件")
        else:
            with allure.step("获取查询箱的邮件数量，并判断是否与收件箱数量一致"):
                emailNum_v2 = self.recipientBoxPageCommon.get_emailNums()
            with allure.step("获取所有的包含已回复的邮件数"):
                emailNum_v3 = self.recipientBoxPageCommon.get_replyedEmailNum()
            with allure.step("获取每页的邮件数"):
                emailNum_pageSize = self.recipientBoxPageCommon.get_pageSizeEmailNum()
            if emailNum_v2 > emailNum_pageSize:
                pytest.assume(emailNum_pageSize == emailNum_v3)
            else:
                pytest.assume(emailNum_v2 == emailNum_v3)


    # 设置查询箱条件-转发状态
    @click_addQueryBoxBtn
    @send_queryBoxName
    def run_setForwardStatusCondition_case(self, data):
        with allure.step("点击{}按钮".format(data["btn_text"])):
            ForwardStatusRadioBtn_loc = self.queryBoxPageCommon.generateRadioBtnXpathBySubject("转发状态")
            self.click_ele(ForwardStatusRadioBtn_loc, index=data["index"])
        with allure.step("点击确定按钮"):
            self.click_ele(self.queryBoxPage_sureBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            pytest.assume(toast_text == "新建成功！", "toast_text:{}".format(toast_text))
        with allure.step("点击第一个查询箱"):
            self.click_ele(self.queryBoxPage_queryBoxList_loc)
        if data["btn_text"] == "未转发":
            with allure.step("判断是否有已转发icon"):
                if self.recipientBoxPageCommon.get_forwardEmailNum():
                    raise Exception("查询箱设置了未转发，但是查询结果却有包含已转发的邮件")
        else:
            with allure.step("获取查询箱的邮件数量，并判断是否与收件箱数量一致"):
                emailNum_v2 = self.recipientBoxPageCommon.get_emailNums()
            with allure.step("获取所有的包含已回复的邮件数"):
                emailNum_v3 = self.recipientBoxPageCommon.get_forwardEmailNum()
            with allure.step("获取每页的邮件数"):
                emailNum_pageSize = self.recipientBoxPageCommon.get_pageSizeEmailNum()
            if emailNum_v2 > emailNum_pageSize:
                pytest.assume(emailNum_pageSize == emailNum_v3)
            else:
                pytest.assume(emailNum_v2 == emailNum_v3)


    # 设置查询箱条件-阅读状态
    @click_addQueryBoxBtn
    @send_queryBoxName
    def run_setReadStatusCondition_case(self, data):
        with allure.step("点击{}按钮".format(data["btn_text"])):
            ForwardStatusRadioBtn_loc = self.queryBoxPageCommon.generateRadioBtnXpathBySubject("阅读状态")
            self.click_ele(ForwardStatusRadioBtn_loc, index=data["index"])
        with allure.step("点击确定按钮"):
            self.click_ele(self.queryBoxPage_sureBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            pytest.assume(toast_text == "新建成功！", "toast_text:{}".format(toast_text))
        with allure.step("点击第一个查询箱"):
            self.click_ele(self.queryBoxPage_queryBoxList_loc)
        if data["btn_text"] == "未阅读":
            with allure.step("判断是否有已读icon"):
                if self.recipientBoxPageCommon.get_readEmailNum(is_read=1):
                    raise Exception("查询箱设置了未读，但是查询结果却有包含已读的邮件")
        else:
            with allure.step("判断是否有未读icon"):
                if self.recipientBoxPageCommon.get_readEmailNum(is_read=0):
                    raise Exception("查询箱设置了已读，但是查询结果却有包含未读的邮件")


    # 设置查询箱条件-内部转发
    @click_addQueryBoxBtn
    @send_queryBoxName
    def run_setInnerForwardStatusCondition_case(self, data):
        with allure.step("点击{}按钮".format(data["btn_text"])):
            innerForwardStatusRadioBtn_loc = self.queryBoxPageCommon.generateRadioBtnXpathBySubject("内部转发")
            self.click_ele(innerForwardStatusRadioBtn_loc, index=data["index"])
        with allure.step("点击确定按钮"):
            self.click_ele(self.queryBoxPage_sureBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            pytest.assume(toast_text == "新建成功！", "toast_text:{}".format(toast_text))
        with allure.step("点击第一个查询箱"):
            self.click_ele(self.queryBoxPage_queryBoxList_loc)
        if data["btn_text"] == "未转发":
            with allure.step("判断是否有已转发icon"):
                if self.recipientBoxPageCommon.get_innerForwardEmailNum():
                    raise Exception("查询箱设置了未转发，但是查询结果却有包含已转发的邮件")
        else:
            with allure.step("获取查询箱的邮件数量，并判断是否与收件箱数量一致"):
                emailNum_v2 = self.recipientBoxPageCommon.get_emailNums()
            with allure.step("获取所有的包含已回复的邮件数"):
                emailNum_v3 = self.recipientBoxPageCommon.get_innerForwardEmailNum()
            with allure.step("获取每页的邮件数"):
                emailNum_pageSize = self.recipientBoxPageCommon.get_pageSizeEmailNum()
            if emailNum_v2 > emailNum_pageSize:
                pytest.assume(emailNum_pageSize == emailNum_v3)
            else:
                pytest.assume(emailNum_v2 == emailNum_v3)


    # 设置查询箱条件-追踪状态
    @click_addQueryBoxBtn
    @send_queryBoxName
    def run_setTraceStatusCondition_case(self, data):
        with allure.step("点击{}按钮".format(data["btn_text"])):
            TraceStatusRadioBtn_loc = self.queryBoxPageCommon.generateRadioBtnXpathBySubject("追踪状态")
            self.click_ele(TraceStatusRadioBtn_loc, index=data["index"])
        with allure.step("点击确定按钮"):
            self.click_ele(self.queryBoxPage_sureBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            pytest.assume(toast_text == "新建成功！", "toast_text:{}".format(toast_text))
        with allure.step("点击第一个查询箱"):
            self.click_ele(self.queryBoxPage_queryBoxList_loc)
        if data["btn_text"] == "未追踪":
            with allure.step("判断是否有追踪icon"):
                if self.recipientBoxPageCommon.get_traceEmailNum():
                    raise Exception("查询箱设置了未追踪，但是查询结果却有包含追踪的邮件")
        else:
            with allure.step("获取查询箱的邮件数量，并判断是否与收件箱数量一致"):
                emailNum_v2 = self.recipientBoxPageCommon.get_emailNums()
            with allure.step("获取所有的包含追踪的邮件数"):
                emailNum_v3 = self.recipientBoxPageCommon.get_traceEmailNum()
            with allure.step("获取每页的邮件数"):
                emailNum_pageSize = self.recipientBoxPageCommon.get_pageSizeEmailNum()
            if emailNum_v2 > emailNum_pageSize:
                pytest.assume(emailNum_pageSize == emailNum_v3)
            else:
                pytest.assume(emailNum_v2 == emailNum_v3)



    # 设置查询箱条件-主营产品，跟进阶段等客户信息
    @click_addQueryBoxBtn
    @send_queryBoxName
    def run_setCustomerCondition_case(self, data):
        with allure.step("点击{}下拉框按钮".format(data["condition"])):
            emailBoxInput_loc = self.queryBoxPageCommon.generateXpathBySubject(data["condition"])
            self.click_ele(emailBoxInput_loc)
        time.sleep(1)
        with allure.step("选择{}:{}".format(data["condition"],data["secondCondition"])):
            dropList_loc = self.queryBoxPageCommon.generateXpathByMainProductList(data["secondCondition"])
            self.click_ele(dropList_loc)
        with allure.step("点击确定按钮"):
            self.click_ele(self.queryBoxPage_sureBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            pytest.assume(toast_text == "新建成功！", "toast_text:{}".format(toast_text))
        with allure.step("点击第一个查询箱"):
            self.click_ele(self.queryBoxPage_queryBoxList_loc)
        with allure.step("获取所有的发件人"):
            senders = self.recipientBoxPageCommon.get_allEmailSender()
            for sender in senders:
                pytest.assume("fttx444" in sender,"sender:{}".format(sender))