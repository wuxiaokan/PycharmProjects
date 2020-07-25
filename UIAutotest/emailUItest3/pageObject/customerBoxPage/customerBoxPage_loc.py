# -*- encoding: utf-8 -*-
'''
@File    :   customerBoxPage_loc.py    
@Contact :   fttxtest@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/21 0021 10:13   dmk      1.0         None
'''

from selenium.webdriver.common.by import By


class customerBoxPageLoc:
    #客户箱页面，客户箱按钮
    customerBoxPage_customerBoxBtn_loc = (By.XPATH,'//div[@id="tab-customer"]')
    #客户箱搜索框
    customerBoxPage_customerBoxSearchInput_loc = (By.XPATH,'//div[@class="menu-tree-search"]//input')
    #客户箱搜索按钮
    customerBoxPage_customerBoxSearchBtn_loc = (By.XPATH,'//div[@id="pane-customer"]//span[@class="el-input__suffix-inner"]//*[name()="svg"]')
    #客户箱分组名
    customerBoxPage_customerBoxGroupNameList_loc = (By.XPATH,'//div[@class="menu-tree search-menu"]//span[@class="el-tooltip level1"]')
    #客户箱二级分组名
    customerBoxPage_customerBoxSecondGroupNameList_loc = (By.XPATH,'//div[@class="menu-tree search-menu"]//span[@class="el-tooltip level2"]')
    #客户箱三级分组名
    customerBoxPage_customerBoxThirdGroupNameList_loc = (By.XPATH,'//div[@class="menu-tree search-menu"]//span[@class="el-tooltip level3"]')
    #客户箱设置按钮
    customerBoxPage_customerBoxSettingBtn_loc = (By.XPATH,'//div[@id="pane-customer"]//span[@class="el-tooltip icon-border"]')
    #显示方式-客户名称
    customerBoxPage_showCustomerName_loc = (By.XPATH,'//div[@class="customer-set-list-group"]//div[@name="客户名称"]//label')
    #确定按钮
    customerBoxPage_sureBtn_loc = (By.XPATH,'//button[@class="el-button el-button--primary"]//span[text()="确定"]/..')
    # #客户箱页面，加号图标按钮
    # customerBoxPage_addIconBtn_loc = (By.XPATH,'//span[@class="el-tree-node__expand-icon el-icon-caret-right"]')
    # #客户箱页面，最近联系分组下的客户
    # customerBoxPage_recentContactGroupCustomer_loc = (By.XPATH,'//div[@class="el-tree base-tree el-tree--highlight-current"]//span[@class="el-tooltip level2"]')
    # #客户箱页面，客户分组的三个点，即操作按钮
    # customerBoxPage_customerGroupMoreOperate_loc = (By.XPATH,'//div[@class="el-tree base-tree el-tree--highlight-current"]//span[@class="right-box-btn"]')
    # #客户箱页面，新增自定义箱按钮
    # customerBoxPage_addCustomerBoxBtn_loc = (By.XPATH,"//ul[@x-placement='bottom']//li[text()='新增下级自定义箱']")
    # #客户箱页面，新增自定义箱输入框
    # customerBoxPage_addCustomerBoxInput_loc = (By.XPATH,'//div[@class="customer-menu-page"]//div[@class="input3 JOINF el-input el-input--suffix"]//input')
    # #客户箱页面，确定新增自定义箱按钮,√，×，是同一个xpath，index不一样，分别是0,1
    # customerBoxPage_sureAddCustomerBoxBtn_loc = (By.XPATH,'//input[@placeholder="限16字符"]/following-sibling::span//*[name()="svg"]')
    # #客户箱页面，自定义箱列表
    # customerBoxPage_customBox_loc = (By.XPATH,'//div[@class="el-tree base-tree el-tree--highlight-current"]//span[@class="el-tooltip level3"]')
    #客户箱页面，具体的一级客户箱
    customerBoxPage_firstCustomerBoxBtn_loc = (By.XPATH,'//div[@id="pane-customer"]//span[text()="测试，勿动"]')
    #客户箱页面，一级分类下拉框按钮
    customerBoxPage_firstCategoryInput_loc = (By.XPATH,'//div[@aria-label="显示设置"]//label[text()="一级分类"]/..//input')
    #客户箱页面，二级分类下拉框按钮
    customerBoxPage_secondCategoryInput_loc = (By.XPATH,'//div[@aria-label="显示设置"]//label[text()="二级分类"]/..//input')
    #下拉列表-客户类型
    customerBoxPage_customerCategoryList_loc = (By.XPATH,'//div[@x-placement="bottom-start"]/descendant::span[text()="客户类型"]/..')