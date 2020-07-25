# -*- encoding: utf-8 -*-
'''
@File    :   emailCustomerFollowPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/6 0006 9:44   dmk      1.0         None
'''

import time,random
from utils.log import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from .basePage import Action

class emailCustomerFollowPage(Action):
    #客户图标color
    customer_xlink_href_loc = "#icon-iconkehu2"
    #未建档客户图标color
    newCustomer_xlink_href_loc = "#icon-iconxinkehu"
    #客户箱按钮
    customerBoxBtn_loc = (By.XPATH,'//div[@id="tab-customer"]')
    #最近联系的第一个箱子
    lastestContact_firstCustomerBox_loc = (By.XPATH,'//div[@id="pane-customer"]//div[@class="el-tree-node__children"]/div')
    #发件人图标
    senderIcon_loc = (By.XPATH,"//a[@class='pointer']//*[name()='svg']//*[name()='use']")
    #跟进阶段编辑按钮
    followStepEditBtn_loc = (By.XPATH,'//div[@class="t-flex-row el-col el-col-12"]//i[@class="el-tooltip icon pointer"]')
    #跟进列表一级选择框
    followStepListInput_loc = (By.XPATH,'//div[@class="edit-stage"]//input')
    #跟进列表
    followStepList_loc = (By.XPATH,'//div[@x-placement="bottom-start"]//li')
    #确定新增跟进
    sureAddFollowStepBtn_loc = (By.XPATH,'//div[@class="edit-stage"]//i[@class="el-icon-circle-check pointer f18 icon-hover m-l-10"]')
    #跟进阶段文本
    followStepText_loc = (By.XPATH,'//div[@class="info-item el-row"]//div[@class="flex-col-auto one-line has-icon-right"]//span')
    #跟进页面关闭按钮
    followStepPage_closeBtn_loc = (By.XPATH,'//span[@class="el-tooltip t-icon-bg fr m-l-5"]')
    #跟进页面发邮件按钮图标
    followStepPage_sendMailIcon_loc = (By.XPATH,'//div[@class="fr m-r-10"]/span[1]')
    #写信页面收件人
    writeMailPage_receipt_loc = (By.XPATH,"//p[@class='show_txt f12 fc02 no-sel']")
    #跟进页面上，客户联系人邮箱
    followStepPage_customerContactAccount_loc = (By.XPATH,'//span[@class="cursor0"]//span[@class="contact_names"]')
    #跟进页面基础信息tab
    followStepPage_baseInformation_loc = (By.XPATH,"//li[text()='基础信息']")
    #跟进页面相关业务tab
    followStepPage_relatedBusiness_loc = (By.XPATH,"//li[text()='相关业务']")
    #跟进页面往来邮件tab
    followStepPage_tradeEmail_loc = (By.XPATH,"//li[text()='往来邮件']")


    def __init__(self,driver):
        super(emailCustomerFollowPage,self).__init__(driver)
        self.click_ele(self.customerBoxBtn_loc)
        self.click_ele(self.lastestContact_firstCustomerBox_loc)
        # self.find_element(self.customerBoxBtn_loc).click()
        # self.find_element(self.lastestContact_firstCustomerBox_loc).click()
        self.screenshotImg(key="跟进页面")


    #判断是否有客户，并打开跟进页面
    def openFollowPage(self,xlink_href):
        #判断收发件是否是客户
        allsenders = self.find_element(self.senderIcon_loc,index="all")
        for allsender in allsenders:
            if allsender.get_attribute("xlink:href") == xlink_href:
                time.sleep(1)
                # allsender.click()
                ActionChains(self.driver).click(allsender).perform()
                self.screenshotImg(key="跟进页面打开")
                break

    def run_editFollowStep_case(self):
        self.openFollowPage(self.customer_xlink_href_loc)
        time.sleep(0.3)
        #点击跟进编辑按钮
        self.find_element(self.followStepEditBtn_loc).click()
        #点击跟进列表一级选择框
        self.find_element(self.followStepListInput_loc).click()
        #随机选择一个跟进
        followListNum = len(self.find_element(self.followStepList_loc,index="all"))
        if followListNum == 0:
            raise Exception("没有跟进阶段可以选择，请排查")
        index = random.randint(0,followListNum-1)
        purpose_followStepElement = self.find_element(self.followStepList_loc,index=index)
        purpose_followStepText = purpose_followStepElement.text
        logger.info("要设置的跟进阶段是：{}".format(purpose_followStepText))
        purpose_followStepElement.click()
        #点击确定按钮
        self.find_element(self.sureAddFollowStepBtn_loc).click()
        #点击关闭按钮
        self.find_element(self.followStepPage_closeBtn_loc).click()
        time.sleep(0.5)
        self.openFollowPage(self.customer_xlink_href_loc)
        #获取跟进文本
        followStepText = self.find_element(self.followStepText_loc).text
        logger.info("实际上获取的跟进阶段是：{}".format(followStepText))

        #断言
        if followStepText != purpose_followStepText:
            raise Exception("修改后的跟进阶段不一致，修改的：{}，实际的：{}".format(purpose_followStepText,followStepText))

    def run_sendMailFollowStepPage_case(self):
        self.openFollowPage(self.customer_xlink_href_loc)
        #获取写信icon，并点击
        customerAccount = self.find_element(self.followStepPage_customerContactAccount_loc).text
        logger.info("跟进页面上的客户联系人邮箱是：{}".format(customerAccount))
        self.find_element(self.followStepPage_sendMailIcon_loc).click()
        #获取写信页面收件人
        time.sleep(3)
        self.screenshotImg(key="客户跟进页面")
        writeMailPage_receipt = self.find_element(self.writeMailPage_receipt_loc).text
        logger.info("由跟进页面点击发邮件icon后，带到写信页面的收件人是：{}".format(writeMailPage_receipt))
        if customerAccount not in writeMailPage_receipt:
            raise Exception("跟进页面发送邮件，跟进页面上的邮箱账号：{}，没有带到写信页面的收件人处：{}".format(customerAccount,writeMailPage_receipt))


    def run_followStepPageLayout_case(self,is_newCustomer):
        if is_newCustomer:
            self.openFollowPage(self.newCustomer_xlink_href_loc)
            time.sleep(0.5)
            if EC.visibility_of_any_elements_located(self.followStepPage_baseInformation_loc)(self.driver):
                self.screenshotImg(key="新客户跟进页面")
                raise Exception("该新客户跟进页面有基础信息tab")
            if EC.visibility_of_any_elements_located(self.followStepPage_relatedBusiness_loc)(self.driver):
                self.screenshotImg(key="新客户跟进页面")
                raise Exception("该新客户跟进页面有相关业务tab")
        else:
            self.openFollowPage(self.customer_xlink_href_loc)
            time.sleep(0.5)
            if not EC.visibility_of_any_elements_located(self.followStepPage_baseInformation_loc)(self.driver):
                self.screenshotImg(key="老客户跟进页面")
                raise Exception("该老客户跟进页面没有基础信息tab")
            if EC.invisibility_of_element_located(self.followStepPage_relatedBusiness_loc)(self.driver):
                self.screenshotImg(key="老客户跟进页面")
                raise Exception("该老客户跟进页面没有相关业务tab")
            if EC.invisibility_of_element_located(self.followStepPage_tradeEmail_loc)(self.driver):
                self.screenshotImg(key="老客户跟进页面")
                raise Exception("该老客户跟进页面没有往来tab")
