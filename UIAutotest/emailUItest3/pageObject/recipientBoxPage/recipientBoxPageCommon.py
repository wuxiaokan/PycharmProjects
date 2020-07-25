# -*- encoding: utf-8 -*-
'''
@File    :   recipientBoxPageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/2 0002 10:46   dmk      1.0         None
'''

import allure,time
from selenium.webdriver.common.by import By
from pageObject.basePage import Action
from pageObject.recipientBoxPage.recipientBoxPage_loc import recipientBoxPageLoc
from pageObject.recipientBoxPage.recipientBoxPageAttachShowPage_loc import recipientBoxPageAttachShowPageLoc


class recipientBoxPageCommon(Action,recipientBoxPageLoc,recipientBoxPageAttachShowPageLoc):


    #切换到每页200封邮件
    def switchPageTo200(self,pageNum=None):
        if pageNum:
            pageNum_loc = (By.XPATH,self.recipientBoxPage_200PageBtn_loc[1].replace("200",pageNum))
        else:
            pageNum_loc = self.recipientBoxPage_200PageBtn_loc
        with allure.step("点击分页按钮"):
            self.click_ele(self.recipientBoxPage_pageBtn_loc,key="点击分页按钮")
        time.sleep(0.3)
        with allure.step("点击{}条/每页按钮".format(pageNum)):
            self.click_ele(pageNum_loc,key="点击{}条/每页按钮".format(pageNum))

    #根据主题遍历箱子中邮件
    def get_emailBySubject(self,email_subject=None,box=None,is_click=1,time_num=1):
        if box:
            _box_loc = (By.XPATH,self.recipientBoxPage_recipientBoxBtn_loc[1].replace("收件箱",box))
            _boxName = box
        else:
            _box_loc = self.recipientBoxPage_recipientBoxBtn_loc
            _boxName = "收件箱"
        with allure.step("点击{}箱子".format(_boxName)):
            self.click_ele(_box_loc)
        time.sleep(3)
        if email_subject:
            __num = 0
            while True:
                with allure.step("点击{}箱子".format(_boxName)):
                    self.click_ele(_box_loc)
                time.sleep(3)
                with allure.step("获取所有的邮件主题"):
                    allEmailSubjects = []
                    _allEmailSubjects = self.get_elementText(self.recipientBoxPage_subject_loc, index="all")
                    for subject in _allEmailSubjects:
                        if "】" in subject:
                            allEmailSubjects.append(subject.split("】")[1])
                        else:
                            allEmailSubjects.append(subject)
                with allure.step("遍历主题，查看是否包含要找的主题"):
                    if email_subject in allEmailSubjects:
                        if is_click:
                            __subject_loc = (By.XPATH,'//div[@class="sub_item"]//span[text()="{}"]/../..'.format(email_subject))
                            # __subject_loc = (By.XPATH,'//div[@class="sub_item"]//span[contains(text(),"{}")]/../..'.format(email_subject))
                            self.click_ele(__subject_loc)
                            time.sleep(3)
                            break
                        break
                    elif time_num == 1:
                        raise Exception("{}箱子没有主题是：{}的邮件".format(_boxName,email_subject))
                    else:
                        time.sleep(30)
                        __num = __num + 1
                with allure.step("判断{}分钟内，是否收到邮件".format(time_num)):
                    if __num > time_num * 2:
                        raise Exception("已经过了{}分钟，{}箱子仍然没有主题是：{}的邮件".format(time_num,_boxName,email_subject))
        else:
            with allure.step("点击第一封邮件"):
                self.click_ele(self.recipientBoxPage_subject_loc,key="点击第一封邮件")
                time.sleep(3)


    #点击首页箱子
    def click_box(self,boxName):
        box_loc = (By.XPATH,self.recipientBoxPage_hasSendBoxBtn_loc[1].replace("已发箱",boxName))
        self.click_ele(box_loc,key="点击：{}".format(boxName))


    #根据邮件主题获取邮件
    def get_emailBySubjectAndBox(self,email_subject=None,boxCategory=None,boxName=None,is_contains=0,is_click=1,time_num=1):
        self.click_purposeBox(boxCategory=boxCategory, boxName=boxName)
        if email_subject:
            __num = 0
            while True:
                with allure.step("获取所有的邮件主题"):
                    allEmailSubjects = self.get_elementText(self.recipientBoxPage_emailSubject_loc, index="all")
                    # for subject in _allEmailSubjects:
                    #     if "】" in subject:
                    #         allEmailSubjects.append(subject.split("】")[1])
                    #     else:
                    #         allEmailSubjects.append(subject)
                with allure.step("遍历主题，查看是否包含要找的主题"):
                    if is_contains:
                        i = 0
                        for emailSubject in allEmailSubjects:
                            if email_subject in emailSubject:
                                i = 1000
                                if is_click:
                                    __subject_loc = (By.XPATH, '//div[@class="sub_item"]//span[contains(text(),"{}")]/../..'.format(email_subject))
                                    self.click_ele(__subject_loc)
                                    time.sleep(3)
                                break
                            else:
                                i = i + 1
                            if i == len(allEmailSubjects):
                                time.sleep(10)
                                __num = __num + 1
                                with allure.step("点击刷新按钮"):
                                    self.click_ele(self.recipientBoxPage_refreshBtn_loc, key="点击刷新按钮")
                        if i == 1000:
                            break
                    else:
                        if email_subject in allEmailSubjects:
                            if is_click:
                                __subject_loc = (By.XPATH,'//div[@class="sub_item"]//span[text()="{}"]/../..'.format(email_subject))
                                self.click_ele(__subject_loc)
                                time.sleep(3)
                            break
                        else:
                            time.sleep(10)
                            __num = __num + 1
                            with allure.step("点击刷新按钮"):
                                self.click_ele(self.recipientBoxPage_refreshBtn_loc,key="点击刷新按钮")
                with allure.step("判断{}分钟内，是否收到邮件".format(time_num)):
                    if __num > time_num * 6:
                        raise Exception("已经过了{}分钟，{}箱子仍然没有主题是：{}的邮件".format(time_num,boxName,email_subject))
        else:
            with allure.step("点击第一封邮件"):
                self.click_ele(self.recipientBoxPage_subject_loc,key="点击第一封邮件")
                time.sleep(3)


    #获取前2封邮件主题，并点击第一封邮件
    def get_emailSubjectAndClick(self,num=1,is_click=1,boxName=None):
        if boxName:
            _box_loc = (By.XPATH,self.recipientBoxPage_recipientBoxBtn_loc[1].replace("收件箱",boxName))
            with allure.step("点击{}箱子".format(boxName)):
                self.click_ele(_box_loc)
        else:
            with allure.step("点击刷新按钮"):
                self.click_ele(self.recipientBoxPage_refreshBtn_loc,key="点击刷新按钮")
        time.sleep(1)
        with allure.step("获取前{}封邮件主题".format(num)):
            _emailSubjects = self.get_elementText(self.recipientBoxPage_subject_loc,index="all",key="获取前{}封邮件主题".format(num))
        if is_click:
            with allure.step("点击第一封邮件"):
                self.click_ele(self.recipientBoxPage_subject_loc,key="点击第一封邮件")
                time.sleep(3)
        if num > len(_emailSubjects):
            num = len(_emailSubjects)
        emailSubjects = []
        for i in range(num):
            emailSubjects.append(_emailSubjects[i])
        return emailSubjects


    #点击指定的箱子
    def click_purposeBox(self,boxCategory=None, boxName=None):
        if boxCategory == "客户箱":
            with allure.step("点击客户箱tab"):
                self.click_ele(self.recipientBoxPage_customerBoxBtn_loc, key="点击客户箱按钮")
        elif boxCategory == "供应商箱":
            with allure.step("点击供应商箱tab"):
                self.click_ele(self.recipientBoxPage_supplierBoxBtn_loc, key="点击供应商箱按钮")
        elif boxCategory == "内部联系人箱":
            with allure.step("点击内部联系人箱tab"):
                self.click_ele(self.recipientBoxPage_innerBoxBtn_loc, key="点击内部联系人箱按钮")
        if boxName:
            _box_loc = (By.XPATH, self.recipientBoxPage_recipientBoxBtn_loc[1].replace("收件箱", boxName))
            _boxName = boxName
        else:
            _box_loc = self.recipientBoxPage_recipientBoxBtn_loc
            _boxName = "收件箱"
        with allure.step("点击{}箱子".format(_boxName)):
            self.click_ele(_box_loc)
        time.sleep(3)

    #判断箱子内是否有指定主题邮件
    def is_existEmailOfBox(self, email_subject=None, boxCategory=None, boxName=None,is_click=0, time_num=0):
            self.click_purposeBox(boxCategory=boxCategory,boxName=boxName)
            __num = -1
            while True:
                with allure.step("获取所有的邮件主题"):
                    allEmailSubjects = self.get_elementText(self.recipientBoxPage_emailSubject_loc, index="all")
                with allure.step("遍历主题，查看是否包含要找的主题"):
                    if email_subject in allEmailSubjects:
                        if is_click:
                            __subject_loc = (By.XPATH,'//div[@class="sub_item"]//span[text()="{}"]/../..'.format(email_subject))
                            self.click_ele(__subject_loc)
                            time.sleep(3)
                            break
                        return True
                    else:
                        time.sleep(10)
                        __num = __num + 1
                        with allure.step("点击刷新按钮"):
                            self.click_ele(self.recipientBoxPage_refreshBtn_loc, key="点击刷新按钮")
                with allure.step("判断{}分钟内，是否收到邮件".format(time_num)):
                    if __num > time_num * 6:
                        return False


    #获取未读邮件个数
    def get_unReadEmailNum(self):
        return self.get_elementText(self.recipientBoxPage_unReadEmailNum_loc,key="获取首页未读邮件个数")

    #获取星标邮件个数
    def get_starEmailNum(self):
        return self.get_elementText(self.recipientBoxPage_starEmailNum_loc,key="获取首页星标邮件个数")

    #获取免回复邮件个数
    def get_freeReplyEmailNum(self):
        eles = self.find_element(self.recipientBoxPage_freeReplyBtn_loc,index="all")
        if eles:
            return len(eles)
        return eles


    #获取未建档的邮件数
    def get_unArchiverEmailNum(self):
        if self.is_element_exist(self.recipientBoxPage_unArchiverIconBtn_loc[1]):
            return len(self.find_element(self.recipientBoxPage_unArchiverIconBtn_loc,index="all",key="获取未建档邮件数"))
        else:
            return 0

    #选中几封邮件
    def selectEmail(self,email_num=1):
        with allure.step("勾选{}封邮件".format(email_num)):
            for i in range(email_num):
                self.click_ele(self.recipientBoxPage_emailCheckBoxBtn_loc,index=19+i)

    #点击移动到箱子
    def moveToBox(self, boxCategory="收件箱"):
        with allure.step("点击移动按钮"):
            self.click_ele(self.recipientBoxPage_moveBtn_loc)
        time.sleep(0.5)
        with allure.step("点击{}箱子按钮".format(boxCategory)):
            customBoxBtn_loc = (By.XPATH,self.recipientBoxPage_moveToRecipientBoxBtn_loc[1].replace("收件箱",boxCategory))
            self.click_ele(customBoxBtn_loc)


    #获取箱子内所有的邮件主题
    def get_allEmailSubject(self):
        if self.is_element_exist(self.recipientBoxPage_subject_loc[1]):
            return self.get_elementText(self.recipientBoxPage_subject_loc,index="all")
        else:
            return False

    #获取箱子内所有的发件人
    def get_allEmailSender(self):
        if self.is_element_exist(self.recipientBoxPage_sender_loc[1]):
            return self.get_elementText(self.recipientBoxPage_sender_loc,index="all")
        else:
            return False

    #获取箱子内所有的收件人
    def get_allEmailRecipient(self):
        if self.is_element_exist(self.recipientBoxPage_recipient_loc[1]):
            return self.get_elementText(self.recipientBoxPage_recipient_loc,index="all")
        else:
            return False

    #获取箱子内所有的日期
    def get_allEmailDate(self):
        if self.is_element_exist(self.recipientBoxPage_date_loc[1]):
            return self.get_elementText(self.recipientBoxPage_date_loc,index="all")
        else:
            return False

    #获取邮件所在箱子名
    def get_allEmailBoxName(self):
        if self.is_element_exist(self.recipientBoxPage_emailBoxName_loc[1]):
            return self.get_elementText(self.recipientBoxPage_emailBoxName_loc,index="all")
        else:
            return False

    #点击刷新按钮
    def click_refreshBtn(self):
        self.click_ele(self.recipientBoxPage_refreshBtn_loc)


    #箱子邮件翻页
    def turnEmailPage(self,index=-1):
        pageNumEles = self.find_element(self.recipientBoxPage_pageNumBtn_loc,index="all")
        if len(pageNumEles) > 1:
            self.click_ele(self.recipientBoxPage_pageNumBtn_loc,index=index)

    #判断右上角是否有提示框，选择关闭
    def is_closeRightTopNotify(self,is_close=1):
        if self.is_element_click(self.recipientBoxPage_closeRightTopNotifyBtn_loc):
            if is_close:
                self.click_ele(self.recipientBoxPage_closeRightTopNotifyBtn_loc)

    #获取每封邮件的标签
    def get_everyEmailMark(self,index="all"):
        if self.is_element_exist(self.recipientBoxPage_everyEmailMarks_loc[1]):
            return self.get_elementText(self.recipientBoxPage_everyEmailMarks_loc,index=index)
        else:
            return False



    #点击邮件主题
    def click_emailSubject(self,index=0):
        self.click_ele(self.recipientBoxPage_subject_loc,index=index)

    #审批邮件
    def run_approvalMail_case(self,subject=None):
        with allure.step("点击审批箱"):
            self.find_element(self.recipientBoxPage_approvalBoxBtn_loc).click()
        with allure.step("点击过滤按钮"):
            self.find_element(self.recipientBoxPage_filterBtn_loc).click()
        time.sleep(0.2)
        with allure.step("点击过滤列表中的待审批按钮"):
            self.find_element(self.recipientBoxPage_filterListWaitApprovalBtn_loc).click()
        time.sleep(0.5)
        approvalMailNum = self.find_element(self.recipientBoxPage_approvalBoxNum_loc).text
        if subject:
            with allure.step("判断审批箱中是否有主题是{}的邮件".format(subject)):
                allEmailSubjectText = self.get_elementText(self.recipientBoxPage_emailSubject_loc,index="all")
                if subject not in allEmailSubjectText:
                    raise Exception("审批箱没有主题是{}的邮件".format(subject))
        if approvalMailNum:
            with allure.step("开始审批邮件"):
                allWaitApprovalMailBtnEle = self.find_element(self.recipientBoxPage_waitapprovalBtn_loc,index="all")
                for waitApprovalMailBtnEle in reversed(allWaitApprovalMailBtnEle):
                    waitApprovalMailBtnEle.click()
                    time.sleep(0.5)
                    self.find_element(self.recipientBoxPage_approvalPassBtn_loc).click()
                    time.sleep(1)


    #点击一封未读邮件
    def clickUnReadEmail(self):
        with allure.step("点击未读邮件箱子"):
            unReadEmailBoxBtn_loc = (By.XPATH,self.receiptBox_loc[1].replace("收件箱","未读邮件"))
            self.click_ele(unReadEmailBoxBtn_loc)
        with allure.step("点击一封未读邮件"):
            self.find_element(self.recipientBoxPage_unReadEmailSubject_loc).click()

    #获取邮件总数量
    def get_emailNums(self):
        if self.is_element_exist(self.emailNumTotal_loc[1]):
            emailNum = self.get_elementText(self.emailNumTotal_loc)
            emailNum = emailNum.split(" ")[1]
            return int(emailNum)
        else:
            return None


    #获取每页邮件数
    def get_pageSizeEmailNum(self):
        pagesize = self.find_element(self.recipientBoxPage_pageBtn_loc).get_attribute("value")
        pagesize = pagesize.split("条")[0]
        return int(pagesize)


    #获取带有附件的邮件数
    def get_containAttachEmailNum(self):
        if self.is_element_click(self.recipientBoxPage_attachIconBtn_loc):
            return len(self.find_element(self.recipientBoxPage_attachIconBtn_loc,index="all"))
        else:
            return None

    #获取已回复邮件数
    def get_replyedEmailNum(self):
        if self.is_element_exist(self.recipientBoxPage_replyedIconBtn_loc[1]):
            return len(self.find_element(self.recipientBoxPage_replyedIconBtn_loc,index="all"))
        else:
            return None


    #获取已转发邮件数
    def get_forwardEmailNum(self):
        if self.is_element_click(self.recipientBoxPage_forwardIconBtn_loc):
            return len(self.find_element(self.recipientBoxPage_forwardIconBtn_loc,index="all"))
        else:
            return None


    #获取内部已转发邮件数
    def get_innerForwardEmailNum(self):
        if self.is_element_click(self.recipientBoxPage_innerForwardIconBtn_loc):
            return len(self.find_element(self.recipientBoxPage_innerForwardIconBtn_loc,index="all"))
        else:
            return None

    #获取已读未读邮件数
    """is_read:0,未读，1"""
    def get_readEmailNum(self,is_read=0):
        if is_read:
            if self.is_element_click(self.recipientBoxPage_readIconBtn_loc):
                return len(self.find_element(self.recipientBoxPage_readIconBtn_loc,index="all"))
            else:
                return None
        else:
            if self.is_element_click(self.recipientBoxPage_unReadIconBtn_loc):
                return len(self.find_element(self.recipientBoxPage_unReadIconBtn_loc,index="all"))
            else:
                return None

    #获取星标邮件数
    def get_starNumOfEmailList(self,is_star=0):
        if is_star:
            eles = self.find_element(self.recipientBoxPage_markStarIconBtn_loc, index="all")
        else:
            eles = self.find_element(self.recipientBoxPage_unMarkStarIconBtn_loc, index="all")
        if eles:
            return len(eles)
        return eles

    #获取追踪邮件数
    def get_traceEmailNum(self):
        # if self.is_element_click(self.recipientBoxPage_traceIconBtn_loc):
        #     return len(self.find_element(self.recipientBoxPage_traceIconBtn_loc,index="all"))
        # else:
        #     return None
        eles = self.find_element(self.recipientBoxPage_traceIconBtn_loc,index="all")
        if eles:
            return len(eles)
        return eles


    #获取附件名
    def get_attachName(self,index="all"):
        with allure.step("点击第一封邮件的附件icon"):
            self.click_ele(self.recipientBoxPage_attachIconBtn_loc)
        time.sleep(1)
        with allure.step("获取附件名"):
            return self.get_elementText(self.recipientBoxPageAttachShowPage_attachName_loc,index=index)