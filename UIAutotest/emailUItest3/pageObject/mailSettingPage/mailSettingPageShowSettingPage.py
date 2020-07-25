# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPageShowSettingPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/27 0027 10:50   dmk      1.0         None
'''

import allure,time,json
from selenium.webdriver.common.by import By
from utils.mail import Email
from utils.generator import *
from .mailSettingPage import mailSettingPage
from pageObject.mailSettingPage.mailSettingPageShowSettingPage_loc import mailSettingPageShowSettingPageLoc
from pageObject.writeMailPage.writeMailCommon import writeMailCommon
from pageObject.recipientBoxPage.recipientBoxPageCommon import recipientBoxPageCommon
from pageObject.writeMailPage.writeMailPage_loc import writeMailPageLoc
from pageObject.emailDetailPage.emailDetailPage_loc import emailDetailPageLoc
from pageObject.recipientBoxPage.recipientBoxPage_loc import recipientBoxPageLoc
from pageObject.mailSettingPage.mailSettingPageBaseSettingPage_loc import mailSettingPageBaseSettingPageLoc

class mailSettingPageShowSettingPage(mailSettingPage,mailSettingPageShowSettingPageLoc,writeMailPageLoc,emailDetailPageLoc,recipientBoxPageLoc,mailSettingPageBaseSettingPageLoc):

    def __init__(self,driver):
        super(mailSettingPageShowSettingPage,self).__init__(driver)
        # self.find_element(self.mailSettingPageShowSettingPage_baseSettingBtn_loc).click()
        self.click_ele(self.mailSettingPageShowSettingPage_showSettingBtn_loc,index=0)
        self.writeMailCommon = writeMailCommon(driver)
        self.recipientBoxPageCommon = recipientBoxPageCommon(driver)


    #设置追踪
    def run_setTrace_case(self,data):
        with allure.step("获取设置追踪的class属性"):
            traceBtnEle = self.find_element(self.mailSettingPageShowSettingPage_traceBtn_loc)
            traceBtnEle_attr = traceBtnEle.get_attribute("class")
        if data["is_open"]:
            with allure.step("开启邮件追踪"):
                if "is-checked" not in traceBtnEle_attr:
                    traceBtnEle.click()
        else:
            with allure.step("关闭邮件追踪"):
                if "is-checked" in traceBtnEle_attr:
                    traceBtnEle.click()
        with allure.step("点击保存按钮"):
            self.click_ele(self.mailSettingPageShowSettingPage_saveBtn_loc)
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc)
            if toast_text != "保存成功":
                raise Exception("设置邮件追踪后，toast提示：{}，不对".format(toast_text))
        with allure.step("回到邮件首页"):
            self.click_ele(self.emailHomePage_loc)
        with allure.step("点击写邮件按钮"):
            self.click_ele(self.writeEmailBtn_loc)
        with allure.step("获取写邮件里面，邮件追踪的属性"):
            writeMailPage_traceBtnEle = self.find_element(self.writeMailPage_emailTraceBtn_loc)
            writeMailPage_traceBtnEle_attr = writeMailPage_traceBtnEle.get_attribute("class")
        with allure.step("判断邮件追踪设置是否带过来"):
            if data["is_open"]:
                if "is-checked" not in writeMailPage_traceBtnEle_attr:
                    raise Exception("邮箱设置开启了邮件追踪，但是写邮件页面，邮件追踪却没有开启")
            else:
                if "is-checked" in writeMailPage_traceBtnEle_attr:
                    raise Exception("邮箱设置关闭了邮件追踪，但是写邮件页面，邮件追踪却没有关闭")
                
                
    #设置字体
    def run_setFont_case(self):
        with allure.step("设置字体"):
            with allure.step("点击字体选择框"):
                self.click_ele(self.mailSettingPageShowSettingPage_defaultFontBtn_loc)
            time.sleep(0.3)
            with allure.step("随机选中一个字体"):
                random_num = random_number(1)
                fontListEle = self.find_element(self.mailSettingPageShowSettingPage_fontSizeList_loc,index=random_num)
                fontListText = fontListEle.text
                fontListEle.click()
        with allure.step("设置字体大小"):
            with allure.step("点击字体大小选择框"):
                self.click_ele(self.mailSettingPageShowSettingPage_fontSizeBtn_loc)
            time.sleep(0.3)
            with allure.step("随机选中一个字体大小"):
                random_num = random_number(1)
                fontSizeListEle = self.find_element(self.mailSettingPageShowSettingPage_fontSizeList_loc,index=random_num)
                fontSizeListText = fontSizeListEle.text
                fontSizeListEle.click()
        with allure.step("设置字体颜色"):
            with allure.step("点击字体颜色选择框"):
                self.click_ele(self.mailSettingPageShowSettingPage_fontColorBtn_loc)
            time.sleep(0.3)
            with allure.step("随机选中一个字体颜色"):
                random_num = random_number(1)
                fontColorListEle = self.find_element(self.mailSettingPageShowSettingPage_fontSizeList_loc,index=random_num)
                fontColorListText = fontColorListEle.value_of_css_property("background-color")
                fontColorListEle.click()
        with allure.step("点击保存按钮"):
            self.click_ele(self.mailSettingPageShowSettingPage_saveBtn_loc)
        with allure.step("获取字体展示板里面的style属性"):
            fontShowELe = self.find_element(self.mailSettingPageShowSettingPage_sizeShowTemplate_loc)
        with allure.step("判断字体，大小前后设置的是否一致"):
            fontShow_fontText = fontShowELe.value_of_css_property("font-family")
            if fontListText not in fontShow_fontText:
                raise Exception("保存成功后的字体：{}，与保存前，选择的字体：{}，不一致".format(fontShow_fontText,fontListText))
            fontShow_fontSize = fontShowELe.value_of_css_property("font-size")
            if fontShow_fontSize != fontSizeListText:
                raise Exception("保存成功后的字体大小：{}，与保存前，选择的字体大小：{}，不一致".format(fontShow_fontSize,fontSizeListText))
        with allure.step("点击邮件首页"):
            self.click_ele(self.emailHomePage_loc)
        with allure.step("点击写邮件按钮"):
            self.click_ele(self.writeEmailBtn_loc)
        with allure.step("获取邮件文本的css属性"):
            with allure.step("随机输入一段文本"):
                self.writeMailCommon.send_emailContent()
            with allure.step("获取邮件文本的css属性"):
                writeMailPage_emailBody_font,writeMailPage_emailBody_fontSize,writeMailPage_emailBody_fontColor = self.writeMailCommon.get_writeMail_css()
            with allure.step("判断写邮件页面，正文的css属性是否正确"):
                if fontListText not in writeMailPage_emailBody_font:
                    raise Exception("设置的字体：{}，与写邮件页面，正文的字体：{}，不一致".format(fontListText,writeMailPage_emailBody_font))
                if fontSizeListText != writeMailPage_emailBody_fontSize:
                    raise Exception("设置的字体大小：{}，与写邮件页面，正文的字体大小：{}，不一致".format(fontSizeListText,writeMailPage_emailBody_fontSize))
                if fontColorListText != writeMailPage_emailBody_fontColor:
                    raise Exception("设置的字体颜色：{}，与写邮件页面，正文的字体颜色：{}，不一致".format(fontColorListText,writeMailPage_emailBody_fontColor))
                
                
    #是否需要回执
    def run_emailReceipt_case(self,is_openReceipt):
        time.sleep(1)
        needReceiptBtnEle = self.find_element(self.mailSettingPageShowSettingPage_needReceiptBtn_loc)
        if is_openReceipt:
            with allure.step("开启回执"):
                if "is-checked" not in needReceiptBtnEle.get_attribute("class"):
                    self.mouseClick(self.mailSettingPageShowSettingPage_needReceiptBtn_loc)
        else:
            with allure.step("关闭回执"):
                if "is-checked" in needReceiptBtnEle.get_attribute("class"):
                    self.mouseClick(self.mailSettingPageShowSettingPage_needReceiptBtn_loc)
        with allure.step("点击保存按钮"):
            self.scroll_element(self.mailSettingPageShowSettingPage_saveBtn_loc)
            self.find_element(self.mailSettingPageShowSettingPage_saveBtn_loc).click()
        with allure.step("点击基础设置"):
            self.click_ele(self.mailSettingPageBaseSettingPage_baseSettingBtn_loc,key="点击基础设置按钮")
            time.sleep(2)
            autoReceiptBtnEle = self.find_element(self.mailSettingPageBaseSettingPage_autoReceiptBtn_loc)
            with allure.step("关闭自动回执"):
                if "is-checked" in autoReceiptBtnEle.get_attribute("class"):
                    self.mouseClick(self.mailSettingPageBaseSettingPage_autoReceiptBtn_loc)
            time.sleep(1)
        with allure.step("回到邮件首页"):
            self.find_element(self.emailHomePage_loc).click()
        with allure.step("点击写邮件"):
            self.find_element(self.writeEmailBtn_loc).click()
        time.sleep(2)
        with allure.step("输入主题"):
            emailTitle = random_name() + "--是否需要回执测试--" + time.strftime("%Y%m%d.%H.%M.%S")
            self.find_element(self.writeMailPage_emailSubjectInput_loc).send_keys(emailTitle)
        with allure.step("输入收件人"):
            self.find_element(self.writeMailPage_recipientInput_loc).send_keys("fttxtest@126.com")
        with allure.step("判断写信页面的需要回执按钮是否与邮箱设置的一致"):
            writeMailPage_needReceiptBtnEle = self.find_element(self.writeMailPage_needReceiptBtn_loc)
            if is_openReceipt:
                if "is-checked" not in writeMailPage_needReceiptBtnEle.get_attribute("class"):
                    raise Exception("设置页面开启了需要回执，但是写信页面并没有开启")
            else:
                if "is-checked" in writeMailPage_needReceiptBtnEle.get_attribute("class"):
                    raise Exception("设置页面关闭了需要回执，但是写信页面并没有关闭")
        with allure.step("切换到邮件编辑器,输入随机文本"):
            self.switch_frame(self.emailEditFrame_loc)
            self.find_element(self.emailBodyInEmailEdit_loc).send_keys(random_text())
            self.switch_parentFrame()
        with allure.step("选择发件账号：fttx222@aliyun.com"):
            # self.find_element(self.writeMailPage_senderInput_loc).click()
            # time.sleep(0.3)
            # self.find_element(self.writeMailPage_sender_loc).click()
            self.writeMailCommon.select_sender(sender="fttx222@aliyun.com")
        with allure.step("点击发送按钮"):
            self.find_element(self.writeMailPage_sendEmailBtn_loc).click()
        time.sleep(150)
        with allure.step("遍历收件箱，查看是否收到主题是：{}的邮件".format(emailTitle)):
            num = 0
            while True:
                self.find_element(self.recipientBoxPage_recipientBoxBtn_loc).click()
                time.sleep(3)
                allMailSubjects = self.get_elementText(self.recipientBoxPage_emailSubject_loc,index="all")
                if emailTitle in allMailSubjects:
                    mailSubject_loc = (By.XPATH,'//span[contains(text(),"{}")]'.format(emailTitle))
                    self.find_element(mailSubject_loc).click()
                    time.sleep(2)
                    with allure.step("判断是否有回执弹框"):
                        if is_openReceipt:
                            if not self.is_element_exist(self.emailDetailPage_autoReceiptBtn_loc[1]):
                                raise Exception("开启了回执，但是邮件详情页面却没有邮件回执弹框")
                        else:
                            if self.is_element_exist(self.emailDetailPage_autoReceiptBtn_loc[1]):
                                raise Exception("关闭了回执，但是邮件详情页面却有邮件回执弹框")
                    break
                else:
                    num = num + 1
                    time.sleep(20)
                if num == 18:
                    raise Exception("收件箱没有主题是：{}的邮件，请排查".format(emailTitle))