# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPageMailRulePage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/15 0015 16:39   dmk      1.0         None
'''

from selenium.webdriver.common.by import By

class mailSettingPageMailRulePageLoc:

    #收件规则按钮
    mailSettingPageMailRulePage_mailRuleBtn = (By.XPATH,'//div[@class="side-bar settings-bar-nav"]//span[text()="收信规则"]')
    #新建收件规则按钮
    mailSettingPageMailRulePage_addMailRuleBtn = (By.XPATH,'//button[@class="el-button add_account el-button--primary"]')
    #收件规则名称输入框
    mailSettingPageMailRulePage_mailRuleNameInput = (By.XPATH,'//label[text()="收信规则名称"]/following-sibling::div//input')
    #收件规则触发条件按钮
    mailSettingPageMailRulePage_conditionBtn = (By.XPATH,'//label[text()="规则触发条件"]/following-sibling::div')
    #收件规则条件是全部邮件
    mailSettingPageMailRulePage_condition_allMails = (By.XPATH,'//div[@x-placement="bottom-start" or @x-placement="top-start"]//span[text()="全部邮件"]')
    # 收件规则条件是新客户邮件
    mailSettingPageMailRulePage_condition_newCustomerMail = (By.XPATH, '//div[@x-placement="bottom-start" or @x-placement="top-start"]//span[text()="新客户邮件"]')
    # 收件规则条件是老客户邮件
    mailSettingPageMailRulePage_condition_oldCustomerMail = (By.XPATH, '//div[@x-placement="bottom-start" or @x-placement="top-start"]//span[text()="老客户邮件"]')
    # 收件规则条件是邮件主题
    mailSettingPageMailRulePage_condition_mailSubject = (By.XPATH, '//div[@x-placement="bottom-start" or @x-placement="top-start"]//span[text()="邮件主题"]')
    # 收件规则条件是发件地址
    mailSettingPageMailRulePage_condition_sendAddress = (By.XPATH, '//div[@x-placement="bottom-start" or @x-placement="top-start"]//span[text()="发件地址"]')
    #收件规则执行操作按钮
    mailSettingPageMailRulePage_excuteOperateBtn = (By.XPATH,'//label[text()="执行操作"]/following-sibling::div/div')
    #收件规则执行操作-分发
    mailSettingPageMailRulePage_excuteOperate_deliver = (By.XPATH,'//div[@x-placement="bottom-start" or @x-placement="top-start"]//span[text()="分发"]')
    #收件规则执行操作-直接归并
    mailSettingPageMailRulePage_excuteOperate_merger = (By.XPATH,'//div[@x-placement="bottom-start" or @x-placement="top-start"]//span[text()="直接归并"]')
    # 收件规则分发给一级按钮
    mailSettingPageMailRulePage_firstDeliverBtn = (By.XPATH, '//label[text()="分发给"]/following-sibling::div//div[@class="el-col el-col-12"][1]')
    # 收件规则分发给二级按钮
    mailSettingPageMailRulePage_secondDeliverBtn = (By.XPATH, '//label[text()="分发给"]/following-sibling::div//div[@class="el-col el-col-12"][2]')
    # 收件规则分发给指定职务
    mailSettingPageMailRulePage_firstDeliver_assignJob = (By.XPATH, '//div[@x-placement="bottom-start" or @x-placement="top-start"]//span[text()="指定职务"]')
    # 收件规则分发给指定人员，每人一封
    mailSettingPageMailRulePage_firstDeliver_assignEveryPerson = (By.XPATH, '//div[@x-placement="bottom-start" or @x-placement="top-start"]//span[text()="指定人员（每人一封）"]')
    # 收件规则分发给指定职务,轮流获取
    mailSettingPageMailRulePage_firstDeliver_assignTurnPerson = (By.XPATH, '//div[@x-placement="bottom-start" or @x-placement="top-start"]//span[text()="指定人员（轮流获取）"]')
    # 收件规则分发人员列表
    mailSettingPageMailRulePage_secondDeliverPersonList = (By.XPATH, '//div[@x-placement="bottom-start" or @x-placement="top-start"]//li')
    #收件规则收取至一级按钮
    mailSettingPageMailRulePage_firstChargeBtn = (By.XPATH,'//label[text()="收取至"]/following-sibling::div//div[@class="el-col el-col-12"][1]')
    #收件规则收取至二级按钮
    mailSettingPageMailRulePage_secondChargeBtn = (By.XPATH,'//label[text()="收取至"]/following-sibling::div//div[@class="el-col el-col-12"][2]')
    #收件规则收取至客户箱
    mailSettingPageMailRulePage_firstCharge_customerBox = (By.XPATH,'//div[@x-placement="bottom-start" or @x-placement="top-start"]//span[text()="客户箱"]')
    #收件规则收取至供应商箱
    mailSettingPageMailRulePage_firstCharge_supplierBox = (By.XPATH,'//div[@x-placement="bottom-start" or @x-placement="top-start"]//span[text()="供应商箱"]')
    #收件规则收取至内部联系人箱
    mailSettingPageMailRulePage_firstCharge_internalBox = (By.XPATH,'//div[@x-placement="bottom-start" or @x-placement="top-start"]//span[text()="内部联系人箱"]')
    #收件规则收取至自定义箱
    mailSettingPageMailRulePage_firstCharge_customizeBox = (By.XPATH,'//div[@x-placement="bottom-start" or @x-placement="top-start"]//span[text()="自定义箱"]')
    #收件规则收取至二级箱子列表
    mailSettingPageMailRulePage_secondCharge_boxList = (By.XPATH,'//div[@x-placement="bottom-start" or @x-placement="top-start"]//li')
    #收件规则保存按钮
    mailSettingPageMailRulePage_saveMailRuleBtn = (By.XPATH,'//div[@class="btn-box"]//button')
    #收件规则包含关键字输入框
    mailSettingPageMailRulePage_containKeyInput = (By.XPATH,'//label[text()="规则触发条件"]/../following-sibling::div[1]//div/input')
    #邮件箱tab
    recipientBoxPage_emailBoxBtn_loc = (By.XPATH,'//div[@id="tab-email"]')
    #客户箱tab
    recipientBoxPage_customerBoxBtn_loc = (By.XPATH,'//div[@id="tab-customer"]')
    #最近联系的第一个客户箱
    customerBoxPage_firstRecentBox_loc = (By.XPATH,'//div[@id="pane-customer"]//div[@class="el-tree-node__children"]')
    #收件规则自定义测试箱
    customizeBoxPage_firstBox_loc = (By.XPATH,'//span[text()="自定义箱测试,勿动"]')
    #供应商tab
    recipientBoxPage_supplierBoxBtn_loc = (By.XPATH,'//div[@id="tab-supplier"]')
    #最近联系的第一个供应商箱
    supplierBoxPage_firstRecentBox_loc = (By.XPATH,'//div[@id="pane-supplier"]//div[@class="el-tree-node__children"]')
    #内部联系人箱子tab
    recipientBoxPage_innerBoxBtn_loc = (By.XPATH,'//div[@id="tab-inner"]')
    #最近联系的第一个内部联系人箱
    innerBoxPage_firstRecentBox_loc = (By.XPATH,'//div[@id="pane-inner"]//div[@class="el-tree-node__content"]')
    #邮件主题
    recipientBoxPage_emailSubject_loc = (By.XPATH,'//div[contains(@class,"sub_info")]')
