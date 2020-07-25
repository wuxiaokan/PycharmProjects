# -*- encoding: utf-8 -*-
'''
@File    :   seniorSearchMailPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/21 0021 14:10   dmk      1.0         None
'''

from selenium.webdriver.common.by import By

class seniorSearchMailPageLoc:
    #高级搜索按钮
    seniorSearchMailPage_seniorSearchBtn_loc = (By.XPATH,'//div[@class="full-header-search-wrap"]//li[@ id="header-search-senior"]')
    #高级搜索页面，不包含附件按钮
    seniorSearchMailPage_hasNoAttchBtn_loc = (By.XPATH,'//label[@for="attachment"]/following-sibling::div//label[2]')
    #高级搜索页面，包含附件按钮
    seniorSearchMailPage_hasAttchBtn_loc = (By.XPATH,'//label[@for="attachment"]/following-sibling::div//label[3]')
    #高级搜索页面，确定按钮
    seniorSearchMailPage_sureBtn_loc = (By.XPATH,'//div[@class="el-dialog__wrapper JOINF inputting_distribution senior-dialog"]//button[@class="el-button el-button--primary"]')
