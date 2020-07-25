# -*- encoding: utf-8 -*-
'''
@File    :   relatedBusinessPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/14 0014 13:53   dmk      1.0         None
'''

from selenium.webdriver.common.by import By

class relatedBusinessPageLoc:

    #相关业务按钮
    relatedBusinessPage_relatedBusinessBtn_loc = (By.XPATH,'//div[@class="slide-box-right"]//li[text()="相关业务"]')
    #所有联系人按钮
    relatedBusinessPage_allContactBtn_loc = (By.XPATH,'//div[@class="slide-box-right"]//span[@class="flex-col-auto one-line has-icon-right"]')
    #联系人列表
    relatedBusinessPage_contactList_loc = (By.XPATH,'//div[@x-placement="bottom-start"]//li')
    #选择商机按钮
    relatedBusinessPage_selectBusinessBtn_loc = (By.XPATH,'//div[@class="tr m-l-10"]//div[@class="m-r-10 f12 el-dropdown"]')
    #商机列表
    relatedBusinessPage_businessList_loc = (By.XPATH,'//ul[@x-placement="bottom-end"]//li')
    #更多条件按钮
    relatedBusinessPage_moreConditionBtn_loc = (By.XPATH,'//div[@class="tr m-l-10"]//div[@class="f12 el-dropdown"]')
    #日志选项
    relatedBusinessPage_moreConditionListBtn_loc = (By.XPATH,'//ul[@x-placement="bottom-end"]//li//span[text()="跟进"]/..')
    #日志列表
    relatedBusinessPage_logList_loc = (By.XPATH,'//ul[@class="t-email-list list2-customer"]//li')
    #跟进内容列表
    relatedBusinessPage_followContentList_loc = (By.XPATH,'//ul[@class="t-email-list list2-follow"]//li//div[@class="flex-col-auto line-clamp"]')