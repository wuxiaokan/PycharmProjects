# -*- encoding: utf-8 -*-
'''
@File    :   customerInfoShowPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/13 0013 10:45   dmk      1.0         None
'''

from selenium.webdriver.common.by import By


class customerInfoShowPageLoc:

    #邮件列表页面，icon图标按钮
    recipientBoxPage_iconBtn_loc = (By.XPATH,'//a[@class="pointer"]//*[name()="svg"]')
    #根据邮件主题获取的icon图标按钮
    recipientBoxPage_iconBtnBySubject_loc = (By.XPATH,'//span[text()="333"]/ancestor::tr//a[@class="pointer"]//*[name()="svg"]')
    #基础信息tab按钮
    customerInfoShowPage_baseInfoTabBtn_loc = (By.XPATH,'//ul[@class="t-tabs-top"]//li[text()="基础信息"]')
    #显示的联系人
    customerInfoShowPage_showContact_loc = (By.XPATH,'//div[@class="slide-box-right"]//span[@class="contact_names"]')
    #显示的联系人列表
    customerInfoShowPage_showContactList_loc = (By.XPATH,'//div[@x-placement="bottom-start"]//span[text()="xxx"]/..')
    #显示的客户名称
    customerInfoShowPage_showCustomerName_loc = (By.XPATH,'//div[@class="slide-box-right"]//span[@class="fc01 pointer"]')
    #添加客户按钮
    unArchiverInfoShowPage_addCustomerBtn_loc = (By.XPATH,'//div[@class="slide-box-right"]//button[@class="el-button el-button--default el-button--small"]')
    #客户类型
    customerInfoShowPage_customerType_loc = (By.XPATH,'//div[@class="slide-box-right"]//label[text()="客户类型："]/following-sibling::div')
    #跟进阶段
    customerInfoShowPage_followStage_loc = (By.XPATH,'//div[@class="slide-box-right"]//label[text()="跟进阶段："]/following-sibling::div')
    #跟进阶段编辑按钮
    customerInfoShowPage_editFollowStageBtn_loc = (By.XPATH,'//div[@class="slide-box-right"]//i[@class="el-tooltip icon pointer"]')
    #跟进阶段下拉框
    customerInfoShowPage_followStageCheckBox_loc = (By.XPATH,'//div[@class="edit-stage"]//div[@class="el-input el-input--small el-input--suffix"]')
    #确认修改跟进阶段按钮
    customerInfoShowPage_sureEditFollowStageBtn_loc = (By.XPATH,'//div[@class="edit-stage"]//i[contains(@class,"el-icon-circle-check")]')
    #跟进阶段列表
    customerInfoShowPage_followStageList_loc = (By.XPATH,'//div[@x-placement="bottom-start"]//li')
    #客户标签
    customerInfoShowPage_customerMark_loc = (By.XPATH,'//div[@class="slide-box-right"]//label[text()="客户标签："]/following-sibling::div')
    #联系地址
    customerInfoShowPage_adrress_loc = (By.XPATH,'//div[@class="slide-box-right"]//label[text()="联系地址"]/following-sibling::div')
    #联系人名称
    customerInfoShowPage_contactName_loc = (By.XPATH,'//div[@class="slide-box-right"]//ul[@class="contact-list"]//li//b[@class="f14 one-line fl"]')
    #联系人邮箱地址
    customerInfoShowPage_contactEmailAct_loc = (By.XPATH,'//div[@class="slide-box-right"]//ul[@class="contact-list"]//li//span[@class="fl one-line"]')
    #邮件个数
    customerInfoShowPage_contactEmailNum_loc = (By.XPATH,'//div[@class="slide-box-right"]//ul[@class="contact-list"]//li//span[@class="p-l-10 fc01 pointer"]')
    #联系人手机号
    customerInfoShowPage_contactTel_loc = (By.XPATH,'//div[@class="slide-box-right"]//ul[@class="contact-list"]//li//div[contains(@class,"t-flex-row")][3]')
    #写邮件按钮
    customerInfoShowPage_sendEmailBtn_loc = (By.XPATH,'//div[@class="fr m-r-10"]//span[1]')
    #新建跟进按钮
    customerInfoShowPage_addFollowBtn_loc = (By.XPATH,'//div[@class="fr m-r-10"]//span[2]')