# -*- encoding: utf-8 -*-
'''
@File    :   emailApprovalRuleSettingPage.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/30 0030 16:12   dmk      1.0         None
'''


import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .emailSettingPage import emailSettingPage

class emailApprovalRuleSettingPage(emailSettingPage):

    #审批规则按钮
    approvalRule_loc = (By.XPATH,"//span[text()='审批规则']")
    #新增审批规则按钮
    addApprovalRule_loc = (By.XPATH,"//button[@class='el-button add_account el-button--primary']")
    #审批人选择框
    approvalOperatorSelectTag_loc = (By.XPATH,'//span[contains(text(),"审批人")]/../following-sibling::div//div[@class="el-select"]')
    #管理员审批人
    approvalOperator_loc = (By.XPATH,"//div[@x-placement]//span[text()='管理员']/..")

    def run_currentApprovalClick_case(self,is_new):
        #进入设置页面
        self.click_settingBtn()
        #进入审批规则设置页面
        self.find_element(self.approvalRule_loc).click()
        print("截图")
        self.screenshotImg(key="审批规则设置页面")
        #判断是新增还是编辑
        if is_new:
            self.find_element(self.addApprovalRule_loc).click()
        #点击审批人选择框，获取审批人属性
        time.sleep(1)
        self.find_element(self.approvalOperatorSelectTag_loc).click()
        return self.find_element(self.approvalOperator_loc).get_attribute("class")