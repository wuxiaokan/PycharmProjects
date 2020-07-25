# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPageMergerRulePage_loc.py.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/26 0026 11:26   dmk      1.0         None
'''

from selenium.webdriver.common.by import By

class mailSettingPageMergerRulePageLoc:

    #邮件设置页面，归并规则按钮
    mailSettingPageMergerRulePage_mergerRuleBtn_loc = (By.XPATH,'//div[@class="side-bar settings-bar-nav"]//span[text()="归并规则"]')
    #归并规则名称输入框
    mailSettingPageMergerRulePage_mergerRuleNameInput_loc = (By.XPATH,'//label[text()="归并规则名称"]/following-sibling::div//input')
    #归并条件选择框按钮
    mailSettingPageMergerRulePage_mergerConditionBtn_loc = (By.XPATH,'//label[text()="规则触发条件"]/following-sibling::div/div')
    #归并条件,主题，地址等
    mailSettingPageMergerRulePage_mergerCondition_loc = (By.XPATH,'//div[@x-placement="bottom-start" or @x-placement="top-start"]//span[contains(text(),"邮件主题")]')
    #归并条件包含按钮
    mailSettingPageMergerRulePage_conditionContainBtn_loc = (By.XPATH,'//section[@class="el-container mergerRules"]//span[text()="包含"]')
    #归并条件等于按钮
    mailSettingPageMergerRulePage_conditionEqualBtn_loc = (By.XPATH,'//section[@class="el-container mergerRules"]//span[text()="等于"]')
    #归并条件包含输入框
    mailSettingPageMergerRulePage_conditionContainInput_loc = (By.XPATH,'//div[@class="JOINF el-input"]//input[@placeholder="请输入"]')
    #归并条件，等于场景下二级选择框
    mailSettingPageMergerRulePage_conditionEqualSecondBtn_loc = (By.XPATH,'//div[@class="el-row"]//div[@class="el-select"]')
    #归并规则收取至一级按钮
    mailSettingPageMergerRulePage_firstChargeBtn = (By.XPATH,'//label[text()="收取至"]/following-sibling::div//div[@class="el-col el-col-12"][1]')
    #归并规则收取至二级按钮
    mailSettingPageMergerRulePage_secondChargeBtn = (By.XPATH,'//label[text()="收取至"]/following-sibling::div//div[@class="el-col el-col-12"][2]')
    #归并规则收取至二级输入框
    mailSettingPageMergerRulePage_secondChargeInput = (By.XPATH,'//label[text()="收取至"]/following-sibling::div//div[@class="el-col el-col-12"][2]//input')
    #自定义箱测试，勿动箱子
    mailSettingPageMergerRulePage_customBoxTest_loc = (By.XPATH,'//div[@x-placement="bottom-start" or @x-placement="top-start"]//span[contains(text(),"自定义箱测试，勿动")]/preceding-sibling::label')
    #归并规则保存按钮
    mailSettingPageMergerRulePage_saveMergerRuleBtn = (By.XPATH,'//section[@class="el-container mergerRules"]//button[@class="el-button el-button--primary"]')