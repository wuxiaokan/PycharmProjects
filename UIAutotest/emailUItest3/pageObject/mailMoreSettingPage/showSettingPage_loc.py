# -*- encoding: utf-8 -*-
'''
@File    :   showSettingPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/11 0011 16:58   dmk      1.0         None
'''

from selenium.webdriver.common.by import By


class showSettingPageLoc:

    #更多设置按钮
    mailMoreSettingPage_moreSettingBtn_loc = (By.XPATH,'//div[@class="setMore"]')
    #显示设置按钮
    showSettingPage_showSettingBtn_loc = (By.XPATH,'//ul[@x-placement="bottom-end"]//li[contains(text(),"显示设置")]')
    #显示邮件地址按钮
    showSettingPage_showEmailactBtn_loc = (By.XPATH,'//ul[@x-placement="bottom-end"]//span[text()="显示邮件地址"]/..')
    #显示确定按钮
    showSettingPage_sureBtn_loc = (By.XPATH,'//ul[@x-placement="bottom-end"]//span[text()="确定"]/..')
    #勾选按钮对应的选项
    showSettingPage_selectedShowSettingList_loc = (By.XPATH,'//ul[@x-placement="bottom-end"]//li[text()="显示设置"]//div[@class="show-set-box"]//li//*[name()="svg"]/../span')
    #发件人
    showSettingPage_sender_loc = (By.XPATH,'//span[not(contains(@class,"compact"))]//span[@class="contact_names"]')
    #邮件列表上摘要
    showSettingPage_emailListAbstract_loc = (By.XPATH,'//span[@class="fc05"]')
    #邮件分组名
    showSettingPage_emailGroupName_loc = (By.XPATH,'//div[@class="cue_bar f12 fc02"]//span[@class="text"]')
    #快捷阅读
    showSettingPage_quickRead_loc = (By.XPATH,'//div[contains(@class,"mail_read_group")]')
    #快捷阅读勾选标识
    showSettingPage_quickReadSelectedIcon_loc = (By.XPATH,'//ul[@x-placement="bottom-end"]//li[text()="启用快捷阅读"]//*[name()="svg"]')