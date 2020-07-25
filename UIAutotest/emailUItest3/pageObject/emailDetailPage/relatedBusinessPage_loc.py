# -*- encoding: utf-8 -*-
'''
@File    :   relatedBusinessPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/9 0009 11:39   dmk      1.0         None
'''

from selenium.webdriver.common.by import By


class relatedBusinessPageLoc:

    #相关业务,已关联的报价单号
    relatedBusinessPage_relatedQuoteCode_loc = (By.XPATH,'//div[@aria-label="相关业务"]//div[@class="el-table dialog_table el-table--fit el-table--enable-row-hover el-table--enable-row-transition"]//tbody//td[1]//div[@class="cell"]')
    #相关业务，已关联的商机编码
    relatedBusinessPage_relatedBusinessCode_loc = (By.XPATH,'//div[@aria-label="相关业务"]//span[text()="商机编码"]/following-sibling::span')
    #相关业务，报价编号列表
    relatedBusinessPage_quoteList_loc = (By.XPATH,'//div[@aria-label="选择要关联的业务信息"]//tbody//tr//td[2]//div[@class="cell"]')
    #相关业务，报价tab按钮
    relatedBusinessPage_quoteTabBtn_loc = (By.XPATH,'//div[@aria-label="相关业务"]//li[text()="报价"]')
    #相关业务，订单tab按钮
    relatedBusinessPage_orderTabBtn_loc = (By.XPATH,'//div[@aria-label="相关业务"]//li[text()="订单"]')
    #相关业务，商机tab按钮
    relatedBusinessPage_businessTabBtn_loc = (By.XPATH,'//div[@aria-label="相关业务"]//li[text()="商机"]')
    #相关业务，添加关联按钮
    relatedBusinessPage_addRelatedBtn_loc = (By.XPATH,'//span[text()="添加关联"]/..')
    #相关业务，建立关联按钮
    relatedBusinessPage_buildRelatedBtn_loc = (By.XPATH,'//span[text()="建立关联"]/..')
    #相关业务，返回按钮
    relatedBusinessPage_backReleatedBtn_loc = (By.XPATH,'//span[text()="返回"]/..')
    #取消关联商机按钮
    relatedBusinessPage_cancelRelatedBtn_loc = (By.XPATH,'//div[@aria-label="相关业务"]//h4//*[name()="svg"]')