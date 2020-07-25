# -*- encoding: utf-8 -*-
'''
@File    :   supplierInfoShowPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/15 0015 14:05   dmk      1.0         None
'''

from selenium.webdriver.common.by import By

class supplierInfoShowPageLoc:

    #邮件列表页面，icon图标按钮
    recipientBoxPage_iconBtn_loc = (By.XPATH,'//a[@class="pointer"]//*[name()="svg"]')
    #显示的联系人
    supplierInfoShowPage_showContact_loc = (By.XPATH,'//div[@class="slide-box-right"]//span[@class="contact_names"]')
    #显示的供应商名称
    supplierInfoShowPage_showSupplierName_loc = (By.XPATH,'//div[@class="slide-box-right"]//span[@class="fc01 pointer"]')
    #供应商类型
    supplierInfoShowPage_supplierType_loc = (By.XPATH,'//div[@class="slide-box-right"]//label[text()="供应商类型："]/following-sibling::div')
    #供应商标签
    supplierInfoShowPage_supplierMark_loc = (By.XPATH,'//div[@class="slide-box-right"]//label[text()="供应商标签："]/following-sibling::div')
    #联系地址
    supplierInfoShowPage_adrress_loc = (By.XPATH,'//div[@class="slide-box-right"]//label[text()="联系地址"]/following-sibling::div')
    #联系人名称
    supplierInfoShowPage_contactName_loc = (By.XPATH,'//div[@class="slide-box-right"]//ul[@class="contact-list"]//li//b[@class="f14 one-line fl"]')
    #联系人邮箱地址
    supplierInfoShowPage_contactEmailAct_loc = (By.XPATH,'//div[@class="slide-box-right"]//ul[@class="contact-list"]//li//span[@class="fl one-line"]')
    #联系人手机号
    supplierInfoShowPage_contactTel_loc = (By.XPATH,'//div[@class="slide-box-right"]//ul[@class="contact-list"]//li//div[contains(@class,"t-flex-row")][3]')
    #邮件个数
    supplierInfoShowPage_contactEmailNum_loc = (By.XPATH,'//div[@class="slide-box-right"]//ul[@class="contact-list"]//li//span[@class="p-l-10 fc01 pointer"]')
    #新建跟进按钮
    supplierInfoShowPage_addFollowBtn_loc = (By.XPATH,'//div[@class="fr m-r-10"]//span[2]')
    #写邮件按钮
    supplierInfoShowPage_sendEmailBtn_loc = (By.XPATH,'//div[@class="fr m-r-10"]//span[1]')