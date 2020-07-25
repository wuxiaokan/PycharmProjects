# -*- encoding: utf-8 -*-
'''
@File    :   unArchiverInfoShowPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/15 0015 16:14   dmk      1.0         None
'''

from selenium.webdriver.common.by import By


class unArchiverInfoShowPageLoc:

    #邮件列表页面，icon图标按钮
    recipientBoxPage_iconBtn_loc = (By.XPATH,'//a[@class="pointer"]//*[name()="svg"]')
    #邮件列表页面，未建档联系人地址
    recipientBoxPage_unArchiverEmailAct_loc = (By.XPATH,'//a[@class="pointer"]//*[name()="svg" and contains(@style,"rgb(92, 107, 119)")]/../..//span[@class="contact_names"]')
    #联系人邮件地址
    unArchiverInfoShowPage_contactEmailAct_loc = (By.XPATH,'//div[@class="slide-box-right"]//span[@class="contact_names"]')
    #添加客户下拉按钮
    unArchiverInfoShowPage_addCustomerDropdownBtn_loc = (By.XPATH,'//div[@class="slide-box-right"]//button[@class="el-button el-button--default el-button--small el-dropdown__caret-button"]')
    #添加客户按钮
    unArchiverInfoShowPage_addCustomerBtn_loc = (By.XPATH,'//div[@class="slide-box-right"]//button[@class="el-button el-button--default el-button--small"]')
    #添加供应商按钮
    unArchiverInfoShowPage_addSupplierBtn_loc = (By.XPATH,'//ul[@x-placement="bottom-end"]//li[text()="添加供应商"]')
    #添加联系人按钮
    unArchiverInfoShowPage_addContactBtn_loc = (By.XPATH,'//div[@class="slide-box-right"]//button[@class="el-button m-l-10 btn-small el-button--default"]')
    #客户页面，客户名称
    customerPage_customerName_loc = (By.XPATH,'//div[@class="customer_edit_add_vue"]//span[text()="客户名称"]/../..//input')
    #客户页面，联系人姓名
    customerPage_contactName_loc = (By.XPATH,'//div[@class="contact-cards"]//span[text()="姓名"]/../..//span[@class="el-input__inner"]')
    #客户页面，联系人邮箱
    customerPage_contactEmailAct_loc = (By.XPATH,'//div[@class="contact-cards"]//span[text()="邮箱"]/../..//span[@class="el-input__inner"]')
    #供应商页面，联系人姓名
    supplierPage_contactName_loc = (By.XPATH,'//tr[@class="contact"]//td[@data-name="姓名"]//input')
    #供应商页面，联系人邮箱
    supplierPage_contactEmailAct_loc = (By.XPATH,'//tr[@class="contact"]//td[@data-name="邮箱"]//input')
    #供应商页面，供应商名称
    supplierPage_supplierName_loc = (By.XPATH,'//li[@data-name="供应商名称"]//input')
    #客户列表
    unArchiverInfoShowPage_customerList_loc = (By.XPATH,'//div[@aria-label="添加联系人"]//tbody//tr')
    #供应商tab按钮
    unArchiverInfoShowPage_supplierTabBtn_loc = (By.XPATH,'//div[@aria-label="添加联系人"]//li[text()="供应商"]')
    #确认添加联系人按钮
    unArchiverInfoShowPage_sureAddContactBtn_loc = (By.XPATH,'//div[@aria-label="添加联系人"]//button[@class="el-button small el-button--primary"]')
    #智能推荐tab按钮
    unArchiverInfoShowPage_smartRecommendBtn_loc = (By.XPATH,'//div[@class="slide-box-right"]//li[text()="智能推荐"]')
    #往来邮件tab按钮
    unArchiverInfoShowPage_dealingEmailBtn_loc = (By.XPATH,'//div[@class="slide-box-right"]//li[text()="智能推荐"]')