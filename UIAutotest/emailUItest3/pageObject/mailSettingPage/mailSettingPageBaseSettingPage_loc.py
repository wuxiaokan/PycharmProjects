# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPageBaseSettingPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/2 0002 15:11   dmk      1.0         None
'''

from selenium.webdriver.common.by import By


class mailSettingPageBaseSettingPageLoc:

    #基础设置按钮
    mailSettingPageBaseSettingPage_baseSettingBtn_loc = (By.XPATH,'//div[@class="settings-component__nav el-scrollbar"]//span[text()="基础设置"]/..')
    #已读设置
    mailSettingPageBaseSettingPage_readedSettingBtn_loc = (By.XPATH,'//div[text()="已读设置"]/following-sibling::div[1]')
    #自动回执按钮
    mailSettingPageBaseSettingPage_autoReceiptBtn_loc = (By.XPATH,'//div[text()="自动回执"]/following-sibling::div[contains(@class,"switch")]')
    #延迟发送按钮
    mailSettingPageBaseSettingPage_delaySendBtn_loc = (By.XPATH,'//div[text()="延迟发送"]/following-sibling::div[contains(@class,"switch")]')
    #基础设置按钮
    mailSettingPageCcAndBcSettingPage_ccAndBcSettingBtn_loc = (By.XPATH,'//div[@class="settings-component__nav el-scrollbar"]//span[text()="抄送密送"]/..')
    #默认抄送人输入框
    mailSettingPageCcAndBcSettingPage_defaultCcInput_loc = (By.XPATH,'//div[@class="main-content"]//div[text()="默认抄送人"]/..//input')
    #默认密送人输入框
    mailSettingPageCcAndBcSettingPage_defaultBcInput_loc = (By.XPATH,'//div[@class="main-content"]//div[text()="默认密送人"]/..//input')
    #强制抄送人输入框
    mailSettingPageCcAndBcSettingPage_forceCcInput_loc = (By.XPATH,'//div[@class="main-content"]//div[text()="强制抄送人"]/..//input')
    #删除抄送密送人按钮
    mailSettingPageCcAndBcSettingPage_delCcAndBcSettingBtn_loc = (By.XPATH,'//div[@class="copy_by_secret"]//li//div[contains(@class,"close_btn")]')
    #抄送密送保存按钮
    mailSettingPageCcAndBcSettingPage_saveBtn_loc = (By.XPATH,'//button[contains(@class,"save_btn")]')