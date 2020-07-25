# -*- encoding: utf-8 -*-
'''
@File    :   showSettingPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/11 0011 16:58   dmk      1.0         None
'''

import allure,time,re
from selenium.webdriver.common.by import By
from utils.log import logger
from pageObject.basePage import Action
from pageObject.mailMoreSettingPage.showSettingPage_loc import showSettingPageLoc
from pageObject.recipientBoxPage.recipientBoxPageCommon import recipientBoxPageCommon

class showSettingPage(Action,showSettingPageLoc):

    def __init__(self,driver):
        super(showSettingPage,self).__init__(driver)
        self.recipientBoxPageCommon = recipientBoxPageCommon(driver)


    #显示设置用例
    def run_showSetting_case(self,casename,data):
        with allure.step("点击查询箱-合作客户，勿动"):
            queryBox_loc = (By.XPATH,self.receiptBox_loc[1].replace("收件箱","合作客户，勿动"))
            self.click_ele(queryBox_loc,key="点击合作客户，勿动查询箱")
        with allure.step("点击更多设置按钮"):
            self.click_ele(self.mailMoreSettingPage_moreSettingBtn_loc,key="点击更多设置按钮")
        with allure.step("悬浮显示设置按钮"):
            time.sleep(0.5)
            self.mouseHover(self.showSettingPage_showSettingBtn_loc)
        with allure.step("获取已选中的显示设置列表"):
            selectedShowSettingList = self.get_elementText(self.showSettingPage_selectedShowSettingList_loc,index="all",key="获取已勾选的设置")
        showSettingList_loc = (By.XPATH,self.showSettingPage_showEmailactBtn_loc[1].replace("显示邮件地址",data["option"]))
        if data["is_select"]:
            with allure.step("勾选{}".format(data["option"])):
                if data["option"] not in selectedShowSettingList:
                    self.click_ele(showSettingList_loc,key="勾选：{}".format(data["option"]))
        else:
            with allure.step("取消勾选{}".format(data["option"])):
                if data["option"] in selectedShowSettingList:
                    self.click_ele(showSettingList_loc,key="取消勾选：{}".format(data["option"]))
        with allure.step("点击确定按钮"):
            self.click_ele(self.showSettingPage_sureBtn_loc,key="点击确定按钮")
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc,key="获取显示设置的toast提示")
            if toast_text != "操作成功！":
                raise Exception("显示设置之后，toast：{}，不对".format(toast_text))
        if "摘要" not in casename:
            with allure.step("获取发件人信息"):
                senderInfo = self.get_elementText(self.showSettingPage_sender_loc,key="获取发件人信息")
            with allure.step("判断发件人信息中是否包含：{}".format(data["option"])):
                if data["is_select"]:
                    if data["key"] not in senderInfo:
                        raise Exception("勾选了：{}，但是发件人信息：{}，没有显示:{}".format(data['option'],senderInfo,data["key"]))
                else:
                    if data["key"] in senderInfo:
                        raise Exception("取消勾选了：{}，但是发件人信息：{}，显示:{}".format(data['option'],senderInfo,data["key"]))
        else:
            with allure.step("查看是否有摘要"):
                if data["is_select"]:
                    if not self.is_element_exist(self.showSettingPage_emailListAbstract_loc[1]):
                        raise Exception("勾选了显示摘要，但是没有展示")
                else:
                    if self.is_element_exist(self.showSettingPage_emailListAbstract_loc[1]):
                        raise Exception("取消勾选了显示摘要，但是却显示了")


    #邮件分组
    def run_groupEmail_case(self,data):
        with allure.step("点击更多设置按钮"):
            self.click_ele(self.mailMoreSettingPage_moreSettingBtn_loc,key="点击更多设置按钮")
        with allure.step("点击:{}".format(data["option"])):
            groupBtn_loc = (By.XPATH,self.showSettingPage_showSettingBtn_loc[1].replace("显示设置",data["option"]))
            self.click_ele(groupBtn_loc,key="点击:{}".format(data["option"]))
        with allure.step("获取分组名"):
            groupNames = self.get_elementText(self.showSettingPage_emailGroupName_loc,index="all",key="获取所有的分组名")
        with allure.step("判断分组名是否正确"):
            if "地址" in data["option"]:
                for groupName in groupNames:
                    if not re.match('^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$',groupName):
                        raise Exception("选择按邮件地址分组，邮件列表分组名包含非邮件地址：{}".format(groupName))
            else:
                l = list(set(data["except_groupNames"]).intersection(set(groupNames)))
                if not l:
                    raise Exception("选择分组：{}，邮件列表展示不正确,分组名：{}".format(data["option"],groupNames))


    #快捷阅读相关操作
    def run_quickRead_case(self,data):
        with allure.step("点击更多设置按钮"):
            self.click_ele(self.mailMoreSettingPage_moreSettingBtn_loc,key="点击更多设置按钮")
        quickReadBtn_loc = (By.XPATH, self.showSettingPage_showSettingBtn_loc[1].replace("显示设置", "启用快捷阅读"))
        if data["is_select"]:
            with allure.step("勾选快捷阅读"):
                if not self.is_element_exist(self.showSettingPage_quickReadSelectedIcon_loc[1]):
                    self.click_ele(quickReadBtn_loc, key="点击快捷阅读")
        else:
            with allure.step("取消勾选快捷阅读"):
                if self.is_element_exist(self.showSettingPage_quickReadSelectedIcon_loc[1]):
                    self.click_ele(quickReadBtn_loc,key="取消勾选快捷阅读")
        with allure.step("随机点击一封邮件"):
            self.recipientBoxPageCommon.get_emailBySubjectAndBox()
        with allure.step("判断是否出现快捷阅读页面"):
            if data["is_select"]:
                if not self.is_element_exist(self.showSettingPage_quickRead_loc[1]):
                    raise Exception("勾选快捷阅读后，没有出现快捷页面")
            else:
                if self.is_element_exist(self.showSettingPage_quickRead_loc[1]):
                    raise Exception("取消勾选快捷阅读后，出现了快捷页面")