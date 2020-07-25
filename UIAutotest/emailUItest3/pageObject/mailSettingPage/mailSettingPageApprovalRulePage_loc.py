# -*- encoding: utf-8 -*-
'''
@File    :   ApprovalSettingPageApprovalRulePage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/19 0019 11:16   dmk      1.0         None
'''

from selenium.webdriver.common.by import By

class mailSettingPageApprovalRulePageLoc:
    #邮箱设置按钮
    mailSettingBtn_loc = (By.XPATH,'//div[@class="setIcon icon"]')
    #审批规则按钮
    mailSettingPageApprovalRulePage_approvalRuleBtn_loc = (By.XPATH,'//div[@class="side-bar settings-bar-nav"]//span[text()="审批规则"]')
    #新建审批规则按钮
    mailSettingPageApprovalRulePage_addApprovalRuleBtn_loc = (By.XPATH,'//button[@class="el-button add_account el-button--primary"]')
    #审批规则名称输入框
    mailSettingPageApprovalRulePage_approvalRuleNameInput_loc = (By.XPATH,'//label[text()="审批规则名称"]/following-sibling::div//input')
    #审批条件选择框按钮
    mailSettingPageApprovalRulePage_approvalConditionBtn_loc = (By.XPATH,'//label[text()="审批条件"]/following-sibling::div/div')
    #审批条件,强制，可选等
    mailSettingPageApprovalRulePage_approvalCondition_loc = (By.XPATH,'//div[@x-placement="bottom-start" or @x-placement="top-start"]//span[text()="全部审批（强制）"]')
    #审批条件包含，关键词输入框
    mailSettingPageApprovalRulePage_approvalConditionContainKeyInput_loc = (By.XPATH,'//div[@class="t-flex-row"]//input[@maxlength="100"]')
    #审批人选择框按钮
    mailSettingPageApprovalRulePage_approvalPersonBtn_loc = (By.XPATH,'//span[contains(text(),"审批人")]/../following-sibling::div//div[@class="el-select__tags"]')
    #审批人，管理员
    mailSettingPageApprovalRulePage_approvalPerson_loc = (By.XPATH,'//div[@x-placement="bottom-start" or @x-placement="top-start"]//span[text()="管理员"]')
    #审批规则保存按钮
    mailSettingPageApprovalRulePage_saveApprovalRuleBtn = (By.XPATH,'//div[@class="rules-component__nav x-hidden el-scrollbar"]//button[@class="el-button el-button--primary"]')
    #审批规则列表
    mailSettingPageApprovalRulePage_approvalRuleList_loc = (By.XPATH,'//section[@class="el-container approval-rules"]//ul[@class="aside-list"]//li')
    #审批规则禁用，启用按钮
    mailSettingPageApprovalRulePage_disableApprovalRuleBtn_loc = (By.XPATH,'//section[@class="el-container approval-rules"]//ul[@class="aside-list"]//li//div[@class="icon-fr v-hidden"]//*[name()="svg"][1]')
    #审批规则删除按钮
    mailSettingPageApprovalRulePage_approvalRuleDelBtn_loc = (By.XPATH,'//section[@class="el-container approval-rules"]//ul[@class="aside-list"]//li//div[@class="icon-fr v-hidden"]//*[name()="svg"][2]')
    #审批规则确定删除按钮
    mailSettingPageApprovalRulePage_approvalRuleSureDelBtn_loc = (By.XPATH,'//button[@class="el-button el-button--default el-button--small el-button--primary "]')
