# -*- encoding: utf-8 -*-
'''
@File    :   saasHomePage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/25 0025 19:52   dmk      1.0         None
'''

from selenium.webdriver.common.by import By


class saasHomePageLoc:

    #导航栏，外贸管理tab
    saasHomePage_sysNav_tradeTabBtn_loc = (By.XPATH,'//div[@class="sysnav-header-select"]//a[contains(text(),"外贸管理")]')
    #导航栏,邮件查询
    saasHomePage_sysNav_emailSearch_loc = (By.XPATH,'//div[@class="sysnav-header-select"]//a[contains(text(),"邮件查询")]')
    #导航栏，写邮件
    saasHomePage_sysNav_writeMailBtn_loc = (By.XPATH,'//div[@class="sysnav-header-select"]//a[contains(text(),"写邮件")]')
    #导航栏，未读邮件tab
    saasHomePage_sysNav_unReadMailBtn_loc = (By.XPATH,'//div[@class="sysnav-header-select"]//a[contains(text(),"未读箱")]')
    #导航栏，审批箱tab
    saasHomePage_sysNav_approvalMailBtn_loc = (By.XPATH,'//div[@class="sysnav-header-select"]//a[contains(text(),"审批箱")]')