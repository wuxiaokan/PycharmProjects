# -*- encoding: utf-8 -*-
'''
@File    :   addFollowPageCommon.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/14 0014 19:40   dmk      1.0         None
'''

import allure,time
from utils.generator import *
from utils.log import logger
from pageObject.basePage import Action
from pageObject.customerInfoShowPage.addFollowPage_loc import addFollowPageLoc

class addFollowPageCommon(Action,addFollowPageLoc):

    #新建一个跟进
    def addFollow(self,followContent=None,is_customer=1):
        try:
            self.switch_mainPage()
            if is_customer:
                with allure.step("点击商机下拉框"):
                    self.click_ele(self.addFollowPage_selectBusinessBtn_loc,key="点击商机下拉框")
                time.sleep(1)
                with allure.step("选中第一个商机"):
                    self.click_ele(self.addFollowPage_businessList_loc,index=1,key="选中一个商机")
                time.sleep(0.5)
            with allure.step("输入框跟进内容"):
                if not followContent:
                    followContent = random_text().replace("\n","")
                self.sendKeys(self.addFollowPage_followContentInput_loc,key=followContent)
            with allure.step("点击保存按钮"):
                self.click_ele(self.addFollowPage_saveFollowBtn_loc,key="点击保存跟进按钮")
        except Exception as e:
            logger.info("新建跟进报错：{}".format(e))
        finally:
            self.switch_frame(self.mainFrame_loc)