# -*- encoding: utf-8 -*-
'''
@File    :   dealingEmailPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/13 0013 15:50   dmk      1.0         None
'''

from selenium.webdriver.common.by import By


class dealingEmailPageLoc:

    #往来邮件按钮
    dealingEmailPage_dealingEmailBtn_loc = (By.XPATH,'//div[@class="slide-box-right"]//li[text()="往来邮件"]')
    #所有联系人按钮
    dealingEmailPage_allContactBtn_loc = (By.XPATH,'//div[@class="slide-box-right"]//span[@class="flex-col-auto one-line has-icon-right"]')
    #邮件地址列表
    dealingEmailPage_emailActList_loc = (By.XPATH,'//div[@x-placement="bottom-start"]//li')
    #邮件列表
    dealingEmailPage_emailList_loc = (By.XPATH,'//div[@class="slide-box-right"]//ul[@class="t-email-list"]//li')
    #邮件主题
    dealingEmailPage_emailSubjectList_loc = (By.XPATH,'//div[@class="slide-box-right"]//ul[@class="t-email-list"]//li//div[@class="flex-col-auto one-line"]')
    #全部邮件按钮
    dealingEmailPage_allEmailBtn_loc = (By.XPATH,'//div[@class="slide-box-right"]//div[@class="t-switch-btn"]//span[text()="全"]')
    #收邮件按钮
    dealingEmailPage_receiveEmailBtn_loc = (By.XPATH,'//div[@class="slide-box-right"]//div[@class="t-switch-btn"]//span[text()="收"]')
    #发邮件按钮
    dealingEmailPage_sendEmailBtn_loc = (By.XPATH,'//div[@class="slide-box-right"]//div[@class="t-switch-btn"]//span[text()="发"]')
    #邮件收发状态图标
    dealingEmailPage_emailReceiveSendIcon_loc = (By.XPATH,'//div[@class="slide-box-right"]//ul[@class="t-email-list"]//div[@class="flex-col-auto one-line" or @class="flex-col-auto one-line f-w-bold"]/..//div[@class="flex-col-icon"]//*[name()="svg"]')
    #全屏按钮
    dealingEmailPage_fullScreenBtn_loc = (By.XPATH,'//div[@class="slide-box-right"]//div[@class="t-switch-btn"]/../../div[@class="flex-col-center m-l-10"]')
    #标记未读已读按钮
    dealingEmailPage_markReadBtn_loc = (By.XPATH,'//div[@class="slide-box-right"]//ul[@class="t-email-list"]//li//span[@class="t-icon pointer"]')
    #标记星标按钮
    dealingEmailPage_markStarBtn_loc = (By.XPATH,'//div[@class="slide-box-right"]//ul[@class="t-email-list"]//li//span[@class="icon pointer"]')