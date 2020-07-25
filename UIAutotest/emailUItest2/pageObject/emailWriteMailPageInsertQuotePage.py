# -*- encoding: utf-8 -*-
'''
@File    :   emailWriteMailPageInsertQuotePage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/7 0007 9:30   dmk      1.0         None
'''

import time,traceback
from utils.log import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .emailWriteMailPage import emailWriteMailPage

class emailWriteMailPageInsertQuotePage(emailWriteMailPage):
    #插入报价按钮
    insertQuoteBtn_loc = (By.XPATH,'//div[@class="tool"]//li[text()="报价"]')
    #报价单联系人
    quoteContactAccountList_loc = (By.XPATH,'//div[@class="el-dialog__wrapper JOINF orderSelectdialog align-center"]//tbody//tr/td[4]')
    #全选按钮
    allQuoteSelectBtn_loc = (By.XPATH,'//div[@class="el-dialog__wrapper JOINF orderSelectdialog align-center"]//thead//tr/th[1]//label')
    #插入PDF报价
    insertPDFQuoteBtn_loc = (By.XPATH,'//div[@class="el-dialog__wrapper JOINF orderSelectdialog align-center"]//span[text()="插入PDF"]')
    #插入EXCEL报价
    insertEXCELQuoteBtn_loc = (By.XPATH,'//div[@class="el-dialog__wrapper JOINF orderSelectdialog align-center"]//span[text()="插入EXCEL"]')
    #确定插入按钮
    sureInsertQuoteBtn_loc = (By.XPATH,'//button[@class="el-button el-button--default el-button--small el-button--primary "]')
    #报价搜索输入框
    quoteSearchInput_loc = (By.XPATH,'//div[@class="el-dialog__wrapper JOINF orderSelectdialog align-center"]//input[@placeholder="请输入单号、客户名称、联系人姓名/邮箱"]')
    #正在生成文件提示语
    generatingFileToast_loc = (By.XPATH,'//p[text()="正在生成文件，请稍后"]')



    def __init__(self,driver):
        super(emailWriteMailPageInsertQuotePage,self).__init__(driver)
        self.find_element(self.insertQuoteBtn_loc).click()


    def run_insertQuote_case(self,is_all,file_type):
        #判断是否插入所有第一页报价
        #self.screenshotImg(key="插入报价")
        if is_all == "1":
            allQuoteContactAccount = self.get_elementText(self.quoteContactAccountList_loc,index="all")
            logger.info(allQuoteContactAccount)
            self.find_element(self.allQuoteSelectBtn_loc).click()
        else:
            firstQuoteContactAccount = self.find_element(self.quoteContactAccountList_loc).text
            logger.info(firstQuoteContactAccount)
            self.find_element(self.quoteContactAccountList_loc).click()
        #判断是否插入PDF，Excel
        if file_type == "PDF":
            self.scroll_element(self.insertPDFQuoteBtn_loc)
            self.find_element(self.insertPDFQuoteBtn_loc).click()
        elif file_type == "EXCEL":
            self.scroll_element(self.insertEXCELQuoteBtn_loc)
            self.find_element(self.insertEXCELQuoteBtn_loc).click()
        else:
            raise Exception("选择了其他不正确的格式：{}，请排查".format(file_type))
        #判断是否有确定按钮
        try:
            self.find_element(self.sureInsertQuoteBtn_loc).click()
        except Exception as e:
            logger.info(e)
        #直到提示语消失后，开始获取写信页面的收件人
        try:
            n = 0
            while n < 10:
                if self.is_element_exist(self.generatingFileToast_loc[1]):
                    time.sleep(2)
                    print(n)
                    n = n + 1
                else:
                    break
            #WebDriverWait(self.driver,30).until(EC.invisibility_of_element_located(self.generatingFileToast_loc))
            #写信页面获取收件人
            emailWriteMailPage_receipt = self.get_elementText(self.emailWriteReceipt_loc,index="all")
            logger.info(emailWriteMailPage_receipt)
            print(emailWriteMailPage_receipt)
        except Exception as e:
            traceback.print_exc()
            #self.screenshotImg(key="插入报价")
            logger.info(e)

        #再次点击报价，查看搜索框里面的联系人
        self.find_element(self.insertQuoteBtn_loc).click()
        quoteContactAccount_searchInput = self.find_element(self.quoteSearchInput_loc).get_attribute("value")
        logger.info(quoteContactAccount_searchInput)

        #判断选择的报价联系人邮箱是否与带入写信页面的收件人是否一致
        if is_all == "1":
            allContact = "".join(allQuoteContactAccount)
            for receipt in emailWriteMailPage_receipt:
                if receipt.split("<")[1].split(">")[0] not in allContact:
                    raise Exception("该收件人：{}，不是选中的报价联系人".format(receipt))
        else:
            if firstQuoteContactAccount != emailWriteMailPage_receipt[0]:
                raise Exception("选中的报价联系人：{}，与带入到写信页面的收件人：{}，不一致，请排查".format(firstQuoteContactAccount,emailWriteMailPage_receipt))

        if quoteContactAccount_searchInput != emailWriteMailPage_receipt[0].split("<")[1].split(">")[0]:
            raise Exception("再次点击报价后，刚刚选中的联系人：{}，与报价搜索输入框里面的联系人：{}，不一致，请排查".format(emailWriteMailPage_receipt[0],quoteContactAccount_searchInput))