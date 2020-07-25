# -*- encoding: utf-8 -*-
'''
@File    :   searchEmailPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/1 0001 14:51   dmk      1.0         None
'''

from selenium.webdriver.common.by import By

class searchEmailPageLoc:

    #搜索输入框
    searchEmailPage_searchInput_loc = (By.XPATH,'//li[@id="header-search-wrap"]//input')
    #搜索按钮
    searchEmailPage_searchBtn_loc = (By.XPATH,'//li[@id="header-search-wrap"]//a[@class="btn btn-search searchBtn top-2"]')
    #普通搜索下拉列表
    searchEmailPage_searchList_loc = (By.XPATH,'//ul[@id="search-menu"]//li')
    #搜索结果组名
    searchEmailPage_searchResultGroupNameList_loc = (By.XPATH,'//section[@class="el-container search-email-menu"]//div[@class="el-submenu__title"]')
