# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPageEmailTemplatePage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/29 0029 15:19   dmk      1.0         None
'''

from selenium.webdriver.common.by import By


class mailSettingPageEmailTemplatePageLoc:

    #邮箱设置按钮
    mailSettingBtn_loc = (By.XPATH,'//div[@class="setIcon icon"]')
    #邮件模板按钮
    mailSettingPageEmailTemplatePage_emailTemplateBtn_loc = (By.XPATH,'//div[@class="side-bar settings-bar-nav"]//span[text()="邮件模板"]')
    #模板名字
    mailSettingPageEmailTemplatePage_emailTemplateName_loc = (By.XPATH,'//div[@class="contentpart"]//div[contains(@class,"tpl-name")]')