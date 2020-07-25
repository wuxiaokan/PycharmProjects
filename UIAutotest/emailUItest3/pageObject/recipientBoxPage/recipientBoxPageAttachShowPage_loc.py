# -*- encoding: utf-8 -*-
'''
@File    :   recipientBoxPageAttachShowPage_loc.py
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/21 0021 11:30   dmk      1.0         None
'''

from selenium.webdriver.common.by import By


class recipientBoxPageAttachShowPageLoc:
    #收件箱页面，附件图标
    recipientBoxPageAttachShowPage_attachIcon_loc = (By.XPATH,'//section[@class="el-container search-email-menu"]//div[@class="attach_item"]')
    #收件箱页面，通过附件图标获取到对应的邮件主题
    recipientBoxPageAttachShowPage_subjectByAttachIcon_loc = (By.XPATH,'//section[@class="el-container search-email-menu"]//div[@class="attach_item"]/../../../following-sibling::td//div[@class="sub_item"]')
    #收件箱页面，附件总大小
    recipientBoxPageAttachShowPage_emailTotalSize_loc = (By.XPATH,'//div[@x-placement="right"]//p[@class="title1"]/span[1]')
    #收件箱页面，正文大小
    recipientBoxPageAttachShowPage_emailBodySize_loc = (By.XPATH,'//div[@x-placement="right"]//p[@class="title1"]/span[2]')
    #收件箱页面，附件列表
    recipientBoxPageAttachShowPage_attachList_loc = (By.XPATH,'//div[@x-placement="right"]//li[@class="item"]//span[@class="name"]')
    #收件箱页面，附件图片地址
    recipientBoxPageAttachShowPage_attachImgSrc_loc = (By.XPATH,'//div[@x-placement="right"]//li[@class="item"]//img')
    #收件箱页面，附件名
    recipientBoxPageAttachShowPage_attachName_loc = (By.XPATH,'//div[@x-placement="right"]//li[@class="item"]//span[@class="name"]')
    #收件箱页面，附件大小
    recipientBoxPageAttachShowPage_attachSize_loc = (By.XPATH,'//div[@x-placement="right"]//li[@class="item"]//span[@class="size"]')
