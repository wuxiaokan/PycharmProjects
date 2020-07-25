# -*- encoding: utf-8 -*-
'''
@File    :   writeMailPageInsertFastTextPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/15 0015 10:56   dmk      1.0         None
'''

import allure,time
from selenium.webdriver.common.by import By
from utils.log import logger
from utils.config import IMAGE_PATH
from utils.generator import *
from .writeMailPage import writeMailPage
from pageObject.writeMailPage.writeMailPageInsertFastTextPage_loc import writeMailPageInsertFastTextPageLoc

class writeMailPageInsertFastTextPage(writeMailPage,writeMailPageInsertFastTextPageLoc):



    def __init__(self,driver):
        super(writeMailPageInsertFastTextPage,self).__init__(driver)
        self.find_element(self.writeMailPage_insertFastTextBtn_loc).click()


    #写信页面，新增快速文本
    def run_writeMailPageAddFastText_case(self,casename):
        newFastTextTitle = random_name()+"快速文本测试，可删除"
        newFastTextBody = random_text()
        with allure.step("点击新增按钮"):
            self.find_element(self.writeMailPageInsertFastTextPage_addFastTextBtn_loc).click()
        if "不重名" in casename:
            with allure.step("输入不重名的快速文本主题"):
                self.find_element(self.writeMailPageInsertFastTextPage_addFastTextTitleInput_loc).send_keys(newFastTextTitle)
        else:
            existFastTextTitle = self.find_element(self.writeMailPageInsertFastTextPage_fastTextTitle_loc).text
            with allure.step("输入重名的快速文本主题"):
                self.find_element(self.writeMailPageInsertFastTextPage_addFastTextTitleInput_loc).send_keys(existFastTextTitle)
        with allure.step("输入快速文本内容"):
            self.find_element(self.writeMailPageInsertFastTextPage_addFastTextBodyInput_loc).send_keys(newFastTextBody)
        with allure.step("点击保存按钮"):
            self.find_element(self.writeMailPageInsertFastTextPage_saveAddFastTextBtn_loc).click()

        if "不重名" in casename:
            with allure.step("判断新增快速文本是否在快速文本列表中"):
                assert newFastTextTitle == self.find_element(self.writeMailPageInsertFastTextPage_fastTextTitle_loc).text
                assert newFastTextBody.replace("\n","") == self.find_element(self.writeMailPageInsertFastTextPage_fastTextBody_loc).text.replace(" ","")
        else:
            with allure.step("判断toast提示是否是文本名称已存在"):
                excep_toast = self.find_element(self.toast_loc).text
                actual_toast = '文本名称 "{}"已存在'.format(existFastTextTitle)
                if excep_toast != actual_toast:
                    raise Exception("新增重名快速文本，toast提示不正确")

    #写信页面，编辑快速文本
    def run_writeMailPageEditFastText_case(self,casename):
        newFastTextTitle = random_name() + "快速文本测试，可删除"
        newFastTextBody = random_text()
        with allure.step("悬浮第一个主题包含可删除的快速文本"):
            self.mouseHover(self.writeMailPageInsertFastTextPage_fastTextTitleContainsDel_loc)
        with allure.step("点击编辑按钮"):
            self.find_element(self.writeMailPageInsertFastTextPage_editFastTextBtn_loc).click()
        fastTextTitleElement = self.find_element(self.writeMailPageInsertFastTextPage_addFastTextTitleInput_loc)
        fastTextTitleElement.clear()
        if "不重名" in casename:
            with allure.step("输入不重名的快速文本主题"):
                fastTextTitleElement.send_keys(newFastTextTitle)
        else:
            existFastTextTitle = self.find_element(self.writeMailPageInsertFastTextPage_fastTextTitle_loc,index=2).text
            with allure.step("输入重名的快速文本主题"):
                fastTextTitleElement.send_keys(existFastTextTitle)
        with allure.step("输入快速文本内容"):
            fastTextBodyElement = self.find_element(self.writeMailPageInsertFastTextPage_addFastTextBodyInput_loc)
            fastTextBodyElement.clear()
            fastTextBodyElement.send_keys(newFastTextBody)
        with allure.step("点击保存按钮"):
            self.find_element(self.writeMailPageInsertFastTextPage_saveAddFastTextBtn_loc).click()

        if "不重名" in casename:
            with allure.step("判断新增快速文本是否在快速文本列表中"):
                assert newFastTextTitle == self.find_element(self.writeMailPageInsertFastTextPage_fastTextTitle_loc).text
                assert newFastTextBody.replace("\n", "") == self.find_element(self.writeMailPageInsertFastTextPage_fastTextBody_loc).text.replace(" ", "")
        else:
            with allure.step("判断toast提示是否是文本名称已存在"):
                excep_toast = self.find_element(self.toast_loc).text
                actual_toast = '文本名称 "{}"已存在'.format(existFastTextTitle)
                if excep_toast != actual_toast:
                    raise Exception("新增重名快速文本，toast提示不正确")


    #写信页面，删除快速文本
    def run_writeMailPageDelFastText_case(self):
        #获取第一个快速文本标题
        firstCanDelFastTextTitle = self.find_element(self.writeMailPageInsertFastTextPage_fastTextTitleContainsDel_loc)
        with allure.step("悬浮第一个主题包含可删除的快速文本"):
            self.mouseHover(self.writeMailPageInsertFastTextPage_fastTextTitleContainsDel_loc)
        with allure.step("点击删除按钮"):
            self.find_element(self.writeMailPageInsertFastTextPage_delFastTextBtn_loc).click()
        with allure.step("点击确定删除按钮"):
            self.find_element(self.writeMailPageInsertFastTextPage_sureDelFastTextBtn_loc).click()
        with allure.step("判断快速文本列表中是否还有删除的快速文本"):
            allFastTextTitle = self.get_elementText(self.writeMailPageInsertFastTextPage_fastTextTitle_loc,index="all")
            if firstCanDelFastTextTitle in allFastTextTitle:
                logger.info("已删除的快速文本：{}".format(firstCanDelFastTextTitle))
                logger.info("删除后的快速文本列表：{}".format(allFastTextTitle))
                raise Exception("刚刚删除的快速文本：{}，仍然在快速文本列表：{}".format(firstCanDelFastTextTitle,allFastTextTitle))

    #写信页面，搜索快速文本
    def run_writeMailPageSearchFastText_case(self):
        with allure.step("搜索框输入关键词"):
            self.find_element(self.writeMailPageInsertFastTextPage_searchFastTextInput_loc).send_keys("测试")
        with allure.step("点击搜索按钮"):
            self.find_element(self.writeMailPageInsertFastTextPage_searchFastTextBtn_loc).click()
        with allure.step("获取搜索结果"):
            allFastTextTitles = self.get_elementText(self.writeMailPageInsertFastTextPage_fastTextTitle_loc,index="all")
        with allure.step("遍历搜索结果，查看是否包含关键词"):
            for fastTextTitle in allFastTextTitles:
                if "测试" not in fastTextTitle:
                    self.screenshotImg(key="写信页面搜索关键词")
                    logger.info("写信页面快速文本搜索，关键词：{}，搜索的快速文本标题结果：{}".format("测试",allFastTextTitles))
                    raise Exception("写信页面快速文本搜索报错，关键词：{},结果：{}".format("测试",fastTextTitle))


    #写信页面，插入快速文本
    def run_writeMailPageInsertFastText_case(self,fastText_num,is_newLine):
        # 根据入参选择快速文本，fastText_num,1:一个纯文本，2：一个富文本，3：2个纯文本，4:2个富文本，5：同时有纯文本，富文本，各1个
        with allure.step("获取所有的快速文本"):
            allFastTextList = self.find_element(self.writeMailPageInsertFastTextPage_fastTextTitle_loc,index="all")
        for fastTextList in allFastTextList:
            if fastText_num == "1":
                with allure.step("选择一个纯文本-快速文本"):
                    if "纯文本测试1" in fastTextList.text:
                        fastTextList.click()
            elif fastText_num == "2":
                with allure.step("选择一个富文本-快速文本"):
                    if "富文本测试1" in fastTextList.text:
                        fastTextList.click()
            elif fastText_num == "3":
                with allure.step("选择多个纯文本-快速文本"):
                    if "纯文本测试1" in fastTextList.text or "纯文本测试2" in fastTextList.text:
                        fastTextList.click()
            elif fastText_num == "4":
                with allure.step("选择多个富文本-快速文本"):
                    if "富文本测试1" in fastTextList.text or "富文本测试2" in fastTextList.text:
                        fastTextList.click()
            elif fastText_num == "5":
                with allure.step("选择一个富文本，一个纯文本-快速文本"):
                    if "纯文本测试1" in fastTextList.text or "富文本测试1" in fastTextList.text:
                        fastTextList.click()
        #根据入参选择是否换行
        if is_newLine == "1":
            with allure.step("判断换行显示按钮是否被选中"):
                if "is-ckecked" not in self.find_element(self.writeMailPageInsertFastTextPage_newLineShowBtn_loc).get_attribute("class"):
                    with allure.step("点击换行显示按钮"):
                        self.find_element(self.writeMailPageInsertFastTextPage_newLineShowBtn_loc).click()
        else:
            with allure.step("判断换行显示按钮是否被选中"):
                if "is-ckecked" in self.find_element(self.writeMailPageInsertFastTextPage_newLineShowBtn_loc).get_attribute("class"):
                    with allure.step("点击换行显示按钮,取消换行显示"):
                        self.find_element(self.writeMailPageInsertFastTextPage_newLineShowBtn_loc).click()
        with allure.step("点击插入按钮"):
            self.find_element(self.writeMailPageInsertFastTextPage_insertFastTextBtn_loc).click()
            time.sleep(2)
        with allure.step("点击关闭选择快速文本页面，关闭按钮"):
            self.find_element(self.writeMailPageInsertFastTextPage_closeSelectFastTextPageBtn_loc).click()

    #获取邮件内插入的快速文本内容
    def get_fastTextInEmailBody(self):
        try:
            self.switch_frame(self.emailEditFrame_loc)
            emailBody = self.find_element(self.emailBodyInEmailEdit_loc).text.replace("\n","").replace(" ","")
            logger.info("插入的邮件文本：{}".format(emailBody))
            emailBodyImgSrc = ""
            if self.is_element_exist(self.emailBodyImgInEmailEdit_loc[1]):
                emailBodyImgElements = self.find_element(self.emailBodyImgInEmailEdit_loc,index="all")
                emailBodyImgSrcList = []
                for emailBodyImgElement in emailBodyImgElements:
                    emailBodyImgSrcList.append(emailBodyImgElement.get_attribute("src").split("/")[-1].split("?")[0])
                emailBodyImgSrc = ",".join(emailBodyImgSrcList)
                logger.info("插入的图片地址：{}".format(emailBodyImgSrc))
            return emailBody,emailBodyImgSrc
        except Exception as e:
            print(e)
        finally:
            self.switch_parentFrame()