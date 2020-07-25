# -*- encoding: utf-8 -*-
'''
@File    :   searchEmailPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/1 0001 14:51   dmk      1.0         None
'''

import allure,pytest,time
from pageObject.basePage import Action
from pageObject.searchEmailPage.searchEmailPage_loc import searchEmailPageLoc
from pageObject.recipientBoxPage.recipientBoxPageCommon import recipientBoxPageCommon
from pageObject.emailDetailPage.emailDetailPageCommon import emailDetailPageCommon

class searchEmailPage(Action,searchEmailPageLoc):

    def __init__(self,driver):
        super().__init__(driver)
        self.recipientBoxPageCommon = recipientBoxPageCommon(driver)
        self.emailDetailPageCommon = emailDetailPageCommon(driver)


    #普通搜索邮件
    def run_searchEmail_case(self,data):
        try:
            self.switch_mainPage()
            with allure.step("输入关键词：{}".format(data["keyword"])):
                self.sendKeys(self.searchEmailPage_searchInput_loc,key=data["keyword"])
            if data["select_index"] == 4:
                with allure.step("点击搜索按钮"):
                    self.click_ele(self.searchEmailPage_searchBtn_loc)
            else:
                time.sleep(1)
                with allure.step("点击第{}个搜索下拉列表".format(int(data["select_index"])+1)):
                    self.click_ele(self.searchEmailPage_searchList_loc,index=data["select_index"])
        except Exception as e:
            print(e)
        finally:
            with allure.step("切回主frame"):
                self.switch_frame(self.mainFrame_loc)
        if data["select_index"] == 0:
            with allure.step("获取所有的邮件主题"):
                allEmailSubjects = self.recipientBoxPageCommon.get_allEmailSubject()
                for subject in allEmailSubjects:
                    pytest.assume(data["keyword"] in subject,'data["keyword"]:{},subject:{}'.format(data["keyword"],subject))
        elif data["select_index"] == 1:
            with allure.step("点击第一封邮件"):
                self.click_ele(self.recipientBoxPage_emailSubject_loc)
            with allure.step("获取正文内容"):
                email_text = self.emailDetailPageCommon.get_emailTextOfEmailDetail(index="all")
                emailContent_contain = [content for content in email_text if data["keyword"] in content]
                if not emailContent_contain:
                    raise Exception("邮件正文：{}，不包含搜索的关键词：{}".format(email_text,data["keyword"]))
        elif data["select_index"] == 2:
            with allure.step("获取所有的附件标题"):
                attachNames = self.recipientBoxPageCommon.get_attachName()
                temp_l = [name for name in attachNames if data["keyword"] in name]
                pytest.assume(temp_l != [],"attachNames:{}".format(attachNames))
        elif data["select_index"] == 3:
            with allure.step("获取所有的发件人"):
                senders = self.recipientBoxPageCommon.get_allEmailSender()
                for sender in senders:
                    pytest.assume(data["keyword"] in sender,'data["keyword"]:{},sender:{}'.format(data["keyword"], sender))