# -*- encoding: utf-8 -*-
'''
@File    :   customBox.py
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/18 0018 10:02   dmk      1.0         None
'''

import allure,time
from selenium.webdriver.common.by import By
from utils.generator import *
from pageObject.basePage import Action
from pageObject.customBoxPage.customBoxPage_loc import customBoxPageLoc
from pageObject.customBoxPage.customBoxPageCommon import customBoxPageCommon
from pageObject.recipientBoxPage.recipientBoxPageCommon import recipientBoxPageCommon
from pageObject.moveToBoxPage.moveToBoxPageCommon import moveToBoxPageCommon

class customBoxPage(Action,customBoxPageLoc):

    def __init__(self,driver):
        super(customBoxPage,self).__init__(driver)
        self.customBoxPageCommon = customBoxPageCommon(driver)
        self.recipientBoxPageCommon = recipientBoxPageCommon(driver)
        self.moveToBoxPageCommon = moveToBoxPageCommon(driver)


    #新增自定义箱子
    def run_addCustomBox_case(self,data):
        with allure.step("获取所有的自定义箱子"):
            allCustomBoxNames = self.customBoxPageCommon.get_allCustomBoxName(is_del=1)
            print(allCustomBoxNames)
        if data["is_parent"]:
            with allure.step("点击添加自定义箱子按钮"):
                self.click_ele(self.customBoxPage_addCustomBoxBtn_loc)
        else:
            with allure.step("悬浮第一个可删除的自定义箱子"):
                self.mouseHover(self.customBoxPage_canCancelParentCustomBoxList_loc,index=2)
            time.sleep(1)
            with allure.step("悬浮更多操作按钮"):
                self.mouseHover_visibleEle(self.customBoxPage_customBoxMoreOperateBtn_loc)
            time.sleep(1)
            with allure.step("点击新增下级自定义箱子"):
                self.click_ele(self.customBoxPage_addChildCustomBoxBtn_loc)
        if data["is_repeat"]:
            with allure.step("输入一个已经存在的自定义箱子名"):
                self.sendKeys(self.customBoxPage_addCustomBoxNameInput_loc,key=allCustomBoxNames[1])
        else:
            with allure.step("输入新的自定义箱子名"):
                customBoxName = random_name()+"test@$"+"，可删除"+str(random_number(1))
                if customBoxName in allCustomBoxNames:
                    customBoxName = random_name() + "test@$" + "，可删除" + str(random_number(-1))
                self.sendKeys(self.customBoxPage_addCustomBoxNameInput_loc,key=customBoxName)
        with allure.step("点击确定按钮"):
            self.click_ele(self.customBoxPage_sureAddCustomBoxBtn_loc)
        with allure.step("获取toast提示，并且断言"):
            toast_text = self.get_elementText(self.toast_loc)
        assert toast_text == data["expect_toast"]
        if not data["is_repeat"]:
            with allure.step("判断新增的不重名自定义箱子，是否在列表中"):
                allCustomBoxNames = self.customBoxPageCommon.get_allCustomBoxName(is_del=1)
                print(allCustomBoxNames)
                if customBoxName not in allCustomBoxNames:
                    raise Exception("新增的不重名的自定义箱子：{}，不在自定义箱子列表中：{}".format(customBoxName,allCustomBoxNames))


    #修改自定义箱子
    def run_editCustomBox_case(self,data):
        with allure.step("获取所有的自定义箱子"):
            allCustomBoxNames = self.customBoxPageCommon.get_allCustomBoxName(is_del=1)
            print(allCustomBoxNames)
        if data["is_parent"]:
            with allure.step("悬浮第一个可删除的一级自定义箱子"):
                self.mouseHover(self.customBoxPage_canCancelParentCustomBoxList_loc)
        else:
            with allure.step("悬浮第一个可删除的子级自定义箱子"):
                self.mouseHover(self.customBoxPage_canCancelChildCustomBoxList_loc)
        time.sleep(0.5)
        with allure.step("悬浮更多操作按钮"):
            self.mouseHover_visibleEle(self.customBoxPage_customBoxMoreOperateBtn_loc)
        time.sleep(0.5)
        with allure.step("点击修改自定义箱子"):
            editCustomBoxBtn_loc = (By.XPATH,self.customBoxPage_addChildCustomBoxBtn_loc[1].replace("新增下级自定义箱","修改此自定义箱"))
            self.click_ele(editCustomBoxBtn_loc)
        if data["is_repeat"]:
            with allure.step("输入一个已经存在的自定义箱子名"):
                self.sendKeys(self.customBoxPage_addCustomBoxNameInput_loc,key=allCustomBoxNames[-1])
        else:
            with allure.step("输入新的自定义箱子名"):
                customBoxName = random_name()+"test@$"+"，可删除"+str(random_number(1))
                if customBoxName in allCustomBoxNames:
                    customBoxName = random_name() + "test@$" + "，可删除" + str(random_number(1))
                self.sendKeys(self.customBoxPage_addCustomBoxNameInput_loc,key=customBoxName)
        with allure.step("点击确定按钮"):
            self.click_ele(self.customBoxPage_sureAddCustomBoxBtn_loc)
        with allure.step("获取toast提示，并且断言"):
            toast_text = self.get_elementText(self.toast_loc)
            assert toast_text == data["expect_toast"]
        if not data["is_repeat"]:
            with allure.step("判断编辑的不重名自定义箱子，是否在列表中"):
                allCustomBoxNames = self.customBoxPageCommon.get_allCustomBoxName(is_del=1)
                print(allCustomBoxNames)
                if customBoxName not in allCustomBoxNames:
                    raise Exception("编辑的不重名的自定义箱子：{}，不在自定义箱子列表中：{}".format(customBoxName,allCustomBoxNames))

    #删除自定义箱子
    def run_delCustomBox_case(self,data):
        with allure.step("获取所有的可删除的自定义箱子"):
            allCustomBoxNames = self.customBoxPageCommon.get_allCustomBoxName(is_del=1)
            print(allCustomBoxNames)
        if data["is_parent"]:
            with allure.step("悬浮第一个可删除的一级自定义箱子"):
                self.mouseHover(self.customBoxPage_canCancelParentCustomBoxList_loc)
        else:
            with allure.step("悬浮第一个可删除的子级自定义箱子"):
                self.mouseHover(self.customBoxPage_canCancelChildCustomBoxList_loc)
        time.sleep(0.5)
        with allure.step("悬浮更多操作按钮"):
            self.mouseHover_visibleEle(self.customBoxPage_customBoxMoreOperateBtn_loc)
        time.sleep(0.5)
        with allure.step("点击删除自定义箱子"):
            delCustomBoxBtn_loc = (By.XPATH,self.customBoxPage_addChildCustomBoxBtn_loc[1].replace("新增下级自定义箱","删除此自定义箱"))
            self.click_ele(delCustomBoxBtn_loc)
        with allure.step("点击确定按钮"):
            self.click_ele(self.customBoxPage_sureDelCustomBoxBtn_loc)
        with allure.step("获取toast提示，并断言"):
            toast_text = self.get_elementText(self.toast_loc)
            assert toast_text == data["expect_toast"]

    #清空自定义箱子
    def run_clearCustomBox_case(self):
        with allure.step("移动2封邮件到第一个可删除的自定义箱子中"):
            self.moveToBoxPageCommon.moveEmailToCustomBox()
        with allure.step("点击第一个可删除的自定义箱子"):
            self.click_ele(self.customBoxPage_canCancelParentCustomBoxList_loc)
        time.sleep(0.5)
        with allure.step("悬浮更多操作按钮"):
            self.mouseHover_visibleEle(self.customBoxPage_customBoxMoreOperateBtn_loc)
        with allure.step("点击清空自定义箱按钮"):
            clearCustomBoxBtn_loc = (By.XPATH,self.customBoxPage_addChildCustomBoxBtn_loc[1].replace("新增下级自定义箱","清空此自定义箱"))
            self.click_ele(clearCustomBoxBtn_loc)
        with allure.step("点击确定按钮"):
            self.click_ele(self.customBoxPage_sureDelCustomBoxBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            if toast_text != "邮件清空成功":
                raise Exception("清空自定义箱子后，toast：{}，不对".format(toast_text))
        with allure.step("查看该箱子是否清空"):
            if self.recipientBoxPageCommon.get_allEmailSubject():
                self.screenshotImg(key="清空之后，自定义箱子仍然有邮件")
                raise Exception("清空之后，该自定义箱子仍然有邮件")


    #移动全部邮件
    def run_moveAllEmail_case(self,data):
        with allure.step("移动2封邮件到第一个可删除的自定义箱子中"):
            self.moveToBoxPageCommon.moveEmailToCustomBox()
        with allure.step("点击第一个可删除的自定义箱子"):
            self.click_ele(self.customBoxPage_canCancelParentCustomBoxList_loc)
        with allure.step("获取该箱子下的所有邮件主题"):
            emailSubjects = self.recipientBoxPageCommon.get_allEmailSubject()
            print(emailSubjects)
        if not emailSubjects:
            raise Exception("该自定义箱子下没有邮件，请检查移动操作")
        with allure.step("悬浮更多操作按钮"):
            self.mouseHover_visibleEle(self.customBoxPage_customBoxMoreOperateBtn_loc)
        time.sleep(1)
        with allure.step("悬浮移动全部邮件按钮"):
            self.mouseHover_visibleEle(self.customBoxPage_moveAllEmailBtn_loc)
        time.sleep(1)
        with allure.step("点击{}".format(data["boxCategory"])):
            purposeBoxCategory_loc = (By.XPATH,self.customBoxPage_moveToRecipientBoxBtn_loc[1].replace("收件箱",data["boxCategory"]))
            self.click_ele(purposeBoxCategory_loc)
        time.sleep(0.5)
        if data["boxCategory"] in ["客户箱","供应商箱","内部联系人箱","自定义箱"]:
            if data["boxCategory"] == "客户箱":
                with allure.step("选中第一个客户箱"):
                    movedBoxName = self.moveToBoxPageCommon.selectCustomerOrSupplierBox()
            elif data["boxCategory"] == "供应商箱":
                with allure.step("选中第一个供应商箱"):
                    movedBoxName = self.moveToBoxPageCommon.selectCustomerOrSupplierBox()
            elif data["boxCategory"] == "内部联系人箱":
                with allure.step("选中第一个内部联系人箱"):
                    movedBoxName = self.moveToBoxPageCommon.selectInnerBox()
            elif data["boxCategory"] == "自定义箱":
                with allure.step("选中第一个自定义箱"):
                    movedBoxName = self.moveToBoxPageCommon.selectCustomBox(index=1)
            with allure.step("点击确认移动按钮"):
                self.moveToBoxPageCommon.click_sureMove()
        elif data["boxCategory"] in ["收件箱","已发箱","群发箱"]:
            movedBoxName = data["boxCategory"]
            data["boxCategory"] = None
        else:
            with allure.step("输入自定义箱名"):
                movedBoxName = random_name() + "test@$" + "，可删除" + str(random_number(1))
                self.sendKeys(self.customBoxPage_addCustomBoxPage_customBoxNameInput_loc,key=movedBoxName)
            with allure.step("点击保存按钮"):
                self.click_ele(self.customBoxPage_addCustomBoxPage_saveCustomBoxBtn_loc)
        with allure.step("查看是否还有邮件"):
            self.recipientBoxPageCommon.click_refreshBtn()
            time.sleep(1)
            if self.is_element_exist(self.recipientBoxPage_emailSubject_loc[1]):
                raise Exception("全部移到后，该箱子仍然有邮件")
        with allure.step("跳转到对应的箱子：{}，查看是否有邮件".format(data["boxCategory"])):
            self.recipientBoxPageCommon.click_purposeBox(boxCategory=data["boxCategory"],boxName=movedBoxName)
        with allure.step("获取所有的邮件主题"):
            emailSubjects_moved = self.recipientBoxPageCommon.get_allEmailSubject()
        with allure.step("判断移动前的邮件是否在移动之后的箱子里面"):
            for subject in emailSubjects:
                if subject not in emailSubjects_moved:
                    raise Exception("移动前的邮件：{}，不在移动之后的箱子里面，移动之后箱子的所有邮件：{}".format(emailSubjects,emailSubjects_moved))