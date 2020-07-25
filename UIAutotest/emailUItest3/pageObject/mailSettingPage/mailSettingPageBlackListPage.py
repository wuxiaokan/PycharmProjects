# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPageBlackListPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/4 0004 16:27   dmk      1.0         None
'''

import allure,time
from selenium.webdriver.common.by import By
from utils.generator import *
from utils.mail import Email
from pageObject.mailSettingPage.mailSettingPage import mailSettingPage
from pageObject.mailSettingPage.mailSettingPageBlackListPage_loc import mailSettingPageBlackListPageLoc
from pageObject.recipientBoxPage.recipientBoxPage_loc import recipientBoxPageLoc


class mailSettingPageBlackListPage(mailSettingPage,mailSettingPageBlackListPageLoc,recipientBoxPageLoc):

    def __init__(self,driver):
        super(mailSettingPageBlackListPage,self).__init__(driver)
        with allure.step("进入黑名单页面"):
            self.find_element(self.mailSettingPageBlackListPage_blackListBtn_loc).click()

    def run_addBlackList_case(self,is_del):
        time.sleep(1)
        with allure.step("判断是否有黑名单列表,如果有，则全部删除"):
            headCheckboxEle = self.find_element(self.mailSettingPageBlackListPage_headCheckbox_loc)
            if "is-disabled" not in headCheckboxEle.get_attribute("class"):
                headCheckboxEle.click()
                with allure.step("点击删除按钮"):
                    self.find_element(self.mailSettingPageBlackListPage_delBlackListBtn_loc).click()
                    time.sleep(4)
        with allure.step("点击添加按钮"):
            self.find_element(self.mailSettingPageBlackListPage_addBlackListBtn_loc).click()
        with allure.step("输入邮件地址"):
            self.find_element(self.mailSettingPageBlackListPage_emailAccountInput_loc).send_keys("163.com")
        with allure.step("输入邮件主题"):
            self.find_element(self.mailSettingPageBlackListPage_emailSubjectInput_loc).send_keys("广告")
        if is_del:
            with allure.step("点击直接删除按钮"):
                self.mouseClick(self.mailSettingPageBlackListPage_directDelBtn_loc)
        else:
            with allure.step("点击存放到垃圾箱按钮"):
                self.mouseClick(self.mailSettingPageBlackListPage_storeRubbishBoxBtn_loc)
        with allure.step("点击确定按钮"):
            self.find_element(self.mailSettingPageBlackListPage_sureAddBlackListBtn_loc).click()
        with allure.step("判断添加成功后的toast提示是否正确"):
            toast_text = self.get_elementText(self.toast_loc)
            if toast_text != "保存成功":
                raise Exception("添加成功黑名单的toast提示不对，：{}".format(toast_text))
        with allure.step("判断添加之后，列表中是否存在相应信息"):
            allMatchInfomations = self.get_elementText(self.mailSettingPageBlackListPage_matchInfomationTd_loc,index="all")
            allHandleWays = self.get_elementText(self.mailSettingPageBlackListPage_handleWayTd_loc,index="all")
            if "163.com" not in allMatchInfomations or "广告" not in allMatchInfomations:
                raise Exception("添加的黑名单，不在黑名单列表中")
            for handleWay in allHandleWays:
                if is_del:
                    if handleWay != "直接删除":
                        raise Exception("列表中的处理方式：{}，不对".format(handleWay))
                else:
                    if handleWay != "存入垃圾箱":
                        raise Exception("列表中的处理方式：{}，不对".format(handleWay))
        with allure.step("给该账号发送两封邮件"):
            emailTitle_account = random_name() + "--黑名单测试--" + time.strftime("%Y%m%d.%H.%M.%S")
            emailTitle_subject = random_name() + "--黑名单测试--广告--" + time.strftime("%Y%m%d.%H.%M.%S")
            e1 = Email(
                title=emailTitle_account,
                message=random_text(),
                receiver="fttx222@aliyun.com",
                server='smtp.163.com',
                sender='fttxtest@163.com',
                password='fttxtest321'
            )
            e1.send()
            e2 = Email(
                title=emailTitle_subject,
                message=random_text(),
                receiver="fttx222@aliyun.com",
                server='smtp.aliyun.com',
                sender='fttx888@aliyun.com',
                password='fttxtest123'
            )
            e2.send()
        time.sleep(150)
        with allure.step("回到邮件首页"):
            self.find_element(self.emailHomePage_loc).click()
        if is_del:
            boxName = "回收箱"
        else:
            boxName = "垃圾箱"
        boxNameBtn_loc = (By.XPATH,self.recipientBoxPage_approvalBoxBtn_loc[1].replace("审批箱",boxName))
        self.find_element(boxNameBtn_loc).click()
        with allure.step("查询{}是否收到发送的邮件".format(boxName)):
            num = 0
            while True:
                time.sleep(3)
                subjects = self.get_elementText(self.recipientBoxPage_emailSubject_loc, index="all")
                # allMailSubjects = []
                # for subject in subjects:
                #     allMailSubjects.append(subject.split("】")[1])
                if emailTitle_subject in subjects and emailTitle_account in subjects:
                    break
                else:
                    num = num + 1
                    time.sleep(20)
                    self.find_element(boxNameBtn_loc).click()
                if num == 15:
                    raise Exception("{}箱没有主题是：{}或者{}的邮件，请排查".format(boxName,emailTitle_account,emailTitle_subject))
        with allure.step("回到设置tab页面"):
            self.find_element(self.recipientBoxPage_settingTabBtn_loc).click()
        time.sleep(0.3)
        with allure.step("单个删除黑名单"):
            with allure.step("获取第一个黑名单"):
                firstBlackListEle = self.find_element(self.mailSettingPageBlackListPage_matchInfomationTd_loc)
                firstBlackList_matchInfomationText = firstBlackListEle.text
                print(firstBlackList_matchInfomationText)
            with allure.step("悬浮第一个黑名单"):
                self.mouseHover(self.mailSettingPageBlackListPage_matchInfomationTd_loc)
            time.sleep(0.2)
            with allure.step("点击单个删除按钮"):
                self.find_element(self.mailSettingPageBlackListPage_delSingleBlackListBtn_loc).click()
            with allure.step("判断删除成功后的toast提示是否正确"):
                toast_text = self.get_elementText(self.toast_loc)
                if toast_text != "删除成功":
                    raise Exception("删除黑名单的toast提示不对，：{}".format(toast_text))
            with allure.step("判断列表中是否还有删除的黑名单信息"):
                allMatchInfomations = self.get_elementText(self.mailSettingPageBlackListPage_matchInfomationTd_loc,index="all")
                if firstBlackList_matchInfomationText in allMatchInfomations:
                    raise Exception("已删除的黑名单信息：{}，仍然在列表中：{}".format(firstBlackList_matchInfomationText,allMatchInfomations))
        time.sleep(0.3)
        with allure.step("全部删除黑名单"):
            with allure.step("勾选全选选择框"):
                self.find_element(self.mailSettingPageBlackListPage_headCheckbox_loc).click()
            with allure.step("点击删除按钮"):
                self.find_element(self.mailSettingPageBlackListPage_delBlackListBtn_loc).click()
            with allure.step("判断删除成功后的toast提示是否正确"):
                toast_text = self.get_elementText(self.toast_loc)
                if toast_text != "删除成功":
                    raise Exception("删除黑名单的toast提示不对，：{}".format(toast_text))
            with allure.step("判断列表中是否还有黑名单信息"):
                time.sleep(1)
                if self.is_element_exist(self.mailSettingPageBlackListPage_matchInfomationTd_loc[1]):
                    raise Exception("已经全部删除了黑名单，但是列表中中依然存在黑名单信息")