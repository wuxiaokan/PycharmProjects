# -*- encoding: utf-8 -*-
'''
@File    :   customerPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/17 0017 16:57   dmk      1.0         None
'''
from selenium.webdriver.common.by import By

class customerPageLoc:

    #客户名称
    customerPage_customerName_loc = (By.XPATH,'//div[@class="customer_List_vue"]//div[@isbody="true"]//div[contains(@class,"fl-table__row")]//div[contains(@class,"cell")][3]')
    #可删除的客户名称
    customerPage_canDelCustomerName_loc = (By.XPATH,'//div[contains(@class,"fl-table__row")]//span[contains(text(),"测试，可删除")]')
    #客户选择框
    customerPage_customerCheckBox_loc = (By.XPATH,'//div[@id="main-content"]//div[@class="table_con"]//div[@class="el-table__fixed"]//div[contains(@class,"fl-table__row")]//label')
    #删除按钮
    customerPage_customerDelBtn_loc = (By.XPATH,'//span[@class="icon-txt"]//span[text()="删除"]/..')
    #确认删除按钮
    customerPage_customerSureDelBtn_loc = (By.XPATH,'//button[contains(@class,"el-button--primary")]//span[contains(text(),"确")]')
    #回收箱tab按钮
    customerRecycleBoxPage_RecycleBoxBtn_loc = (By.XPATH,'//div[@class="tabs_nav"]//div[text()="回收箱"]')
    #恢复按钮
    customerPage_customerRestoreBtn_loc = (By.XPATH,'//span[@class="icon-txt"]//span[text()="恢复"]/..')
    #更多按钮
    customerPage_moreBtn_loc = (By.XPATH,'//div[@class="icon el-dropdown"]//span[contains(@class,"icon-txt")]')
    #刷新按钮
    customerPage_refreshBtn_loc = (By.XPATH,'//ul[@x-placement="bottom"]//li[text()="刷新"]')