# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPageFastTextPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/7 0007 9:56   dmk      1.0         None
'''

import allure,time,os
from selenium.webdriver.common.by import By
from utils.config import ATTACH_PATH
from utils.generator import *
from pageObject.mailSettingPage.mailSettingPage import mailSettingPage
from pageObject.mailSettingPage.mailSettingPageFastTextPage_loc import mailSettingPageFastTextPageLoc
from pageObject.writeMailPage.writeMailCommon import writeMailCommon
from pageObject.writeMailPage.writeMailPageInsertFastTextPageCommon import writeMailPageInsertFastTextPageCommon


class mailSettingPageFastTextPage(mailSettingPage,mailSettingPageFastTextPageLoc):

    def __init__(self,driver):
        super(mailSettingPageFastTextPage,self).__init__(driver)
        self.writeMailCommon = writeMailCommon(driver)
        self.writeMailPageInsertFastTextPageCommon = writeMailPageInsertFastTextPageCommon(driver)
        self.click_ele(self.mailSettingPageFastTextPage_fastTextBtn_loc,key="快速文本设置")

    #新增快速文本
    def run_addFastText_case(self,data):
        with allure.step("获取所有的快速文本列表名"):
            fastTextNames = self.get_elementText(self.mailSettingPageFastTextPage_fastTextNameList_loc,index="all")
        if data["is_repeat"]:
            random_fastTextName = fastTextNames[1]
            data["expect_toast"] = data["expect_toast"].replace("xx",random_fastTextName)
        else:
            random_fastTextName = random_name() + "快速文本测试，可删除"
        with allure.step("点击新建快速文本按钮"):
            self.click_ele(self.mailSettingPageFastTextPageLoc_addFastTextBtn_loc)
        with allure.step("获取富文本按钮的属性"):
            richTextBtnEle = self.find_element(self.mailSettingPageFastTextPage_richTextBtn_loc)
            richTextBtnEle_attr = richTextBtnEle.get_attribute("class")
        with allure.step("输入快速文本名称"):
            self.sendKeys(self.mailSettingPageFastTextPage_fastTextNameInput_loc, key=random_fastTextName)
        if data["is_pure"]:
            with allure.step("输入快速文本"):
                random_fastText = random_text().replace("\n","")
                self.sendKeys(self.mailSettingPageFastTextPage_fastTextContentInput_loc,key=random_fastText)
            with allure.step("不勾选富文本选择框"):
                if "is-checked" in richTextBtnEle_attr:
                    with allure.step("点击富文本选择框，使它变成未勾选状态"):
                        richTextBtnEle.click()
                    with allure.step("点击确定按钮"):
                        self.click_ele(self.mailSettingPageFastTextPage_sureSwitchRichTextBtn_loc)
        else:
            with allure.step("勾选富文本选择框"):
                if "is-checked" not in richTextBtnEle_attr:
                    with allure.step("点击富文本选择框，使它变成勾选状态"):
                        richTextBtnEle.click()
            with allure.step("插入一张图片"):
                file = "5648215.jpg"
                self.writeMailCommon.insert_img(file)
            time.sleep(2)
            with allure.step("输入富文本"):
                richText = self.writeMailCommon.send_emailContent()
        with allure.step("点击保存按钮"):
            self.click_ele(self.mailSettingPageFastTextPage_saveFastTextBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            if toast_text != data["expect_toast"]:
                raise Exception("保存后的toast：{}，与预期的toast提示：{}，不一致".format(toast_text,data["expect_toast"]))
        time.sleep(2)
        with allure.step("获取所有的快速文本列表名"):
            fastTextNames_added = self.get_elementText(self.mailSettingPageFastTextPage_fastTextNameList_loc,index="all")
        with allure.step("判断快速文本是否在列表中"):
            if data["is_repeat"]:
                if fastTextNames_added.count(random_fastTextName) != 1:
                    raise Exception("新增重名的快速文本：{}，存在在列表中：{}".format(random_fastTextName,fastTextNames_added))
            else:
                if random_fastTextName not in fastTextNames_added:
                    raise Exception("新增重名的快速文本：{}，不存在在列表中：{}".format(random_fastTextName,fastTextNames_added))
                with allure.step("判断写信页面是否存在新增的快速文本"):
                    with allure.step("关闭邮箱设置tab"):
                        self.click_ele(self.closeTabBtn,key="关闭邮箱设置tab")
                    with allure.step("获取写信页面的快速文本"):
                        writeMailPage_fastTextName,writeMailPage_fastTextText,writeMailPage_fastTextImgUrl = self.writeMailPageInsertFastTextPageCommon.get_firstFastText(is_pure=data["is_pure"])
                    with allure.step("判断快速文本名是否在写信页面"):
                        if writeMailPage_fastTextName != random_fastTextName:
                            raise Exception("写信页面第一个快速文本：{}，与邮箱设置页面，新增的快速文本：{}，不一样".format(writeMailPage_fastTextName,random_fastTextName))
                        if data["is_pure"]:
                            if writeMailPage_fastTextText != random_fastText:
                                raise Exception("写信页面的第一个快速文本的主体：{}，与邮箱设置页面，新增的快速文本主体：{}，不一样".format(writeMailPage_fastTextText,random_fastText))
                        else:
                            if writeMailPage_fastTextText != richText:
                                raise Exception("写信页面的第一个快速文本的主体：{}，与邮箱设置页面，新增的快速文本主体：{}，不一样".format(writeMailPage_fastTextText,richText))
                            if not writeMailPage_fastTextImgUrl:
                                raise Exception("新增的富文本，快速文本，插入写信页面后，没有img图片")


    #删除快速文本
    def run_delFastText_case(self):
        with allure.step("悬浮可以删除的快速文本"):
            fastTextEles = self.find_element(self.mailSettingPageFastTextPage_fastTextNameList_loc,index="all",key="获取所有的快速文本元素")
            for fastTextEle in fastTextEles:
                del_fastTextTitle = fastTextEle.text
                if "可删除" in del_fastTextTitle:
                    fastTextEle.click()
                    break
        with allure.step("点击删除按钮"):
            self.click_ele(self.mailSettingPageFastTextPage_delFastTextBtn_loc,key="点击删除快速文本按钮")
        with allure.step("点击确定按钮"):
            self.click_ele(self.mailSettingPageFastTextPage_sureDelFastTextBtn_loc,key="点击确定按钮")
        time.sleep(3)
        with allure.step("获取所有的快速文本标题"):
            fastTextTitles = self.get_elementText(self.mailSettingPageFastTextPage_fastTextNameList_loc,index="all")
        with allure.step("判断删除的快速文本是否还在列表中"):
            if del_fastTextTitle in fastTextTitles:
                raise Exception("删除的快速文本：{}，依然存在在快速文本列表中：{}".format(del_fastTextTitle,fastTextTitles))
        with allure.step("关闭邮件设置tab"):
            self.click_ele(self.closeTabBtn,key="关闭邮箱设置tab")
        with allure.step("查看写信页面是否存在删除的快速文本"):
            writeMailPage_fastTextTitles = self.writeMailPageInsertFastTextPageCommon.get_allFastTextTitle()
            if del_fastTextTitle in writeMailPage_fastTextTitles:
                raise Exception("删除的快速文本：{}，依然存在在快速文本列表中：{}".format(del_fastTextTitle,writeMailPage_fastTextTitles))