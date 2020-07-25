# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPage.py
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/19 0019 16:12   dmk      1.0         None
'''
import allure,time,os,shutil
from selenium.webdriver.common.by import By
from utils.log import logger
from utils.generator import *
# from utils.config import DOWNLOAD_PATH
from pageObject.basePage import Action
from pageObject.emailDetailPage.emailDetailPage_loc import emailDetailPageLoc
from pageObject.emailDetailPage.emailDetailPageCommon import emailDetailPageCommon
from pageObject.writeMailPage.writeMailCommon import writeMailCommon
from pageObject.recipientBoxPage.recipientBoxPageCommon import recipientBoxPageCommon
from pageObject.mailSettingPage.mailSettingPageEmailTemplatePageCommon import mailSettingPageEmailTemplatePageCommon
from pageObject.mailSettingPage.mailSettingPageBlackListPageCommon import mailSettingPageBlackListPageCommon
from pageObject.recipientBoxPage.recipientBoxPage import recipientBoxPage

DOWNLOAD_PATH = os.path.join(os.path.dirname(os.getcwd()),"download")

class emailDetailPage(Action,emailDetailPageLoc):

    def __init__(self,driver):
        super(emailDetailPage,self).__init__(driver)
        self.writeMailCommon = writeMailCommon(driver)
        self.recipientBoxPageCommon = recipientBoxPageCommon(driver)
        self.emailDetailPageCommon = emailDetailPageCommon(driver)
        self.mailSettingPageEmailTemplatePageCommon = mailSettingPageEmailTemplatePageCommon(driver)
        self.mailSettingPageBlackListPageCommon = mailSettingPageBlackListPageCommon(driver)

    #邮件详情内，转发操作
    '''forward字段：1，转发，2，内部转发，3，作为附件转发'''
    def run_forwardEmail_case(self,caseid,casename,data):
        with allure.step("随机点击一封邮件，进入详情"):
            self.click_ele(self.recipientBoxPage_emailSubject_loc,key="点击第一封收件箱的邮件")
        with allure.step("获取该邮件的主题"):
            emailSubject = self.get_elementText(self.emailDetailPage_subject_loc,key="获取邮件详情主题")
            forwardIdea = None
            logger.info("caseid:{}--casename:{}--邮件主题：{}".format(caseid,casename,emailSubject))
        with allure.step("点击转发下拉按钮"):
            self.click_ele(self.emailDetailPage_forwardDropDownBtn_loc,key="点击转发下拉按钮")
        if data["forward"] == 1:
            with allure.step("点击转发按钮"):
                self.click_ele(self.emailDetailPage_forwardBtn_loc,key="点击转发按钮")
            time.sleep(3)
            with allure.step("获取转发后的邮件主题"):
                forwarded_emailSubject = self.writeMailCommon.get_emailSubjectInSubjectInput()
                logger.info(forwarded_emailSubject)
            with allure.step("判断转发前后的主题"):
                if forwarded_emailSubject != "Fw:"+emailSubject:
                    raise Exception("转发后的主题：{}，与转发前的主题：Fw:{}，不一样".format(forwarded_emailSubject,emailSubject))
        elif data["forward"] == 2:
            with allure.step("点击内部转发按钮"):
                self.click_ele(self.emailDetailPage_innerForwardBtn_loc,key="点击内部转发按钮")
            with allure.step("选择内部转发人"):
                self.click_ele(self.emailDetailPage_innerForwardPage_inner_loc,key="选择内部联系人")
            with allure.step("输入转发意见"):
                forwardIdea = random_text().replace("\n","")
                self.sendKeys(self.emailDetailPage_innerForwardPage_forwardIdeaInput_loc,key=forwardIdea)
            with allure.step("点击确定按钮"):
                self.click_ele(self.emailDetailPage_innerForwardPage_sureBtn_loc,key="点击内部转发确定按钮")
            with allure.step("切换到dmktest_001"):
                self.switch_operator(operator="dmktest_001")
            with allure.step("判断云基础账号是否收到内部转发的邮件"):
                recipientBoxPage(driver=self.driver).assert_emailSubjectAndForwardIdea(emailSubject,forwardIdea)
        elif data["forward"] == 3:
            with allure.step("点击作为附件发送"):
                self.click_ele(self.emailDetailPage_forwardAsAttachBtn_loc,key="点击作为附件发送")
            with allure.step("获取所有的附件名"):
                attachNames = self.writeMailCommon.get_allAttachNamesOfWriteEmailPage()
            with allure.step("判断是否生成了附件"):
                if "." in emailSubject:
                    emailSubject = emailSubject.replace(".","")
                if "@" in emailSubject:
                    emailSubject = emailSubject.replace("@","")
                if ":" in emailSubject:
                    emailSubject = emailSubject.replace(":","")
                if attachNames[0] != emailSubject+".eml":
                    raise Exception("邮件主题是：{}的邮件，作为附件转发后，附件名：{}，不对".format(emailSubject,attachNames[0]))
                if len(attachNames) != 1:
                    raise Exception("邮件主题是：{}的邮件，作为附件转发后，附件数量不对，附件名：{}".format(emailSubject, attachNames[0]))


    #邮件详情内，移动操作
    def run_moveEmail_case(self,data):
        with allure.step("点击查询箱，主题包含重构，勿动,并进入第一封邮件的详情页面"):
            self.recipientBoxPageCommon.get_emailBySubject(box="主题包含重构，勿动")
        with allure.step("获取邮件的所有信息"):
            with allure.step("获取邮件的主题"):
                emailSubject = self.emailDetailPageCommon.get_subjectOfEmailDetail()
                logger.info("要移动邮件的主题：{}".format(emailSubject))
                if not emailSubject:
                    raise Exception("要移动的邮件没有主题")
            with allure.step("获取邮件发件人"):
                emailSender = self.emailDetailPageCommon.get_senderOfEmailDetail()
                logger.info("要移动邮件的发件人：{}".format(emailSender))
                if not emailSender:
                    raise Exception("要移动的邮件没有发件人")
            with allure.step("获取所有的收件人"):
                emailRecipients = self.emailDetailPageCommon.get_recipientOfEmailDetail()
                logger.info("要移动邮件的收件人：{}".format(emailRecipients))
                if len(emailRecipients) == 0:
                    raise Exception("要移动的邮件没有收件人")
            with allure.step("获取所有的小附件"):
                emailSmallAttachNames = self.emailDetailPageCommon.get_allSmallAttachNamesOfEmailDetail()
                logger.info("要移动邮件的小附件：{}".format(emailSmallAttachNames))
                if len(emailSmallAttachNames) == 0:
                    raise Exception("要移动的邮件没有小附件")
            # with allure.step("获取所有的大附件"):
            #     emailBigAttachNames = self.emailDetailPageCommon.get_allBigAttachNamesOfEmailDetail()
            #     logger.info("要移动邮件的大附件：{}".format(emailBigAttachNames))
            #     if len(emailBigAttachNames) == 0:
            #         raise Exception("要移动的邮件没有大附件")
            with allure.step("获取邮件文本"):
                emailBody = self.emailDetailPageCommon.get_emailTextOfEmailDetail(index="all")
                logger.info("要移动邮件的邮件文本：{}".format(emailBody))
                if len(emailBody) == 0:
                    raise Exception("要移动的邮件没有邮件文本")
            with allure.step("获取所有的快照链接"):
                emailSites = self.emailDetailPageCommon.get_allSiteUrlsOfEmailDetail()
                logger.info("要移动邮件的营销网站快照：{}".format(emailSites))
                if len(emailSites) == 0:
                    raise Exception("要移动的邮件没有营销快照")
            with allure.step("获取所有的产品图片地址,编码"):
                emailProductImgUrls,emailProductCodes = self.emailDetailPageCommon.get_allProductImgUrlsOfEmailDetail()
                logger.info("要移动邮件的产品图片地址，编码：{}".format(emailProductImgUrls,emailProductCodes))
                if len(emailProductImgUrls) == 0:
                    raise Exception("要移动的邮件没有产品图片")
                if len(emailProductCodes) == 0:
                    raise Exception("要移动的邮件没有产品编码")
        with allure.step("点击移动按钮"):
            self.click_ele(self.emailDetailPage_moveBtn_loc,key="点击邮件详情移动按钮")
        with allure.step("点击{}".format(data["boxCategory"])):
            self.emailDetailPageCommon.clickBoxCategory_toMove(data["boxCategory"])
        if "发" not in data["boxCategory"]:
            if data["boxCategory"] == "客户箱":
                with allure.step("点击第一个客户箱"):
                    firstCustomerBoxEle = self.find_element(self.emailDetailPage_moveToCustomerBoxList_loc,key="获取第一个客户箱")
                    moveToBoxName = firstCustomerBoxEle.text
                    logger.info(moveToBoxName)
                    firstCustomerBoxEle.click()
            elif data["boxCategory"] == "供应商箱":
                with allure.step("点击第一个供应商箱"):
                    firstSupplierBoxEle = self.find_element(self.emailDetailPage_moveToCustomerBoxList_loc,key="获取第一个供应商箱")
                    moveToBoxName = firstSupplierBoxEle.text
                    logger.info(moveToBoxName)
                    firstSupplierBoxEle.click()
            elif data["boxCategory"] == "内部联系人箱":
                with allure.step("点击第一个内部联系人箱"):
                    time.sleep(1)
                    firstInnerBoxEle = self.find_element(self.emailDetailPage_moveToInnerBoxList_loc,key="获取第一个内部联系人箱")
                    moveToBoxName = firstInnerBoxEle.text.split("<")[0]
                    logger.info(moveToBoxName)
                    firstInnerBoxEle.click()
            elif data["boxCategory"] == "自定义箱":
                with allure.step("点击第一个自定义箱"):
                    firstCustomBoxEle = self.find_element(self.emailDetailPage_moveToCustomBoxList_loc,key="获取第一个自定义箱")
                    moveToBoxName = firstCustomBoxEle.text
                    logger.info(moveToBoxName)
                    firstCustomBoxEle.click()
            with allure.step("点击确定按钮"):
                self.click_ele(self.emailDetailPage_sureMoveBtn_loc,key="点击确定移动按钮")
        else:
            moveToBoxName = data["boxCategory"]
        with allure.step("点击关闭邮件详情tab"):
            self.click_ele(self.closeTabBtn,key="关闭邮件详情")
        with allure.step("查看箱子：{}，是否有主题是：{}的邮件".format(moveToBoxName,emailSubject)):
            self.recipientBoxPageCommon.get_emailBySubjectAndBox(email_subject=emailSubject,boxCategory=data["boxCategory"],boxName=moveToBoxName)
        with allure.step("获取移动后邮件的所有信息,并判断是否有丢失"):
            with allure.step("获取移动后邮件的主题"):
                emailSubject_moved = self.emailDetailPageCommon.get_subjectOfEmailDetail()
                logger.info("emailSubject_moved:{}".format(emailSubject_moved))
                if emailSubject_moved != emailSubject:
                    raise Exception("移动后的邮件主题：{}，与移动前的邮件主题：{}，不一致".format(emailSubject_moved,emailSubject))
                else:
                    logger.info("移动前的主题：{}，移动后的主题：{}".format(emailSubject,emailSubject_moved))
            with allure.step("获取移动后邮件发件人"):
                emailSender_moved = self.emailDetailPageCommon.get_senderOfEmailDetail()
                logger.info("emailSender_moved:{}".format(emailSender_moved))
                if emailSender_moved.split("<")[1].split(">")[0] != emailSender.split("<")[1].split(">")[0]:
                    raise Exception("移动后的邮件发件人：{}，与移动前的邮件发件人：{}，不一致".format(emailSender_moved,emailSender))
            with allure.step("获取移动后所有的收件人"):
                emailRecipients_moved = self.emailDetailPageCommon.get_recipientOfEmailDetail()
                logger.info("emailRecipients_moved:{}".format(emailRecipients_moved))
                if emailRecipients_moved != emailRecipients:
                    raise Exception("移动后的邮件收件人：{}，与移动前的邮件收件人：{}，不一致".format(emailRecipients_moved,emailRecipients))
            # with allure.step("获取移动后所有的大附件"):
            #     emailBigAttachNames_moved = self.emailDetailPageCommon.get_allBigAttachNamesOfEmailDetail()
            #     logger.info("emailBigAttachNames_moved:{}".format(emailBigAttachNames_moved))
            #     if emailBigAttachNames_moved != emailBigAttachNames:
            #         raise Exception("移动后的邮件大附件：{}，与移动前的邮件大附件：{}，不一致".format(emailBigAttachNames_moved,emailBigAttachNames))
            with allure.step("获取移动后所有的小附件"):
                emailSmallAttachNames_moved = self.emailDetailPageCommon.get_allSmallAttachNamesOfEmailDetail()
                logger.info("emailSmallAttachNames_moved:{}".format(emailSmallAttachNames_moved))
                if emailSmallAttachNames_moved != emailSmallAttachNames:
                    raise Exception("移动后的邮件小附件：{}，与移动前的邮件小附件：{}，不一致".format(emailSmallAttachNames_moved,emailSmallAttachNames))
            with allure.step("获取移动后邮件文本"):
                emailBody_moved = self.emailDetailPageCommon.get_emailTextOfEmailDetail(index="all")
                logger.info("emailBody_moved:{}".format(emailBody_moved))
                if emailBody_moved != emailBody:
                    raise Exception("移动后的邮件文本：{}，与移动前的邮件文本：{}，不一致".format(emailBody_moved,emailBody))
            with allure.step("获取移动后所有的快照链接"):
                emailSites_moved = self.emailDetailPageCommon.get_allSiteUrlsOfEmailDetail()
                logger.info("emailSites_moved:{}".format(emailSites_moved))
                if emailSites_moved != emailSites:
                    raise Exception("移动后的邮件营销网站快照链接：{}，与移动前的邮件营销网站快照链接：{}，不一致".format(emailSites_moved,emailSites))
            with allure.step("获取移动后所有的产品图片地址,编码"):
                emailProductImgUrls_moved, emailProductCodes_moved = self.emailDetailPageCommon.get_allProductImgUrlsOfEmailDetail()
                logger.info("emailProductImgUrls_moved:{}, emailProductCodes_moved:{}".format(emailProductImgUrls_moved, emailProductCodes_moved))
                if emailProductImgUrls_moved != emailProductImgUrls:
                    raise Exception("移动后的邮件产品图地址：{}，与移动前的邮件产品图地址：{}，不一致".format(emailProductImgUrls_moved,emailProductImgUrls))
                if emailProductCodes_moved != emailProductCodes:
                    raise Exception("移动后的邮件产品编码：{}，与移动前的邮件产品编码：{}，不一致".format(emailProductCodes_moved,emailProductCodes))


    #邮件详情内，上一封，下一封操作
    def run_pageUpAndPageDown_case(self):
        with allure.step("获取前2封邮件主题，并点击第一封邮件"):
            recipientBoxPage_emailSubjects = self.recipientBoxPageCommon.get_emailSubjectAndClick(num=2)
        with allure.step("获取邮件详情内的主题"):
            detailPage_firstEmailSubject = self.emailDetailPageCommon.get_subjectOfEmailDetail()
            if detailPage_firstEmailSubject != recipientBoxPage_emailSubjects[0]:
                raise Exception("详情页面的主题：{}，与收件箱第一封邮件的主题：{}，不一致".format(detailPage_firstEmailSubject,recipientBoxPage_emailSubjects[0]))
        with allure.step("点击左翻页按钮"):
            self.click_ele(self.emailDetailPage_leftTurnPageBtn_loc,key="点击左翻页按钮")
        with allure.step("判断toast提示是否正确"):
            toast_text = self.get_elementText(self.toast_loc,key="获取点击左翻页的toast提示")
            if toast_text != "没有更多邮件了！":
                raise Exception("点击第一封邮件的左翻页按钮，toast提示：{}，不对".format(toast_text))
        with allure.step("点击有翻页按钮"):
            self.click_ele(self.emailDetailPage_rightTurnPageBtn_loc,key="点击右翻页按钮")
        with allure.step("获取邮件详情的内的主题"):
            detailPage_secondEmailSubject = self.emailDetailPageCommon.get_subjectOfEmailDetail()
            if detailPage_secondEmailSubject != recipientBoxPage_emailSubjects[1]:
                raise Exception("详情页面的主题：{}，与收件箱第二封邮件的主题：{}，不一致".format(detailPage_secondEmailSubject,recipientBoxPage_emailSubjects[1]))
        with allure.step("点击左翻页按钮"):
            self.click_ele(self.emailDetailPage_leftTurnPageBtn_loc,key="点击左翻页按钮")
        with allure.step("获取邮件的主题"):
            detailPage_turnedEmailSubject = self.emailDetailPageCommon.get_subjectOfEmailDetail()
            if detailPage_turnedEmailSubject != recipientBoxPage_emailSubjects[0]:
                raise Exception("详情页面的主题：{}，与收件箱第一封邮件的主题：{}，不一致".format(detailPage_turnedEmailSubject,recipientBoxPage_emailSubjects[1]))


    #邮件详情内，查看日志
    def run_checkLog_case(self):
        with allure.step("随机进入一封邮件详情"):
            detailPage_emailSubjects = self.recipientBoxPageCommon.get_emailSubjectAndClick()
        with allure.step("点击更多操作按钮"):
            self.click_ele(self.emailDetailPage_moreOperateBtn_loc,key="点击更多操作")
        with allure.step("点击查看日志按钮"):
            checkLog_loc = (By.XPATH,self.emailDetailPage_mergerBtn_loc[1].replace("归并","查看日志"))
            self.click_ele(checkLog_loc,key="点击查看日志")
        with allure.step("获取日志条数"):
            logEles = self.find_element(self.emailDetailPage_emailLog_loc,index="all")
            logger.info(logEles)
            if len(logEles) < 1:
                self.screenshotImg(key="邮件日志页面截图")
                raise Exception("主题是：{}的邮件，日志不对".format(detailPage_emailSubjects[0]))


    #邮件详情内，删除操作
    '''boxName字段：收件箱，垃圾箱，回收箱'''
    def run_delEmail_case(self,data):
        with allure.step("进入{}的第一封邮件详情"):
            self.recipientBoxPageCommon.get_emailSubjectAndClick(boxName=data["boxName"])
        with allure.step("获取邮件详情内的主题"):
            emailSubject = self.emailDetailPageCommon.get_subjectOfEmailDetail()
        with allure.step("点击删除按钮"):
            self.click_ele(self.emailDetailPage_delBtn_loc,key="点击删除按钮")
        if data["boxName"] == "回收箱":
            self.click_ele(self.emailDetailPage_sureDelBtn_loc,key="点击确认删除按钮")
        with allure.step("获取删除之后的toast提示"):
            toast_text = self.get_elementText(self.toast_loc,key="获取删除后的toast提示")
            if toast_text != "删除成功":
                raise Exception("删除邮件后的toast：{}，不对".format(toast_text))
        with allure.step("获取{}箱子的第一封邮件主题".format(data["boxName"])):
            firstEmailSubject = self.recipientBoxPageCommon.get_emailSubjectAndClick(is_click=0,boxName=data["boxName"])[0]
        with allure.step("判断{}箱子是否还有删除的邮件".format(data["boxName"])):
            if firstEmailSubject == emailSubject:
                raise Exception("已经删除的邮件：{}，仍然存在于{}箱子里面".format(emailSubject,data["boxName"]))
        # 删除后要验证的箱子
        purposeBox = None
        if data["boxName"] == "收件箱":
            purposeBox = "垃圾箱"
            with allure.step("获取垃圾箱中第一封邮件"):
                del_firstEmailSubjects = self.recipientBoxPageCommon.get_emailSubjectAndClick(num=30,is_click=0,boxName="垃圾箱")
        elif data["boxName"] == "垃圾箱":
            purposeBox = "回收箱"
            with allure.step("获取回收箱中第一封邮件"):
                del_firstEmailSubjects = self.recipientBoxPageCommon.get_emailSubjectAndClick(num=30,is_click=0, boxName="回收箱")
        if purposeBox:
            with allure.step("判断{}箱子中是否有刚刚删除的邮件"):
                if emailSubject not in del_firstEmailSubjects:
                    raise Exception("{}箱子中，没有删除的主题是：{}的邮件，该箱子前30封邮件是：{}".format(purposeBox,emailSubject,del_firstEmailSubjects))


    #邮件翻译相关操作
    def run_transEmail_case(self):
        with allure.step("随机进入一封邮件详情"):
            self.recipientBoxPageCommon.get_emailSubjectAndClick()
        with allure.step("获取邮件的主题"):
            emailSubject = self.emailDetailPageCommon.get_subjectOfEmailDetail()
            logger.info("要翻译的邮件主题：{}".format(emailSubject))
        with allure.step("获取邮件文本"):
            emailBody = self.emailDetailPageCommon.get_emailTextOfEmailDetail()
        with allure.step("点击更多操作按钮"):
            self.click_ele(self.emailDetailPage_moreOperateBtn_loc,key="点击更多操作按钮")
        with allure.step("点击翻译按钮"):
            trans_loc = (By.XPATH,self.emailDetailPage_mergerBtn_loc[1].replace("归并","翻译"))
            self.click_ele(trans_loc,key="点击翻译按钮")
        time.sleep(2)
        with allure.step("获取左翻译框里面的文本内容"):
            transText = self.emailDetailPageCommon.get_textOfTransInput()
        with allure.step("判断邮件文本是否带到翻译框"):
            if emailBody not in transText:
                raise Exception("邮件的文本：{}，不在翻译框：{}".format(emailBody,transText))


    #邮件详情内，归并操作，无归并规则
    def run_mergerEmailWithoutMergerRule_case(self,data):
        with allure.step("切换到dmktest_001"):
            self.switch_operator(operator="dmktest_001")
        with allure.step("点击查询箱：{}".format(data["queryBoxName"])):
            self.recipientBoxPageCommon.get_emailBySubjectAndBox(boxName=data["queryBoxName"])
        with allure.step("获取该邮件的主题"):
            emailSubject = self.emailDetailPageCommon.get_subjectOfEmailDetail()
            logger.info("邮件详情内要归并的邮件主题：{}".format(emailSubject))
        with allure.step("点击更多操作按钮"):
            self.click_ele(self.emailDetailPage_moreOperateBtn_loc,key="点击更多操作按钮")
        with allure.step("点击归并按钮"):
            self.click_ele(self.emailDetailPage_mergerBtn_loc,key="点击归并按钮")
        with allure.step("点击确定归并按钮"):
            self.click_ele(self.emailDetailPage_sureBtn_loc,key="点击确定归并按钮")
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc,key="获取toast提示")
        with allure.step("关闭邮件详情tab"):
            self.click_ele(self.closeTabBtn, key="点击关闭邮件详情按钮")
        with allure.step("获取所有的邮件主题"):
            allEmailSubjects = self.recipientBoxPageCommon.get_emailSubjectAndClick(num=50,boxName=data["queryBoxName"],is_click=0)
        if "未建档" in data["queryBoxName"]:
            with allure.step("判断未建档邮件，归并之后的toast提示"):
                if toast_text != "没有可以归并的邮件":
                    raise Exception("归并未建档联系人，toast提示：{}，不对".format(toast_text))
            with allure.step("判断未建档的邮件，是否还在查询箱:{}中".format(data["queryBoxName"])):
                if emailSubject not in allEmailSubjects:
                    raise Exception("未建档联系人的邮件：{}，点击归并后，查询箱：{}，没有了该邮件".format(emailSubject,data["queryBoxName"]))
        else:
            with allure.step("判断已建档邮件，归并之后的toast提示"):
                if toast_text != "操作成功！":
                    raise Exception("归并{}联系人，toast提示：{}，不对".format(data["boxCategory"],toast_text))
            with allure.step("判断未建档的邮件，是否还在查询箱:{}中".format(data["queryBoxName"])):
                if emailSubject in allEmailSubjects:
                    raise Exception("已建档联系人的邮件：{}，点击归并后，查询箱：{}，仍然有该邮件".format(emailSubject,data["queryBoxName"]))
            with allure.step("点击{}中，{}箱子内部是否有主题是：{}的邮件".format(data["boxCategory"],data["purposeBoxName"],emailSubject)):
                self.recipientBoxPageCommon.get_emailBySubjectAndBox(email_subject=emailSubject,boxCategory=data["boxCategory"],boxName=data["purposeBoxName"],is_click=0)

    #邮件详情内，分发操作
    def run_deliveryEmail_case(self):
        with allure.step("随机进入一封邮件详情"):
             self.recipientBoxPageCommon.get_emailBySubjectAndBox()
        with allure.step("获取邮件详情内的主题"):
            num = 0
            while num < 30:
                emailSubject = self.emailDetailPageCommon.get_subjectOfEmailDetail()
                if emailSubject == "系统退信":
                    with allure.step("点击下一封邮件按钮"):
                        self.click_ele(self.emailDetailPage_rightTurnPageBtn_loc,key="点击下一封邮件按钮")
                    num = num + 1
                    time.sleep(2)
                else:
                    emailSubject = self.emailDetailPageCommon.get_subjectOfEmailDetail()
                    logger.info("邮件详情内，要分发的邮件主题：{}".format(emailSubject))
                    break
        with allure.step("点击更多操作按钮"):
            self.click_ele(self.emailDetailPage_moreOperateBtn_loc,key="点击更多操作按钮")
        with allure.step("点击分发按钮"):
            deliveryBtn_loc = (By.XPATH,self.emailDetailPage_mergerBtn_loc[1].replace("归并","分发"))
            self.click_ele(deliveryBtn_loc,key="点击分发按钮")
        with allure.step("点击云基础联系人"):
            self.click_ele(self.emailDetailPage_innerForwardPage_inner_loc,key="选中内部联系人")
        with allure.step("输入分发意见"):
            deliveryText = random_text().replace("\n","")
            self.sendKeys(self.emailDetailPage_innerForwardPage_forwardIdeaInput_loc,key=deliveryText)
        with allure.step("点击确定按钮"):
            self.click_ele(self.emailDetailPage_innerForwardPage_sureBtn_loc,key="点击确定分发按钮")
        with allure.step("判断toast提示是否正确"):
            toast_text = self.get_elementText(self.toast_loc,key="获取toast提示")
            if toast_text != "分发成功！":
                raise Exception("分发成功后的，toast提示：{}，不对".format(toast_text))
        with allure.step("点击关闭邮件详情按钮"):
            self.click_ele(self.closeTabBtn,key="点击关闭邮件详情按钮")
        with allure.step("判断分发后，箱子内是否还有该邮件"):
            allEmailSubjects_currentOperator = self.recipientBoxPageCommon.get_emailSubjectAndClick(num=50,is_click=0)
            logger.info("emailSubject:{}".format(emailSubject))
            logger.info("allEmailSubjects_currentOperator:{}".format(allEmailSubjects_currentOperator))
            if emailSubject in allEmailSubjects_currentOperator:
                raise Exception("邮件：{}，分发后，仍然存在于该业务员".format(emailSubject))
        with allure.step("切换到dmktest_001"):
            self.switch_operator(operator="dmktest_001")
        with allure.step("判断云基础账号是否收到分发的邮件"):
            recipientBoxPage(driver=self.driver).assert_emailSubjectAndForwardIdea(emailSubject, deliveryText)



    #邮件详情内，重发操作
    def run_resendEmail_case(self):
        with allure.step("点击查询箱，主题包含重构，勿动,并进入第一封邮件的详情页面"):
            self.recipientBoxPageCommon.get_emailBySubject(box="主题包含重构，勿动")
        with allure.step("获取邮件的所有信息"):
            with allure.step("获取邮件的主题"):
                emailSubject = self.emailDetailPageCommon.get_subjectOfEmailDetail()
                logger.info("要重发邮件的主题：{}".format(emailSubject))
                if not emailSubject:
                    raise Exception("要重发的邮件没有主题")
            with allure.step("获取邮件发件人"):
                emailSender = self.emailDetailPageCommon.get_senderOfEmailDetail()
                logger.info("要重发邮件的发件人：{}".format(emailSender))
                if not emailSender:
                    raise Exception("要重发的邮件没有发件人")
            with allure.step("获取所有的收件人"):
                emailRecipients = self.emailDetailPageCommon.get_recipientOfEmailDetail()
                logger.info("要重发邮件的收件人：{}".format(emailRecipients))
                if not emailRecipients:
                    raise Exception("要重发的邮件没有收件人")
            # with allure.step("获取所有的大附件"):
            #     emailBigAttachNames = self.emailDetailPageCommon.get_allBigAttachNamesOfEmailDetail()
            #     logger.info("要重发邮件的大附件：{}".format(emailBigAttachNames))
            #     if not emailBigAttachNames:
            #         raise Exception("要重发的邮件没有大附件")
            with allure.step("获取所有的小附件"):
                emailSmallAttachNames = self.emailDetailPageCommon.get_allSmallAttachNamesOfEmailDetail()
                logger.info("要重发邮件的小附件：{}".format(emailSmallAttachNames))
                if not emailSmallAttachNames:
                    raise Exception("要重发的邮件没有小附件")
            with allure.step("获取邮件文本"):
                emailBody = self.emailDetailPageCommon.get_emailTextOfEmailDetail(index="all")
                logger.info("要重发邮件的邮件文本：{}".format(emailBody))
                if not emailBody:
                    raise Exception("要重发的邮件没有邮件文本")
            with allure.step("获取所有的快照链接"):
                emailSites = self.emailDetailPageCommon.get_allSiteUrlsOfEmailDetail()
                logger.info("要重发邮件的营销网站快照：{}".format(emailSites))
                if not emailSites:
                    raise Exception("要重发的邮件没有营销快照")
            with allure.step("获取所有的产品图片地址,编码"):
                emailProductImgUrls, emailProductCodes = self.emailDetailPageCommon.get_allProductImgUrlsOfEmailDetail()
                logger.info("要重发邮件的产品图片地址:{}，编码：{}".format(emailProductImgUrls, emailProductCodes))
                if not emailProductImgUrls:
                    raise Exception("要重发的邮件没有产品图片")
                if not emailProductCodes:
                    raise Exception("要重发的邮件没有产品编码")
        with allure.step("点击更多按钮"):
            self.click_ele(self.emailDetailPage_moreOperateBtn_loc,key="点击更多按钮")
        with allure.step("点击重发按钮"):
            resend_loc = (By.XPATH,self.emailDetailPage_mergerBtn_loc[1].replace("归并","重发"))
            self.click_ele(resend_loc,key="点击重发按钮")
        with allure.step("点击关闭邮件详情tab按钮"):
            self.click_ele(self.closeTabBtn,key="点击关闭详情按钮")
        with allure.step("获取重发后的邮件信息"):
            with allure.step("获取重发后的邮件收件人"):
                emailRecepients_resended = self.writeMailCommon.get_recipientsOfWriteEmailPage()
                logger.info("重发之后的邮件的收件人：{}".format(emailRecepients_resended))
                if emailRecepients_resended[0].split("<")[1].split(">")[0] != emailRecipients[0].split("<")[1].split(">")[0]:
                    raise Exception("重发之后的收件人：{}，与重发之前的收件人：{}，不一致".format(emailRecepients_resended,emailRecipients))
            with allure.step("获取重发后的邮件主题"):
                emailSubject_resended = self.writeMailCommon.get_emailSubjectInSubjectInput()
                logger.info("重发之后的邮件的主题：{}".format(emailSubject_resended))
                if emailSubject_resended != emailSubject:
                    raise Exception("重发之后的主题：{}，与重发之前的主题：{}，不一致".format(emailSubject_resended,emailSubject))
            with allure.step("获取重发后的发件人"):
                emailSender_resended = self.writeMailCommon.get_sendersOfWriteEmailPage()
                logger.info("重发之后的邮件的发件人：{}".format(emailSender_resended))
                # if emailSender_resended != emailSender:
                #     raise Exception("重发之后的发件人：{}，与重发之前的发件人：{}，不一致".format(emailSender_resended,emailSender))
            with allure.step("获取重发后的小附件"):
                emailSmallAttachNames_resended = self.writeMailCommon.get_allAttachNamesOfWriteEmailPage()
                logger.info("重发之后的小附件：{}".format(emailSmallAttachNames_resended))
                if emailSmallAttachNames_resended != emailSmallAttachNames:
                    raise Exception("重发之后的小附件：{}，与重发之前的小附件：{}，不一致".format(emailSmallAttachNames_resended,emailSmallAttachNames))
            with allure.step("获取重发后的邮件文本"):
                emailBody_resended = self.writeMailCommon.get_emailBodyOfWriteEmailPage()
                logger.info("重发之后的邮件文本：{}".format(emailBody_resended))
                if emailBody_resended != emailBody:
                    raise Exception("重发之后的邮件文本：{}，与重发之前的邮件文本：{}，不一致".format(emailBody_resended,emailBody))
            with allure.step("获取重发后的产品图片地址，编码"):
                emailProductImgUrls_resended, emailProductCodes_resended = self.writeMailCommon.get_productInfoOfWriteEmailPage()
                logger.info("重发之后的邮件产品图片地址：{}，编码：{}".format(emailProductImgUrls_resended, emailProductCodes_resended))
                if emailProductImgUrls_resended != emailProductImgUrls:
                    raise Exception("重发之后的产品图片地址：{}，与重发之前的产品图片地址：{}，不一致".format(emailProductImgUrls_resended,emailProductImgUrls))
                if emailProductCodes_resended != emailProductCodes:
                    raise Exception("重发之后的产品编码：{}，与重发之前的产品编码：{}，不一致".format(emailProductCodes_resended,emailProductCodes))
            with allure.step("获取重发后的邮件快照地址"):
                emailSites_resended = self.writeMailCommon.get_sitesOfWriteEmailPage()
                logger.info("重发之后的邮件快照地址：{}".format(emailSites_resended))
                if emailSites_resended != emailSites_resended:
                    raise Exception("重发之后的营销快照地址：{}，与重发之前的营销快照地址：{}，不一致".format(emailSites_resended,emailSites))
            # with allure.step("获取重发后的所有大附件"):
            #     emailBigAttachNames_resended = self.writeMailCommon.get_allBigAttachNamesOfWriteEmailPage()
            #     logger.info("重发之后的大附件：{}".format(emailBigAttachNames_resended))
            #     if emailBigAttachNames_resended != emailBigAttachNames:
            #         raise Exception("重发之后的大附件：{}，与重发之前的大附件：{}，不一致".format(emailBigAttachNames_resended,emailBigAttachNames))


    #邮件详情内，重新生成操作
    def run_reGenerateEmail_case(self):
        with allure.step("随机进入一封邮件详情"):
            self.recipientBoxPageCommon.get_emailBySubjectAndBox()
        with allure.step("获取邮件主题"):
            emailSubject = self.emailDetailPageCommon.get_subjectOfEmailDetail()
            logger.info("重新生成操作的邮件主题：{}".format(emailSubject))
        with allure.step("点击更多操作按钮"):
            self.click_ele(self.emailDetailPage_moreOperateBtn_loc,key="点击更多操作按钮")
        with allure.step("点击重新生成按钮"):
            reGenerateBtn_loc = (By.XPATH,self.emailDetailPage_mergerBtn_loc[1].replace("归并","重新生成"))
            self.click_ele(reGenerateBtn_loc,key="点击重新生成按钮")
        with allure.step("获取toast提示，并判断是否正确"):
            toast_text = self.get_elementText(self.toast_loc,key="获取重新生成后的toast提示")
            if toast_text != "执行成功，邮件已经重新从邮局导入":
                raise Exception("邮件详情内，点击重新生成后，toast提示：{}，不对".format(toast_text))


    #邮件详情内，导出操作
    def run_exportEmail_case(self):
        with allure.step("随机进入一封邮件详情"):
            self.recipientBoxPageCommon.get_emailBySubjectAndBox()
        with allure.step("获取邮件主题"):
            emailSubject = self.emailDetailPageCommon.get_subjectOfEmailDetail()
            logger.info("要导出的邮件主题：{}".format(emailSubject))
        with allure.step("获取句柄的个数"):
            hanler_num = len(self.driver.window_handles)
        with allure.step("点击更多操作按钮"):
            self.click_ele(self.emailDetailPage_moreOperateBtn_loc,key="点击更多操作按钮")
        with allure.step("点击导出按钮"):
            reGenerateBtn_loc = (By.XPATH,self.emailDetailPage_mergerBtn_loc[1].replace("归并","导出"))
            self.click_ele(reGenerateBtn_loc,key="点击导出按钮")
        time.sleep(3)
        with allure.step("获取导出之后的句柄个数"):
            hanler_num_exported = len(self.driver.window_handles)
            if hanler_num != hanler_num_exported != 1:
                self.screenshotImg(key="点击导出按钮")
                raise Exception("点击导出之后，出现了新的窗口")


    #邮件详情内，存为模板
    def run_saveTemplate_case(self):
        with allure.step("随机进入一封邮件详情"):
            self.recipientBoxPageCommon.get_emailBySubjectAndBox()
        with allure.step("获取邮件主题"):
            emailSubject = self.emailDetailPageCommon.get_subjectOfEmailDetail()
            logger.info("要存模板的邮件主题：{}".format(emailSubject))
        with allure.step("点击更多操作按钮"):
            self.click_ele(self.emailDetailPage_moreOperateBtn_loc,key="点击更多操作按钮")
        with allure.step("点击存模板按钮"):
            reGenerateBtn_loc = (By.XPATH,self.emailDetailPage_mergerBtn_loc[1].replace("归并","存为模板"))
            self.click_ele(reGenerateBtn_loc,key="点击存为模板按钮")
        with allure.step("点击保存按钮"):
            self.click_ele(self.emailDetailPage_saveTemplateBtn_loc,key="点击保存模板按钮")
        with allure.step("判断是否有toast提示"):
            toast_text = ""
            if self.is_element_exist(self.toast_loc[1]):
                toast_text = self.get_elementText(self.toast_loc, key="获取toast提示")
                if toast_text != "转存成功":
                    raise Exception("存模板的toast：{}，不对".format(toast_text))
        if not toast_text:
            with allure.step("判断是否有确定按钮,有则点击"):
                if self.is_element_exist(self.emailDetailPage_sureDelBtn_loc[1]):
                    self.click_ele(self.emailDetailPage_sureDelBtn_loc,key="点击确认保存按钮")
            with allure.step("获取toast提示"):
                toast_text = self.get_elementText(self.toast_loc,key="获取toast提示")
                if toast_text != "转存成功":
                    raise Exception("存模板的toast：{}，不对".format(toast_text))
        with allure.step("判断邮箱设置，模板设置是否有转存的模板"):
            with allure.step("获取所有的模板名"):
                emailTemplateNames = self.mailSettingPageEmailTemplatePageCommon.get_emailTemplateNames()
            with allure.step("判断保存的模板名是否在邮件模板中"):
                if emailSubject not in emailTemplateNames:
                    raise Exception("保存的模板：{}，不在邮件模板中：{}".format(emailSubject,emailTemplateNames))
                if emailTemplateNames.count(emailSubject) != 1:
                    raise Exception("保存的模板名有重复：{}".format(emailTemplateNames))


    #邮件详情内，标记垃圾邮件
    def run_markRubbishEmail_case(self,caseid,casename,data):
        with allure.step("切换到dmktest_001"):
            self.switch_operator(operator="dmktest_001")
        with allure.step("进入{}箱子的第一封邮件".format(data["boxName"])):
            self.recipientBoxPageCommon.get_emailBySubjectAndBox(boxName=data["boxName"])
        with allure.step("获取邮件主题和收件人"):
            emailSubject = self.emailDetailPageCommon.get_subjectOfEmailDetail()
            emailSender = self.emailDetailPageCommon.get_senderOfEmailDetail()
            logger.info("用例-{}-{}：要标记垃圾的邮件主题：{}".format(caseid,casename,emailSubject))
        with allure.step("点击更多操作按钮"):
            self.click_ele(self.emailDetailPage_moreOperateBtn_loc,key="点击更多操作按钮")
        with allure.step("点击标记为垃圾邮件"):
            markRubbishBtn_loc = (By.XPATH,self.emailDetailPage_mergerBtn_loc[1].replace("归并","标为垃圾邮件"))
            self.click_ele(markRubbishBtn_loc,key="点击标为垃圾邮件按钮")
        with allure.step("点击确定标记按钮"):
            self.click_ele(self.emailDetailPage_innerForwardPage_sureBtn_loc,key="点击确定标记按钮")
        with allure.step("获取toast提示"):
            toast_text = self.get_elementText(self.toast_loc,key="获取标记垃圾邮件的toast提示")
            if "未建档" in data["boxName"]:
                if toast_text != "标记成功！":
                    raise Exception("未建档联系人邮件标记垃圾邮件的toast：{}，不对".format(toast_text))
                with allure.step("进入垃圾箱子查看是否还有邮件"):
                    with allure.step("关闭邮件详情"):
                        self.click_ele(self.closeTabBtn, key="点击关闭邮件详情按钮")
                    with allure.step("判断垃圾箱子内是否有邮件主题：{}的邮件".format(emailSubject)):
                        if not self.recipientBoxPageCommon.is_existEmailOfBox(email_subject=emailSubject,boxName="垃圾箱"):
                            raise Exception("垃圾箱中没有标记垃圾邮件的邮件：{}".format(emailSubject))
                with allure.step("查看邮箱设置里面，黑名单是否有标记垃圾的邮箱账号"):
                    blackLists = self.mailSettingPageBlackListPageCommon.get_blackList()
                    if "<" in emailSender:
                        emailSender = emailSender.split("<")[1].split(">")[0]
                    if emailSender not in blackLists:
                        raise Exception("标记垃圾邮件的邮箱账号：{}，不在黑名单列表中：{}".format(emailSender,blackLists))
            else:
                if "不允许加入黑名单" not in toast_text:
                    raise Exception("内部联系人邮件标记垃圾邮件的toast：{}，不对".format(toast_text))


    #邮件详情内，跟进按钮展示
    def run_showFollowBtn_case(self,caseid,casename,data):
        with allure.step("切换到dmktest_001"):
            self.switch_operator(operator="dmktest_001")
        with allure.step("进入{}箱子的第一封邮件".format(data["boxName"])):
            self.recipientBoxPageCommon.get_emailBySubjectAndBox(boxName=data["boxName"])
        with allure.step("获取邮件主题和收件人"):
            emailSubject = self.emailDetailPageCommon.get_subjectOfEmailDetail()
            logger.info("用例-{}-{}：要跟进的邮件主题：{}".format(caseid,casename,emailSubject))
        with allure.step("点击更多操作按钮"):
            self.click_ele(self.emailDetailPage_moreOperateBtn_loc,key="点击更多操作按钮")
        time.sleep(2)
        with allure.step("判断{}里面的邮件详情内，是否有跟进按钮"):
            followBtn_loc = (By.XPATH,self.emailDetailPage_mergerBtn_loc[1].replace("归并","跟进"))
            if "客户" in data["boxName"] or "供应商" in data["boxName"]:
                if not self.is_element_exist(followBtn_loc[1]):
                    raise Exception("{}箱子里面的邮件详情,没有跟进按钮".format(data["boxName"]))
            else:
                if self.is_element_exist(followBtn_loc[1]):
                    raise Exception("{}箱子里面的邮件详情,有跟进按钮".format(data["boxName"]))


    #邮件详情内，标记邮件
    def run_markEmail_case(self,caseid,casename):
        # if caseid == 1:
        #     with allure.step("获取未读邮件数"):
        #         '''首页未读邮件数'''
        #         unReadEmail_num_v1 = self.recipientBoxPageCommon.get_unReadEmailNum()
        if caseid == 2:
            with allure.step("获取星标邮件数"):
                '''首页星标邮件数'''
                starEmail_num_v1 = self.recipientBoxPageCommon.get_starEmailNum()
        elif caseid == 3:
            with allure.step("获取免回复邮件数"):
                freeReplyEmail_num_v1 = self.recipientBoxPageCommon.get_freeReplyEmailNum()
        with allure.step("进入收件箱的第一封邮件"):
            self.recipientBoxPageCommon.get_emailBySubjectAndBox()
        with allure.step("获取邮件主题"):
            emailSubject = self.emailDetailPageCommon.get_subjectOfEmailDetail()
            logger.info("用例-{}-{}：要标记的邮件主题：{}".format(caseid,casename,emailSubject))
        if caseid == 1:
            with allure.step("回到邮件首页"):
                self.click_ele(self.emailHomePage_loc, key="点击邮件首页")
            with allure.step("获取未读邮件数，并判断是否正确"):
                '''点击一封未读邮件后，首页未读邮件数'''
                unReadEmail_num_v2 = self.recipientBoxPageCommon.get_unReadEmailNum()
                # assert int(unReadEmail_num_v1) == int(unReadEmail_num_v2)+1
            with allure.step("回到邮件详情tab"):
                self.click_ele(self.emailDetailPage_detailTabBtn_loc,key="回到邮件详情tab")
        with allure.step("点击更多操作按钮"):
            self.click_ele(self.emailDetailPage_moreOperateBtn_loc,key="点击更多操作按钮")
        time.sleep(1)
        with allure.step("悬浮标记为按钮"):
            self.mouseHover(self.emailDetailPage_moreOperateMarkBtn_loc)
        if caseid == 1:
            self.click_ele(self.emailDetailPage_moreOperateList_loc,key="点击未读按钮")
        elif caseid == 2:
            self.click_ele(self.emailDetailPage_moreOperateList_loc,index=1,key="点击星标按钮")
        elif caseid == 3:
            self.click_ele(self.emailDetailPage_moreOperateList_loc,index=2,key="点击免回复按钮")
        with allure.step("回到邮件首页"):
            self.click_ele(self.emailHomePage_loc,key="点击邮件首页")
        if caseid == 1:
            with allure.step("获取未读邮件数"):
                unReadEmail_num_v3 = self.recipientBoxPageCommon.get_unReadEmailNum()
                assert int(unReadEmail_num_v3) == int(unReadEmail_num_v2) + 1
        elif caseid == 2:
            with allure.step("获取星标邮件数"):
                starEmail_num_v2 = self.recipientBoxPageCommon.get_starEmailNum()
                assert int(starEmail_num_v2) == int(starEmail_num_v1) + 1
        elif caseid == 3:
            with allure.step("获取免回复邮件数"):
                freeReplyEmail_num_v2 = self.recipientBoxPageCommon.get_freeReplyEmailNum()
                assert int(freeReplyEmail_num_v2) == int(freeReplyEmail_num_v1) + 1
        with allure.step("回到邮件详情"):
            self.click_ele(self.emailDetailPage_detailTabBtn_loc,key="点击邮件详情tab")
        with allure.step("点击更多操作按钮"):
            self.click_ele(self.emailDetailPage_moreOperateBtn_loc,key="点击更多操作按钮")
        time.sleep(1)
        with allure.step("悬浮标记为按钮"):
            self.mouseHover(self.emailDetailPage_moreOperateMarkBtn_loc)
        if caseid == 1:
            self.click_ele(self.emailDetailPage_moreOperateList_loc,key="点击已读按钮")
        elif caseid == 2:
            self.click_ele(self.emailDetailPage_moreOperateList_loc,index=1,key="点击取消星标按钮")
        elif caseid == 3:
            self.click_ele(self.emailDetailPage_moreOperateList_loc,index=2,key="点击取消免回复按钮")
        with allure.step("回到邮件首页"):
            self.click_ele(self.emailHomePage_loc,key="点击邮件首页")
        if caseid == 1:
            with allure.step("获取未读邮件数"):
                unReadEmail_num_v4 = self.recipientBoxPageCommon.get_unReadEmailNum()
                assert int(unReadEmail_num_v4) == int(unReadEmail_num_v2)
        elif caseid == 2:
            with allure.step("获取星标邮件数"):
                starEmail_num_v3 = self.recipientBoxPageCommon.get_starEmailNum()
                assert int(starEmail_num_v3) == int(starEmail_num_v1)
        elif caseid == 3:
            with allure.step("获取免回复邮件数"):
                freeReplyEmail_num_v3 = self.recipientBoxPageCommon.get_freeReplyEmailNum()
                assert int(freeReplyEmail_num_v3) == int(freeReplyEmail_num_v1)


    #邮件详情内，预览文件
    def run_previewFile_case(self,caseid,casename,data):
        with allure.step("进入主题包含重构，勿动箱子的第一封邮件"):
            self.recipientBoxPageCommon.get_emailBySubjectAndBox(boxName="主题包含重构，勿动")
        with allure.step("获取邮件主题"):
            emailSubject = self.emailDetailPageCommon.get_subjectOfEmailDetail()
            logger.info("用例-{}-{}：要标记的邮件主题：{}".format(caseid,casename,emailSubject))
        with allure.step("预览{}文件".format(data["fileType"])):
            previewBtn_loc = (By.XPATH,self.emailDetailPage_previewPDFBtn_loc[1].replace("pdf",data["fileType"]))
            self.click_ele(previewBtn_loc,key="点击预览{}按钮".format(data["fileType"]))
            time.sleep(5)
        if caseid != 3:
            with allure.step("切换到预览的窗口"):
                try:
                    all_h = self.driver.window_handles
                    self.driver.switch_to.window(all_h[1])
                    time.sleep(2)
                    file_source = self.driver.page_source
                except Exception as e:
                    logger.info("切换窗口的时候报错：{}".format(e))
                finally:
                    self.driver.close()
                    self.driver.switch_to.window(all_h[0])
            if caseid == 1:
                with allure.step("判断文件类型是否是pdf"):
                    assert "application/pdf" in file_source
                    assert "attach.ceshi.joinf.com" or "aliyuncs.com" in file_source
            elif caseid == 2:
                with allure.step("判断源码中是否有Date，FROM，TOTAL"):
                    assert "attach.ceshi.joinf.com" or "aliyuncs.com" in file_source
                    assert "wacframe" in file_source
        else:
            with allure.step("获取预览之后的图片地址"):
                previewedImgEle = self.find_element(self.emailDetailPage_previewedImg_loc,key="获取预览之后的图片")
                previewedImgEle_attr = previewedImgEle.get_attribute("src")
                assert ("com" in previewedImgEle_attr,"previewedImgEle_attr:{}".format(previewedImgEle_attr))

    #邮件详情内，相关邮件
    def run_relatedEmail_case(self):
        with allure.step("进入收件箱的第一封邮件"):
            self.recipientBoxPageCommon.get_emailBySubjectAndBox()
        with allure.step("获取邮件主题和收件人"):
            emailSubject = self.emailDetailPageCommon.get_subjectOfEmailDetail()
            logger.info("要查询相关邮件的邮件主题：{}".format(emailSubject))
        with allure.step("点击更多操作按钮"):
            self.click_ele(self.emailDetailPage_moreOperateBtn_loc,key="点击更多操作按钮")
        with allure.step("点击相关邮件"):
            relatedEmailBtn_loc = (By.XPATH,self.emailDetailPage_mergerBtn_loc[1].replace("归并","相关邮件"))
            self.click_ele(relatedEmailBtn_loc,key="点击相关邮件按钮")
        time.sleep(1)
        with allure.step("判断是否有相关邮件tab"):
            if not self.is_element_exist(self.emailDetailPage_relatedEmailBtn_loc[1]):
                self.screenshotImg(key="邮件详情内点击相关邮件")
                raise Exception("未找到相关邮件tab按钮")
        with allure.step("判断相关邮件数量"):
            if len(self.find_element(self.emailDetailPage_relatedEmailList_loc,index="all")) < 1:
                self.screenshotImg(key="邮件详情内点击相关邮件")
                raise Exception("相关邮件数量最低是1，此时却没有相关邮件")


    #邮件详情内，下载附件
    def run_downloadAttach_case(self,caseid,casename):
        with allure.step("进入收件箱的第一封邮件"):
            self.recipientBoxPageCommon.get_emailBySubjectAndBox(boxName="主题包含重构，勿动")
        with allure.step("获取邮件主题和收件人"):
            emailSubject = self.emailDetailPageCommon.get_subjectOfEmailDetail()
            logger.info("用例-{}-{}的邮件主题：{}".format(caseid,casename,emailSubject))
        with allure.step("清空下载文件夹"):
            if not os.path.exists(DOWNLOAD_PATH):
                os.mkdir(DOWNLOAD_PATH)
            else:
                shutil.rmtree(DOWNLOAD_PATH)
                os.mkdir(DOWNLOAD_PATH)
        if caseid == 3:
            with allure.step("获取所有的大附件"):
                bigAttachNames = self.emailDetailPageCommon.get_allBigAttachNamesOfEmailDetail()
        else:
            with allure.step("获取所有的小附件"):
                smallAttachNames = self.emailDetailPageCommon.get_allSmallAttachNamesOfEmailDetail()
                print("smallAttachNames:{}".format(smallAttachNames))
        if caseid == 1:
            with allure.step("点击第一个下载按钮"):
                self.click_ele(self.emailDetailPage_downloadSmallAttachBtn_loc,key="点击下载按钮")
        elif caseid == 2:
            with allure.step("点击打包下载按钮"):
                self.click_ele(self.emailDetailPage_downloadAllBtn_loc,key="点击打包下载按钮")
        elif caseid == 3:
            with allure.step("点击大附件进行下载"):
                try:
                    self.switch_frame(self.emailBodyFrame_loc)
                    self.click_ele(self.emailDetailPage_bigAttachName_loc,key="点击大附件")
                except Exception as e:
                    logger.info("点击邮件详情中的大附件报错：{}".format(e))
                finally:
                    self.switch_parentFrame()
        time.sleep(10)
        with allure.step("获取所有的文件名"):
            downloadFiles = []
            for root,dir,files in os.walk(DOWNLOAD_PATH):
                downloadFiles = files
            print(downloadFiles)
        if caseid == 1:
            with allure.step("判断下载的文件数是否是1"):
                assert len(downloadFiles) == 1
            with allure.step("判断下载的文件是不是第一个附件"):
                assert downloadFiles[0] == smallAttachNames[0]
        elif caseid == 2:
            suffixes = []
            for file in downloadFiles:
                if "crdownload" in file:
                    suffixes.append("crdownload")
                    break
            if len(suffixes) == 0:
                assert downloadFiles[0] == emailSubject.replace(":","_")+".zip"
            else:
                with allure.step("由于文件中有需要确认安全的文件，拿不到确切的文件名，所以判断个数是否一致"):
                    assert len(downloadFiles) == len(smallAttachNames)
        elif caseid == 3:
            with allure.step("判断下载的大附件是否正确"):
                assert downloadFiles == bigAttachNames