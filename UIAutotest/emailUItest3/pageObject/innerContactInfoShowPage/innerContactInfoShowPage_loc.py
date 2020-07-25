# -*- encoding: utf-8 -*-
'''
@File    :   innerContactInfoShowPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/15 0015 19:33   dmk      1.0         None
'''

from selenium.webdriver.common.by import By

class innerContactInfoShowPageLoc:

    #邮件列表页面，icon图标按钮
    recipientBoxPage_iconBtn_loc = (By.XPATH,'//a[@class="pointer"]//*[name()="svg"]')
    #邮件列表页面，内部联系人地址
    recipientBoxPage_innerContactEmailAct_loc = (By.XPATH,'//a[@class="pointer"]//*[name()="svg" and contains(@style,"rgb(23, 131, 251)")]/../..//span[@class="contact_names"]')
    #联系人邮件地址
    innerContactInfoShowPage_contactEmailAct_loc = (By.XPATH,'//div[@class="slide-box-right"]//span[@class="contact_names"]')
    #智能推荐tab按钮
    innerContactInfoShowPage_smartRecommendBtn_loc = (By.XPATH,'//div[@class="slide-box-right"]//li[text()="智能推荐"]')
    #往来邮件tab按钮
    innerContactInfoShowPage_dealingEmailBtn_loc = (By.XPATH,'//div[@class="slide-box-right"]//li[text()="智能推荐"]')