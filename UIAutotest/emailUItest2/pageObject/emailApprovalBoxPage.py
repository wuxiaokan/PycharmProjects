# -*- encoding: utf-8 -*-
'''
@File    :   emailApprovalBoxPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/30 0030 17:23   dmk      1.0         None
'''

import time
from selenium.webdriver.common.by import By
from .basePage import Action

class emailApprovalBoxPage(Action):
    #审批箱按钮
    approvalBox_loc = (By.XPATH,"//span[text()='审批箱']")
    #审批箱邮件数量
    approvalEmailNum_loc = (By.XPATH,"//span[text()='审批箱']/following-sibling::span")
    #过滤按钮
    filterBtn_loc = (By.XPATH,'//div[@class="icon_group"]/div[1]')
    #待审批按钮
    waitApproval_loc = (By.XPATH,"//li[text()='待审批']")
    #邮件总数量
    emailTotal_loc = (By.XPATH,"//span[@class='el-pagination__total']")

    def run_waitApprovalEmailNum_case(self):
        #进入审批箱
        self.find_element(self.approvalBox_loc).click()
        #获取待审批的数量
        waitApprovalNum = self.find_element(self.approvalEmailNum_loc).text
        #过滤待审批的邮件
        self.find_element(self.filterBtn_loc).click()
        time.sleep(0.5)
        self.find_element(self.waitApproval_loc).click()
        time.sleep(0.5)
        #获取过滤后的邮件数量
        if self.is_element_exist(self.emailTotal_loc[1]):
            totalEmailNum = self.find_element(self.emailTotal_loc).text
            totalEmailNum = totalEmailNum.split(" ")[1]
            #目前有7个历史数据有问题，待以后更新后，在同步代码
            if int(waitApprovalNum) != int(totalEmailNum):
                print(int(waitApprovalNum),int(totalEmailNum))
                raise Exception("待审批邮件数量，角标显示与审批箱主页面不一致")