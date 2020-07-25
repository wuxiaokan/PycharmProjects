# -*- encoding: utf-8 -*-
'''
@File    :   recipientBoxPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/19 0019 16:38   dmk      1.0         None
'''
import allure,time,traceback
from selenium.webdriver.common.by import By
from utils.log import logger
from utils.config import IMAGE_PATH
from pageObject.basePage import Action
from pageObject.recipientBoxPage.recipientBoxPage_loc import recipientBoxPageLoc
from pageObject.emailDetailPage.emailDetailPage_loc import emailDetailPageLoc


class recipientBoxPage(Action,recipientBoxPageLoc,emailDetailPageLoc):


    def switch_operator(self,operator):
        with allure.step("切换到主文档"):
            self.switch_mainPage()
        with allure.step("悬浮当前登录人"):
            self.mouseClick(self.userNav_loc)
        with allure.step("点击当前用户"):
            self.find_element(self.userText_loc).click()
        with allure.step("点击要切换的业务员"):
            operator_loc = (By.XPATH,'//li[@data-user="{}"]'.format(operator))
            self.find_element(operator_loc).click()
        time.sleep(2)
        with allure.step("切换到主frame"):
            self.switch_frame(self.mainFrame_loc)



    def get_emailAndClick(self,subject,time_min=8):
        with allure.step("遍历收件箱，查看是否有主题是：{}的邮件".format(subject)):
            num = 0
            while True:
                self.click_ele(self.recipientBoxPage_recipientBoxBtn_loc)
                time.sleep(3)
                allMailSubjects = self.get_elementText(self.recipientBoxPage_emailSubject_loc,index="all")
                print("allMailSubjects:{}".format(allMailSubjects))
                if subject in allMailSubjects:
                    mailSubject_loc = (By.XPATH,'//span[contains(text(),"{}")]'.format(subject))
                    self.find_element(mailSubject_loc).click()
                    break
                else:
                    num = num + 1
                    time.sleep(10)
                if num == time_min * 6:
                    raise Exception("收件箱没有主题是：{}的邮件，请排查".format(subject))


    #获取转发，分发意见文本
    def get_forwardText_emailDetail(self):
        with allure.step("点击转发意见按钮"):
            self.click_ele(self.emailDetailPage_forwardIdeaBtn_loc)
        with allure.step("获取转发意见文本"):
            return self.get_elementText(self.emailDetailPage_forwardIdeaText_loc)


    #判断收件箱是否有该主题邮件，转发意见是否正确
    def assert_emailSubjectAndForwardIdea(self,subject,idea):
        with allure.step("点击主题是：{}的邮件"):
            self.get_emailAndClick(subject,time_min=3)
        with allure.step("判断转发意见是否正确"):
            forwardIdea = self.get_forwardText_emailDetail()
            if idea != forwardIdea:
                raise Exception("转发之后的转发意见：{}，与转发前输入的转发意见：{}，不一致".format(forwardIdea,idea))


    #移动查询箱邮件到收件箱
    def moveEmailToRecipientBox(self):
        with allure.step("点击恢复数据箱按钮"):
            boxName_loc = (By.XPATH,self.recipientBoxPage_recipientBoxBtn_loc[1].replace("收件箱","恢复数据箱，勿动"))
            self.click_ele(boxName_loc,key="点击数据恢复箱子")
        time.sleep(2)
        with allure.step("点击全选选择框"):
            seleclAllCheckboxEle = self.find_element(self.recipientBoxPage_selectAllCheckBox_loc,key="获取全选选择框")
            seleclAllCheckboxAttr = seleclAllCheckboxEle.get_attribute("class")
            if "is-disabled" not in seleclAllCheckboxAttr:
                seleclAllCheckboxEle.click()
                with allure.step("点击移动按钮"):
                    self.click_ele(self.recipientBoxPage_moveBtn_loc,key="点击移动按钮")
                with allure.step("点击收件箱"):
                    self.mouseHover(self.recipientBoxPage_moveToRecipientBoxBtn_loc)
                    self.click_ele(self.recipientBoxPage_moveToRecipientBoxBtn_loc,key="点击收件箱按钮")