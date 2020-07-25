# -*- encoding: utf-8 -*-
'''
@File    :   seniorSearchEmailPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/25 0025 20:06   dmk      1.0         None
'''

from selenium.webdriver.common.by import By

class seniorSearchEmailPageLoc:

    #高级搜索页面，主题输入框
    seniorSearchEmailPage_subjectInput_loc = (By.XPATH,'//div[contains(@class,"senior-dialog")]//input[@placeholder="请输入主题"]')