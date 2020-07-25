# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPageBlackListPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/4 0004 16:30   dmk      1.0         None
'''

from selenium.webdriver.common.by import By


class mailSettingPageBlackListPageLoc:

    #邮箱设置按钮
    mailSettingBtn_loc = (By.XPATH,'//div[@class="setIcon icon"]')
    #黑名单按钮
    mailSettingPageBlackListPage_blackListBtn_loc = (By.XPATH,'//div[@class="side-bar settings-bar-nav"]//span[text()="黑名单"]/..')
    #黑名单页面，头部选择框
    mailSettingPageBlackListPage_headCheckbox_loc = (By.XPATH,'//div[contains(@class,"black-list")]//div[@class="table_thead"]//div[@class="plugins"]//label')
    #新增黑名单按钮
    mailSettingPageBlackListPage_addBlackListBtn_loc = (By.XPATH,'//div[contains(@class,"black-list")]//button[contains(@class,"add-black-btn")][2]')
    #删除黑名单按钮
    mailSettingPageBlackListPage_delBlackListBtn_loc = (By.XPATH,'//div[contains(@class,"black-list")]//button[contains(@class,"add-black-btn")][1]')
    #邮件地址输入框
    mailSettingPageBlackListPage_emailAccountInput_loc = (By.XPATH,'//label[contains(text(),"邮箱地址")]/following-sibling::div//input')
    #邮件主题输入框
    mailSettingPageBlackListPage_emailSubjectInput_loc = (By.XPATH,'//label[contains(text(),"邮箱主题")]/following-sibling::div//input')
    #存放垃圾箱按钮
    mailSettingPageBlackListPage_storeRubbishBoxBtn_loc = (By.XPATH,'//span[text()="临时存放在垃圾箱中"]/..')
    #直接删除按钮
    mailSettingPageBlackListPage_directDelBtn_loc = (By.XPATH, '//span[text()="直接删除"]/..')
    #确定添加按钮
    mailSettingPageBlackListPage_sureAddBlackListBtn_loc = (By.XPATH,'//div[@aria-label="添加黑名单"]//button[contains(@class,"el-button--primary")]')
    #匹配信息单元格
    mailSettingPageBlackListPage_matchInfomationTd_loc = (By.XPATH,'//div[contains(@class,"black-list")]//tr[@class="el-table__row"]//td[3]')
    #处理方式单元格
    mailSettingPageBlackListPage_handleWayTd_loc = (By.XPATH,'//div[contains(@class,"black-list")]//tr[@class="el-table__row"]//td[4]')
    #单个黑名单删除按钮
    mailSettingPageBlackListPage_delSingleBlackListBtn_loc = (By.XPATH,'//div[contains(@class,"black-list")]//tr[@class="el-table__row"]//td[5]//span')