# -*- encoding: utf-8 -*-
'''
@File    :   emailFastReplyPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/3 0003 16:15   dmk      1.0         None
'''
import time
from utils.log import logger
from selenium.webdriver.common.by import By
from .basePage import Action

class emailFastReplyPage(Action):
    #第一封邮件,根据主题来获取
    firstEmailSubject_loc = (By.XPATH,"//div[@class='sub_item']")
    #快速回复按钮
    fastReplyBtn_loc = (By.XPATH,"//div[@class='el-tooltip quick_btn pointer']")
    #快速回复发送按钮
    fastReplySendBtn_loc = (By.XPATH,"//div[@class='quick_response_vue quick_response']//button[@class='el-button el-button--primary']")
    #全屏按钮
    fastReplyFullScreenBtn_loc = (By.XPATH,"//a[@class='close pointer']")
    #快速回复输入框
    fastReplyInput_loc = (By.XPATH,"//textarea[@class='el-textarea__inner']")
    #快速回复成功message
    fastReplySuccessMessage_loc = (By.XPATH,"//div[@class='msg_title']/span")
    #不审批按钮
    directSendEmail_loc = (By.XPATH,"//span[text()='不审，发送']")
    #详情页邮件主题
    emailDetailSubject_loc = (By.XPATH,"//div[@class='subject f18 fc02 f-w-400 line-clamp']//span")
    #详情页发件人
    emailDetailSender_loc = (By.XPATH,"//span[@class='contact_names fc01']")
    #详情页邮件正文
    emailDetailBody_loc = (By.XPATH,"/html/body")
    #写邮件页面主题
    emailWriteSubject_loc = (By.XPATH,"//div[@class='no_border input JOINF el-input el-input--suffix']/input")
    #写邮件页面收件人
    emailWriteReceipt_loc = (By.XPATH,"//p[@class='show_txt f12 fc02 no-sel']")
    #写邮件页面邮件主体
    emailWriteEmailBody_loc = (By.XPATH,"/html/body")



    def __init__(self,driver):
        super(emailFastReplyPage,self).__init__(driver)
        #进入第一封邮件详情
        time.sleep(2)
        logger.info(len(self.find_element(self.firstEmailSubject_loc,index="all")))
        self.find_element(self.firstEmailSubject_loc).click()


    def run_fastReplySend_case(self):
        #点击快速回复
        self.find_element(self.fastReplyBtn_loc).click()
        #输入回复文本
        self.find_element(self.fastReplyInput_loc).send_keys("快速回复测试")
        #点击发送按钮
        self.find_element(self.fastReplySendBtn_loc).click()
        #判断是否有审批框
        try:
            self.find_element(self.directSendEmail_loc).click()
        except Exception as e:
            logger.info("没有找到审批框，直接发送")
        #判断是否有发送成功弹框
        try:
            self.switch_parentFrame()
            if self.find_element(self.fastReplySuccessMessage_loc).text != "邮件已发出":
                raise Exception("快速回复发送失败,原因：{}".format(self.find_element(self.fastReplySuccessMessage_loc).text))
        except Exception as e:
            raise Exception("快速回复消息未展示")
        finally:
            self.switch_frame(self.mainFrame_loc)


    def run_fastReplyFullScreen_case(self):
        #获取邮件标题
        time.sleep(1)
        emailDetailSubject = self.find_element(self.emailDetailSubject_loc).text
        logger.info("详情里面的主题：{}".format(emailDetailSubject))
        #获取发件人
        emailDetailSender = self.find_element(self.emailDetailSender_loc).text
        logger.info("详情里面的发件人：{}".format(emailDetailSender))
        #获取邮件主体
        try:
            time.sleep(1)
            self.switch_frame(self.emailBodyFrame_loc)
            logger.info(len(self.find_element(self.emailWriteEmailBody_loc,index="all")))
            emailDetailBody = self.find_element(self.emailDetailBody_loc).text
            logger.info("邮件详情：{}".format(emailDetailBody))
        except Exception as e:
            raise Exception("获取邮件详情失败,主题是：{}".format(emailDetailSubject))
        finally:
            self.switch_parentFrame()

        #点击快速回复
        self.find_element(self.fastReplyBtn_loc).click()
        #点击全屏按钮
        time.sleep(0.5)
        self.find_element(self.fastReplyFullScreenBtn_loc).click()
        time.sleep(3)
        #获取邮件主题
        emailWriteSubject = self.find_element(self.emailWriteSubject_loc).get_attribute("value")
        logger.info("写信页面的主题：{}".format(emailWriteSubject))
        #获取收件人
        emailWriteReceipt = self.find_element(self.emailWriteReceipt_loc).text
        logger.info("写信页面的发件人：{}".format(emailWriteReceipt))
        #获取邮件正文
        try:
            self.switch_frame(self.emailEditFrame_loc)
            emailWriteEmailBody = self.find_element(self.emailWriteEmailBody_loc).text
            logger.info("写信页面的邮件内容：{}".format(emailWriteEmailBody))
            
        except Exception as e:
            raise Exception("获取编辑器里面的邮件主体报错，主题是：{}".format(emailWriteEmailBody))
        finally:
            self.switch_parentFrame()

        #开始断言主题，收发人，以及邮件主题是否与回复之前一致
        if emailWriteSubject != "Re:" + emailDetailSubject:
            raise Exception("快速回复前后，回复前的主题：{}，与回复后的主题：{}，不一致".format(emailDetailSubject,emailWriteSubject))
        emailDetailSender = emailDetailSender.split("<")[1].split(">")[0]

        if emailDetailSender not in emailWriteReceipt:
            raise Exception("快速回复前后，回复前的发件人：{},与回复后的收件人：{}，不一致".format(emailDetailSender,emailWriteReceipt))

        if emailDetailBody not in emailWriteEmailBody:
            raise Exception("快速回复前后，回复前的邮件主体：{}，与回复后的邮件主体：{}，不一致".format(emailDetailBody,emailWriteEmailBody))