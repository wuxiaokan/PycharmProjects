# -*- encoding: utf-8 -*-
'''
@File    :   supplierBoxPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/2/26 0026 17:40   dmk      1.0         None
'''

from selenium.webdriver.common.by import By

class supplierBoxPageLoc:
    
    #供应商页面，供应商tab按钮
    supplierBoxPage_supplierBoxBtn_loc = (By.XPATH,'//div[@id="tab-supplier"]')
    #供应商箱页面，具体的一级供应商箱
    supplierBoxPage_firstsupplierBoxBtn_loc = (By.XPATH,'//div[@id="pane-supplier"]//span[text()="fttxtest@sina.cn"]')
    #显示方式-供应商名称
    supplierBoxPage_showSupplierName_loc = (By.XPATH,'//div[@class="customer-set-list-group"]//div[@name="供应商名称"]//label')
    #供应商箱设置按钮
    supplierBoxPage_supplierBoxSettingBtn_loc = (By.XPATH,'//div[@id="pane-supplier"]//span[@class="el-tooltip icon-border"]')
    #确定按钮
    supplierBoxPage_sureBtn_loc = (By.XPATH,'//button[@class="el-button el-button--primary"]//span[text()="确定"]/..')
    #供应商箱分组名
    supplierBoxPage_supplierBoxGroupNameList_loc = (By.XPATH,'//div[@class="menu-tree search-menu"]//span[@class="el-tooltip level1"]')
    #供应商箱二级分组名
    supplierBoxPage_supplierBoxSecondGroupNameList_loc = (By.XPATH,'//div[@class="menu-tree search-menu"]//span[@class="el-tooltip level2"]')
    #供应商箱三级分组名
    supplierBoxPage_supplierBoxThirdGroupNameList_loc = (By.XPATH,'//div[@class="menu-tree search-menu"]//span[@class="el-tooltip level3"]')
    #供应商箱搜索框
    supplierBoxPage_supplierBoxSearchInput_loc = (By.XPATH,'//div[@class="menu-tree-search"]//input')
    #供应商箱搜索按钮
    supplierBoxPage_supplierBoxSearchBtn_loc = (By.XPATH,'//div[@id="pane-supplier"]//span[@class="el-input__suffix-inner"]//*[name()="svg"]')
    #供应商箱页面，一级分类下拉框按钮
    supplierBoxPage_firstCategoryInput_loc = (By.XPATH,'//div[@aria-label="显示设置"]//label[text()="一级分类"]/..//input')
    #供应商箱页面，二级分类下拉框按钮
    supplierBoxPage_secondCategoryInput_loc = (By.XPATH,'//div[@aria-label="显示设置"]//label[text()="二级分类"]/..//input')
    #下拉列表-供应商类型
    supplierBoxPage_supplierCategoryList_loc = (By.XPATH,'//div[@x-placement="bottom-start"]/descendant::span[text()="供应商类型"]/..')