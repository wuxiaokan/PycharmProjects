# -*- encoding: utf-8 -*-
'''
@File    :   emailWriteMailPageInsertOrderPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/7 0007 9:30   dmk      1.0         None
'''

import time
from utils.log import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .emailWriteMailPage import emailWriteMailPage

class emailWriteMailPageInsertOrderPage(emailWriteMailPage):
    #插入订单按钮
    insertOrderBtn_loc = (By.XPATH,'//div[@class="tool"]//li[text()="订单"]')
    #订单单联系人
    OrderContactAccountList_loc = (By.XPATH,'//div[contains(@class,"orderSelectdialog")]//tbody//tr/td[4]')
    #全选按钮
    allOrderSelectBtn_loc = (By.XPATH,'//div[@class="el-dialog__wrapper JOINF orderSelectdialog align-center"]//thead//tr/th[1]//label')
    #插入PDF订单
    insertPDFOrderBtn_loc = (By.XPATH,'//div[@class="el-dialog__wrapper JOINF orderSelectdialog align-center"]//span[text()="插入PDF"]')
    #插入EXCEL订单
    insertEXCELOrderBtn_loc = (By.XPATH,'//div[@class="el-dialog__wrapper JOINF orderSelectdialog align-center"]//span[text()="插入EXCEL"]')
    #确定插入按钮
    sureInsertOrderBtn_loc = (By.XPATH,'//button[@class="el-button el-button--default el-button--small el-button--primary "]')
    #订单搜索输入框
    OrderSearchInput_loc = (By.XPATH,'//div[@class="el-dialog__wrapper JOINF orderSelectdialog align-center"]//input[@placeholder="请输入单号、客户名称、联系人姓名/邮箱"]')
    #正在生成文件提示语
    generatingFileToast_loc = (By.XPATH,'//p[text()="正在生成文件，请稍后"]')



    def __init__(self,driver):
        super(emailWriteMailPageInsertOrderPage,self).__init__(driver)
        self.find_element(self.insertOrderBtn_loc).click()


    def run_insertOrder_case(self,is_all,file_type):
        #判断是否插入所有第一页订单
        #self.screenshotImg(key="插入订单")
        if is_all == "1":
            #self.screenshotImg(key="全部插入订单")
            allOrderContactAccount = self.get_elementText(self.OrderContactAccountList_loc,index="all")
            logger.info(allOrderContactAccount)
            self.find_element(self.allOrderSelectBtn_loc).click()
        else:
            self.screenshotImg(key="部分插入订单")
            firstOrderContactAccount = self.find_element_byPresence(self.OrderContactAccountList_loc).text
            logger.info(firstOrderContactAccount)
            self.find_element(self.OrderContactAccountList_loc).click()
        #判断是否插入PDF，Excel
        if file_type == "PDF":
            self.scroll_element(self.insertPDFOrderBtn_loc)
            self.find_element(self.insertPDFOrderBtn_loc).click()
        elif file_type == "EXCEL":
            self.scroll_element(self.insertEXCELOrderBtn_loc)
            self.find_element(self.insertEXCELOrderBtn_loc).click()
        else:
            raise Exception("选择了其他不正确的格式：{}，请排查".format(file_type))
        #判断是否有确定按钮
        try:
            self.find_element(self.sureInsertOrderBtn_loc).click()
        except Exception as e:
            logger.info(e)
        #直到提示语消失后，开始获取写信页面的收件人
        try:
            n = 0
            while n < 10:
                if self.is_element_exist(self.generatingFileToast_loc[1]):
                    time.sleep(2)
                    n = n + 1
                else:
                    break
            #WebDriverWait(self.driver,30).until(EC.invisibility_of_element_located(self.generatingFileToast_loc))
            #写信页面获取收件人
            time.sleep(0.5)
            emailWriteMailPage_receipt = self.get_elementText(self.emailWriteReceipt_loc,index="all")
            logger.info(emailWriteMailPage_receipt)
        except Exception as e:
            #self.screenshotImg(key="插入订单")
            logger.info(e)

        #再次点击订单，查看搜索框里面的联系人
        self.find_element(self.insertOrderBtn_loc).click()
        OrderContactAccount_searchInput = self.find_element(self.OrderSearchInput_loc).get_attribute("value")
        logger.info(OrderContactAccount_searchInput)

        #判断选择的订单联系人邮箱是否与带入写信页面的收件人是否一致
        if is_all == "1":
            allContact = "".join(allOrderContactAccount)
            for receipt in emailWriteMailPage_receipt:
                if receipt.split("<")[1].split(">")[0] not in allContact:
                    raise Exception("该收件人：{}，不是选中的订单联系人".format(receipt))
        else:
            if firstOrderContactAccount != emailWriteMailPage_receipt[0]:
                raise Exception("选中的订单联系人：{}，与带入到写信页面的收件人：{}，不一致，请排查".format(firstOrderContactAccount,emailWriteMailPage_receipt))

        if OrderContactAccount_searchInput != emailWriteMailPage_receipt[0].split("<")[1].split(">")[0]:
            raise Exception("再次点击订单后，刚刚选中的联系人：{}，与订单搜索输入框里面的联系人：{}，不一致，请排查".format(emailWriteMailPage_receipt[0],OrderContactAccount_searchInput))