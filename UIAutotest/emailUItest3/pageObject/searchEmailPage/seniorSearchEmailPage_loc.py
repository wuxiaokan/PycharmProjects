# -*- encoding: utf-8 -*-
'''
@File    :   seniorSearchEmailPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/2 0002 10:13   dmk      1.0         None
'''

from selenium.webdriver.common.by import By

class seniorSearchEmailPageLoc:

    #高级搜索按钮
    seniorSearchEmailPage_seniorSearchBtn_loc = (By.XPATH,'//div[@class="full-header-search-wrap"]//li[@ id="header-search-senior"]')
    #主题输入框
    seniorSearchEmailPage_subjectInput_loc = (By.XPATH,'//div[@aria-label="高级搜索"]//form//label[text()="主题"]/..//input')
    #确定按钮
    seniorSearchEmailPage_sureBtn_loc = (By.XPATH,'//button[@class="el-button el-button--primary"]//span[text()="确定"]/..')
    #相关客户，供应商邮件个数
    seniorSearchEmailPage_customerEmailNumList_loc = (By.XPATH,'//span[text()="相关客户/供应商等"]/ancestor::li//div[@class="el-menu-div el-contact"]//span[@class="el-gray"]')
    #全部位置，邮件个数
    seniorSearchEmailPage_allPositionEmailNumList_loc = (By.XPATH,'//span[text()="全部位置"]/ancestor::li//div[@class="el-menu-div el-contact"]//span[@class="el-gray"]')
    #回复状态，邮件个数
    seniorSearchEmailPage_replyStatusEmailNumList_loc = (By.XPATH,'//span[text()="回复状态"]/ancestor::li//span[@class="el-gray"]')
    #阅读状态，邮件个数
    seniorSearchEmailPage_readStatusEmailNumList_loc = (By.XPATH,'//span[text()="阅读状态"]/ancestor::li//span[@class="el-gray"]')
    #邮件箱子下拉列表
    seniorSearchEmailPage_emailBoxList_loc = (By.XPATH,'//div[@x-placement="bottom-start"]//li//span[text()="收件箱"]/..')
    #发送的按钮
    seniorSearchEmailPage_sendedBtn_loc = (By.XPATH,'//div[@class="el-form-item"]//label[text()="收发类型"]/..//span[text()="发送的"]/..')