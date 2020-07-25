# -*- encoding: utf-8 -*-
'''
@File    :   writeMailPageInsertFastTextPageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/8 0008 10:08   dmk      1.0         None
'''

import allure,time
from selenium.webdriver.common.by import By
from utils.log import logger
from pageObject.basePage import Action
from pageObject.writeMailPage.writeMailPageInsertFastTextPage_loc import writeMailPageInsertFastTextPageLoc

class writeMailPageInsertFastTextPageCommon(Action,writeMailPageInsertFastTextPageLoc):

    def __init__(self,driver):
        super(writeMailPageInsertFastTextPageCommon,self).__init__(driver)


    #获取第一个快速文本的名称，内容
    def get_firstFastText(self,is_pure):
        with allure.step("点击写邮件按钮"):
            self.click_ele(self.writeEmailBtn_loc,key="点击写邮件")
        time.sleep(2)
        with allure.step("点击插入快速文本按钮"):
            self.click_ele(self.writeMailPage_insertFastTextBtn_loc,key="点击插入快速文本按钮")
        time.sleep(1)
        with allure.step("选中第一个快速文本"):
            fastTextName = self.get_elementText(self.writeMailPageInsertFastTextPage_fastTextTitle_loc)
            self.mouseClick(self.writeMailPageInsertFastTextPage_fastTextList_loc)
        with allure.step("点击插入按钮"):
            self.click_ele(self.writeMailPageInsertFastTextPage_insertFastTextBtn_loc,key="点击插入快速文本")
        time.sleep(3)
        self.screenshotImg(key="插入快速富文本")
        with allure.step("获取快速文本的主体"):
            try:
                logger.info("切入编辑器frame")
                self.switch_frame(self.emailEditFrame_loc)
                fastTextBody = self.find_element((By.XPATH,"/html/body/p")).text
                fastTextBodyImg = ""
                fastTextBodyImgUrl = ""
                logger.info("is_pure".format(is_pure))
                if not is_pure:
                    fastTextBodyImg = self.find_element((By.XPATH,'/html/body/p/img')).get_attribute("src")
                    logger.info('fastTextBodyImg:{}'.format(fastTextBodyImg))
                if fastTextBodyImg:
                    fastTextBodyImgUrl = fastTextBodyImg.split("?")[0].split("/")[-1]
                else:
                    fastTextBodyImgUrl = None
                logger.info("fastTextBodyImgUrl:{}".format(fastTextBodyImgUrl))
            except Exception as e:
                print(e)
            finally:
                self.switch_parentFrame()
                return fastTextName,fastTextBody,fastTextBodyImgUrl

    #获取所有的快速文本标题
    def get_allFastTextTitle(self):
        with allure.step("点击写邮件按钮"):
            self.click_ele(self.writeEmailBtn_loc,key="点击写邮件")
        time.sleep(2)
        with allure.step("点击插入快速文本按钮"):
            self.click_ele(self.writeMailPage_insertFastTextBtn_loc,key="点击插入快速文本按钮")
        time.sleep(1)
        return self.get_elementText(self.writeMailPageInsertFastTextPage_fastTextTitle_loc,index="all")