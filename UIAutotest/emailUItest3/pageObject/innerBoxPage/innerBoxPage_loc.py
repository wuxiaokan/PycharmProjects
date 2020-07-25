# -*- encoding: utf-8 -*-
'''
@File    :   innerBoxPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/27 0027 16:56   dmk      1.0         None
'''

from selenium.webdriver.common.by import By


class innerBoxPageLoc:
    # 内部联系人页面，内部联系人tab按钮
    innerBoxPage_innerBoxBtn_loc = (By.XPATH, '//div[@id="tab-inner"]')
    # 内部联系人箱页面，具体的一级内部联系人箱
    innerBoxPage_firstinnerBoxBtn_loc = (By.XPATH, '//div[@id="pane-inner"]//span[text()="管理员"]')