# -*- encoding: utf-8 -*-
'''
@File    :   writeMailPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/14 0014 14:06   dmk      1.0         None
'''

import allure,time,traceback,os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.log import logger
from utils.config import IMAGE_PATH
from utils.config import ATTACH_PATH
from utils.generator import *
from pageObject.basePage import Action
from .writeMailPage_loc import writeMailPageLoc
from .writeMailCommon import writeMailCommon
from pageObject.recipientBoxPage.recipientBoxPage import recipientBoxPage


class writeMailPage(Action,writeMailPageLoc):


    def __init__(self,driver):
        super(writeMailPage,self).__init__(driver)
        #进入写信页面
        self.find_element(self.writeEmailBtn_loc).click()
        time.sleep(3)
        self.writeMailCommon = writeMailCommon(driver)


    #写信页面新建签名
    def run_writeMailPageAddSignature_case(self):
        with allure.step("悬浮插入签名按钮"):
            #悬浮插入签名按钮
            self.mouseHover(self.writeMailPage_insertSignatureBtn_loc)
        time.sleep(1)
        with allure.step("点击新建签名按钮"):
            #点击插入签名按钮
            self.find_element(self.writeMailPage_addSignatureBtn_loc).click()
        with allure.step("判断是否跳转到设置页面"):
            #判断是否跳转到设置页面
            if self.find_element(self.settingPage_selectedOption_loc).text != "签名设置":
                self.screenshotImg(key="写信页面点击新增签名")
                raise Exception("写邮件页面点击新增签名，未跳转到新建签名设置页面")

    #写信页面最近联系人显示
    def run_writeMailPageShowRecentContacts_case(self,recipient,subject):
        self.sendEmail(recipient,subject,sender="fttx222@aliyun.com")
        with allure.step("进入写信页面"):
            self.find_element(self.writeEmailBtn_loc).click()
        with allure.step("光标点击收件人输入框"):
            time.sleep(0.5)
            self.find_element(self.writeMailPage_recipientInput_loc).click()
        with allure.step("获取收件人输入框下的最近联系人列表"):
            recipient_recentContactList = self.get_elementText(self.writeMailPage_recentContactList_loc,index="all")
        with allure.step("断言最近联系人是否有刚刚发送邮件的邮箱地址"):
            if recipient not in recipient_recentContactList:
                self.screenshotImg(key="最近联系人列表截图")
                logger.info("收件人下的最近联系人列表：{}".format(recipient_recentContactList))
                raise Exception("刚刚发送的收件人：{}，没有出现在最近联系人列表：{}，请排查".format(recipient,recipient_recentContactList))
        with allure.step("光标点击抄送人输入框"):
            self.find_element(self.writeMailPage_ccSendEmailBtn_loc).click()
            self.find_element(self.writeMailPage_ccInput_loc).click()
        with allure.step("获取抄送人输入框下的最近联系人列表"):
            cc_recentContactList = self.get_elementText(self.writeMailPage_recentContactList_loc,index="all")
        with allure.step("断言最近联系人是否有刚刚发送邮件的邮箱地址"):
            if recipient not in cc_recentContactList:
                self.screenshotImg(key="最近联系人列表截图")
                logger.info("抄送人下的最近联系人列表：{}".format(cc_recentContactList))
                raise Exception("刚刚发送的收件人：{}，没有出现在最近联系人列表：{}，请排查".format(recipient,cc_recentContactList))
        with allure.step("光标点击密送人输入框"):
            self.find_element(self.writeMailPage_bcSendEmailBtn_loc).click()
            self.find_element(self.writeMailPage_bcInput_loc).click()
        with allure.step("获取密送人输入框下的最近联系人列表"):
            bc_recentContactList = self.get_elementText(self.writeMailPage_recentContactList_loc,index="all")
        with allure.step("断言最近联系人是否有刚刚发送邮件的邮箱地址"):
            if recipient not in bc_recentContactList:
                self.screenshotImg(key="最近联系人列表截图")
                logger.info("密送人下的最近联系人列表：{}".format(recipient_recentContactList))
                raise Exception("刚刚发送的收件人：{}，没有出现在最近联系人列表：{}，请排查".format(recipient,bc_recentContactList))
        with allure.step("按下esc键，判断最近联系人下拉框是否会消失"):
            self.find_element(self.writeMailPage_bcInput_loc).send_keys(Keys.ESCAPE)
            time.sleep(0.5)
            if self.is_element_exist(self.writeMailPage_recentContactList_loc[1]):
                self.screenshotImg(key="按esc后的最近联系人列表截图")
                raise Exception("按esc后，最近联系人列表未消失")


    #写信页面发送一封邮件
    def sendEmail(self,recipient,subject,cc=None,bc=None,sender=None):
        if recipient:
            with allure.step("输入收件人"):
                self.find_element(self.writeMailPage_recipientInput_loc).send_keys(recipient)
        if cc:
            with allure.step("点击抄送按钮"):
                self.find_element(self.writeMailPage_ccSendEmailBtn_loc).click()
            with allure.step("输入抄送人"):
                self.find_element(self.writeMailPage_ccInput_loc).send_keys(cc)
        if bc:
            with allure.step("点击密送按钮"):
                self.find_element(self.writeMailPage_bcSendEmailBtn_loc).click()
            with allure.step("输入密送人"):
                self.find_element(self.writeMailPage_bcInput_loc).send_keys(bc)
        with allure.step("输入主题"):
            subject = random_name()+subject+time.strftime("%Y%m%d.%H.%M.%S")
            self.find_element(self.writeMailPage_emailSubjectInput_loc).send_keys(subject)
        with allure.step("输入邮件内容"):
            try:
                self.switch_frame(self.emailEditFrame_loc)
                self.find_element(self.emailBodyInEmailEdit_loc).send_keys(random_text())
            except Exception as e:
                traceback.print_exc()
            finally:
                self.switch_parentFrame()
        # if sender:
        #     with allure.step("点击发件人选择框"):
        #         self.find_element(self.writeMailPage_senderInput_loc).click()
        #     with allure.step("选择指定的发件人"):
        #         sender_loc = (By.XPATH,'//div[@x-placement="top-start"]//span[text()="{}"]'.format(sender))
        #         self.find_element(sender_loc).click()
        #         self.find_element()
        with allure.step("选择发件人"):
            self.writeMailCommon.select_sender(sender=sender)
        with allure.step("点击发送按钮"):
            self.find_element(self.writeMailPage_sendEmailBtn_loc).click()
            time.sleep(2)

    #写信页面，重新编辑收件人
    def run_editRecipientAgain_case(self,is_valid):
        if is_valid:
            emailAccount = random_email()
        else:
            emailAccount = random_email().split("@")[0]
        with allure.step("输入收件邮箱账号：{}".format(emailAccount)):
            self.find_element(self.writeMailPage_recipientInput_loc).send_keys(emailAccount)
        with allure.step("点击抄送按钮，使刚刚输入的收件账号变成完整状态"):
            self.find_element(self.writeMailPage_ccSendEmailBtn_loc).click()
        with allure.step("双击已输入的收件账号"):
            self.mouseDoubleClick(self.writeMailPage_recipientList_loc)
        with allure.step("获取双击后的收件账号"):
            edited_emailAccount = self.find_element(self.writeMailPage_recipientList_loc).text
        logger.info(edited_emailAccount)
        if emailAccount not in edited_emailAccount:
            raise Exception("原账号是：{}，双击后，账号是：{}，不一致，请排查".format(emailAccount,edited_emailAccount))


    #写信页面，保存纯文本草稿
    def run_savePureEmailDraft_case(self,is_pure):
        time.sleep(2)
        with allure.step("判断首次进入写邮件页面，纯文本是否选中"):
            pureTextLabelAttribute_init = self.find_element(self.writeMailPage_pureTextBtn_loc).get_attribute("class")
            if "is-checked" in pureTextLabelAttribute_init:
                raise Exception("首次进入写邮件页面，纯文本按钮不应该选中")
        if is_pure:
            with allure.step("点击纯文本按钮"):
                self.find_element(self.writeMailPage_pureTextBtn_loc).click()
            with allure.step("点击纯文本取消按钮"):
                self.find_element(self.writeMailPage_cancelPureTextBtn_loc).click()
            time.sleep(1)
            with allure.step("判断纯文本是否选中"):
                pureTextLabelAttribute_init = self.find_element(self.writeMailPage_pureTextBtn_loc).get_attribute("class")
                if "is-ckecked" in pureTextLabelAttribute_init:
                    raise Exception("选中取消按钮后，纯文本框不应该被选中")
            with allure.step("再次点击纯文本选择框"):
                self.find_element(self.writeMailPage_pureTextBtn_loc).click()
            with allure.step("点击纯文本确定按钮"):
                self.find_element(self.writeMailPage_surePureTextBtn_loc).click()
            time.sleep(1)
            with allure.step("判断纯文本选择框是否被选中"):
                pureTextLabelAttribute_init = self.find_element(self.writeMailPage_pureTextBtn_loc).get_attribute("class")
                if "is-checked" not in pureTextLabelAttribute_init:
                    raise Exception("选中驱动按钮后，纯文本框应该被选中")
            with allure.step("判断产品是否可以点击"):
                insertProductBtnEle = self.find_element(self.writeMailPage_insertProductBtn_loc)
                logger.info(insertProductBtnEle.get_attribute("title"))
                if insertProductBtnEle.get_attribute("title") != "纯文本状态下无法使用":
                    raise Exception("纯文本场景下，产品按钮不应该是可点击状态")
            with allure.step("判断营销网站是否可以点击"):
                insertProductBtnEle = self.find_element(self.writeMailPage_insertSiteBtn_loc)
                if insertProductBtnEle.get_attribute("title") != "纯文本状态下无法使用":
                    raise Exception("纯文本场景下，营销网站按钮不应该是可点击状态")
            with allure.step("判断邮件模板是否可以点击"):
                insertProductBtnEle = self.find_element(self.writeMailPage_insertMailTemplateBtn_loc)
                if insertProductBtnEle.get_attribute("title") != "纯文本状态下无法使用":
                    raise Exception("纯文本场景下，邮件模板按钮不应该是可点击状态")
            with allure.step("点击上传附件下拉按钮"):
                self.find_element(self.writeMailPage_attachPullDownBtn_loc).click()
            time.sleep(1)
            with allure.step("上传一个普通附件"):
                smallAttachPath = os.path.join(ATTACH_PATH,'5648215.jpg')
                self.find_element_byPresence(self.writeMailPage_smallAttachInput_loc).send_keys(smallAttachPath)
            with allure.step("上传一个超大附件"):
                bigAttachPath = os.path.join(ATTACH_PATH,'backend.zip')
                self.find_element_byPresence(self.writeMailPage_bigAttachInput_loc).send_keys(bigAttachPath)
            with allure.step("邮件编辑器中输入随机文本"):
                emailContent = random_text().replace("\n","")
                self.find_element(self.writeMailPage_pureTextEdit_loc).send_keys(emailContent)
            with allure.step("点击保存草稿"):
                self.find_element(self.writeMailPage_saveDraftBtn_loc).click()
            # with allure.step("回到邮件首页"):
            #     self.find_element(self.emailHomePage_loc).click()
            time.sleep(3)
            with allure.step("关闭写邮件tab"):
                self.find_element(self.writeMailPage_closeTabBtn_loc).click()
            time.sleep(0.5)
            with allure.step("点击草稿箱"):
                self.find_element(self.draftBox_loc).click()
            with allure.step("点击第一封草稿"):
                # self.find_element(self.recipientBoxPage_emailSubject_loc).click()
                self.click_ele(self.recipientBoxPage_emailSubject_loc)
            with allure.step("获取附件名,并断言"):
                allAttachName = self.get_elementText(self.writeMailPage_attachName_loc,index="all")
                if "5648215.jpg" not in allAttachName or "backend.zip" not in allAttachName:
                    raise Exception("保存草稿后，附件丢失，保存后的附件：{}".format(allAttachName))
            with allure.step("判断纯文本框是否被勾选"):
                if "is-checked" not in self.find_element(self.writeMailPage_pureTextBtn_loc).get_attribute("class"):
                    raise Exception("保存草稿后，纯文本框没有被选中")
            with allure.step("获取保存草稿后的邮件文本"):
                draftContent = self.find_element(self.writeMailPage_pureTextEdit_loc).get_attribute("value").replace("\n","")
                if emailContent not in draftContent:
                    raise Exception("存草稿前的文本：{}，与存草稿后的文本：{}，不一样".format(emailContent,draftContent))


    #写信页面，保存富文本草稿
    def run_saveEmailDraft_case(self,data):
        with allure.step("输入邮件内容"):
            email_text = self.writeMailCommon.send_emailContent()
            logger.info("输入的邮件文本:{}".format(email_text))
        with allure.step("上传附件"):
            smallAttach = ['5648215.jpg']
            bigAttach = ['backend.zip']
            self.writeMailCommon.upload_attach(smallAttach,bigAttach)
        with allure.step("输入收件人"):
            random_recepient = random_email()
            self.sendKeys(self.writeMailPage_recipientInput_loc,key=random_recepient)
        with allure.step("输入主题"):
            emailSubject = random_name() + "--富文本草稿测试--" + time.strftime("%Y%m%d.%H.%M.%S")
            self.sendKeys(self.writeMailPage_emailSubjectInput_loc,key=emailSubject)
        with allure.step("插入标签"):
            insertedmark_text = self.writeMailCommon.insert_mark()
        if data["is_timeSend"]:
            with allure.step("开启定时发送"):
                with allure.step("点击定时发送按钮"):
                    self.click_ele(self.writeMailPage_timedSendBtn_loc)
                with allure.step("获取要定时的时间"):
                    setted_time = self.get_elementText(self.writeMailPage_setTimePage_settedTime_loc)
                with allure.step("点击确定定时发送按钮"):
                    self.click_ele(self.writeMailPage_sureTimedSendBtn_loc)
                with allure.step("获取设置后的定时时间"):
                    writeMail_setted_time = self.get_elementText(self.writeMailPage_settedTime_loc)
                    if setted_time != writeMail_setted_time:
                        raise Exception("设置页面上显示的时间：{}，与点击确定后，写信页面上显示的定时时间：{}，不一致".format(setted_time,writeMail_setted_time))
        with allure.step("点击存草稿按钮"):
            self.click_ele(self.writeMailPage_saveDraftBtn_loc)
        if data["is_timeSend"]:
            with allure.step("获取通知里面的时间"):
                notify_time = self.get_elementText(self.writeMailPage_notifyTime_loc)
                if notify_time != writeMail_setted_time:
                    raise Exception("存草稿成功后，通知里面的定时发送时间：{}，与存草稿前设置的定时时间：{}，不一致".format(notify_time,writeMail_setted_time))
        else:
            with allure.step("获取toast提示"):
                toast_text = self.get_elementText(self.toast_loc)
                if "邮件成功保存到草稿箱" not in toast_text:
                    raise Exception("草稿保存成功后的提示语：{}，不对".format(toast_text))
        with allure.step("关闭写信页面"):
            self.click_ele(self.writeMailPage_closeTabBtn_loc)
        with allure.step("点击草稿箱按钮"):
            self.click_ele(self.draftBox_loc)
        with allure.step("遍历存草稿的邮件主题，并点击"):
            self.writeMailCommon.click_draftBoxEmailBySubject(subject=emailSubject)
        with allure.step("判断附件，主题，标签等是否会消失"):
            with allure.step("获取收件人"):
                draft_recipient = self.get_elementText(self.writeMailPage_recipientList_loc)
                random_recepient_format = random_recepient.split("@")[0]+"<"+random_recepient+">"
                if draft_recipient != random_recepient_format:
                    raise Exception("保存草稿后的收件人：{}，与存草稿前输入收件人之后生成的收件人：{}，不一致,直接输入的收件人：{}".format(draft_recipient,random_recepient_format,random_recepient))
            with allure.step("获取邮件主题"):
                draft_subject = self.find_element(self.writeMailPage_emailSubjectInput_loc).get_attribute("value")
                if draft_subject != emailSubject:
                    raise Exception("保存草稿后的邮件主题：{}，与存草稿前输入的主题：{}，不一致".format(draft_subject,emailSubject))
            with allure.step("获取所有的附件名"):
                draft_allAttachNames = self.get_elementText(self.writeMailPage_attachName_loc,index="all")
                if draft_allAttachNames != smallAttach + bigAttach:
                    raise Exception("保存草稿后的所有附件：{}，与存草稿前的附件：{}，不一致".format(draft_allAttachNames,smallAttach+bigAttach))
            with allure.step("获取标签"):
                draft_markText = self.get_elementText(self.writeMailPage_insertedMarkList_loc)
                if draft_markText != insertedmark_text:
                    raise Exception("保存草稿后的标签：{}，与存草稿前，插入的标签：{}，不一致".format(draft_markText,insertedmark_text))
            with allure.step("获取邮件文本内容"):
                try:
                    self.switch_frame(self.emailEditFrame_loc)
                    draft_emailContent = self.get_elementText(self.emailBodyInEmailEdit_loc)
                    if email_text not in draft_emailContent:
                        raise Exception("保存草稿后的邮件文本：{}，与存草稿前，输入的文本：{}，不一致".format(draft_emailContent,email_text))
                except Exception:
                    return False
                finally:
                    self.switch_parentFrame()
            if data["is_timeSend"]:
                with allure.step("获取草稿里面的定时时间"):
                    draft_timedSend = self.get_elementText(self.writeMailPage_settedTime_loc)
                    if draft_timedSend != writeMail_setted_time:
                        raise Exception("存草稿后的定时时间：{}，与存草稿前的定时时间：{}，不一致".format(draft_timedSend,writeMail_setted_time))
                with allure.step("取消定时"):
                    self.click_ele(self.writeMailPage_cancelTimedSendBtn_loc)
                with allure.step("点击存草稿按钮"):
                    self.click_ele(self.writeMailPage_saveDraftBtn_loc)
                with allure.step("获取toast提示"):
                    toast_text_second = self.get_elementText(self.toast_loc)
                    if "邮件成功保存到草稿箱" not in toast_text_second:
                        raise Exception("草稿保存成功后的提示语：{}，不对".format(toast_text_second))


    #写信页面，发送一封邮件
    def run_sendEmailMainProcess_case(self):
        with allure.step("输入邮件内容"):
            email_text = self.writeMailCommon.send_emailContent()
            logger.info("输入的邮件文本:{}".format(email_text))
        with allure.step("上传附件"):
            smallAttach = ['5648215.jpg']
            bigAttach = ['backend.zip']
            self.writeMailCommon.upload_attach(smallAttach,bigAttach)
        with allure.step("插入产品"):
            allProductImgs,allProductCodes = self.writeMailCommon.insert_product()
            logger.info("插入的产品地址：{}，产品名：{}".format(allProductImgs,allProductCodes))
        with allure.step("插入报价"):
            allQuoteCodes = self.writeMailCommon.insert_quote()
            logger.info("插入的报价编码：{}".format(allQuoteCodes))
        with allure.step("插入订单"):
            allOrderNames = self.writeMailCommon.insert_order()
            logger.info("插入的订单名：{}".format(allOrderNames))
        with allure.step("插入营销网站"):
            allSiteUrls = self.writeMailCommon.insert_site()
            logger.info("插入的营销网站url：{}".format(allSiteUrls))
        with allure.step("插入云文件"):
            allDishFiles = self.writeMailCommon.insert_dishFile()
            logger.info("插入的云文件：{}".format(allDishFiles))
        with allure.step("选中模板"):
            self.writeMailCommon.insert_template()
        with allure.step("输入收件人"):
            self.scroll_element(self.writeMailPage_senderInput_loc)
            time.sleep(0.5)
            self.find_element(self.writeMailPage_recipientInput_loc).send_keys("fttx222@aliyun.com")
        with allure.step("输入主题"):
            emailSubject = random_name() + "--重构版本--" + time.strftime("%Y%m%d.%H.%M.%S")
            self.find_element(self.writeMailPage_emailSubjectInput_loc).clear()
            self.find_element(self.writeMailPage_emailSubjectInput_loc).send_keys(emailSubject)
        with allure.step("选择发件人"):
            self.writeMailCommon.select_sender()
        with allure.step("点击发送按钮"):
            self.find_element(self.writeMailPage_sendEmailBtn_loc).click()
            time.sleep(5)
        with allure.step("接收邮件"):
            self.writeMailCommon.click_emailBySubject(subject=emailSubject)
        with allure.step("获取邮件详情里面的各个信息"):
            with allure.step("获取邮件详情里面的收件人"):
                emailDetail_recipient = self.writeMailCommon.get_recipientOfEmailDetail()
                logger.info("收件详情中的收件人：{}".format(emailDetail_recipient))
                if "fttx<fttx222@aliyun.com>" not in emailDetail_recipient:
                    raise Exception("邮件详情中的收件人：{}，不是刚刚发送邮件时候的发送人：fttx<fttx222@aliyun.com>".format(emailDetail_recipient))
            with allure.step("获取邮件详情里面的发件人"):
                emailDetail_sender = self.writeMailCommon.get_senderOfEmailDetail()
                emailDetail_sender = emailDetail_sender.split("<")[-1].split(">")[0]
                logger.info("收件详情中的发件人：{}".format(emailDetail_sender))
                if emailDetail_sender != "fttxtest@126.com":
                    raise Exception("邮件详情中的发件人：{}，不是刚刚发送邮件时候的收件人：管理员<fttxtest@126.com>".format(emailDetail_sender))
            with allure.step("获取邮件详情里面的小附件"):
                emailDetail_smallAttachNames = self.writeMailCommon.get_allSmallAttachNamesOfEmailDetail()
                logger.info("收件详情中的小附件：{}".format(emailDetail_smallAttachNames))
                writeMail_allSmallAttachNames = smallAttach+allQuoteCodes+allOrderNames+allDishFiles
                if sorted(emailDetail_smallAttachNames) != sorted(writeMail_allSmallAttachNames):
                    raise Exception("收件详情里面的所有小附件：{}，与写信时候插入的小附件：{}，不一致".format(emailDetail_smallAttachNames,writeMail_allSmallAttachNames))
            with allure.step("获取邮件详情里面的产品图片，产品编码"):
                emailDetail_producturls,emailDetail_productCodes = self.writeMailCommon.get_allProductImgUrlsOfEmailDetail()
                logger.info("收件详情中的产品图片:{}，产品编码：{}".format(emailDetail_producturls,emailDetail_productCodes))
                if sorted(emailDetail_producturls) != sorted(allProductImgs):
                    raise Exception("收件详情中的产品名：{}，与写信时候插入的产品名：{}，不一致".format(emailDetail_producturls,allProductImgs))
                if sorted(emailDetail_productCodes) != sorted(allProductCodes):
                    raise Exception("收件详情中的产品编码：{}，与写信时候插入的产品编码：{}，不一致".format(emailDetail_productCodes,allProductCodes))
            with allure.step("获取邮件详情里面的营销快照url"):
                emailDetail_siteUrl = self.writeMailCommon.get_allSiteUrlsOfEmailDetail()
                logger.info("收件详情中的营销快照url：{}".format(emailDetail_siteUrl))
            with allure.step("获取邮件详情里面的邮件文本"):
                emailDetail_emailText = self.writeMailCommon.get_emailTextOfEmailDetail()
                logger.info("收件详情中的邮件文本：{}".format(emailDetail_emailText))
                if emailDetail_emailText != email_text:
                    raise Exception("收件详情中的邮件内容文本：{}，与写信时候输入的邮件内容文本：{}，不一致".format(emailDetail_emailText,email_text))
            with allure.step("获取邮件详情里面的大附件"):
                emailDetail_bigAttachNames = self.writeMailCommon.get_allBigAttachNamesOfEmailDetail()
                logger.info("收件详情中的大附件：{}".format(emailDetail_bigAttachNames))
                if emailDetail_bigAttachNames != bigAttach:
                    raise Exception("收件详情中的大附件：{}，与写信时候插入的大附件：{}，不一致".format(emailDetail_bigAttachNames,bigAttach))
        with allure.step("回复该邮件"):
            self.writeMailCommon.click_replyContainsAttach()
        time.sleep(1)
        with allure.step("输入回复的文本内容"):
            replyed_emailContent = self.writeMailCommon.send_emailContent()
            logger.info("输入的回复文本：{}".format(replyed_emailContent))
        with allure.step("点击发送按钮"):
            self.find_element(self.writeMailPage_sendEmailBtn_loc).click()
            time.sleep(3)
        with allure.step("关闭邮件详情，回到邮件首页"):
            self.find_element(self.writeMailPage_closeTabBtn_loc).click()
        with allure.step("接收回复的邮件"):
            replyed_emailSubject = "Re:"+emailSubject
            self.writeMailCommon.click_emailBySubject(subject=replyed_emailSubject)
        with allure.step("获取回复的邮件详情里面的各个信息"):
            with allure.step("获取回复的邮件详情里面的回复的收件人"):
                replyedEmailDetail_recipient = self.writeMailCommon.get_recipientOfEmailDetail()
                logger.info("回复的收件详情中的回复的收件人：{}".format(replyedEmailDetail_recipient))
                if "fttxtest<fttxtest@126.com>" not in replyedEmailDetail_recipient:
                    raise Exception("收到的回复的邮件详情中的收件人：{}，没有回复时候的发件人：fttxtest<fttxtest@126.com>".format(replyedEmailDetail_recipient))
            with allure.step("获取回复的邮件详情里面的发件人"):
                replyedEmailDetail_sender = self.writeMailCommon.get_senderOfEmailDetail()
                replyedEmailDetail_sender = replyedEmailDetail_sender.split("<")[-1].split(">")[0]
                logger.info("回复的收件详情中的发件人：{}".format(replyedEmailDetail_sender))
                if replyedEmailDetail_sender != "fttx222@aliyun.com":
                    raise Exception("收到的回复的邮件详情中的发件人：{}，不是：管理员<fttx222@aliyun.com>".format(replyedEmailDetail_sender))
            with allure.step("获取回复的邮件详情里面的小附件"):
                replyedEmailDetail_smallAttachNames = self.writeMailCommon.get_allSmallAttachNamesOfEmailDetail()
                logger.info("回复的收件详情中的小附件：{}".format(replyedEmailDetail_smallAttachNames))
                if sorted(replyedEmailDetail_smallAttachNames) != sorted(emailDetail_smallAttachNames):
                    raise Exception("收到的回复的邮件详情中的所有小附件：{}，与回复之前，邮件详情中的小附件：{}，不一致".format(replyedEmailDetail_smallAttachNames,emailDetail_smallAttachNames))
            with allure.step("获取回复的邮件详情里面的产品图片，产品编码"):
                replyedEmailDetail_producturls, replyedEmailDetail_productCodes = self.writeMailCommon.get_allProductImgUrlsOfEmailDetail()
                logger.info("回复的收件详情中的产品图片:{}，产品编码：{}".format(replyedEmailDetail_producturls, replyedEmailDetail_productCodes))
                if sorted(replyedEmailDetail_producturls) != sorted(emailDetail_producturls):
                    raise Exception("收到的回复的邮件详情中的产品图片地址：{}，与回复之前，邮件详情中的产品图片地址：{}，不一致".format(replyedEmailDetail_producturls,emailDetail_producturls))
                if sorted(replyedEmailDetail_productCodes) != sorted(emailDetail_productCodes):
                    raise Exception("收到的回复的邮件详情中的产品编码：{}，与回复之前，邮件详情中的产品编码：{}，不一致".format(replyedEmailDetail_productCodes,emailDetail_productCodes))
            with allure.step("获取回复的邮件详情里面的营销快照url"):
                replyedEmailDetail_siteUrl = self.writeMailCommon.get_allSiteUrlsOfEmailDetail()
                logger.info("回复的收件详情中的营销快照url：{}".format(replyedEmailDetail_siteUrl))
            with allure.step("获取回复的邮件详情里面的回复的邮件文本"):
                replyedEmailDetail_emailText = self.writeMailCommon.get_emailTextOfEmailDetail()
                logger.info("回复的收件详情中的回复的邮件文本：{}".format(replyedEmailDetail_emailText))
                if replyedEmailDetail_emailText != replyed_emailContent:
                    raise Exception("收到的回复邮件的详情中的邮件内容文本：{}，与回复之前，邮件详情中的邮件文本：{}，不一致".format(replyedEmailDetail_emailText,replyed_emailContent))
            with allure.step("获取回复的邮件详情里面的大附件"):
                replyedEmailDetail_bigAttachNames = self.writeMailCommon.get_allBigAttachNamesOfEmailDetail()
                logger.info("回复的收件详情中的大附件：{}".format(replyedEmailDetail_bigAttachNames))
                if replyedEmailDetail_bigAttachNames != emailDetail_bigAttachNames:
                    raise Exception("收到的回复邮件的详情中的大附件：{}，与回复之前，邮件详情中的大附件：{}，不一致".format(replyedEmailDetail_bigAttachNames,emailDetail_bigAttachNames))


    #群发单显邮件
    def run_massEmail_case(self):
        with allure.step("点击群发单显按钮"):
            self.click_ele(self.writeMailPage_massSendBtn_loc)
        with allure.step("输入收件人"):
            recipients = ["fttx222@aliyun.com","fttxtest@126.com"]
            for recipient in recipients:
                self.sendKeys(self.writeMailPage_recipientInput_loc,key=recipient)
                time.sleep(0.3)
                self.click_ele(self.writeMailPage_writeMailTabBtn_loc)
        with allure.step("选择内部转发"):
            inner = "云基础"
            forwardIdeaText = random_text().replace("\n","")
            self.writeMailCommon.selectInnerToForward(inner,forwardIdeaText)
        with allure.step("输入邮件主题"):
            random_subject = random_name() + "-群发单显测试-内部转发-" + time.strftime("%Y%m%d.%H.%M.%S")
            self.sendKeys(self.writeMailPage_emailSubjectInput_loc,key=random_subject)
        with allure.step("输入邮件文本"):
            email_text = self.writeMailCommon.send_emailContent()
        with allure.step("点击发送按钮"):
            self.click_ele(self.writeMailPage_sendEmailBtn_loc)
            time.sleep(3)
        with allure.step("切换到dmktest_001"):
            self.switch_operator(operator="dmktest_001")
        with allure.step("判断云基础账号是否收到分发的邮件"):
            recipientBoxPage(driver=self.driver).assert_emailSubjectAndForwardIdea(random_subject, forwardIdeaText)


    #插入宏,发送测试
    def run_sendMacro_case(self):
        with allure.step("输入收件人"):
            self.sendKeys(self.writeMailPage_recipientInput_loc,key="fttx444@aliyun.com")
            self.click_ele(self.writeMailPage_writeMailTabBtn_loc)
        with allure.step("输入主题"):
            emailSubject = random_name() + "--插入宏--" + time.strftime("%Y%m%d.%H.%M.%S")
            self.sendKeys(self.writeMailPage_emailSubjectInput_loc,key=emailSubject)
        with allure.step("插入宏"):
            self.writeMailCommon.insert_macro()
        with allure.step("选择发件人"):
            self.writeMailCommon.select_sender(sender="fttx222@aliyun.com")
        with allure.step("点击发送按钮"):
            self.click_ele(self.writeMailPage_sendEmailBtn_loc)
        with allure.step("获取宏邮件"):
            self.writeMailCommon.click_emailBySubject(subject=emailSubject)
        with allure.step("获取宏邮件的宏文本"):
            emailDetail_macroText = self.writeMailCommon.get_emailTextOfEmailDetail()
        with allure.step("判断宏文本是否正确"):
            expected_macroText = "客户简称test-勿动测试，勿动AFGHANISTAN阿富汗125742382069967吉林省文市海港孙路x座 389615广交会fttx444其他186384862291383616761915672213865"
            if expected_macroText != emailDetail_macroText:
                raise Exception("邮件详情中的宏文本：{}，与预期的宏文本：{}，不一致".format(emailDetail_macroText,expected_macroText))