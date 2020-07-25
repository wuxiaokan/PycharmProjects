# -*- encoding: utf-8 -*-
'''
@File    :   emailAttachSavePage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/4 0004 15:11   dmk      1.0         None
'''

import time
from utils.log import logger
from selenium.webdriver.common.by import By
from .basePage import Action


class emailAttachSavePage(Action):
    #邮件附件标志
    attachFlag_loc = (By.XPATH,"//div[@class='attach']//div[@class='attach_item']")
    #带有附件的邮件主题
    attachFlag_emailSubject_loc = (By.XPATH,"//div[@class='attach']//div[@class='attach_item']/../../../following-sibling::td[1]")
    #附件列表
    attachList_loc = (By.XPATH,"//div[@x-placement='right']//li[@class='item']")
    #单个转存按钮
    singleSaveAttachBtn_loc = (By.XPATH,"//div[@x-placement='right']//li[@class='item'][1]//span[@class='icons']//div[contains(@class,'icon-wrap')][3]//*[name()='svg']")
    #批量转存按钮
    multipleSaveAttachBtn_loc = (By.XPATH,"//div[@x-placement='right']//span[text()='批量转存']")
    #邮件第二页
    secondPage_loc = (By.XPATH,"//ul[@class='el-pager']/li[2]")
    #个人云盘
    privateDish_loc = (By.XPATH,"//div[@aria-label='选择云盘']//li[text()='个人']")
    #云盘保存按钮
    dishSaveBtn_loc = (By.XPATH,"//button[@class='el-button m-l-10 el-button--primary el-popover__reference']")
    #重名文件提示文案
    sameNameFileTip_loc = (By.XPATH,"//div[@x-placement='top-end']//p[@class='m-b-10']")
    #重名文件确定按钮
    sameNameFileSureBtn_loc = (By.XPATH,"//div[@x-placement='top-end']//button[@class='el-button el-button--primary']")

    def __init__(self,driver):
        super(emailAttachSavePage,self).__init__(driver)
        self.get_hasAttachEmail()

    #获取有附件的邮件
    def get_hasAttachEmail(self):
        time.sleep(2)
        if self.is_element_exist(self.attachFlag_loc[1]):
            logger.info(self.find_element(self.attachFlag_emailSubject_loc).text)
            self.scroll_element(self.attachFlag_loc)
            self.find_element(self.attachFlag_loc).click()
            
        else:
            #点击下一页
            self.find_element(self.secondPage_loc).click()
            time.sleep(1)
            logger.info(self.find_element(self.attachFlag_emailSubject_loc).text)
            self.scroll_element(self.attachFlag_loc)
            self.find_element(self.attachFlag_loc).click()

    def run_saveEmailAttach_case(self,casename,is_share,is_multiple):
        #判断是否是批量转存
        if is_multiple:
            self.find_element(self.multipleSaveAttachBtn_loc).click()
        else:
            #悬浮第一个附件
            self.mouseHover(self.attachList_loc)
            time.sleep(0.5)
            #获取第一个附件的信息
            firstAttachInfo = self.get_elementText(self.attachList_loc)
            logger.info("第一个附件信息:{}".format(firstAttachInfo))
            #点击转存按钮
            if self.is_element_exist(self.singleSaveAttachBtn_loc[1]):
                self.find_element(self.singleSaveAttachBtn_loc).click()
            else:
                self.screenshotImg(key="保存附件")
                singleSaveAttachBtn_loc = (By.XPATH,self.singleSaveAttachBtn_loc[1].replace("3","2"))
                logger.info("单个附件转存按钮：{}".format(singleSaveAttachBtn_loc))
                self.click_ele(singleSaveAttachBtn_loc)
                # self.find_element((By.XPATH,self.singleSaveAttachBtn_loc[1].replace("3","2"))).click()
        #判断是否是共享
        if not is_share:
            #点击个人云盘
            self.find_element(self.privateDish_loc).click()
        #点击保存
        self.find_element(self.dishSaveBtn_loc).click()
        #判断是否会有重名的提示
        time.sleep(0.5)
        try:
            if "选中目录内含有重名文件，是否覆盖" in self.find_element(self.sameNameFileTip_loc).text:
                self.find_element(self.sameNameFileSureBtn_loc).click()
        except Exception as e:
            logger.debug("重名文件提示部分报错")
        #获取保存成功toast提示
        toastSuccessText = self.find_element(self.toast_loc).text
        if toastSuccessText != "保存成功":
            raise Exception("邮件附件,转存不成功,邮件主题：{}，用例：{}，toast提示：{}".format(self.find_element(self.attachFlag_emailSubject_loc).text,casename,toastSuccessText))

    #获取云盘文件列表
    # def get_dishFileList(self,is_share):
