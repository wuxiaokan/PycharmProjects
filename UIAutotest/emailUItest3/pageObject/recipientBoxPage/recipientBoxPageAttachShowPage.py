# -*- encoding: utf-8 -*-
'''
@File    :   recipientBoxPageAttachShowPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/21 0021 11:30   dmk      1.0         None
'''

import allure,time,traceback
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from utils.log import logger
from utils.config import IMAGE_PATH
from pageObject.recipientBoxPage.recipientBoxPage import recipientBoxPage
from pageObject.recipientBoxPage.recipientBoxPageAttachShowPage_loc import recipientBoxPageAttachShowPageLoc
from pageObject.emailDetailPage.emailDetailPage_loc import emailDetailPageLoc
from pageObject.seniorSearchMailPage.seniorSearchMailPage import seniorSearchMailPage

class recipientBoxPageAttachShowPage(recipientBoxPage,recipientBoxPageAttachShowPageLoc,emailDetailPageLoc):

    def run_recipientBoxPageAttachInfoShow_case(self,is_attach):
        if is_attach:
            with allure.step("点击附件icon"):
                # self.find_element(self.recipientBoxPageAttachShowPage_attachIcon_loc).click()
                self.click_ele(self.recipientBoxPageAttachShowPage_attachIcon_loc)
            with allure.step("获取所有的附件文本"):
                allAttachText = self.get_elementText(self.recipientBoxPageAttachShowPage_attachList_loc,index="all")
                print(allAttachText)
            with allure.step("按下esc，使附件信息页面消失"):
                ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            with allure.step("点击刚刚带有附件图标的邮件"):
                self.find_element(self.recipientBoxPageAttachShowPage_subjectByAttachIcon_loc).click()
            time.sleep(3)
            with allure.step("获取邮件的主题"):
                emailSubject = self.get_elementText(self.emailDetailPage_subject_loc,key="获取详情内的主题")
                logger.info("附件展示用例的邮件主题的：{}".format(emailSubject))
            with allure.step("获取详情页面下的附件文本"):
                detailPage_allAttachText = self.get_elementText(self.emailDetailPage_attachList_loc,index="all")
                print(detailPage_allAttachText)
            if allAttachText != detailPage_allAttachText:
                raise Exception("收件箱页面的附件信息:{},与详情页面的附件信息:{},不一致，请排查".format(allAttachText,detailPage_allAttachText))
        else:
            with allure.step("查看收件箱页面，邮件列表是否有附件icon"):
                if self.is_element_exist(self.recipientBoxPageAttachShowPage_attachIcon_loc[1]):
                    self.screenshotImg(key="搜索的不含附件截图")
                    raise Exception("搜索的条件是不含附件，但是结果列表中含有附件icon，请排查")
            with allure.step("查看邮件详情内是否有附件"):
                self.find_element(self.recipientBoxPage_subject_loc).click()
                if self.is_element_exist(self.emailDetailPage_attachList_loc[1]):
                    self.screenshotImg(key="邮件列表没有附件图标的邮件详情")
                    raise Exception("邮件列表没有附件图标，但是邮件详情却有附件，请排查")