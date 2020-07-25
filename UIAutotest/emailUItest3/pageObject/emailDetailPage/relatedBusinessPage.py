# -*- encoding: utf-8 -*-
'''
@File    :   relatedBusinessPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/9 0009 11:39   dmk      1.0         None
'''

import allure,time,os,shutil
from selenium.webdriver.common.by import By
from utils.log import logger
from utils.generator import *
from pageObject.basePage import Action
from pageObject.emailDetailPage.relatedBusinessPage_loc import relatedBusinessPageLoc
from pageObject.emailDetailPage.emailDetailPageCommon import emailDetailPageCommon
from pageObject.emailDetailPage.relatedBusinessPageCommon import relatedBusinessPageCommon
from pageObject.recipientBoxPage.recipientBoxPageCommon import recipientBoxPageCommon
from pageObject.writeMailPage.writeMailCommon import writeMailCommon



class relatedBusinessPage(Action,relatedBusinessPageLoc):

    def __init__(self,driver):
        super(relatedBusinessPage,self).__init__(driver)
        self.emailDetailPageCommon = emailDetailPageCommon(driver)
        self.relatedBusinessPageCommon = relatedBusinessPageCommon(driver)
        self.recipientBoxPageCommon = recipientBoxPageCommon(driver)
        self.writeMailCommon = writeMailCommon(driver)

    #邮件详情内，已关联的订单，报价相关业务
    def run_relatedQuoteAndOrder_case(self,caseid,casename,data):
        with allure.step("进入查询箱：主题包含重构，勿动，已发箱，第一封邮件"):
            self.recipientBoxPageCommon.get_emailBySubjectAndBox(email_subject="重构版本",boxName="主题包含重构，勿动，已发箱",is_contains=1)
        with allure.step("获取邮件主题和收件人"):
            emailSubject = self.emailDetailPageCommon.get_subjectOfEmailDetail()
            logger.info("用例-{}-{}：邮件主题：{}".format(caseid,casename,emailSubject))
        with allure.step("获取所有的小附件"):
            smallAttachs = self.emailDetailPageCommon.get_allSmallAttachNamesOfEmailDetail()
        quoteOrOrderCodes = []
        if data["type"] == "报价":
            with allure.step("获取所有的报价单号"):
                for attach in smallAttachs:
                    if "quo" in attach:
                        quoteOrOrderCodes.append(attach.split("_")[-1].split(".")[0])
                logger.info("quoteOrOrderCodes:{}".format(quoteOrOrderCodes))
        else:
            with allure.step("获取所有的订单单号"):
                for attach in smallAttachs:
                    if "pi" in attach:
                        quoteOrOrderCodes.append(attach.split("_")[-1].split(".")[0])
                logger.info("quoteOrOrderCodes:{}".format(quoteOrOrderCodes))
        with allure.step("点击更多按钮"):
            self.emailDetailPageCommon.clickMoreOperateBtn()
        time.sleep(0.5)
        with allure.step("点击相关业务按钮"):
            self.emailDetailPageCommon.clickBtn_moreOperate(btn_text="相关业务")
        with allure.step("获取所有的已关联的{}编码".format(data["type"])):
            codes = self.relatedBusinessPageCommon.get_relatedCode(type=data["type"])
            logger.info("codes:{}".format(codes))
            assert sorted(codes) == sorted(quoteOrOrderCodes)


    #邮件详情内，已关联的商机相关业务
    def run_relatedBusiness_case(self):
        with allure.step("先到商机发送一封邮件"):
            subject = random_name() + "--由商机开启邮件发送测试--" + time.strftime("%Y%m%d.%H.%M.%S")
            self.writeMailCommon.sendEmail_businessPage(subject=subject,)
        with allure.step("切换到已发箱，查找该邮件：{}".format(subject)):
            self.recipientBoxPageCommon.get_emailBySubjectAndBox(email_subject=subject,boxName="已发箱",time_num=3)
        with allure.step("点击更多按钮"):
            self.emailDetailPageCommon.clickMoreOperateBtn()
        time.sleep(0.5)
        with allure.step("点击相关业务按钮"):
            self.emailDetailPageCommon.clickBtn_moreOperate(btn_text="相关业务")
        with allure.step("获取商机编码"):
            businessCode = self.relatedBusinessPageCommon.get_relatedCode(type="商机")
            logger.info("businessCode:{}".format(businessCode))
            assert businessCode == "B00000002"



    #邮件详情内，关联相关业务
    def run_buildRelateBusiness_case(self,caseid,casename,data):
        with allure.step("进入已发箱指定邮件"):
            self.recipientBoxPageCommon.get_emailBySubjectAndBox(email_subject="插入宏",boxName="已发箱",is_contains=1)
        with allure.step("获取邮件主题和收件人"):
            emailSubject = self.emailDetailPageCommon.get_subjectOfEmailDetail()
            logger.info("用例-{}-{}：邮件主题：{}".format(caseid,casename,emailSubject))
        with allure.step("点击更多按钮"):
            self.emailDetailPageCommon.clickMoreOperateBtn()
        time.sleep(0.5)
        with allure.step("点击相关业务按钮"):
            self.emailDetailPageCommon.clickBtn_moreOperate(btn_text="相关业务")
        with allure.step("点击{}tab按钮".format(data["type"])):
            type_loc = (By.XPATH,self.relatedBusinessPage_quoteTabBtn_loc[1].replace("报价",data["type"]))
            self.click_ele(type_loc,key="点击{}tab按钮".format(data["type"]))
        with allure.step("点击添加关联按钮"):
            self.click_ele(self.relatedBusinessPage_addRelatedBtn_loc,key="点击添加关联按钮")
        with allure.step("选中一个{}，并获取编码".format(data["type"])):
            businessCode = self.get_elementText(self.relatedBusinessPage_quoteList_loc,key="获取编码")
            self.click_ele(self.relatedBusinessPage_quoteList_loc,key="选中一个{}".format(data["type"]))
        with allure.step("点击建立关联按钮"):
            self.click_ele(self.relatedBusinessPage_buildRelatedBtn_loc,key="点击建立关联按钮")
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc,key="获取toast提示")
            assert toast_text == "操作成功！"
        time.sleep(1)
        with allure.step("获取所有的已关联的{}编码".format(data["type"])):
            codes = self.relatedBusinessPageCommon.get_relatedCode(type=data["type"])
            if data['type'] == "商机":
                assert codes == businessCode
            else:
                assert businessCode in codes
        with allure.step("判断商机是否只能添加一个"):
            if data["type"] == "商机":
                with allure.step("点击添加关联按钮"):
                    self.click_ele(self.relatedBusinessPage_addRelatedBtn_loc, key="点击添加关联按钮")
                with allure.step("选中一个{}，并获取编码".format(data["type"])):
                    self.click_ele(self.relatedBusinessPage_quoteList_loc, key="选中一个{}".format(data["type"]))
                with allure.step("点击建立关联按钮"):
                    self.click_ele(self.relatedBusinessPage_buildRelatedBtn_loc, key="点击建立关联按钮")
                with allure.step("获取toast提示"):
                    toast_text = self.get_elementText(self.toast_loc, key="获取toast提示")
                    assert toast_text == "邮件已经关联了商机"
                with allure.step("点击返回商机详情按钮"):
                    self.click_ele(self.relatedBusinessPage_backReleatedBtn_loc,key="点击返回按钮")
                with allure.step("取消关联商机"):
                    self.click_ele(self.relatedBusinessPage_cancelRelatedBtn_loc,key="点击取消关联按钮")
                with allure.step("获取toast提示"):
                    toast_text = self.get_elementText(self.toast_loc, key="获取toast提示")
                    assert toast_text == "操作成功！"