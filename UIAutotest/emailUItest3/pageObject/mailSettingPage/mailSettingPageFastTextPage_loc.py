# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPageFastTextPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/7 0007 9:56   dmk      1.0         None
'''

from selenium.webdriver.common.by import By


class mailSettingPageFastTextPageLoc:

    #快速文本按钮
    mailSettingPageFastTextPage_fastTextBtn_loc = (By.XPATH,'//div[@class="side-bar settings-bar-nav"]//span[text()="快速文本"]/..')
    #新建快速文本按钮
    mailSettingPageFastTextPageLoc_addFastTextBtn_loc = (By.XPATH,'//section[contains(@class,"fast-text")]//button[contains(@class,"add_account")]')
    #文本名称输入框
    mailSettingPageFastTextPage_fastTextNameInput_loc = (By.XPATH,'//section[contains(@class,"fast-text")]//input[contains(@placeholder,"请输入文本名称")]')
    #文本内容输入框
    mailSettingPageFastTextPage_fastTextContentInput_loc = (By.XPATH,'//section[contains(@class,"fast-text")]//div[contains(@class,"t-textarea")]//textarea')
    #富文本按钮
    mailSettingPageFastTextPage_richTextBtn_loc = (By.XPATH,'//section[contains(@class,"fast-text")]//span[text()="富文本"]/..')
    #保存按钮
    mailSettingPageFastTextPage_saveFastTextBtn_loc = (By.XPATH,'//section[contains(@class,"fast-text")]//button[@class="el-button el-button--primary"]')
    #快速文本名字列表
    mailSettingPageFastTextPage_fastTextNameList_loc = (By.XPATH,'//section[contains(@class,"fast-text")]//ul[@class="aside-list"]//li//span')
    #富文本切换确定按钮
    mailSettingPageFastTextPage_sureSwitchRichTextBtn_loc = (By.XPATH,'//button[@class="el-button el-button--default el-button--small el-button--primary "]')
    #插入图片按钮
    mailSettingPageFastTextPage_insertImgBtn_loc = (By.XPATH,'//a[@class="cke_button cke_button__myimage cke_button_off"]')
    #快速文本删除按钮
    mailSettingPageFastTextPage_delFastTextBtn_loc = (By.XPATH,'//div[@class="main-content"]//div[@class="icon-fr v-hidden"]')
    #确定删除快速文本按钮
    mailSettingPageFastTextPage_sureDelFastTextBtn_loc = (By.XPATH,'//button[@class="el-button el-button--default el-button--small el-button--primary "]')