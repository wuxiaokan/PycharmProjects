# -*- encoding: utf-8 -*-
'''
@File    :   customerRecycleBoxPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/20 0020 10:14   dmk      1.0         None
'''
from selenium.webdriver.common.by import By


class customerRecycleBoxPageLoc:

    #回收箱tab按钮
    customerRecycleBoxPage_RecycleBoxBtn_loc = (By.XPATH,'//div[@class="tabs_nav"]//div[text()="回收箱"]')
    #客户名称列表
    customerRecycleBoxPage_customerName_loc = (By.XPATH,'//div[@class="customer_List_vue"]//div[@isbody="true"]//div[contains(@class,"fl-table__row")]//div[contains(@class,"cell")][3]')
    #客户选择框
    customerPage_customerCheckBox_loc = (By.XPATH,'//div[@id="main-content"]//div[@class="table_con"]//div[@class="el-table__fixed"]//div[contains(@class,"fl-table__row")]//label')