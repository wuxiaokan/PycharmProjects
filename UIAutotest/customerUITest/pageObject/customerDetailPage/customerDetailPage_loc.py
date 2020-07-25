# -*- encoding: utf-8 -*-
'''
@File    :   customerDetailPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/17 0017 15:05   dmk      1.0         None
'''

from selenium.webdriver.common.by import By


class customerDetailPageLoc:

    #客户详情页面，客户代码详情
    customerDetailPage_customerCodeDetail_loc = (By.XPATH,'//div[@class="kehu-detail"]//label[contains(text(),"客户代码")]/following-sibling::div')
    #客户信息展开按钮
    customerDetailPage_customerInfoShowBtn_loc = (By.XPATH,'//dt[@class="line36 has-icon-right pointer"]')
    #联系人展开按钮
    customerDetailPage_contactInfoShowBtn_loc = (By.XPATH,'//div[contains(@class,"contact-info")]//i[@title="展开"]')
    #联系人姓名详情
    customerDetailPage_contactName_loc = (By.XPATH,'//div[contains(@class,"contact-info")]//div[contains(@class,"contact-name")]')
    #联系人职务详情
    customerDetailPage_contactJob_loc = (By.XPATH,'//div[contains(@class,"contact-info")]//div[@class="drag-filter"]')
    #编辑按钮
    customerDetailPage_customerEditBtn_loc = (By.XPATH,'//span[@class="customer-icon-text"]//span[text()="编辑"]')
    #写邮件按钮
    customerDetailPage_writeMailBtn_loc = (By.XPATH,'//span[@class="customer-icon-text"]//span[text()="写邮件"]/..')
    #收件人
    customerDetailPage_recipent_loc = (By.XPATH,'//div[@class="addressee"]//p[contains(@class,"show_txt")]')
    #文件按钮
    customerDetailPage_fileBtn_loc = (By.XPATH,'//div[contains(@class,"subTabs")]//div[text()="文件"]')
    #附件名
    customerDetailPage_attachName_loc = (By.XPATH,'//div[@class="attachment_list_box"]//div[contains(@class,"text1")]//p')