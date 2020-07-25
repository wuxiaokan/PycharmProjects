# -*- encoding: utf-8 -*-
'''
@File    :   mailSettingPageShowSettingPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/27 0027 10:50   dmk      1.0         None
'''

from selenium.webdriver.common.by import By


class mailSettingPageShowSettingPageLoc:

    #显示设置按钮
    mailSettingPageShowSettingPage_showSettingBtn_loc = (By.XPATH,'//div[@id="main-content"]//span[text()="显示设置"]/..')
    #追踪按钮
    mailSettingPageShowSettingPage_traceBtn_loc = (By.XPATH,'//div[@class="basic_setting"]//span[text()="默认勾选“邮件追踪”"]/..')
    #默认字体一级选择框按钮
    mailSettingPageShowSettingPage_defaultFontBtn_loc = (By.XPATH,'//div[@class="basic_setting"]//div[text()="默认字体"]/following-sibling::div')
    #字体大小一级选择框按钮
    mailSettingPageShowSettingPage_fontSizeBtn_loc = (By.XPATH,'//div[@class="basic_setting"]//div[text()="字体大小"]/following-sibling::div')
    #字体，大小列表
    mailSettingPageShowSettingPage_fontSizeList_loc = (By.XPATH,'//div[contains(@x-placement,"bottom") or contains(@x-placement,"top")]//li')
    #字体颜色一级选择框按钮
    mailSettingPageShowSettingPage_fontColorBtn_loc = (By.XPATH,'//div[@class="basic_setting"]//div[text()="字体颜色"]/following-sibling::div')
    #字体展示板
    mailSettingPageShowSettingPage_sizeShowTemplate_loc = (By.XPATH,'//div[@class="basic_setting"]//div[@class="show_font"]')
    #是否需要回执按钮
    mailSettingPageShowSettingPage_needReceiptBtn_loc = (By.XPATH,'//span[contains(text(),"默认勾选“需要回执”")]/..')
    #保存按钮
    mailSettingPageShowSettingPage_saveBtn_loc = (By.XPATH,'//button[contains(@class,"save_btn")]')